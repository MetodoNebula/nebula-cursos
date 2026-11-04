# -*- coding: utf-8 -*-
import json,re,glob,os
from collections import defaultdict,OrderedDict
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
blocks=['fundamentos','campo_gravitatorio','mas','ondas','electromagnetismo','optica','relatividad','cuantica','nuclear']
# 1) load current LPAU exam_questions from bundles
B={}; allq=[]
for suf in blocks:
    b=json.load(open(os.path.join(ROOT,'bundles','selectividad_fisica__%s.json'%suf),encoding='utf-8'))
    qs=b['99_Ejercicios_de_selectividad_PAU.json']['exam_questions']
    B[suf]=qs
    for e in qs: e['_blk']=suf; allq.append(e)
byid={e['id']:e for e in allq}
print("loaded",len(allq),"exam_questions")

# 2) refresh ALL figure SVGs from svgs/*_final.json (recolored graphs + fixes)
allsvg={}
for f in glob.glob('svgs/G*_final.json'): allsvg.update(json.load(open(f,encoding='utf-8')))
nref=0
for e in allq:
    if e.get('assets') and e['id'] in allsvg:
        e['assets'][0]['svg']=allsvg[e['id']]; nref+=1
print("refreshed figure svgs:",nref)

def rep(iid,old,new,n=1):
    e=byid[iid]; 
    for fld in ('statement','full_solution','answer'):
        if old in e.get(fld,''):
            e[fld]=e[fld].replace(old,new); return True
    raise SystemExit("MISS %s :: %r"%(iid,old[:50]))

# 3) content fixes
rep('PAU-FIS-NUC-015', r'5{,}0\cdot10^{-6}\ \text{pg}', r'5{,}0\cdot10^{-3}\ \text{pg}')
e=byid['PAU-FIS-NUC-024']; e['full_solution']=e['full_solution'].replace(r'3{,}38\cdot10^{-23}',r'3{,}38\cdot10^{-20}')
rep('PAU-FIS-CUAN-033','dos transiciones de la serie de Balmer','dos transiciones electrónicas')
rep('PAU-FIS-OPT-030','real (misma lado contrario)','real (se forma al otro lado de la lente)')
# MAS-005 statement + solution
rep('PAU-FIS-MAS-005',
  '**(b)** Un rayo de luz penetra por la cara superior de un medio de índice $n_v = 1{,}5$ rodeado de agua ($n_a = 1{,}33$) y, tras refractarse, alcanza la cara lateral justo en el ángulo límite, saliendo paralelo a ella. Calcule el ángulo de incidencia máximo $\\alpha$ en la cara superior.',
  '**(b)** Un rayo de luz incide **desde el aire** sobre la cara superior de un bloque de vidrio ($n_v = 1{,}5$) cuya cara lateral está en contacto con **agua** ($n_a = 1{,}33$). Tras refractarse en la cara superior, el rayo alcanza la cara lateral justo en el ángulo límite (saliendo paralelo a ella). Calcule el ángulo de incidencia máximo $\\alpha$ en la cara superior.')
rep('PAU-FIS-MAS-005',
  '**(b)** Snell en la cara superior (incidencia $\\alpha$, refracción $\\beta$ desde la normal): $\\operatorname{sen}\\alpha = n_v\\operatorname{sen}\\left(\\tfrac{\\pi}{2}-\\beta\\right) = n_v\\cos\\beta$',
  '**(b)** Snell en la cara superior, con el rayo incidente **desde el aire** ($n=1$): $\\operatorname{sen}\\alpha = n_v\\operatorname{sen}\\left(\\tfrac{\\pi}{2}-\\beta\\right) = n_v\\cos\\beta$')
# EM-111 (d) sign fix
rep('PAU-FIS-EM-111',
  '**(d)** La fuerza eléctrica es conservativa: cuando el protón regresa a $A$ tiene la misma rapidez ($1000\\ \\text{m/s}$) pero sentido opuesto. Por tanto\n$$\\Delta p=m_p(-v_A)-m_p(v_A)=-2m_p v_A,$$',
  '**(d)** La fuerza eléctrica es conservativa: el protón llega a $A$ moviéndose hacia el origen (sentido $-x$) y, tras ser repelido, vuelve a pasar por $A$ con la misma rapidez pero en sentido $+x$. Tomando $+x$ como positivo, $\\vec p_i=-m_p v_A\\,\\vec\\imath$ y $\\vec p_f=+m_p v_A\\,\\vec\\imath$, luego\n$$\\Delta \\vec p=\\vec p_f-\\vec p_i=+2m_p v_A\\,\\vec\\imath,$$')
# EM-103 physics rewrite
e=byid['PAU-FIS-EM-103']
e['full_solution']=("El campo de cada hilo tiene módulo $B=\\dfrac{\\mu_0 I}{2\\pi r}$ y es tangente a las "
 "circunferencias centradas en el hilo (regla de la mano derecha). Para que el campo total se anule, "
 "$\\vec B_1$ y $\\vec B_2$ deben tener **igual módulo y sentidos opuestos**.\n\n"
 "- **Igual módulo:** como las corrientes son iguales, $B_1=B_2$ exige $r_1=r_2$, es decir, puntos "
 "equidistantes de ambos hilos (la mediatriz del segmento que los une).\n"
 "- **Sentidos opuestos:** sobre esa mediatriz, $\\vec B_1$ y $\\vec B_2$ solo son exactamente antiparalelos "
 "en el **punto medio** del segmento que une los hilos. En cualquier otro punto de la mediatriz ambos "
 "vectores forman un ángulo y su suma no se anula.\n\n"
 "Por tanto, para dos corrientes iguales y del mismo sentido, el campo magnético total se anula "
 "**únicamente en un punto: el punto medio del segmento que une los dos hilos**; no existe un lugar "
 "geométrico (recta) de cancelación.")
e['answer']=("El campo se anula en un **único punto**: el punto medio del segmento que une los dos hilos, "
 "donde $\\vec B_1$ y $\\vec B_2$ tienen igual módulo y sentidos opuestos. Para corrientes iguales y del "
 "mismo sentido no hay una recta de puntos de campo nulo.")
ce=e.get('common_errors',[])
ce=[c for c in ce if 'mediatriz' not in c.lower()]
ce.append("Creer que el campo se anula en toda la mediatriz: solo se anula en el punto medio del segmento que une los hilos.")
e['common_errors']=ce[:3] if len(ce)>3 else ce

# 4) remove CV Junio 2022 duplicates (keep lower id / figure-bearing)
remove={'PAU-FIS-GRAV-042','PAU-FIS-GRAV-041','PAU-FIS-OND-026','PAU-FIS-OND-028',
 'PAU-FIS-EM-051','PAU-FIS-EM-053','PAU-FIS-EM-055','PAU-FIS-EM-057','PAU-FIS-OPT-037',
 'PAU-FIS-REL-008','PAU-FIS-CUAN-020','PAU-FIS-NUC-022'}
allq=[e for e in allq if e['id'] not in remove]
print("removed",len(remove),"duplicates; remaining:",len(allq))

# 5) renumber per block (assets travel inside each problem)
CODE={'fundamentos':'FUND','campo_gravitatorio':'GRAV','mas':'MAS','ondas':'OND','electromagnetismo':'EM','optica':'OPT','relatividad':'REL','cuantica':'CUAN','nuclear':'NUC'}
bb=defaultdict(list)
for e in allq: bb[e['_blk']].append(e)
KEEP=['id','title','statement','knowns','full_solution','answer','common_errors','mark_scheme','marks','provenance','source','assets']
os.makedirs('out',exist_ok=True)
tot=0;figtot=0
for suf in blocks:
    items=sorted(bb[suf],key=lambda e:int(re.match(r'.*-(\d+)$',e['id']).group(1)))
    out=[]
    for i,e in enumerate(items,1):
        e['id']="PAU-FIS-%s-%03d"%(CODE[suf],i)
        out.append(OrderedDict((k,e[k]) for k in KEEP if k in e and e[k] not in (None,[],'')))
    json.dump(out,open('out/%s.json'%suf,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    f=sum(1 for x in out if x.get('assets')); tot+=len(out); figtot+=f
    print("  %-20s %3d ejercicios  %d figuras"%(suf,len(out),f))
print("TOTAL:",tot,"| figuras:",figtot)
