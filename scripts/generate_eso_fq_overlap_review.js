/* Renders the Física y Química ESO SVGs that need a human layout review. */
'use strict';

const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..');
const bundles = path.join(root, 'bundles');
const targets = new Set(['U-ESO-01:2', 'U-ESO-01:4', 'U-ESO-01:7', 'U-ESO-02:7', 'U-ESO-02:8', 'U-ESO-02:9', 'U-ESO-02:10', 'U-ESO-02:12', 'U-ESO-04:2', 'U-ESO-04:3', 'U-ESO-04:4', 'foundations:9']);
const cards = [];
for (const name of fs.readdirSync(bundles).filter((file) => /^eso_fisicaquimica__.*\.json$/i.test(file)).sort()) {
  const data = JSON.parse(fs.readFileSync(path.join(bundles, name), 'utf8'));
  const unit = name.replace(/^eso_fisicaquimica__/, '').replace(/\.json$/, '');
  let ordinal = 0;
  (function walk(value) {
    if (!value || typeof value !== 'object') return;
    if (typeof value.svg === 'string' && value.svg.includes('<svg')) {
      ordinal += 1;
      const key = `${unit}:${ordinal}`;
      if (targets.has(key)) cards.push(`<article><h2>${key}</h2>${value.svg}</article>`);
    }
    Object.values(value).forEach(walk);
  })(data);
}
const html = `<!doctype html><html lang="es"><meta charset="utf-8"><title>Revisión de composición · FyQ ESO</title><style>body{margin:0;padding:28px;background:#eef2f1;color:#24312c;font:16px Segoe UI,system-ui,sans-serif}h1{margin:0 0 8px}p{margin:0 0 24px;color:#5c6b67}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}article{padding:18px;background:white;border-radius:16px;box-shadow:0 8px 24px #24312c12}h2{font-size:14px;margin:0 0 12px;color:#0e7a68}svg{display:block;width:100%;height:auto}</style><h1>Física y Química ESO · revisión de composición</h1><p>Solo candidatos detectados por la auditoría automática; se valida visualmente antes de corregir.</p><main class="grid">${cards.join('')}</main></html>`;
const out = path.join(root, '_audit_scratch', 'eso_fq_overlap_review.html');
fs.writeFileSync(out, html, 'utf8');
console.log(out);
