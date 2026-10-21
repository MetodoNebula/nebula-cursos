/* Generates local render/audit pages from the current Math ESO source assets. */
'use strict';

const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..');
const bundlesDir = path.join(root, 'bundles');
const auditDir = path.join(root, '_audit_scratch');
const files = fs.readdirSync(bundlesDir).filter((name) => /^eso_matematicas__.*\.json$/i.test(name)).sort();
const assets = [];

for (const file of files) {
  const data = JSON.parse(fs.readFileSync(path.join(bundlesDir, file), 'utf8'));
  let ordinal = 0;
  (function walk(value) {
    if (!value || typeof value !== 'object') return;
    if (typeof value.svg === 'string' && value.svg.includes('<svg')) {
      ordinal += 1;
      assets.push({ id: `${file}:${ordinal}`, bundle: file, svg: value.svg });
    }
    Object.values(value).forEach(walk);
  })(data);
}

const sections = assets.map((asset) => `<section data-asset="${asset.id}">${asset.svg}</section>`).join('\n');
fs.writeFileSync(path.join(auditDir, 'math_eso_atlas_collision_audit.html'), `<!doctype html><html><meta charset="utf-8"><body>${sections}<script>
const all=[]; const overlaps=[];
for(const section of document.querySelectorAll('section')){
  const labels=[...section.querySelectorAll('svg text')].map(el=>{const b=el.getBBox();return {text:el.textContent.trim(),x:b.x,y:b.y,w:b.width,h:b.height};});
  all.push(labels.length);
  for(let i=0;i<labels.length;i+=1)for(let j=i+1;j<labels.length;j+=1){const a=labels[i],b=labels[j],w=Math.max(0,Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x)),h=Math.max(0,Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y));if(w*h>.5)overlaps.push({asset:section.dataset.asset,a:a.text,b:b.text,area:+(w*h).toFixed(2)});}
}
const pre=document.createElement('pre');pre.textContent=JSON.stringify({assets:all.length,labels:all.reduce((a,b)=>a+b,0),overlaps});document.body.replaceChildren(pre);
</script></body></html>`, 'utf8');

const samples = [];
for (const file of files) { const asset = assets.find((item) => item.bundle === file); if (asset) samples.push(asset); }
const cards = samples.map((asset) => `<figure><figcaption>${asset.bundle.replace('eso_matematicas__', '').replace('.json','')}</figcaption>${asset.svg}</figure>`).join('\n');
fs.writeFileSync(path.join(auditDir, 'math_eso_atlas_preview.html'), `<!doctype html><html lang="es"><meta charset="utf-8"><title>Atlas ESO Matemáticas</title><style>*{box-sizing:border-box}body{margin:0;padding:28px;background:#eaf0f7;font-family:"Albert Sans","Segoe UI",Arial,sans-serif;color:#101828}h1{margin:0 0 8px;font-weight:700}p{margin:0 0 24px;color:#475467}.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}figure{margin:0;padding:13px;background:#fff;border-radius:14px;box-shadow:0 9px 24px rgba(16,24,40,.09)}figcaption{margin:0 0 10px;font-size:13px;font-weight:600;word-break:break-word}svg{display:block;width:100%;height:auto}</style><h1>Matemáticas ESO · Atlas</h1><p>Una muestra por bloque de contenido.</p><main class="grid">${cards}</main></html>`, 'utf8');

console.log(JSON.stringify({ assets: assets.length, audit: path.join(auditDir, 'math_eso_atlas_collision_audit.html'), preview: path.join(auditDir, 'math_eso_atlas_preview.html') }, null, 2));
