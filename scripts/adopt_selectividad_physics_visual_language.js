/*
 * Applies the visual language used by Selectividad Física to ESO Matemáticas
 * and ESO Física y Química only. It never traverses Selectividad bundles.
 */
'use strict';

const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..');
const bundlesDir = path.join(root, 'bundles');
const selected = fs.readdirSync(bundlesDir)
  .filter((name) => /^(eso_matematicas__|eso_fisicaquimica__).*\.json$/i.test(name))
  .sort();
const palette = new Map([
  ['#2e7d5b', '#0e7a68'], ['#0f7b6c', '#0e7a68'], ['#007c72', '#0e7a68'], ['#155eef', '#0e7a68'],
  ['#b77916', '#c17a17'], ['#a85f00', '#c17a17'], ['#b54708', '#c17a17'],
  ['#d65d4b', '#b4483b'], ['#e23d2f', '#b4483b'], ['#d92d20', '#b4483b'],
  ['#7952a3', '#8a3d6b'], ['#6d28d9', '#8a3d6b'], ['#5b21b6', '#8a3d6b'],
  ['#0b1f3a', '#24312c'], ['#101828', '#24312c'], ['#20302a', '#24312c'],
  ['#334e68', '#5c6b67'], ['#243b53', '#5c6b67'], ['#475467', '#5c6b67'], ['#667085', '#5c6b67'], ['#5a6b62', '#5c6b67'],
  ['#d9e2ec', '#e8e3d8'], ['#e4eaf0', '#e8e3d8'], ['#cdd8e7', '#e8e3d8'], ['#e4e9f1', '#e8e3d8'],
  ['#f6f8fb', '#ffffff'], ['#f5f8fc', '#ffffff'], ['#fbfcfd', '#ffffff']
]);
const stats = { bundles: 0, svgs: 0, changed: 0, backgroundsRemoved: 0, textHalosRemoved: 0, paletteSubstitutions: 0 };

function updateSvg(svg) {
  let next = svg;
  // The Selectividad Física figures sit directly on the course canvas.
  next = next.replace(/<rect\b(?=[^>]*data-nebula-background="true")[^>]*\/>/gi, () => { stats.backgroundsRemoved += 1; return ''; });
  next = next.replace(/<rect\b(?=[^>]*\bwidth="400")(?=[^>]*\bheight="300")[^>]*(?:fill="(?:#ffffff|var\(--bg, #fbfcfd\))")[^>]*\/>/gi, () => { stats.backgroundsRemoved += 1; return ''; });
  next = next.replace(/<text\b([^>]*)>/gi, (tag, attributes) => {
    const clean = attributes
      .replace(/\spaint-order="stroke fill"/gi, '')
      .replace(/\sstroke="#(?:f6f8fb|f5f8fc|ffffff)"/gi, '')
      .replace(/\sstroke-width="2\.5"/gi, '')
      .replace(/\sstroke-linejoin="round"/gi, '');
    if (clean !== attributes) stats.textHalosRemoved += 1;
    return `<text${clean}>`;
  });
  next = next
    .replace(/font-family="[^"]*"/gi, 'font-family="Segoe UI,system-ui,-apple-system,sans-serif"')
    .replace(/font-family\s*:\s*[^;"']+(?=;|["'])/gi, "font-family:'Segoe UI',system-ui,-apple-system,sans-serif")
    .replace(/font-weight="(?:750|800|850|bold)"/gi, 'font-weight="700"');
  for (const [from, to] of palette) {
    const expression = new RegExp(from, 'gi'); const found = next.match(expression);
    if (found) { stats.paletteSubstitutions += found.length; next = next.replace(expression, to); }
  }
  next = next.replace(/^<svg\b([^>]*)>/i, (tag, attrs) => {
    const without = attrs.replace(/\sdata-nebula-visual-language="[^"]*"/gi, '');
    return `<svg${without} data-nebula-visual-language="physics-selectivity-v1">`;
  });
  return next;
}
function visit(value) {
  if (!value || typeof value !== 'object') return;
  if (typeof value.svg === 'string' && value.svg.includes('<svg')) {
    stats.svgs += 1; const next = updateSvg(value.svg);
    if (next !== value.svg) { value.svg = next; stats.changed += 1; }
  }
  for (const child of Object.values(value)) visit(child);
}
for (const name of selected) {
  const file = path.join(bundlesDir, name); const source = fs.readFileSync(file, 'utf8'); const data = JSON.parse(source);
  visit(data); const output = `${JSON.stringify(data, null, 2)}\n`;
  if (output !== source) fs.writeFileSync(file, output, 'utf8'); stats.bundles += 1;
}
console.log(JSON.stringify(stats, null, 2));
