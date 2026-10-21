'use strict';
const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..');
function asset(fileName, predicate) {
  const data = JSON.parse(fs.readFileSync(path.join(root, 'bundles', fileName), 'utf8'));
  let ordinal = 0;
  function walk(value) {
    if (!value || typeof value !== 'object') return null;
    if (typeof value.svg === 'string' && value.svg.includes('<svg')) { ordinal += 1; if (predicate(value, ordinal)) return value; }
    for (const child of Object.values(value)) { const hit = walk(child); if (hit) return hit; }
    return null;
  }
  return walk(data);
}
const math = asset('eso_matematicas__mat_ecuaciones.json', (item) => item.id === 'diag_mat_ecuaciones_balance');
const fq = asset('eso_fisicaquimica__U-ESO-03.json', (_, ordinal) => ordinal === 3);
if (!math || !fq) throw new Error('Reference illustrations not found.');
const html = `<!doctype html><html lang="es"><meta charset="utf-8"><title>Referencia Física Selectividad</title><style>*{box-sizing:border-box}body{margin:0;padding:32px;background:#f4f6f5;font-family:'Segoe UI',system-ui,sans-serif;color:#24312c}h1{margin:0 0 7px;font-size:28px}p{margin:0 0 25px;color:#5c6b67}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}figure{margin:0;padding:22px;background:#fff;border-radius:16px;box-shadow:0 8px 24px rgba(36,49,44,.1)}figcaption{margin-bottom:10px;font-weight:700;color:#0e7a68}svg{display:block;width:100%;height:auto}</style><h1>Lenguaje visual de Física Selectividad</h1><p>Objetos reales, color funcional y etiquetas integradas sin paneles decorativos.</p><main class="grid"><figure><figcaption>Matemáticas ESO · ecuación</figcaption>${math.svg}</figure><figure><figcaption>Física y Química ESO · filtración</figcaption>${fq.svg}</figure></main></html>`;
const out = path.join(root, '_audit_scratch', 'selectividad_style_review.html'); fs.writeFileSync(out, html, 'utf8'); console.log(out);
