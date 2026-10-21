/* Rebuilds two target diagrams with the Selectividad Física visual grammar. */
'use strict';

const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..');
const font = "'Segoe UI',system-ui,-apple-system,sans-serif";
const ink = '#24312c', teal = '#0e7a68', gold = '#c17a17', plum = '#8a3d6b', muted = '#5c6b67';

const balance = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 245" width="380" height="245" role="img" aria-labelledby="math-balance-title math-balance-desc" preserveAspectRatio="xMidYMid meet" focusable="false" data-nebula-style="physics-selectivity-v1">
  <title id="math-balance-title">Ecuación como una balanza en equilibrio</title><desc id="math-balance-desc">Una balanza equilibrada representa la ecuación tres x más dos igual a catorce.</desc>
  <text x="70" y="38" fill="${ink}" font-size="16" font-weight="700" text-anchor="middle" style="font-family:${font}">3x + 2</text>
  <text x="190" y="40" fill="${ink}" font-size="20" font-weight="700" text-anchor="middle" style="font-family:${font}">=</text>
  <text x="310" y="38" fill="${ink}" font-size="16" font-weight="700" text-anchor="middle" style="font-family:${font}">14</text>
  <line x1="190" y1="76" x2="190" y2="178" stroke="${ink}" stroke-width="3"/>
  <polygon points="166,205 214,205 190,178" fill="${ink}"/>
  <line x1="70" y1="76" x2="310" y2="76" stroke="${ink}" stroke-width="4" stroke-linecap="round"/>
  <line x1="70" y1="76" x2="70" y2="110" stroke="${ink}" stroke-width="1.5"/>
  <path d="M36 110H104L93 148Q70 158 47 148Z" fill="#d9efe8" stroke="${teal}" stroke-width="2.2" stroke-linejoin="round"/>
  <line x1="310" y1="76" x2="310" y2="110" stroke="${ink}" stroke-width="1.5"/>
  <path d="M276 110H344L333 148Q310 158 287 148Z" fill="#fbe8cf" stroke="${gold}" stroke-width="2.2" stroke-linejoin="round"/>
  <path d="M116 220H264" stroke="#d6e2df" stroke-width="1.3"/>
  <path d="M132 220v-7M248 220v-7" stroke="${plum}" stroke-width="1.8"/>
  <text x="190" y="233" fill="${muted}" font-size="12.5" font-weight="600" text-anchor="middle" style="font-family:${font}">misma operación en ambos lados</text>
</svg>`;

const filtration = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 270" width="400" height="270" role="img" aria-labelledby="filter-title filter-desc" preserveAspectRatio="xMidYMid meet" focusable="false" data-nebula-style="physics-selectivity-v1">
  <title id="filter-title">Filtración de una mezcla heterogénea</title><desc id="filter-desc">La mezcla atraviesa un embudo con papel de filtro. El sólido queda retenido y el líquido se recoge como filtrado.</desc>
  <defs><marker id="filter-arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0 0L6 3L0 6Z" fill="${muted}"/></marker></defs>
  <path d="M42 65V151Q42 164 55 164H115Q128 164 128 151V65" fill="none" stroke="${ink}" stroke-width="2.2"/>
  <path d="M44 111H126V150Q126 161 115 161H55Q44 161 44 150Z" fill="#fbe8cf" fill-opacity=".9"/>
  <path d="M42 65H128" stroke="${ink}" stroke-width="2.2"/>
  <circle cx="65" cy="128" r="3.2" fill="${plum}"/><circle cx="82" cy="139" r="3.2" fill="${plum}"/><circle cx="102" cy="123" r="3.2" fill="${plum}"/><circle cx="111" cy="145" r="3.2" fill="${plum}"/>
  <path d="M138 112C156 103 171 96 184 91" fill="none" stroke="${muted}" stroke-width="1.8" marker-end="url(#filter-arrow)"/>
  <path d="M166 72H258L240 168H184Z" fill="#d9efe8" fill-opacity=".65" stroke="${teal}" stroke-width="2.4" stroke-linejoin="round"/>
  <path d="M175 82H249L239 145H185Z" fill="#fff" stroke="${muted}" stroke-width="1.2" stroke-dasharray="3 3"/>
  <path d="M212 168V194" stroke="${teal}" stroke-width="2.5"/>
  <path d="M212 194C212 198 208 202 208 208" fill="none" stroke="${teal}" stroke-width="2.2"/>
  <circle cx="194" cy="126" r="3" fill="${plum}"/><circle cx="207" cy="134" r="3" fill="${plum}"/><circle cx="220" cy="121" r="3" fill="${plum}"/><circle cx="230" cy="138" r="3" fill="${plum}"/>
  <path d="M167 151H257" stroke="${gold}" stroke-width="2"/>
  <path d="M179 208V239Q179 251 191 251H249Q261 251 261 239V208L252 194H188Z" fill="none" stroke="${ink}" stroke-width="2.2" stroke-linejoin="round"/>
  <path d="M181 226H259V239Q259 249 249 249H191Q181 249 181 239Z" fill="#d9efe8" fill-opacity=".9"/>
  <path d="M286 84L253 110" fill="none" stroke="${muted}" stroke-width="1.2"/><text x="292" y="80" fill="${teal}" font-size="12.5" font-weight="700" style="font-family:${font}">embudo + filtro</text>
  <path d="M287 143L239 143" fill="none" stroke="${muted}" stroke-width="1.2"/><text x="292" y="147" fill="${plum}" font-size="12.5" font-weight="700" style="font-family:${font}">residuo</text>
  <path d="M289 222L261 228" fill="none" stroke="${muted}" stroke-width="1.2"/><text x="294" y="226" fill="${teal}" font-size="12.5" font-weight="700" style="font-family:${font}">filtrado</text>
  <text x="85" y="185" fill="${gold}" font-size="12" font-weight="600" text-anchor="middle" style="font-family:${font}">mezcla</text>
  <text x="200" y="268" fill="${muted}" font-size="11.5" font-weight="600" text-anchor="middle" style="font-family:${font}">el sólido queda retenido · el líquido atraviesa el filtro</text>
</svg>`;

function updateById(file, id, svg) {
  const source = fs.readFileSync(file, 'utf8'); const data = JSON.parse(source); let found = false;
  (function walk(value) { if (!value || typeof value !== 'object') return; if (value.id === id && typeof value.svg === 'string') { value.svg = svg; found = true; return; } Object.values(value).forEach(walk); })(data);
  if (!found) throw new Error(`Missing ${id}`); fs.writeFileSync(file, `${JSON.stringify(data, null, 2)}\n`, 'utf8');
}
function updateByOrdinal(file, ordinal, svg) {
  const source = fs.readFileSync(file, 'utf8'); const data = JSON.parse(source); let count = 0; let found = false;
  (function walk(value) { if (!value || typeof value !== 'object' || found) return; if (typeof value.svg === 'string' && value.svg.includes('<svg')) { count += 1; if (count === ordinal) { value.svg = svg; found = true; return; } } Object.values(value).forEach(walk); })(data);
  if (!found) throw new Error(`Missing SVG ${ordinal}`); fs.writeFileSync(file, `${JSON.stringify(data, null, 2)}\n`, 'utf8');
}

updateById(path.join(root, 'bundles', 'eso_matematicas__mat_ecuaciones.json'), 'diag_mat_ecuaciones_balance', balance);
updateByOrdinal(path.join(root, 'bundles', 'eso_fisicaquimica__U-ESO-03.json'), 3, filtration);
console.log(JSON.stringify({ updated: ['eso_matematicas__mat_ecuaciones:balance', 'eso_fisicaquimica__U-ESO-03:filtration'] }, null, 2));
