// Diagnóstico temporal: comprueba si algún "bundle" de una lección apunta a un
// archivo cuyo prefijo (el curso que cifrar.js usaría para la clave) no
// coincide con el "key" real del proyecto al que pertenece esa lección.
// Uso: node _debug_bundle_course_match.js
'use strict';
const fs = require('fs');
const cat = JSON.parse(fs.readFileSync('catalog.json', 'utf8'));

function courseOfBundle(rel){
  const base = rel.replace(/^bundles\//, '').replace(/\.json$/, '');
  const m = base.match(/^(.+?)__/);
  return m ? m[1] : null;
}

let mismatches = 0, total = 0;
for (const p of cat.projects){
  const seen = new Set();
  for (const u of p.units || []){
    for (const l of u.lecciones || []){
      total++;
      const c = courseOfBundle(l.bundle);
      if (c !== p.key) {
        mismatches++;
        const key = c + ' -> ' + p.key;
        if (!seen.has(key)){
          seen.add(key);
          console.log(`DESAJUSTE  proyecto="${p.key}"  bundle="${l.bundle}"  curso_detectado="${c}"`);
        }
      }
    }
  }
}
console.log(`\nTotal lecciones: ${total}, con desajuste: ${mismatches}`);
