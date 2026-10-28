// Cifra catalog.json y bundles/*.json en cifrado/ para publicar la web sin dejar
// el contenido legible. Formato de cada .bin: IV (12 bytes) + AES-256-GCM(gzip(json)).
// La clave se deriva de la contraseña con PBKDF2-SHA256 (sal e iteraciones en cifrado/meta.json).
//
// catalog.json se cifra con esa clave maestra (es solo navegación: títulos y
// recuentos, no el contenido real). Cada bundles/<curso>__*.json se cifra con
// una clave propia de ese curso, derivada de la maestra por HKDF — así un
// alumno con acceso a un curso no puede usar esa clave para descifrar los
// bundles de otro curso al que no tiene acceso (la restricción por curso deja
// de ser solo visual y pasa a ser también criptográfica).
//
// Uso:  node cifrar.js                 (pide la contraseña)
//       node cifrar.js --nueva-clave   (cambia la contraseña: genera sal nueva y lo recifra todo)
// También acepta la contraseña en la variable de entorno NEBULA_PASS.
//
// Al terminar, escribe cifrado/course_keys_SECRETO_NO_SUBIR.sql con el INSERT
// para la tabla course_secrets de Supabase. Ese archivo NUNCA se sube a git
// (está en .gitignore): pega su contenido en el SQL Editor de Supabase y
// luego puedes borrarlo.
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

// Clave propia de un curso, derivada de la clave maestra por HKDF (el "info"
// es el key del curso, p.ej. "gcse_mates"): independiente y no reversible
// hacia la clave maestra ni hacia la de otro curso.
function courseKey(masterKey, course){
  return Buffer.from(crypto.hkdfSync('sha256', masterKey, Buffer.alloc(0), Buffer.from(course), 32));
}
// bundles/<course>__resto.json -> "<course>". null si el nombre no sigue ese patrón.
function courseOfBundle(rel){
  const base = path.basename(rel, '.json');
  const m = base.match(/^(.+?)__/);
  return m ? m[1] : null;
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
  const courseKeys = new Map(); // course -> Buffer, para todos los cursos vistos (se usen o no bundles sin cambios)
  for (const rel of sources){
    let useKey = key;
    if (rel !== 'catalog.json'){
      const course = courseOfBundle(rel);
      if (course){
        if (!courseKeys.has(course)) courseKeys.set(course, courseKey(key, course));
        useKey = courseKeys.get(course);
      } else {
        console.warn(`AVISO: ${rel} no sigue el patrón "<curso>__..."; se cifra con la clave maestra (sin aislar por curso).`);
      }
    }
    const src = fs.readFileSync(path.join(ROOT, rel));
    const hash = crypto.createHash('sha256').update(src).digest('hex');
    const dst = path.join(OUT, rel.replace(/\.json$/, '.bin'));
    if (cache.files[rel] === hash && fs.existsSync(dst)){ skipped++; continue; }
    fs.writeFileSync(dst, encrypt(useKey, normalizeJSON(rel, src, repaired)));
    cache.files[rel] = hash; done++;
  }
  for (const rel of repaired)
    console.warn(`AVISO: ${rel} tenía saltos de línea sueltos dentro de textos (JSON inválido); se ha corregido en la copia cifrada, el original no se toca.`);

  if (courseKeys.size){
    const rows = [...courseKeys.entries()].sort(([a],[b]) => a.localeCompare(b))
      .map(([course, buf]) => `  ('${course.replace(/'/g, "''")}', '${buf.toString('base64')}')`).join(',\n');
    const sql = `-- Generado por cifrar.js. Pega esto en Supabase (SQL Editor) y luego borra\n`
      + `-- este archivo: son las claves reales de descifrado de cada curso.\n`
      + `insert into public.course_secrets (course_key, value) values\n${rows}\n`
      + `on conflict (course_key) do update set value = excluded.value;\n`;
    fs.writeFileSync(path.join(OUT, 'course_keys_SECRETO_NO_SUBIR.sql'), sql);
    console.log(`\nClaves por curso listas: ${courseKeys.size} cursos. Pega el contenido de`);
    console.log(`cifrado/course_keys_SECRETO_NO_SUBIR.sql en el SQL Editor de Supabase (y luego bórralo).`);
  }

  // Borra los .bin cuyo bundle ya no existe.
  const wanted = new Set(sources.map(r => r.replace(/\.json$/, '.bin')));
  for (const f of fs.readdirSync(path.join(OUT, 'bundles'))){
    if (!wanted.has('bundles/' + f)){ fs.unlinkSync(path.join(OUT, 'bundles', f)); delete cache.files['bundles/' + f.replace(/\.bin$/, '.json')]; }
  }

  fs.writeFileSync(CACHE, JSON.stringify(cache));
  console.log(`Cifrado listo: ${done} archivos cifrados, ${skipped} sin cambios.`);
}

main().catch(e => { console.error('ERROR: ' + e.message); process.exit(1); });
