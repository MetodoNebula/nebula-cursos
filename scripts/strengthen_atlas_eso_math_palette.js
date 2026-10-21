/* Applies the high-contrast academic Atlas palette to Math ESO SVGs only. */
'use strict';

const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const bundlesDir = path.join(root, 'bundles');
const names = fs.readdirSync(bundlesDir).filter((name) => /^eso_matematicas__.*\.json$/i.test(name)).sort();

// Each accent has a teaching function: blue = focus, teal = construction or
// positive progression, coral = contrast/error, gold = key relationship.
const palette = new Map([
  ['#f6f8fc', '#f5f8fc'],
  ['#fbfcfd', '#f8fafc'],
  ['#e4eaf0', '#d9e2ec'],
  ['#0f7b6c', '#007c72'],
  ['#a85f00', '#b54708'],
  ['#e23d2f', '#d92d20'],
  ['#6d28d9', '#5b21b6'],
  ['#101828', '#0b1f3a'],
  ['#667085', '#334e68'],
  ['#475467', '#243b53'],
  ['#cdd8e7', '#c4d3e3'],
  ['#e4e9f1', '#d9e2ec'],
]);
const stats = { bundles: 0, svgs: 0, changed: 0, substitutions: 0 };

function updateSvg(svg) {
  if (!svg.includes('data-nebula-atlas=')) return svg;
  let next = svg;
  for (const [from, to] of palette) {
    const expression = new RegExp(from, 'gi');
    const matches = next.match(expression);
    if (matches) {
      stats.substitutions += matches.length;
      next = next.replace(expression, to);
    }
  }
  return next;
}

function visit(value) {
  if (!value || typeof value !== 'object') return;
  if (typeof value.svg === 'string' && value.svg.includes('<svg')) {
    stats.svgs += 1;
    const next = updateSvg(value.svg);
    if (next !== value.svg) {
      value.svg = next;
      stats.changed += 1;
    }
  }
  for (const child of Object.values(value)) visit(child);
}

for (const name of names) {
  const file = path.join(bundlesDir, name);
  const source = fs.readFileSync(file, 'utf8');
  const data = JSON.parse(source);
  visit(data);
  const output = `${JSON.stringify(data, null, 2)}\n`;
  if (output !== source) fs.writeFileSync(file, output, 'utf8');
  stats.bundles += 1;
}

console.log(JSON.stringify(stats, null, 2));
