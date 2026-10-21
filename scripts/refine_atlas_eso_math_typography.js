/*
 * Refines typography in the already scoped Math ESO Atlas assets.
 *
 * This is intentionally a source-only pass over `eso_matematicas__*.json`:
 * GCSE, Selectividad and encrypted delivery bundles are excluded by design.
 */
'use strict';

const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const bundlesDir = path.join(root, 'bundles');
const fontStack = 'Albert Sans,Segoe UI,Arial,Helvetica,sans-serif';
const bundleNames = fs.readdirSync(bundlesDir)
  .filter((name) => /^eso_matematicas__.*\.json$/i.test(name))
  .sort();

const stats = { bundles: 0, svgs: 0, changed: 0, fontFamilies: 0, weights: { to600: 0, to700: 0 } };

function refineSvg(svg) {
  if (!svg.includes('data-nebula-atlas=')) return svg;
  let changed = false;
  let next = svg.replace(/font-family="[^"]*"/g, (attribute) => {
    if (attribute === `font-family="${fontStack}"`) return attribute;
    stats.fontFamilies += 1;
    changed = true;
    return `font-family="${fontStack}"`;
  });
  // The hierarchy is concise: 600 for all diagram labels; 700 only for the
  // two top-level headings in the reviewed coordinate-plane example.
  next = next.replace(/font-weight="(?:700|750)"/g, () => {
    stats.weights.to600 += 1;
    changed = true;
    return 'font-weight="600"';
  });
  next = next.replace(/font-weight="(?:800|850)"/g, () => {
    stats.weights.to700 += 1;
    changed = true;
    return 'font-weight="700"';
  });
  if (!changed) return svg;
  return next;
}

function visit(value) {
  if (!value || typeof value !== 'object') return;
  if (typeof value.svg === 'string' && value.svg.includes('<svg')) {
    stats.svgs += 1;
    const next = refineSvg(value.svg);
    if (next !== value.svg) {
      value.svg = next;
      stats.changed += 1;
    }
  }
  for (const child of Object.values(value)) visit(child);
}

for (const bundleName of bundleNames) {
  const target = path.join(bundlesDir, bundleName);
  const source = fs.readFileSync(target, 'utf8');
  const bundle = JSON.parse(source);
  visit(bundle);
  const output = `${JSON.stringify(bundle, null, 2)}\n`;
  if (output !== source) fs.writeFileSync(target, output, 'utf8');
  stats.bundles += 1;
}

console.log(JSON.stringify(stats, null, 2));
