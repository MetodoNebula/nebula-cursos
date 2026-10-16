// Cifra catalog.json y bundles/*.json en cifrado/ para publicar la web sin dejar
// el contenido legible. Formato de cada .bin: IV (12 bytes) + AES-256-GCM(gzip(json)).
// La clave se deriva de la contraseña con PBKDF2-SHA256 (sal e iteraciones en cifrado/meta.json).
//
// Uso:  node cifrar.js                 (pide la contraseña)
//       node cifrar.js --nueva-clave   (cambia la contraseña: genera sal nueva y lo recifra todo)
// También acepta la contraseña en la variable de entorno NEBULA_PASS.
'use strict';
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const zlib = require('zlib');

const ROOT = __dirname;
const OUT = path.join(ROOT, 'cifrado');
const META = path.join(OUT, 'meta.json');
const CACHE = path.join(ROOT, '.cifrado_cache.json');
const ITER = 310000;
const CHECK_TEXT = '{"ok":true}';

function encrypt(key, buf){
  const iv = crypto.randomBytes(12);
  const c = crypto.createCipheriv('aes-256-gcm', key, iv);
  const gz = zlib.gzipSync(buf, { level: 9 });
  return Buffer.concat([iv, c.update(gz), c.final(), c.getAuthTag()]);
}
function decrypt(key, buf){
  const d = crypto.createDecipheriv('aes-256-gcm', key, buf.subarray(0, 12));
  d.setAuthTag(buf.subarray(buf.length - 16));
  return zlib.gunzipSync(Buffer.concat([d.update(buf.subarray(12, buf.length - 16)), d.final()]));
}

// Escapa los caracteres de control sueltos dentro de cadenas (p. ej. un salto de línea literal),
// que hacen el JSON inválido y la lección imposible de cargar en el navegador.
function repairControlChars(text){
  let out = '', inStr = false, esc = false;
  for (const ch of text){
    if (inStr){
      if (esc) esc = false;
      else if (ch === '\\') esc = true;
      else if (ch === '"') inStr = false;
      else if (ch < ' '){
        out += ch === '\n' ? '\\n' : ch === '\r' ? '\\r' : ch === '\t' ? '\\t' : '\\u' + ch.charCodeAt(0).toString(16).padStart(4, '0');
        continue;
      }
    } else if (ch === '"') inStr = true;
    out += ch;
  }
  return out;
}
// Valida el JSON (reparándolo si hace falta) y lo devuelve minificado.
function normalizeJSON(rel, buf, repaired){
  const text = buf.toString('utf8');
  try { return Buffer.from(JSON.stringify(JSON.parse(text))); }
  catch (e){
    try { const data = JSON.parse(repairControlChars(text)); repaired.push(rel); return Buffer.from(JSON.stringify(data)); }
    catch { throw new Error(`${rel} no es JSON válido: ${e.message}`); }
  }
}

function askPassword(prompt){
  if (process.env.NEBULA_PASS) return Promise.resolve(process.env.NEBULA_PASS);
  return new Promise((resolve, reject) => {
    const stdin = process.stdin;
    process.stdout.write(prompt);
    if (!stdin.isTTY){
      let s = '';
      stdin.on('data', d => s += d).on('end', () => resolve(s.split(/\r?\n/)[0]));
      return;
    }
    let s = '';
    stdin.setRawMode(true); stdin.resume(); stdin.setEncoding('utf8');
    stdin.on('data', function onData(ch){
      if (ch === '\r' || ch === '\n'){
        stdin.setRawMode(false); stdin.pause(); stdin.removeListener('data', onData);
        process.stdout.write('\n'); resolve(s);
      } else if (ch === '\u0003'){ process.stdout.write('\n'); reject(new Error('Cancelado')); }
      else if (ch === '\u0008' || ch === '\u007f'){ if (s){ s = s.slice(0, -1); process.stdout.write('\b \b'); } }
      else { s += ch; process.stdout.write('*'); }
    });
  });
}

async function main(){
  const newKey = process.argv.includes('--nueva-clave');
  fs.mkdirSync(path.join(OUT, 'bundles'), { recursive: true });

  const pass = await askPassword('Contraseña de la web: ');
  if (!pass) throw new Error('La contraseña no puede estar vacía.');

  let meta = fs.existsSync(META) && !newKey ? JSON.parse(fs.readFileSync(META, 'utf8')) : null;
  let key;
  if (meta){
    key = crypto.pbkdf2Sync(pass, Buffer.from(meta.salt, 'base64'), meta.iter, 32, 'sha256');
    try { decrypt(key, Buffer.from(meta.check, 'base64')); }
    catch { throw new Error('La contraseña no coincide con la usada antes. Para cambiarla: node cifrar.js --nueva-clave'); }
  } else {
    if (!process.env.NEBULA_PASS && (await askPassword('Repite la contraseña: ')) !== pass)
      throw new Error('Las contraseñas no coinciden.');
    const salt = crypto.randomBytes(16);
    key = crypto.pbkdf2Sync(pass, salt, ITER, 32, 'sha256');
    meta = { v: 1, iter: ITER, salt: salt.toString('base64'),
             check: encrypt(key, Buffer.from(CHECK_TEXT)).toString('base64') };
    fs.writeFileSync(META, JSON.stringify(meta, null, 1));
  }

  // Solo se recifran los archivos que cambiaron (si no, cada push subiría todo de nuevo).
  let cache = {};
  try { cache = JSON.parse(fs.readFileSync(CACHE, 'utf8')); } catch {}
  if (cache.salt !== meta.salt) cache = { salt: meta.salt, files: {} };

  const sources = ['catalog.json', ...fs.readdirSync(path.join(ROOT, 'bundles'))
    .filter(f => f.endsWith('.json')).sort().map(f => 'bundles/' + f)];
  let done = 0, skipped = 0;
  const repaired = [];
  for (const rel of sources){
    const src = fs.readFileSync(path.join(ROOT, rel));
    const hash = crypto.createHash('sha256').update(src).digest('hex');
    const dst = path.join(OUT, rel.replace(/\.json$/, '.bin'));
    if (cache.files[rel] === hash && fs.existsSync(dst)){ skipped++; continue; }
    fs.writeFileSync(dst, encrypt(key, normalizeJSON(rel, src, repaired)));
    cache.files[rel] = hash; done++;
  }
  for (const rel of repaired)
    console.warn(`AVISO: ${rel} tenía saltos de línea sueltos dentro de textos (JSON inválido); se ha corregido en la copia cifrada, el original no se toca.`);

  // Borra los .bin cuyo bundle ya no existe.
  const wanted = new Set(sources.map(r => r.replace(/\.json$/, '.bin')));
  for (const f of fs.readdirSync(path.join(OUT, 'bundles'))){
    if (!wanted.has('bundles/' + f)){ fs.unlinkSync(path.join(OUT, 'bundles', f)); delete cache.files['bundles/' + f.replace(/\.bin$/, '.json')]; }
  }

  fs.writeFileSync(CACHE, JSON.stringify(cache));
  console.log(`Cifrado listo: ${done} archivos cifrados, ${skipped} sin cambios.`);
}

main().catch(e => { console.error('ERROR: ' + e.message); process.exit(1); });
