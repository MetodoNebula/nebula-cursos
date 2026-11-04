# -*- coding: utf-8 -*-
"""Ensambla (EN EL DISPOSITIVO) la leccion 'Ejercicios de selectividad (PAU)' en
cada bundle de selectividad_matematicas_ccss y anade/actualiza la entrada en
catalog.json. Escribe EN SITIO de forma atomica. Idempotente.
Lee los ejercicios por bloque desde out/<suffix>.json (lista de exam_question).
El unit_id, course_label y subject se toman EXACTOS de la primera leccion del bundle."""
import json, os, sys, re, tempfile
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.dirname(HERE)                 # .../Nebula_Cursos_Web
BUN=os.path.join(ROOT,'bundles')
OUT=os.path.join(HERE,'out')
CAT=os.path.join(ROOT,'catalog.json')

# suffix == bundle suffix == catalog unit id. Block code for ids PAU-MCS-<BLQ>-NNN.
ORDER=['fundamentos','mat_matrices','mat_sistemas','mat_limites','mat_derivadas',
       'mat_representacion','mat_integrales','mat_probabilidad','mat_programacion_lineal',
       'mat_estadistica','mat_muestreo_inferencia']
BLQ={'fundamentos':'FUND','mat_matrices':'MAT','mat_sistemas':'SIS','mat_limites':'LIM',
     'mat_derivadas':'DER','mat_representacion':'REP','mat_integrales':'INT',
     'mat_probabilidad':'PROB','mat_programacion_lineal':'PL','mat_estadistica':'EST',
     'mat_muestreo_inferencia':'INF'}
TITULO="Ejercicios de selectividad (PAU)"
BKEY="99_Ejercicios_de_selectividad_PAU.json"

def balanced(s): return len(re.findall(r'(?<!\\)\$',s))%2==0

def first_lesson(bundle):
    for k,v in bundle.items():
        if isinstance(v,dict) and v.get('id'): return v
    return {}

def build_lesson(suffix, exs, meta):
    blq=BLQ[suffix]
    unit_id=meta['unit_id']; course_label=meta['course_label']; subject=meta.get('subject','Matemáticas CCSS')
    intro={"id":"TH-MCSPAU-%s-1"%blq,"type":"intuition",
      "title":"Cómo usar este banco de problemas de Selectividad",
      "body":("Esta lección reúne **problemas y cuestiones reales de las pruebas de acceso a la universidad "
              "(PAU/EBAU/Selectividad)** de distintas comunidades autónomas, correspondientes a este bloque.\n\n"
              "Cada ejercicio está **resuelto paso a paso, a modo de entrega de examen**: planteamiento, "
              "desarrollo con todos los cálculos y respuesta final. Intenta resolverlo por tu cuenta antes de "
              "desplegar la solución.\n\nEl encabezado de cada ejercicio indica la **comunidad y la convocatoria** "
              "de procedencia. Los enunciados en otras lenguas cooficiales se han traducido al español."),
      "concept_ids":[],"objective_ids":["LO-MCSPAU-%s-1"%blq],"provenance":"PAU","scope":"CORE"}
    objs=[
      {"id":"LO-MCSPAU-%s-1"%blq,"statement":"Resolver problemas y cuestiones de Selectividad del bloque aplicando el método paso a paso exigido en la corrección de la PAU.","bloom":"aplicar","concept_ids":[]},
      {"id":"LO-MCSPAU-%s-2"%blq,"statement":"Plantear el procedimiento en forma simbólica antes de operar, cuidando el rigor, las unidades y las cifras decimales.","bloom":"analizar","concept_ids":[]},
      {"id":"LO-MCSPAU-%s-3"%blq,"statement":"Reconocer los tipos de pregunta recurrentes del bloque y los errores típicos que penalizan en el examen.","bloom":"evaluar","concept_ids":[]},
    ]
    summary={"big_idea":"La mejor preparación para la PAU es resolver exámenes reales del bloque y comparar tu desarrollo con una solución modelo.",
      "key_points":["Lee el enunciado y separa los datos (lo conocido) de lo que se pide.",
        "Plantea el método (sistema, derivada, integral, región factible, intervalo…) antes de calcular.",
        "Cuida las cifras decimales (coma), las unidades y la coherencia del resultado final."],
      "takeaway":"Practicar con problemas reales de distintas comunidades cubre toda la variedad de preguntas del bloque."}
    return {"id":"LPAU","title":TITULO,"subject":subject,"course_label":course_label,
      "unit_id":unit_id,"estimated_length":"variable","estimated_difficulty":4,
      "objectives":objs,"prerequisites":[],"diagnostic_items":[],
      "theory_blocks":[intro],"keywords":[],
      "worked_examples":[],"guided_exercises":[],"exercises":[],
      "exam_questions":exs,"challenge_questions":[],"mcq":[],"flashcards":[],
      "misconceptions":[],"common_mistakes":[],"exam_notes":[],
      "summary":summary,"lang":"es","provenance":"PAU"}

def atomic_write(path,obj):
    s=json.dumps(obj,ensure_ascii=False,indent=1); json.loads(s)
    fd,tmp=tempfile.mkstemp(dir=os.path.dirname(path),suffix='.tmp'); os.close(fd)
    open(tmp,'w',encoding='utf-8').write(s); os.replace(tmp,path)

def main():
    report=[]; ok=True
    cat=json.load(open(CAT,encoding='utf-8'))
    if not (isinstance(cat,dict) and isinstance(cat.get('projects'),list)):
        sys.exit("catalog.json no tiene estructura {projects:[...]} — aborto")
    projs=[p for p in cat['projects'] if p['key']=='selectividad_matematicas_ccss']
    if not projs: sys.exit("no encuentro proyecto selectividad_matematicas_ccss")
    proj=projs[0]
    ubd={u['id']:u for u in proj['units']}
    total=0
    for suffix in ORDER:
        p=os.path.join(OUT,"%s.json"%suffix)
        if not os.path.exists(p): report.append("[%s] SIN FICHERO -> omito"%suffix); continue
        exs=json.load(open(p,encoding='utf-8'))
        if not exs: report.append("[%s] 0 ejercicios -> omito"%suffix); continue
        # min validation + reassign canonical ids
        seen=set(); verr=[]
        for idx,e in enumerate(exs,1):
            e.setdefault('provenance','PAU')
            e['id']="PAU-MCS-%s-%03d"%(BLQ[suffix],idx)
            for fld in ('title','statement','full_solution','answer'):
                if not e.get(fld): verr.append((e['id'],'falta',fld))
            for fld in ('statement','full_solution','answer'):
                v=e.get(fld,'')
                if isinstance(v,str) and not balanced(v): verr.append((e['id'],'$impar',fld))
        if verr: ok=False; report.append("[%s] FALLOS: %s"%(suffix,verr[:8])); continue
        bfn="selectividad_matematicas_ccss__%s.json"%suffix
        bpath=os.path.join(BUN,bfn)
        b=json.load(open(bpath,encoding='utf-8'))
        meta=first_lesson(b)
        les=build_lesson(suffix,exs,meta)
        b[BKEY]=les
        atomic_write(bpath,b)
        u=ubd.get(suffix)
        if u is None:
            ok=False; report.append("[%s] no hay unidad en catalog -> omito catalog"%suffix); continue
        u['lecciones']=[l for l in u['lecciones'] if l.get('bkey')!=BKEY]
        nmax=max([l.get('n',0) for l in u['lecciones']]+[0])
        u['lecciones'].append({"n":nmax+1,"titulo":TITULO,"dificultad":4,"duracion":"variable",
                               "bundle":"bundles/%s"%bfn,"bkey":BKEY})
        total+=len(exs); report.append("[%s] %d ejercicios -> %s"%(suffix,len(exs),bfn))
    atomic_write(CAT,cat)
    print("\n".join(report)); print("TOTAL:",total,"| RESULTADO:","OK" if ok else "CON FALLOS")
    return 0 if ok else 2
if __name__=='__main__': sys.exit(main())
