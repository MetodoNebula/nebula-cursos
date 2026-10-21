/* Review-only Atlas refinement: sparse, collision-safe explanatory graph. */
'use strict';

const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..');
const outputDir = path.join(root, '_audit_scratch', 'atlas_refined');
fs.mkdirSync(outputDir, { recursive: true });

const xTicks = [170, 225, 335, 390, 445, 500, 555, 610]
  .map((x) => `<path d="M${x} 286V294"/>`).join('');
const yTicks = [198, 244, 336, 382]
  .map((y) => `<path d="M276 ${y}H284"/>`).join('');

const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480" width="760" height="480" role="img" aria-labelledby="atlas-title atlas-description">
  <title id="atlas-title">Atlas refinado: una función cuadrática explicada sin solapamientos</title>
  <desc id="atlas-description">Una parábola cobalto con una línea de simetría dorada y un vértice coral. Solo tres anotaciones breves, colocadas en zonas libres y conectadas con líneas guía cortas cuando lo necesitan.</desc>
  <rect width="760" height="480" rx="24" fill="#f5f7fb"/>
  <rect x="28" y="24" width="704" height="432" rx="18" fill="#ffffff"/>
  <g font-family="Inter,Segoe UI,Arial,sans-serif">
    <text x="72" y="72" font-size="13" font-weight="850" letter-spacing="2.4" fill="#155eef">ATLAS / 01</text>
    <text x="72" y="108" font-size="30" font-weight="850" letter-spacing="-.5" fill="#101828">Función cuadrática</text>
    <text x="72" y="134" font-size="15" font-weight="650" fill="#667085">La forma permite localizar el mínimo de un vistazo.</text>
    <path d="M72 152H148" stroke="#155eef" stroke-width="4" stroke-linecap="round"/>
    <text x="688" y="73" text-anchor="end" font-size="12" font-weight="800" letter-spacing="1.2" fill="#667085">LECTURA VISUAL · ESO</text>
    <text x="688" y="104" text-anchor="end" font-size="17" font-weight="800" fill="#101828">f(x) = (x − 1)² − 2</text>
  </g>
  <g fill="none" stroke="#cfd8e6" stroke-width="1.35" stroke-linecap="round">${xTicks}${yTicks}</g>
  <g fill="none" stroke="#101828" stroke-width="2.35" stroke-linecap="round" stroke-linejoin="round">
    <path d="M132 290H638l-12-8M638 290l-12 8"/>
    <path d="M280 402V174l-8 13M280 174l8 13"/>
  </g>
  <path d="M162 198 C224 303 291 352 350 352 C409 352 477 303 558 198" fill="none" stroke="#155eef" stroke-width="4.5" stroke-linecap="round"/>
  <path d="M350 190V392" fill="none" stroke="#d97706" stroke-width="2" stroke-dasharray="6 8"/>
  <circle cx="350" cy="352" r="7" fill="#e23d2f" stroke="#ffffff" stroke-width="3"/>
  <!-- Label 1: direct and clear of the curve. -->
  <g font-family="Inter,Segoe UI,Arial,sans-serif">
    <text data-label="function" x="533" y="185" font-size="18" font-weight="850" fill="#155eef">f(x)</text>
    <path d="M539 190L551 202" stroke="#155eef" stroke-width="1.8" stroke-linecap="round"/>
    <!-- Label 2: above the dashed axis, outside the plot's dense area. -->
    <text data-label="axis" x="367" y="194" font-size="14" font-weight="850" letter-spacing=".6" fill="#a85f00">EJE: x = 1</text>
    <!-- Label 3: external callout with a short, uncrossed leader. -->
    <path d="M357 357L386 379" stroke="#e23d2f" stroke-width="1.8" stroke-linecap="round"/>
    <text data-label="vertex" x="394" y="385" font-size="16" font-weight="850" fill="#e23d2f">V(1, −2)</text>
    <text x="650" y="297" font-size="20" font-weight="850" fill="#101828">x</text>
    <text x="292" y="191" font-size="20" font-weight="850" fill="#101828">y</text>
  </g>
  <path d="M72 416H688" stroke="#e4e9f1" stroke-width="1"/>
  <g font-family="Inter,Segoe UI,Arial,sans-serif">
    <text x="72" y="442" font-size="14" font-weight="850" letter-spacing=".3" fill="#e23d2f">↓ DECRECE</text>
    <text x="252" y="442" font-size="14" font-weight="750" fill="#667085">hasta el vértice</text>
    <text x="504" y="442" font-size="14" font-weight="850" letter-spacing=".3" fill="#155eef">↑ CRECE</text>
  </g>
</svg>`;

fs.writeFileSync(path.join(outputDir, 'atlas-refined.svg'), svg, 'utf8');
fs.writeFileSync(path.join(root, '_audit_scratch', 'atlas_refined.html'), `<!doctype html><html lang="es"><meta charset="utf-8"><title>Atlas refinado</title><style>body{margin:0;min-height:100vh;display:grid;place-items:center;background:#eaf0f7;font-family:Inter,Segoe UI,Arial,sans-serif}main{width:min(920px,94vw)}h1{margin:0 0 8px;color:#101828;font-size:28px}p{margin:0 0 22px;color:#475467}img{display:block;width:100%;height:auto;border-radius:18px;box-shadow:0 18px 45px rgba(16,24,40,.12)}</style><main><h1>Atlas — lectura priorizada</h1><p>Una curva, un eje de simetría, un vértice y tres anotaciones sin colisión.</p><img src="atlas_refined/atlas-refined.svg" alt="Atlas refinado: gráfica de una función cuadrática"></main></html>`, 'utf8');
console.log(path.join(outputDir, 'atlas-refined.svg'));
