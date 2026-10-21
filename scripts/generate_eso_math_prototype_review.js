'use strict';
const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..');
const selections = [
  ['eso_matematicas__mat_funciones_representacion.json', 'diag_004', 'Funciones'],
  ['eso_matematicas__mat_derivadas.json', 'diag_029', 'Derivadas'],
  ['eso_matematicas__mat_ecuaciones.json', 'diag_mat_ecuaciones_balance', 'Ecuaciones'],
  ['eso_matematicas__mat_geometria_metrica.json', 'diag_mat_geometria_metrica_pythagorean', 'Geometría'],
  ['eso_matematicas__mat_probabilidad.json', 'diag_mat_probabilidad_tree', 'Probabilidad'],
  ['eso_matematicas__mat_estadistica_descriptiva.json', 'diag_mat_estadistica_descriptiva_boxplot', 'Estadística'],
];
function findById(value, id) {
  if (!value || typeof value !== 'object') return null;
  if (value.id === id && typeof value.svg === 'string') return value;
  for (const child of Object.values(value)) { const found = findById(child, id); if (found) return found; }
  return null;
}
const cards = selections.map(([file, id, name]) => {
  const data = JSON.parse(fs.readFileSync(path.join(root, 'bundles', file), 'utf8'));
  const asset = findById(data, id);
  if (!asset) throw new Error(`Missing ${id}`);
  return `<figure><figcaption>${name}</figcaption>${asset.svg}</figure>`;
}).join('\n');
const out = path.join(root, '_audit_scratch', 'eso_math_prototype_review.html');
fs.writeFileSync(out, `<!doctype html><html lang="es"><meta charset="utf-8"><title>Prototipos matemáticos ESO</title><style>*{box-sizing:border-box}body{margin:0;padding:28px;background:#eaf0f7;font-family:"Albert Sans","Segoe UI",Arial,sans-serif;color:#0b1f3a}h1{margin:0 0 8px;font-size:28px;font-weight:700}p{margin:0 0 24px;color:#334e68}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}figure{margin:0;padding:14px;background:white;border-radius:16px;box-shadow:0 10px 25px rgba(11,31,58,.1)}figcaption{padding:0 4px 9px;font-size:13px;font-weight:600;color:#334e68}svg{display:block;width:100%;height:auto}</style><h1>Prototipos conceptuales · Matemáticas ESO</h1><p>Seis plantillas específicas, sin tarjetas de texto ni decoración superflua.</p><main class="grid">${cards}</main></html>`, 'utf8');
console.log(out);
