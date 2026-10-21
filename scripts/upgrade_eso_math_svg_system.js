/*
 * Applies the Nebula mathematical-visual system to inline SVG assets.
 * The script is deliberately idempotent: it can safely be run again after
 * editing lessons, and it only touches bundles/eso_matematicas__*.json.
 */
'use strict';

const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const bundlesDir = path.join(root, 'bundles');
const requestedAssets = process.argv.slice(2)
  .filter((argument) => argument.startsWith('--asset='))
  .map((argument) => argument.slice('--asset='.length));
const selectedByBundle = new Map();
for (const asset of requestedAssets) {
  const match = asset.match(/^([\w-]+):(\d+)$/);
  if (!match) throw new Error(`Invalid --asset value "${asset}". Use bundle-name:svg-number.`);
  const [, bundle, index] = match;
  if (!selectedByBundle.has(bundle)) selectedByBundle.set(bundle, new Set());
  selectedByBundle.get(bundle).add(Number(index));
}

const bundleNames = fs.readdirSync(bundlesDir)
  .filter((name) => /^eso_matematicas__.*\.json$/i.test(name) && !/foundations/i.test(name))
  .filter((name) => !selectedByBundle.size || selectedByBundle.has(path.basename(name, '.json')))
  .sort();

const stats = { bundles: 0, svgs: 0, cards: 0, named: 0, axesWithNewTicks: 0 };

function xmlEscape(value) {
  return String(value)
    .replace(/&(?!#(?:x[0-9a-f]+|\d+);|[a-z]+;)/gi, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function idPart(value) {
  return String(value).normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-z0-9]+/gi, '-').replace(/(^-|-$)/g, '').toLowerCase();
}

function attributes(source) {
  const result = {};
  for (const match of source.matchAll(/([:\w-]+)="([^"]*)"/g)) result[match[1]] = match[2];
  return result;
}

function number(value) {
  const parsed = Number.parseFloat(value);
  return Number.isFinite(parsed) ? parsed : null;
}

function lineSegments(svg) {
  return [...svg.matchAll(/<line\b([^>]*?)(?:\/>|><\/line>)/g)].map((match) => {
    const attr = attributes(match[1]);
    return {
      x1: number(attr.x1), y1: number(attr.y1), x2: number(attr.x2), y2: number(attr.y2),
      stroke: attr.stroke, marker: attr['marker-end'],
    };
  }).filter((line) => [line.x1, line.y1, line.x2, line.y2].every(Number.isFinite));
}

function hasTicks(axis, allLines, horizontal) {
  return allLines.some((line) => {
    const short = horizontal ? Math.abs(line.x2 - line.x1) <= 12 && Math.abs(line.y2 - line.y1) >= 4
      : Math.abs(line.y2 - line.y1) <= 12 && Math.abs(line.x2 - line.x1) >= 4;
    if (!short) return false;
    const atAxis = horizontal
      ? Math.abs(line.y1 - axis.y1) <= 4 || Math.abs(line.y2 - axis.y1) <= 4
      : Math.abs(line.x1 - axis.x1) <= 4 || Math.abs(line.x2 - axis.x1) <= 4;
    return atAxis;
  });
}

function tickMarkup(svg) {
  if (svg.includes('data-nebula-auto-ticks')) return '';
  const lines = lineSegments(svg);
  const navy = lines.filter((line) => line.stroke === '#0b1f3a');
  const horizontal = navy.filter((line) => Math.abs(line.y2 - line.y1) < 0.01 && Math.abs(line.x2 - line.x1) >= 160);
  const vertical = navy.filter((line) => Math.abs(line.x2 - line.x1) < 0.01 && Math.abs(line.y2 - line.y1) >= 140);
  let hAxis;
  let vAxis;
  let best = -1;
  for (const h of horizontal) {
    for (const v of vertical) {
      const within = v.x1 >= Math.min(h.x1, h.x2) - 2 && v.x1 <= Math.max(h.x1, h.x2) + 2
        && h.y1 >= Math.min(v.y1, v.y2) - 2 && h.y1 <= Math.max(v.y1, v.y2) + 2;
      if (!within) continue;
      const score = Math.abs(h.x2 - h.x1) + Math.abs(v.y2 - v.y1);
      if (score > best) { best = score; hAxis = h; vAxis = v; }
    }
  }
  if (!hAxis || !vAxis || (hasTicks(hAxis, lines, true) && hasTicks(vAxis, lines, false))) return '';

  const parts = [];
  if (!hasTicks(hAxis, lines, true)) {
    const left = Math.min(hAxis.x1, hAxis.x2);
    const right = Math.max(hAxis.x1, hAxis.x2);
    for (let i = 1; i <= 4; i += 1) {
      const x = left + ((right - left) * i) / 5;
      if (Math.abs(x - vAxis.x1) < 10) continue;
      parts.push(`<line x1="${x.toFixed(1)}" y1="${(hAxis.y1 - 3.5).toFixed(1)}" x2="${x.toFixed(1)}" y2="${(hAxis.y1 + 3.5).toFixed(1)}"/>`);
    }
  }
  if (!hasTicks(vAxis, lines, false)) {
    const top = Math.min(vAxis.y1, vAxis.y2);
    const bottom = Math.max(vAxis.y1, vAxis.y2);
    for (let i = 1; i <= 4; i += 1) {
      const y = top + ((bottom - top) * i) / 5;
      if (Math.abs(y - hAxis.y1) < 10) continue;
      parts.push(`<line x1="${(vAxis.x1 - 3.5).toFixed(1)}" y1="${y.toFixed(1)}" x2="${(vAxis.x1 + 3.5).toFixed(1)}" y2="${y.toFixed(1)}"/>`);
    }
  }
  return parts.length ? `<g data-nebula-auto-ticks="true" aria-hidden="true" fill="none" stroke="#0b1f3a" stroke-width="1.1" opacity="0.72">${parts.join('')}</g>` : '';
}

function upgradeSvg(svg, metadata) {
  if (svg.includes('data-nebula-card="v2"')) return svg;
  const opening = svg.match(/^<svg\b([^>]*)>/);
  if (!opening) throw new Error(`SVG without an opening element: ${metadata.id}`);
  const rootAttributes = opening[1];
  const viewBox = rootAttributes.match(/viewBox="([-\d.]+)\s+([-\d.]+)\s+([\d.]+)\s+([\d.]+)"/);
  if (!viewBox) throw new Error(`SVG without a viewBox: ${metadata.id}`);
  const [, minX, minY, width, height] = viewBox.map(Number);
  const titleId = `nebula-${metadata.id}-title`;
  const descId = `nebula-${metadata.id}-desc`;
  const label = metadata.alt || metadata.caption || 'Diagrama matemático';
  const description = metadata.purpose || metadata.caption || label;

  let attrs = rootAttributes
    .replace(/\saria-labelledby="[^"]*"/g, '')
    .replace(/\saria-label="[^"]*"/g, '');
  attrs += ` aria-labelledby="${titleId} ${descId}"`;
  attrs += ' data-nebula-card="v2"';
  let result = svg.replace(/^<svg\b[^>]*>/, `<svg${attrs}>`);

  result = result.replace(/<title(?:\s[^>]*)?>[\s\S]*?<\/title>/, '');
  const semantic = `<title id="${titleId}">${xmlEscape(label)}</title><desc id="${descId}">${xmlEscape(description)}</desc>`;
  result = result.replace(/^<svg\b[^>]*>/, (tag) => `${tag}${semantic}`);

  const innerX = minX + 6;
  const innerY = minY + 6;
  const innerWidth = width - 12;
  const innerHeight = height - 12;
  const railStart = innerX + 18;
  const railY = innerY + 12;
  const panel = `<g data-nebula-card="v2" aria-hidden="true"><rect x="${innerX}" y="${innerY}" width="${innerWidth}" height="${innerHeight}" rx="12" fill="#fbfcfd" stroke="#d8e2ec" stroke-width="1"/><path d="M${railStart},${railY} H${railStart + 34}" stroke="#0b1f3a" stroke-width="3"/><circle cx="${railStart + 44}" cy="${railY}" r="3" fill="#b77916"/><circle cx="${railStart + 56}" cy="${railY}" r="3" fill="#d65d4b"/></g>`;
  // Several legacy diagrams have a second full-size paper rectangle immediately
  // after the semantic background. Put the panel after it, so the rail is not
  // hidden while all diagram content remains above the panel.
  const background = /<rect\b[^>]*data-nebula-background="true"[^>]*\/>/.exec(result);
  if (background) {
    let insertionAt = background.index + background[0].length;
    const nextRect = result.slice(insertionAt).match(/^<rect\b(?=[^>]*\bfill="#f6f8fb")[^>]*\/>/);
    if (nextRect) insertionAt += nextRect[0].length;
    result = `${result.slice(0, insertionAt)}${panel}${result.slice(insertionAt)}`;
  }

  const ticks = tickMarkup(result);
  if (ticks) {
    result = result.replace(/<\/svg>$/, `${ticks}</svg>`);
    stats.axesWithNewTicks += 1;
  }
  stats.cards += 1;
  stats.named += 1;
  return result;
}

function visit(value, context) {
  if (Array.isArray(value)) return value.map((item, index) => visit(item, { ...context, index }));
  if (!value || typeof value !== 'object') return value;
  if (typeof value.svg === 'string' && value.svg.includes('<svg')) {
    context.counter.value += 1;
    const selected = selectedByBundle.get(context.bundle);
    if (selected && !selected.has(context.counter.value)) {
      for (const [key, child] of Object.entries(value)) value[key] = visit(child, { ...context, key });
      return value;
    }
    value.svg = upgradeSvg(value.svg, {
      id: `${idPart(context.bundle)}-${context.counter.value}`,
      alt: value.alt,
      caption: value.caption,
      purpose: value.purpose,
    });
    stats.svgs += 1;
  }
  for (const [key, child] of Object.entries(value)) value[key] = visit(child, { ...context, key });
  return value;
}

for (const bundleName of bundleNames) {
  const target = path.join(bundlesDir, bundleName);
  const counter = { value: 0 };
  const source = fs.readFileSync(target, 'utf8');
  const data = JSON.parse(source);
  visit(data, { bundle: path.basename(bundleName, '.json'), counter });
  const output = `${JSON.stringify(data, null, 2)}\n`;
  if (output !== source) fs.writeFileSync(target, output, 'utf8');
  stats.bundles += 1;
}

console.log(JSON.stringify(stats, null, 2));
