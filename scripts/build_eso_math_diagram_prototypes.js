/* Six concept-specific reference diagrams for the Math ESO visual system. */
'use strict';

const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..');
const bundles = path.join(root, 'bundles');
const font = 'Albert Sans,Segoe UI,Arial,Helvetica,sans-serif';
const ink = '#0b1f3a', blue = '#155eef', teal = '#007c72', gold = '#b54708', coral = '#d92d20', grid = '#d9e2ec', paper = '#f5f8fc';

function frame(id, title, desc, content) {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 300" width="440" height="300" role="img" aria-labelledby="${id}-title ${id}-desc" preserveAspectRatio="xMidYMid meet" focusable="false" data-nebula-atlas="prototype-v2">
<title id="${id}-title">${title}</title><desc id="${id}-desc">${desc}</desc>
<rect width="440" height="300" fill="${paper}"/>${content}</svg>`;
}

const prototypes = {
  'eso_matematicas__mat_funciones_representacion.json': {
    id: 'diag_004', svg: frame('nebula-parabola', 'Parábola con vértice y raíces', 'La curva corta el eje x en dos raíces y tiene un vértice mínimo.', `
<g font-family="${font}" font-weight="600"><text x="28" y="31" font-size="15" fill="${ink}">Una parábola se lee desde sus puntos clave</text><text x="28" y="52" font-size="11.5" fill="#334e68">raíces · vértice · eje de simetría</text></g>
<g stroke="${grid}" stroke-width="1"><path d="M74 78H396M74 118H396M74 158H396M74 198H396"/><path d="M114 68V238M174 68V238M234 68V238M294 68V238M354 68V238"/></g>
<g stroke="${ink}" stroke-width="1.8"><path d="M58 218H402"/><path d="M74 238V68"/></g><path d="M402 218l-8-4v8zM74 68l-4 8h8z" fill="${ink}"/>
<path d="M106 72Q220 432 334 72" fill="none" stroke="${blue}" stroke-width="3" stroke-linecap="round"/>
<path d="M220 85V218" stroke="${gold}" stroke-width="1.5" stroke-dasharray="5 5"/>
<g fill="${paper}" stroke="${coral}" stroke-width="2.5"><circle cx="160" cy="218" r="5"/><circle cx="280" cy="218" r="5"/></g><circle cx="220" cy="251" r="5" fill="${gold}"/>
<g font-family="${font}" font-weight="600" font-size="12"><text x="142" y="241" fill="${coral}">x₁</text><text x="283" y="241" fill="${coral}">x₂</text><text x="231" y="258" fill="${gold}">V(0, −2)</text><text x="229" y="102" fill="${gold}">eje de simetría</text><text x="368" y="212" fill="${ink}">x</text><text x="82" y="82" fill="${ink}">y</text><text x="306" y="131" fill="${blue}">y = ax² + bx + c</text></g>`)
  },
  'eso_matematicas__mat_derivadas.json': {
    id: 'diag_029', svg: frame('nebula-tangent', 'Derivada como pendiente de la tangente', 'Una recta tangente toca la curva en P y su pendiente describe la derivada en ese punto.', `
<g font-family="${font}" font-weight="600"><text x="28" y="31" font-size="15" fill="${ink}">La derivada mide la inclinación en un punto</text><text x="28" y="52" font-size="11.5" fill="#334e68">la recta tangente solo comparte una dirección local</text></g>
<g stroke="${grid}" stroke-width="1"><path d="M70 78H396M70 118H396M70 158H396M70 198H396"/><path d="M110 66V238M170 66V238M230 66V238M290 66V238M350 66V238"/></g>
<path d="M58 218H402M70 238V66" fill="none" stroke="${ink}" stroke-width="1.8"/><path d="M402 218l-8-4v8zM70 66l-4 8h8z" fill="${ink}"/>
<path d="M92 209C142 208 167 197 199 167S267 92 336 79" fill="none" stroke="${blue}" stroke-width="3" stroke-linecap="round"/>
<path d="M130 222L342 78" fill="none" stroke="${gold}" stroke-width="2" stroke-dasharray="7 5" stroke-linecap="round"/>
<circle cx="220" cy="146" r="6" fill="${coral}" stroke="#fff" stroke-width="2"/><path d="M226 141l42-30" stroke="${coral}" stroke-width="1.4"/>
<g font-family="${font}" font-weight="600" font-size="12"><text x="274" y="108" fill="${coral}">P: punto de contacto</text><text x="290" y="76" fill="${gold}">tangente</text><text x="305" y="133" fill="${blue}">f(x)</text><text x="351" y="212" fill="${ink}">x</text><text x="78" y="81" fill="${ink}">y</text><text x="31" y="272" font-size="13" fill="${ink}">f′(x) = pendiente de la recta tangente</text></g>`)
  },
  'eso_matematicas__mat_ecuaciones.json': {
    id: 'diag_mat_ecuaciones_balance', svg: frame('nebula-equation', 'Ecuación como equilibrio', 'Los dos miembros de una ecuación conservan el mismo valor.', `
<g font-family="${font}" font-weight="600"><text x="28" y="31" font-size="15" fill="${ink}">Resolver es conservar el equilibrio</text><text x="28" y="52" font-size="11.5" fill="#334e68">la misma operación se aplica a ambos miembros</text></g>
<text x="220" y="91" text-anchor="middle" font-family="${font}" font-size="22" font-weight="700" fill="${ink}">3x + 2 = 14</text>
<path d="M80 173H360" stroke="${ink}" stroke-width="3" stroke-linecap="round"/><path d="M220 173V225" stroke="${ink}" stroke-width="3"/><path d="M180 243H260L220 225Z" fill="${ink}"/>
<path d="M117 159l-13 14M117 187l-13-14M323 159l13 14M323 187l13-14" fill="none" stroke="${grid}" stroke-width="2"/>
<g font-family="${font}" font-weight="600" text-anchor="middle"><text x="140" y="148" font-size="18" fill="${teal}">3x + 2</text><text x="300" y="148" font-size="18" fill="${gold}">14</text><text x="220" y="272" font-size="13" fill="${coral}">− 2 en ambos lados → 3x = 12 → x = 4</text></g>`)
  },
  'eso_matematicas__mat_geometria_metrica.json': {
    id: 'diag_mat_geometria_metrica_pythagorean', svg: frame('nebula-pythagoras', 'Teorema de Pitágoras', 'En un triángulo rectángulo, el área del cuadrado de la hipotenusa equivale a la suma de las áreas de los cuadrados de los catetos.', `
<g font-family="${font}" font-weight="600"><text x="28" y="31" font-size="15" fill="${ink}">Pitágoras relaciona áreas, no solo longitudes</text><text x="28" y="52" font-size="11.5" fill="#334e68">en cualquier triángulo rectángulo</text></g>
<path d="M124 224L124 124L224 224Z" fill="#e7f2ff" stroke="${ink}" stroke-width="2.5"/><path d="M124 224h18v-18" fill="none" stroke="${ink}" stroke-width="2"/>
<path d="M124 124V74H224V224" fill="${blue}" fill-opacity=".16" stroke="${blue}" stroke-width="2"/>
<path d="M74 224V124H124V224" fill="${teal}" fill-opacity=".18" stroke="${teal}" stroke-width="2"/>
<path d="M224 224l70-70l-100-100l-70 70" fill="${gold}" fill-opacity=".18" stroke="${gold}" stroke-width="2"/>
<g font-family="${font}" font-size="14" font-weight="600"><text x="83" y="177" fill="${teal}">a²</text><text x="166" y="105" fill="${blue}">b²</text><text x="235" y="139" fill="${gold}">c²</text><text x="137" y="196" fill="${ink}">a</text><text x="176" y="232" fill="${ink}">b</text><text x="220" y="170" fill="${ink}">c</text></g>
<text x="314" y="255" text-anchor="middle" font-family="${font}" font-size="18" font-weight="700" fill="${ink}">a² + b² = c²</text>`)
  },
  'eso_matematicas__mat_probabilidad.json': {
    id: 'diag_mat_probabilidad_tree', svg: frame('nebula-tree', 'Árbol de probabilidades', 'El diagrama muestra dos extracciones independientes y la probabilidad conjunta de cada camino.', `
<g font-family="${font}" font-weight="600"><text x="28" y="31" font-size="15" fill="${ink}">Un árbol hace visibles los caminos posibles</text><text x="28" y="52" font-size="11.5" fill="#334e68">multiplica a lo largo del camino · suma resultados compatibles</text></g>
<g fill="none" stroke-width="2"><path d="M95 150L210 95M95 150L210 205" stroke="${blue}"/><path d="M210 95L338 70M210 95L338 125M210 205L338 175M210 205L338 230" stroke="${ink}"/></g>
<g stroke="#fff" stroke-width="3"><circle cx="95" cy="150" r="8" fill="${blue}"/><circle cx="210" cy="95" r="8" fill="${teal}"/><circle cx="210" cy="205" r="8" fill="${coral}"/><circle cx="338" cy="70" r="7" fill="${teal}"/><circle cx="338" cy="125" r="7" fill="${coral}"/><circle cx="338" cy="175" r="7" fill="${teal}"/><circle cx="338" cy="230" r="7" fill="${coral}"/></g>
<g font-family="${font}" font-size="12" font-weight="600"><text x="48" y="142" fill="${ink}">inicio</text><text x="150" y="108" fill="${blue}">cara · 1/2</text><text x="150" y="196" fill="${blue}">cruz · 1/2</text><text x="221" y="83" fill="${teal}">cara</text><text x="221" y="224" fill="${coral}">cruz</text><text x="350" y="75" fill="${teal}">CC · 1/4</text><text x="350" y="130" fill="${coral}">CX · 1/4</text><text x="350" y="180" fill="${teal}">XC · 1/4</text><text x="350" y="235" fill="${coral}">XX · 1/4</text></g>
<text x="220" y="274" text-anchor="middle" font-family="${font}" font-size="13" font-weight="600" fill="${gold}">P(dos caras) = 1/2 · 1/2 = 1/4</text>`)
  },
  'eso_matematicas__mat_estadistica_descriptiva.json': {
    id: 'diag_mat_estadistica_descriptiva_boxplot', svg: frame('nebula-boxplot', 'Diagrama de caja y bigotes', 'La caja contiene el 50 por ciento central de los datos; la línea interior es la mediana.', `
<g font-family="${font}" font-weight="600"><text x="28" y="31" font-size="15" fill="${ink}">La caja resume cómo se distribuyen los datos</text><text x="28" y="52" font-size="11.5" fill="#334e68">mínimo · Q1 · mediana · Q3 · máximo</text></g>
<path d="M65 205H385" stroke="${ink}" stroke-width="1.8"/><g stroke="${grid}" stroke-width="1"><path d="M85 202V211M145 202V211M205 202V211M265 202V211M325 202V211"/></g>
<path d="M95 150H145M295 150H355M95 137V163M355 137V163" fill="none" stroke="${ink}" stroke-width="2"/>
<rect x="145" y="120" width="150" height="60" fill="#e7f2ff" stroke="${blue}" stroke-width="2.5"/><path d="M220 120V180" stroke="${coral}" stroke-width="3"/>
<g font-family="${font}" font-size="12" font-weight="600" text-anchor="middle"><text x="95" y="110" fill="${ink}">mín.</text><text x="145" y="110" fill="${blue}">Q1</text><text x="220" y="108" fill="${coral}">mediana</text><text x="295" y="110" fill="${blue}">Q3</text><text x="355" y="110" fill="${ink}">máx.</text><text x="85" y="230" fill="#334e68">0</text><text x="145" y="230" fill="#334e68">5</text><text x="205" y="230" fill="#334e68">10</text><text x="265" y="230" fill="#334e68">15</text><text x="325" y="230" fill="#334e68">20</text></g>
<text x="220" y="270" text-anchor="middle" font-family="${font}" font-size="13" font-weight="600" fill="${gold}">La caja contiene el 50% central</text>`)
  }
};

function replaceAsset(value, target) {
  if (!value || typeof value !== 'object') return false;
  if (value.id === target.id && typeof value.svg === 'string') { value.svg = target.svg; return true; }
  return Object.values(value).some((child) => replaceAsset(child, target));
}

const result = [];
for (const [fileName, target] of Object.entries(prototypes)) {
  const file = path.join(bundles, fileName);
  const source = fs.readFileSync(file, 'utf8');
  const data = JSON.parse(source);
  if (!replaceAsset(data, target)) throw new Error(`Asset ${target.id} not found in ${fileName}`);
  fs.writeFileSync(file, `${JSON.stringify(data, null, 2)}\n`, 'utf8');
  result.push({ fileName, id: target.id });
}
console.log(JSON.stringify({ rebuilt: result }, null, 2));
