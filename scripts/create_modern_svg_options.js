/* Review-only modern SVG directions. Course bundles are intentionally untouched. */
'use strict';

const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..');
const outputDir = path.join(root, '_audit_scratch', 'modern_options');
fs.mkdirSync(outputDir, { recursive: true });

const studies = [
  { file: '01-atlas.svg', name: 'Atlas', subtitle: 'Cobalto limpio', paper: '#ffffff', ink: '#101828', grid: '#dce5f0', primary: '#155eef', secondary: '#b54708', coral: '#e23d2f', soft: '#475467' },
  { file: '02-orion.svg', name: 'Orion', subtitle: 'Noche eléctrica', paper: '#0b1628', ink: '#f8fafc', grid: '#2a405e', primary: '#45e0c5', secondary: '#f8c34d', coral: '#ff6b57', soft: '#c7d2e3' },
  { file: '03-vega.svg', name: 'Vega', subtitle: 'Verde de señal', paper: '#f8fafc', ink: '#111827', grid: '#d6e1e7', primary: '#087f5b', secondary: '#155eef', coral: '#e23d2f', soft: '#475569' },
  { file: '04-pulse.svg', name: 'Pulse', subtitle: 'Violeta preciso', paper: '#fffdf9', ink: '#1f2937', grid: '#e6ddd4', primary: '#6d28d9', secondary: '#c2410c', coral: '#e11d48', soft: '#4b5563' },
];

function svg(theme) {
  const vertical = [130, 195, 260, 325, 390, 455, 520, 585].map((x) => `<line x1="${x}" y1="140" x2="${x}" y2="350"/>`).join('');
  const horizontal = [170, 230, 290, 350].map((y) => `<line x1="100" y1="${y}" x2="620" y2="${y}"/>`).join('');
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 440" width="720" height="440" role="img" aria-labelledby="title desc">
  <title id="title">${theme.name}: gráfico moderno de una función cuadrática</title>
  <desc id="desc">Parábola con ejes, eje de simetría, vértice e intervalos de crecimiento. Las etiquetas se expresan con tipografía gruesa y colores de alto contraste, sin cápsulas ni marcos decorativos.</desc>
  <rect width="720" height="440" fill="${theme.paper}"/>
  <text x="64" y="58" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="15" font-weight="900" letter-spacing="2" fill="${theme.primary}">${theme.name.toUpperCase()}</text>
  <text x="64" y="92" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="27" font-weight="900" fill="${theme.ink}">Función cuadrática</text>
  <text x="64" y="118" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="15" font-weight="700" fill="${theme.soft}">${theme.subtitle} · lee la forma antes de calcular</text>
  <path d="M64 132H154" stroke="${theme.primary}" stroke-width="6" stroke-linecap="round"/>
  <g fill="none" stroke="${theme.grid}" stroke-width="1.25">${vertical}${horizontal}</g>
  <g fill="none" stroke="${theme.ink}" stroke-width="3.25" stroke-linecap="round" stroke-linejoin="round">
    <path d="M100 290H634l-13-8M634 290l-13 8"/>
    <path d="M230 366V130l-8 14M230 130l8 14"/>
  </g>
  <path d="M120 155 C184 273 258 330 320 330 C382 330 456 273 540 155" fill="none" stroke="${theme.primary}" stroke-width="6" stroke-linecap="round"/>
  <path d="M320 148V350" fill="none" stroke="${theme.secondary}" stroke-width="2.5" stroke-dasharray="7 8"/>
  <circle cx="320" cy="330" r="8" fill="${theme.coral}" stroke="${theme.paper}" stroke-width="3"/>
  <g font-family="Inter,Segoe UI,Arial,sans-serif" font-weight="900">
    <text x="102" y="166" font-size="15" letter-spacing="1.1" fill="${theme.coral}">↓ DECRECE</text>
    <text x="494" y="364" font-size="15" letter-spacing="1.1" fill="${theme.primary}">↑ CRECE</text>
    <text x="496" y="186" font-size="18" fill="${theme.primary}">f(x)</text>
    <text x="344" y="337" font-size="16" fill="${theme.coral}">V(1, −2)</text>
    <text x="334" y="164" font-size="14" fill="${theme.secondary}">x = 1</text>
    <text x="645" y="298" font-size="20" fill="${theme.ink}">x</text>
    <text x="242" y="151" font-size="20" fill="${theme.ink}">y</text>
  </g>
  <text x="64" y="408" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="14" font-weight="800" letter-spacing=".5" fill="${theme.soft}">VÉRTICE · EJE DE SIMETRÍA · INTERVALOS DE VARIACIÓN</text>
</svg>`;
}

for (const study of studies) fs.writeFileSync(path.join(outputDir, study.file), svg(study), 'utf8');
const tiles = studies.map((study) => `<figure><figcaption>${study.name}<span>${study.subtitle}</span></figcaption><img src="modern_options/${study.file}" alt="${study.name}: ${study.subtitle}"></figure>`).join('');
fs.writeFileSync(path.join(root, '_audit_scratch', 'modern_options.html'), `<!doctype html><html lang="es"><meta charset="utf-8"><title>Direcciones modernas SVG</title><style>
*{box-sizing:border-box}body{margin:0;padding:34px;background:#eef2f6;color:#101828;font:16px Inter,Segoe UI,Arial,sans-serif}h1{margin:0 0 8px;font-size:30px;letter-spacing:-.4px}p{margin:0 0 28px;color:#475467}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px}figure{margin:0;background:#fff;border-radius:14px;padding:14px;box-shadow:0 10px 28px rgba(16,24,40,.10)}figcaption{margin:0 0 10px;font-size:18px;font-weight:900}figcaption span{margin-left:9px;color:#667085;font-size:14px;font-weight:700}img{display:block;width:100%;height:auto;border-radius:9px}</style>
<h1>Cuatro direcciones modernas</h1><p>Tipografía fuerte, color de señal y espacio en blanco. Sin cápsulas, sin bordes de tarjeta dentro del gráfico.</p><main class="grid">${tiles}</main></html>`, 'utf8');
console.log(JSON.stringify({ outputDir, files: studies.map((study) => study.file) }, null, 2));
