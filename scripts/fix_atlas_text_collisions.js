/* Resolves every collision reported by the rendered Math ESO Atlas audit. */
'use strict';

const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..');
const bundlesDir = path.join(root, 'bundles');
const changes = new Map();

function replaceExact(source, from, to, label) {
  if (source.includes(from)) return source.replace(from, to);
  if (source.includes(to)) return source;
  throw new Error(`Expected collision pattern not found: ${label}`);
}

function updateBundle(name, transform) {
  const file = path.join(bundlesDir, name);
  const source = fs.readFileSync(file, 'utf8');
  const data = JSON.parse(source);
  let ordinal = 0;
  (function walk(value) {
    if (!value || typeof value !== 'object') return;
    if (typeof value.svg === 'string' && value.svg.includes('<svg')) {
      ordinal += 1;
      value.svg = transform(value.svg, ordinal);
    }
    Object.values(value).forEach(walk);
  })(data);
  const output = `${JSON.stringify(data, null, 2)}\n`;
  if (output !== source) fs.writeFileSync(file, output, 'utf8');
}

const growthUpFrom = '<text x="87.5" y="255" font-size="12px" fill="#0f7b6c" text-anchor="middle" font-family="Inter, Segoe UI, Arial, Helvetica, sans-serif" paint-order="stroke fill" stroke="#f6f8fc" stroke-width="2.5" stroke-linejoin="round" font-weight="700">Crec.</text><text x="87.5" y="270" font-size="14px" fill="#0f7b6c" text-anchor="middle" font-family="Inter, Segoe UI, Arial, Helvetica, sans-serif" paint-order="stroke fill" stroke="#f6f8fc" stroke-width="2.5" stroke-linejoin="round" font-weight="700">↑</text>';
const growthUpTo = '<text x="87.5" y="264" font-size="13px" fill="#0f7b6c" text-anchor="middle" font-family="Inter, Segoe UI, Arial, Helvetica, sans-serif" paint-order="stroke fill" stroke="#f6f8fc" stroke-width="2.5" stroke-linejoin="round" font-weight="700">↑ Crec.</text>';
const growthDownFrom = '<text x="200" y="255" font-size="12px" fill="#a85f00" text-anchor="middle" font-family="Inter, Segoe UI, Arial, Helvetica, sans-serif" paint-order="stroke fill" stroke="#f6f8fc" stroke-width="2.5" stroke-linejoin="round" font-weight="700">Decr.</text><text x="200" y="270" font-size="14px" fill="#a85f00" text-anchor="middle" font-family="Inter, Segoe UI, Arial, Helvetica, sans-serif" paint-order="stroke fill" stroke="#f6f8fc" stroke-width="2.5" stroke-linejoin="round" font-weight="700">↓</text>';
const growthDownTo = '<text x="200" y="264" font-size="13px" fill="#a85f00" text-anchor="middle" font-family="Inter, Segoe UI, Arial, Helvetica, sans-serif" paint-order="stroke fill" stroke="#f6f8fc" stroke-width="2.5" stroke-linejoin="round" font-weight="700">↓ Decr.</text>';

for (const bundle of ['eso_matematicas__mat_derivadas.json', 'eso_matematicas__mat_funciones_representacion.json']) {
  updateBundle(bundle, (svg, ordinal) => {
    const affected = (bundle.includes('derivadas') && [4, 9].includes(ordinal))
      || (bundle.includes('funciones_representacion') && ordinal === 5);
    if (!affected) return svg;
    let next = replaceExact(svg, growthUpFrom, growthUpTo, `${bundle}:${ordinal}:growth-up`);
    next = replaceExact(next, growthDownFrom, growthDownTo, `${bundle}:${ordinal}:growth-down`);
    changes.set(`${bundle}:${ordinal}`, 'combined growth labels');
    return next;
  });
}

for (const bundle of ['eso_matematicas__mat_familias_funciones.json', 'eso_matematicas__mat_funciones_representacion.json']) {
  updateBundle(bundle, (svg, ordinal) => {
    const affected = (bundle.includes('familias') && [2, 10].includes(ordinal))
      || (bundle.includes('funciones_representacion') && ordinal === 12);
    if (!affected) return svg;
    const from = '<text x="290" y="95" font-size="11px" fill="#0f7b6c" text-anchor="start" font-family="Inter, Segoe UI, Arial, Helvetica, sans-serif" paint-order="stroke fill" stroke="#f6f8fc" stroke-width="2.5" stroke-linejoin="round" font-weight="700">(3, 2)</text>';
    const to = '<text x="312" y="114" font-size="11px" fill="#0f7b6c" text-anchor="start" font-family="Inter, Segoe UI, Arial, Helvetica, sans-serif" paint-order="stroke fill" stroke="#f6f8fc" stroke-width="2.5" stroke-linejoin="round" font-weight="700">(3, 2)</text>';
    changes.set(`${bundle}:${ordinal}`, 'moved point coordinate');
    return replaceExact(svg, from, to, `${bundle}:${ordinal}:point-coordinate`);
  });
}

updateBundle('eso_matematicas__mat_familias_funciones.json', (svg, ordinal) => {
  if (ordinal !== 7) return svg;
  const from = '<text x="2" y="20" font-size="14px" fill="#0b1f3a" font-family="Inter, Segoe UI, Arial, Helvetica, sans-serif" paint-order="stroke fill" stroke="#f6f8fc" stroke-width="2.5" stroke-linejoin="round" font-weight="700">y</text>';
  const to = '<text x="2" y="12" font-size="14px" fill="#0b1f3a" font-family="Inter, Segoe UI, Arial, Helvetica, sans-serif" paint-order="stroke fill" stroke="#f6f8fc" stroke-width="2.5" stroke-linejoin="round" font-weight="700">y</text>';
  changes.set('eso_matematicas__mat_familias_funciones.json:7', 'moved y label');
  return replaceExact(svg, from, to, 'familias:7:y-label');
});

updateBundle('eso_matematicas__mat_sistemas_inecuaciones.json', (svg, ordinal) => {
  if (ordinal !== 3) return svg;
  const to = '<text x="275" y="158" font-size="12px" fill="#0f7b6c" font-family="Inter, Segoe UI, Arial, Helvetica, sans-serif" text-anchor="middle" paint-order="stroke fill" stroke="#f6f8fc" stroke-width="2.5" stroke-linejoin="round" font-weight="700">Región factible</text>';
  changes.set('eso_matematicas__mat_sistemas_inecuaciones.json:3', 'combined feasible-region label');
  if (svg.includes('>Región factible</text>')) return svg;
  const pair = /<text x="280" y="150" font-size="12px" fill="#0f7b6c" font-family="Inter, Segoe UI, Arial, Helvetica, sans-serif" text-anchor="middle" paint-order="stroke fill" stroke="#f6f8fc" stroke-width="2\.5" stroke-linejoin="round" font-weight="700">Región<\/text>\s*<text x="270" y="165" font-size="12px" fill="#0f7b6c" font-family="Inter, Segoe UI, Arial, Helvetica, sans-serif" text-anchor="middle" paint-order="stroke fill" stroke="#f6f8fc" stroke-width="2\.5" stroke-linejoin="round" font-weight="700">factible<\/text>/;
  if (!pair.test(svg)) throw new Error('Expected collision pattern not found: sistemas:3:region-label');
  return svg.replace(pair, to);
});

console.log(JSON.stringify({ fixes: [...changes.entries()] }, null, 2));
