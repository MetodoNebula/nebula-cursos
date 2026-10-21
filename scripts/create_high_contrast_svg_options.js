/* Generates four high-contrast SVG style studies. These are review-only files:
 * they do not modify any course bundle. */
'use strict';

const fs = require('fs');
const path = require('path');

const outputDir = path.resolve(__dirname, '..', '_audit_scratch', 'high_contrast_options');
fs.mkdirSync(outputDir, { recursive: true });

const options = [
  {
    file: '01-atlas.svg', identity: 'ATLAS', name: 'Atlas · Tinta y Sol',
    page: '#f7f9fc', card: '#ffffff', frame: '#0b1f3a', grid: '#d6e1ec', axis: '#0b1f3a',
    curve: '#0d7a5f', point: '#e2533d', gold: '#c68100', text: '#0b1f3a', muted: '#40546b',
    top: '#0b1f3a', chip: '#0b1f3a', chipText: '#ffffff', secondaryChip: '#c68100',
    inverse: false,
  },
  {
    file: '02-orion.svg', identity: 'ORION', name: 'Orion · Observatorio oscuro',
    page: '#06172e', card: '#0b2545', frame: '#5eead4', grid: '#244466', axis: '#f8fafc',
    curve: '#5eead4', point: '#ff7a59', gold: '#ffd166', text: '#f8fafc', muted: '#c9d7e8',
    top: '#102f57', chip: '#f8fafc', chipText: '#06172e', secondaryChip: '#ffd166',
    inverse: true,
  },
  {
    file: '03-vega.svg', identity: 'VEGA', name: 'Vega · Cobalto y Coral',
    page: '#e8f1ff', card: '#ffffff', frame: '#155eef', grid: '#cbdcff', axis: '#102a56',
    curve: '#155eef', point: '#e64b35', gold: '#f4b000', text: '#102a56', muted: '#34527c',
    top: '#155eef', chip: '#102a56', chipText: '#ffffff', secondaryChip: '#e64b35',
    inverse: false,
  },
  {
    file: '04-pulse.svg', identity: 'PULSE', name: 'Pulse · Laboratorio Signal',
    page: '#fff7ed', card: '#fffdf9', frame: '#18212f', grid: '#ded7cf', axis: '#18212f',
    curve: '#7c3aed', point: '#e11d48', gold: '#d97706', text: '#18212f', muted: '#4b5563',
    top: '#18212f', chip: '#18212f', chipText: '#ffffff', secondaryChip: '#7c3aed',
    inverse: false,
  },
];

function pill(x, y, width, label, background, foreground) {
  return `<g><rect x="${x}" y="${y}" width="${width}" height="30" rx="15" fill="${background}"/><text x="${x + 14}" y="${y + 20}" font-size="14" font-weight="800" fill="${foreground}">${label}</text></g>`;
}

function svg(theme) {
  const grid = [150, 220, 290, 360, 430, 500, 570].map((x) => `<line x1="${x}" y1="132" x2="${x}" y2="354"/>`).join('')
    + [160, 220, 280, 340].map((y) => `<line x1="104" y1="${y}" x2="622" y2="${y}"/>`).join('');
  const labelBase = theme.inverse ? theme.chip : theme.chip;
  const labelText = theme.inverse ? theme.chipText : theme.chipText;
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 440" width="720" height="440" role="img" aria-labelledby="title desc">
  <title id="title">${theme.name}: representación de una función cuadrática</title>
  <desc id="desc">Una parábola con los ejes cartesianos, vértice, eje de simetría y una etiqueta de crecimiento. Todos los rótulos usan fondo sólido y alto contraste.</desc>
  <rect width="720" height="440" rx="24" fill="${theme.page}"/>
  <rect x="22" y="20" width="676" height="400" rx="20" fill="${theme.card}" stroke="${theme.frame}" stroke-width="2"/>
  <path d="M22 76H698" stroke="${theme.top}" stroke-width="56"/>
  <text x="52" y="66" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="22" font-weight="850" fill="#ffffff">${theme.identity} · FUNCIÓN CUADRÁTICA</text>
  <circle cx="650" cy="48" r="8" fill="${theme.gold}"/><circle cx="674" cy="48" r="8" fill="${theme.point}"/>
  <g fill="none" stroke="${theme.grid}" stroke-width="1.4">${grid}</g>
  <rect x="104" y="132" width="518" height="222" fill="none" stroke="${theme.grid}" stroke-width="1.4"/>
  <g stroke="${theme.axis}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path d="M104 300H632l-12-7M632 300l-12 7"/>
    <path d="M220 366V120l-7 12M220 120l7 12"/>
    <path d="M120 148 C185 274 260 332 320 332 C380 332 455 274 540 148" stroke="${theme.curve}" stroke-width="5"/>
    <path d="M320 144V354" stroke="${theme.gold}" stroke-width="2.5" stroke-dasharray="8 8"/>
  </g>
  <g fill="${theme.axis}"><path d="M290 296v8M360 296v8M430 296v8M216 240h8M216 180h8"/></g>
  <circle cx="320" cy="332" r="8" fill="${theme.point}" stroke="${theme.card}" stroke-width="3"/>
  <path d="M327 327L365 308" stroke="${theme.point}" stroke-width="2.5"/>
  ${pill(365, 290, 118, 'V(1, −2)', labelBase, labelText)}
  ${pill(458, 102, 138, 'Eje: x = 1', theme.secondaryChip, theme.inverse ? '#06172e' : '#ffffff')}
  ${pill(448, 226, 148, 'f(x) = (x−1)²−2', labelBase, labelText)}
  ${pill(118, 103, 156, '↓ DECRECE', theme.point, '#ffffff')}
  ${pill(454, 368, 142, '↑ CRECE', theme.curve, theme.inverse ? '#06172e' : '#ffffff')}
  <text x="641" y="319" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="19" font-weight="850" fill="${theme.axis}">x</text>
  <text x="232" y="158" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="19" font-weight="850" fill="${theme.axis}">y</text>
  <text x="52" y="402" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="14" font-weight="750" fill="${theme.muted}">VÉRTICE · EJE DE SIMETRÍA · INTERVALOS DE VARIACIÓN</text>
</svg>`;
}

for (const option of options) fs.writeFileSync(path.join(outputDir, option.file), svg(option), 'utf8');

const cards = options.map((option) => `<figure><figcaption>${option.name}</figcaption><img src="high_contrast_options/${option.file}" alt="${option.name}"></figure>`).join('\n');
fs.writeFileSync(path.resolve(__dirname, '..', '_audit_scratch', 'high_contrast_options.html'), `<!doctype html>
<html lang="es"><meta charset="utf-8"><title>Opciones SVG Nebula</title><style>
*{box-sizing:border-box}body{margin:0;padding:32px;background:#e9eff5;color:#0b1f3a;font:16px Inter,Segoe UI,Arial,sans-serif}h1{margin:0 0 8px;font-size:28px}p{margin:0 0 28px;color:#40546b}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:26px}figure{margin:0;padding:18px;background:#fff;border:1px solid #d7e1ec;border-radius:18px;box-shadow:0 14px 34px rgba(11,31,58,.10)}figcaption{margin:0 0 12px;font-size:17px;font-weight:850}img{display:block;width:100%;height:auto;border-radius:12px}</style>
<h1>Cuatro direcciones de alto contraste</h1><p>Mismo contenido pedagógico, distinto lenguaje visual. Todas usan texto con soporte opaco y colores de señal.</p><main class="grid">${cards}</main></html>`, 'utf8');

console.log(JSON.stringify({ outputDir, files: options.map((option) => option.file) }, null, 2));
