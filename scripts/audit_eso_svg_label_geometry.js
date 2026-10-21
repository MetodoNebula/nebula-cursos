/*
 * Emits a browser-run audit for text that intrudes into drawn SVG geometry.
 * It reports candidates rather than changing artwork: a label can legitimately
 * sit in a diagram, but every candidate must be visually reviewed.
 */
'use strict';

const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..');
const bundles = path.join(root, 'bundles');
const assets = [];
for (const file of fs.readdirSync(bundles).filter((name) => /^(eso_matematicas__|eso_fisicaquimica__).*\.json$/i.test(name)).sort()) {
  const data = JSON.parse(fs.readFileSync(path.join(bundles, file), 'utf8'));
  let ordinal = 0;
  (function walk(value) {
    if (!value || typeof value !== 'object') return;
    if (typeof value.svg === 'string' && value.svg.includes('<svg')) { ordinal += 1; assets.push({ id: `${file}:${ordinal}`, svg: value.svg }); }
    Object.values(value).forEach(walk);
  })(data);
}
const html = `<!doctype html><html><meta charset="utf-8"><body>${assets.map(({ id, svg }) => `<section data-asset="${id}">${svg}</section>`).join('')}<script>
const box=(e)=>{const b=e.getBBox(),m=e.getCTM(),p=[[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]].map(([x,y])=>new DOMPoint(x,y).matrixTransform(m));const xs=p.map(q=>q.x),ys=p.map(q=>q.y);return{x:Math.min(...xs),y:Math.min(...ys),w:Math.max(...xs)-Math.min(...xs),h:Math.max(...ys)-Math.min(...ys)}};
const overlap=(a,b)=>Math.max(0,Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x))*Math.max(0,Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y));
const leaf='path,polygon,polyline,circle,ellipse,rect'; const hits=[];
for(const section of document.querySelectorAll('section')){const svg=section.querySelector('svg');const canvas=box(svg);for(const text of svg.querySelectorAll('text')){const t=box(text);if(!t.w||!t.h)continue;for(const shape of svg.querySelectorAll(leaf)){if(shape.closest('defs,marker'))continue;const s=box(shape);if(!s.w||!s.h||s.w*s.h>canvas.w*canvas.h*.45)continue;const area=overlap(t,s);if(area>14)hits.push({asset:section.dataset.asset,text:text.textContent.trim(),shape:shape.tagName,area:+area.toFixed(1)});}}}
document.body.innerHTML='<pre>'+JSON.stringify({assets:${assets.length},candidates:hits})+'</pre>';
</script></body></html>`;
const out = path.join(root, '_audit_scratch', 'eso_label_geometry_audit.html');
fs.writeFileSync(out, html, 'utf8');
console.log(JSON.stringify({ assets: assets.length, out }, null, 2));
