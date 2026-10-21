/*
 * Removes UI-like text containers from the already rebuilt Math ESO SVGs.
 * Rounded shapes that explain a quantity (for example, a layered percentage
 * bar) are retained.  This pass never visits GCSE or Selectividad bundles.
 */
'use strict';

const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const bundlesDir = path.join(root, 'bundles');
const names = fs.readdirSync(bundlesDir).filter((name) => /^eso_matematicas__.*\.json$/i.test(name)).sort();
const number = (value) => Number.parseFloat(value);
const attr = (source, name) => {
  const match = source.match(new RegExp(`\\b${name}="([^"]+)"`, 'i'));
  return match ? match[1] : undefined;
};
const stats = { bundles: 0, svgs: 0, changed: 0, textOutlinesRemoved: 0, decorativeContainersRemoved: 0 };

function simplify(svg) {
  if (!svg.includes('data-nebula-atlas=')) return svg;
  let next = svg;

  // Strong ink text on a calm background needs no white halo. Removing it
  // gives formulas the precise, editorial feeling of a textbook diagram.
  next = next.replace(/<text\b([^>]*)>/g, (tag, attributes) => {
    const clean = attributes
      .replace(/\spaint-order="stroke fill"/gi, '')
      .replace(/\sstroke="#f5f8fc"/gi, '')
      .replace(/\sstroke-width="2\.5"/gi, '')
      .replace(/\sstroke-linejoin="round"/gi, '');
    if (clean !== attributes) stats.textOutlinesRemoved += 1;
    return `<text${clean}>`;
  });

  const rects = [...next.matchAll(/<rect\b([^>]*)\/>/g)].map((match) => ({
    whole: match[0], attrs: match[1], x: number(attr(match[1], 'x') || 0), y: number(attr(match[1], 'y') || 0),
    width: number(attr(match[1], 'width')), height: number(attr(match[1], 'height')), rx: attr(match[1], 'rx'),
  }));
  const texts = [...next.matchAll(/<text\b([^>]*)>/g)].map((match) => ({
    x: number(attr(match[1], 'x')), y: number(attr(match[1], 'y')),
  })).filter((point) => Number.isFinite(point.x) && Number.isFinite(point.y));

  const removals = new Set();
  for (const rect of rects) {
    if (!rect.rx || !Number.isFinite(rect.width) || !Number.isFinite(rect.height)) continue;
    // Canvas surfaces and mathematical plot areas are not text containers.
    if (rect.width >= 380 || rect.height >= 180 || rect.attrs.includes('data-nebula-background')) continue;
    // A duplicated origin is a layered quantitative bar, not a UI pill.
    if (rects.some((other) => other !== rect && other.x === rect.x && other.y === rect.y)) continue;
    const containsText = texts.some((point) => point.x >= rect.x - 4 && point.x <= rect.x + rect.width + 4 && point.y >= rect.y + 3 && point.y <= rect.y + rect.height + 10);
    if (containsText) removals.add(rect.whole);
  }
  for (const element of removals) {
    next = next.replace(element, '');
    stats.decorativeContainersRemoved += 1;
  }
  return next;
}

function visit(value) {
  if (!value || typeof value !== 'object') return;
  if (typeof value.svg === 'string' && value.svg.includes('<svg')) {
    stats.svgs += 1;
    const next = simplify(value.svg);
    if (next !== value.svg) { value.svg = next; stats.changed += 1; }
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
