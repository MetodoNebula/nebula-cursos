'use strict';
const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..');
const files = fs.readdirSync(path.join(root, 'bundles')).filter((name) => /^(eso_matematicas__|eso_fisicaquimica__).*\.json$/i.test(name)).sort();
const assets = [];
for (const file of files) {
  const data = JSON.parse(fs.readFileSync(path.join(root, 'bundles', file), 'utf8')); let ordinal = 0;
  (function walk(value) { if (!value || typeof value !== 'object') return; if (typeof value.svg === 'string' && value.svg.includes('<svg')) { ordinal += 1; assets.push({ id: `${file}:${ordinal}`, svg: value.svg }); } Object.values(value).forEach(walk); })(data);
}
const html = `<!doctype html><html><meta charset="utf-8"><body>${assets.map((asset) => `<section data-asset="${asset.id}">${asset.svg}</section>`).join('')}<script>
const bounds=e=>{const b=e.getBBox(),m=e.getCTM(),pts=[[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]].map(([x,y])=>new DOMPoint(x,y).matrixTransform(m));const xs=pts.map(p=>p.x),ys=pts.map(p=>p.y);return {t:e.textContent.trim(),x:Math.min(...xs),y:Math.min(...ys),w:Math.max(...xs)-Math.min(...xs),h:Math.max(...ys)-Math.min(...ys)}};
const overlaps=[];let labels=0;for(const s of document.querySelectorAll('section')){const a=[...s.querySelectorAll('svg text')].map(bounds);labels+=a.length;for(let i=0;i<a.length;i++)for(let j=i+1;j<a.length;j++){const p=a[i],q=a[j],w=Math.max(0,Math.min(p.x+p.w,q.x+q.w)-Math.max(p.x,q.x)),h=Math.max(0,Math.min(p.y+p.h,q.y+q.h)-Math.max(p.y,q.y));if(w*h>.5)overlaps.push({asset:s.dataset.asset,a:p.t,b:q.t,area:+(w*h).toFixed(2)})}}document.body.innerHTML='<pre>'+JSON.stringify({assets:${assets.length},labels,overlaps})+'</pre>';</script></body></html>`;
const out = path.join(root, '_audit_scratch', 'eso_math_fq_collision_audit.html'); fs.writeFileSync(out, html, 'utf8'); console.log(JSON.stringify({ assets: assets.length, out }, null, 2));
