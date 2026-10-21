/* Applies the reusable Atlas visual system to Math ESO SVGs only.
 * It deliberately never traverses GCSE, Selectividad, or other course bundles. */
'use strict';

const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const bundlesDir = path.join(root, 'bundles');
const bundleNames = fs.readdirSync(bundlesDir)
  .filter((name) => /^eso_matematicas__.*\.json$/i.test(name))
  .sort();
const stats = { bundles: 0, svgs: 0, upgraded: 0, preservedCustom: 0 };

function xmlEscape(value) {
  return String(value || 'Diagrama matemático')
    .replace(/&(?!#(?:x[0-9a-f]+|\d+);|[a-z]+;)/gi, '&amp;')
    .replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function idPart(value) {
  return String(value).normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-z0-9]+/gi, '-').replace(/(^-|-$)/g, '').toLowerCase();
}

function enhanceText(match, rawAttributes) {
  let attrs = rawAttributes;
  // Albert Sans is already loaded by the course shell.  Segoe UI is the
  // high-quality local fallback for previews and offline rendering.
  if (!/\bfont-family=/.test(attrs)) attrs += ' font-family="Albert Sans,Segoe UI,Arial,Helvetica,sans-serif"';
  // Semibold is deliberately the default: it reads clearly without the
  // blocky, over-inked effect of a blanket bold treatment.
  if (!/\bfont-weight=/.test(attrs)) attrs += ' font-weight="600"';
  return `<text${attrs}>`;
}

function upgradeSvg(svg, metadata) {
  if (svg.includes('data-nebula-atlas="quadrants-v1"')) {
    stats.preservedCustom += 1;
    return svg;
  }
  if (svg.includes('data-nebula-atlas="system-v1"')) return svg;
  const opening = svg.match(/^<svg\b([^>]*)>/);
  if (!opening) throw new Error(`Missing SVG root: ${metadata.id}`);
  const titleId = `atlas-${metadata.id}-title`;
  const descId = `atlas-${metadata.id}-description`;
  const label = metadata.alt || metadata.caption || 'Diagrama matemático';
  const description = metadata.purpose || metadata.caption || label;
  let attrs = opening[1]
    .replace(/\saria-labelledby="[^"]*"/g, '')
    .replace(/\saria-label="[^"]*"/g, '')
    .replace(/\sdata-nebula-atlas="[^"]*"/g, '');
  if (!/\srole="img"/.test(attrs)) attrs += ' role="img"';
  if (!/\spreserveAspectRatio=/.test(attrs)) attrs += ' preserveAspectRatio="xMidYMid meet"';
  if (!/\sfocusable=/.test(attrs)) attrs += ' focusable="false"';
  attrs += ` aria-labelledby="${titleId} ${descId}" data-nebula-atlas="system-v1"`;

  let result = svg.replace(/^<svg\b[^>]*>/, `<svg${attrs}>`);
  result = result.replace(/<title(?:\s[^>]*)?>[\s\S]*?<\/title>/g, '');
  result = result.replace(/<desc(?:\s[^>]*)?>[\s\S]*?<\/desc>/g, '');
  result = result.replace(/^<svg\b[^>]*>/, (tag) => `${tag}<title id="${titleId}">${xmlEscape(label)}</title><desc id="${descId}">${xmlEscape(description)}</desc>`);

  // Atlas palette: deeper functional colors, never pale labels.
  result = result
    .replace(/#f6f8fb/gi, '#f5f8fc')
    .replace(/#2e7d5b/gi, '#007c72')
    .replace(/#d65d4b/gi, '#d92d20')
    .replace(/#b77916/gi, '#b54708')
    .replace(/#7952a3/gi, '#5b21b6');

  // Convert the standard full diagram canvas into a calm white Atlas surface.
  result = result.replace(/<rect width="400" height="300" fill="#f6f8fc"\s*\/>/i,
    '<rect width="400" height="300" rx="14" fill="#ffffff"/>');
  result = result.replace(/<text\b([^>]*)>/g, enhanceText);
  stats.upgraded += 1;
  return result;
}

function visit(value, context) {
  if (!value || typeof value !== 'object') return;
  if (typeof value.svg === 'string' && value.svg.includes('<svg')) {
    context.counter.value += 1;
    stats.svgs += 1;
    value.svg = upgradeSvg(value.svg, {
      id: `${idPart(context.bundle)}-${context.counter.value}`,
      alt: value.alt,
      caption: value.caption,
      purpose: value.purpose,
    });
  }
  for (const child of Object.values(value)) visit(child, context);
}

for (const bundleName of bundleNames) {
  const target = path.join(bundlesDir, bundleName);
  const source = fs.readFileSync(target, 'utf8');
  const data = JSON.parse(source);
  visit(data, { bundle: path.basename(bundleName, '.json'), counter: { value: 0 } });
  const output = `${JSON.stringify(data, null, 2)}\n`;
  if (output !== source) fs.writeFileSync(target, output, 'utf8');
  stats.bundles += 1;
}

console.log(JSON.stringify(stats, null, 2));
