/* Applies one reviewed Atlas example to the first real Functions asset only. */
'use strict';

const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const bundlePath = path.join(root, 'bundles', 'eso_matematicas__mat_funciones_representacion.json');
const source = fs.readFileSync(bundlePath, 'utf8');
const bundle = JSON.parse(source);
let target;

(function walk(value) {
  if (target || !value || typeof value !== 'object') return;
  if (typeof value.svg === 'string' && value.svg.includes('<svg')) { target = value; return; }
  Object.values(value).forEach(walk);
})(bundle);

if (!target) throw new Error('No SVG asset found in the Functions bundle.');
target.svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="-14 -14 428 328" width="428" height="328" role="img" aria-labelledby="atlas-quadrants-title atlas-quadrants-description" data-nebula-svg="2026-10-20" data-nebula-atlas="quadrants-v1" preserveAspectRatio="xMidYMid meet" focusable="false">
  <title id="atlas-quadrants-title">Plano cartesiano con cuadrantes y dos puntos</title>
  <desc id="atlas-quadrants-description">Gráfico Atlas para reconocer el signo de las coordenadas. El punto A, de coordenadas tres y dos, está en el primer cuadrante; el punto B, de coordenadas menos dos y menos uno, está en el tercer cuadrante.</desc>
  <rect x="-14" y="-14" width="428" height="328" rx="18" fill="#f5f8fc"/>
  <rect x="8" y="8" width="384" height="284" rx="14" fill="#ffffff"/>
  <g font-family="Albert Sans,Segoe UI,Arial,Helvetica,sans-serif">
    <text x="28" y="28" font-size="10.5" font-weight="700" letter-spacing="1.4" fill="#155eef">ATLAS / PLANO CARTESIANO</text>
    <text x="28" y="60" font-size="18" font-weight="700" fill="#101828">Signo de las coordenadas</text>
    <path d="M28 70H86" stroke="#155eef" stroke-width="3.5" stroke-linecap="round"/>
    <text x="372" y="33" text-anchor="end" font-size="10.5" font-weight="600" letter-spacing=".8" fill="#334e68">LECTURA VISUAL</text>
  </g>
  <g fill="none" stroke="#cdd8e7" stroke-width="1.15" stroke-linecap="round">
    <path d="M100 174V182M135 174V182M170 174V182M240 174V182M275 174V182M310 174V182M345 174V182"/>
    <path d="M201 110H209M201 144H209M201 212H209M201 246H209"/>
  </g>
  <g fill="none" stroke="#101828" stroke-width="2.25" stroke-linecap="round" stroke-linejoin="round">
    <path d="M55 178H362l-11-7M362 178l-11 7"/>
    <path d="M205 270V74l-7 11M205 74l7 11"/>
  </g>
  <g font-family="Albert Sans,Segoe UI,Arial,Helvetica,sans-serif" font-weight="600">
    <text x="257" y="98" font-size="13.5" fill="#155eef">I · (+,+)</text>
    <text x="80" y="98" font-size="13.5" fill="#334e68">II · (−,+)</text>
    <text x="80" y="258" font-size="13.5" fill="#d92d20">III · (−,−)</text>
    <text x="257" y="258" font-size="13.5" fill="#334e68">IV · (+,−)</text>
    <text x="369" y="184" font-size="17" fill="#101828">x</text>
    <text x="214" y="86" font-size="17" fill="#101828">y</text>
  </g>
  <circle cx="310" cy="110" r="6.5" fill="#155eef" stroke="#ffffff" stroke-width="2.5"/>
  <path d="M314 114L320 124" stroke="#155eef" stroke-width="1.6" stroke-linecap="round"/>
  <text x="324" y="132" font-family="Albert Sans,Segoe UI,Arial,Helvetica,sans-serif" font-size="13.5" font-weight="600" fill="#155eef">A(3, 2)</text>
  <circle cx="135" cy="212" r="6.5" fill="#d92d20" stroke="#ffffff" stroke-width="2.5"/>
  <path d="M131 216L118 229" stroke="#d92d20" stroke-width="1.6" stroke-linecap="round"/>
  <text x="76" y="238" font-family="Albert Sans,Segoe UI,Arial,Helvetica,sans-serif" font-size="13.5" font-weight="600" fill="#d92d20">B(−2, −1)</text>
  <path d="M28 280H372" stroke="#d9e2ec" stroke-width="1"/>
  <text x="28" y="305" font-family="Albert Sans,Segoe UI,Arial,Helvetica,sans-serif" font-size="11.5" font-weight="600" fill="#243b53">IZQUIERDA / ABAJO: −</text>
  <text x="372" y="305" text-anchor="end" font-family="Albert Sans,Segoe UI,Arial,Helvetica,sans-serif" font-size="11.5" font-weight="600" fill="#243b53">DERECHA / ARRIBA: +</text>
</svg>`;
const output = `${JSON.stringify(bundle, null, 2)}\n`;
if (output !== source) fs.writeFileSync(bundlePath, output, 'utf8');

console.log(JSON.stringify({ bundle: path.basename(bundlePath), changed: target.svg.includes('data-nebula-atlas="quadrants-v1"') }, null, 2));
