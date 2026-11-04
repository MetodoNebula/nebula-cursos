# -*- coding: utf-8 -*-
"""Ensambla (EN EL DISPOSITIVO) la leccion 'Ejercicios de selectividad (PAU)'
en cada bundle de selectividad_fisica y anade la entrada al catalog.json.
Escribe los ficheros EN SITIO de forma atomica. Idempotente.
Lee los ejercicios por bloque desde out/<suffix>.json (lista de exam_question)."""
import json, os, sys, re, tempfile
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.dirname(HERE)
BUN=os.path.join(ROOT,'bundles')
OUT=os.path.join(HERE,'out')
CAT=os.path.join(ROOT,'catalog.json')

# suffix(bundle y catalog unit id) -> (unit_id de la leccion, course_label)
META={
 'fundamentos':        ('fundamentos','Selectividad Física'),
 'campo_gravitatorio': ('U-FIS-GRAV','Física 2.º Bachillerato · Campo gravitatorio'),
 'mas':                ('fis_mas','Física 2.º Bachillerato · Vibraciones y ondas'),
 'ondas':              ('U-FIS-OND','Física 2.º Bachillerato · Ondas'),
 'electromagnetismo':  ('U-FIS-EM','Física 2.º Bachillerato · Campo eléctrico y campo magnético'),
 'optica':             ('U-FIS-OPT','Física 2.º Bachillerato · Óptica'),
 'relatividad':        ('U-FIS-REL','Física 2.º Bachillerato · Física relativista'),
 'cuantica':           ('U-FIS-CUAN','Física 2.º Bachillerato · Física cuántica'),
 'nuclear':            ('U-FIS-NUC','Física 2.º Bachillerato · Física nuclear'),
}
ORDER=['fundamentos','campo_gravitatorio','mas','ondas','electromagnetismo','optica','relatividad','cuantica','nuclear']
TITULO="Ejercicios de selectividad (PAU)"
BKEY="99_Ejercicios_de_selectividad_PAU.json"

def balanced(s): return len(re.findall(r'(?<!\\)\$',s))%2==0

def build_lesson(suffix,exs):
    unit_id,course_label=META[suffix]
    intro={"id":"TH-FPAU-%s-1"%suffix,"type":"intuition",
      "title":"Cómo usar este banco de problemas de Selectividad",
      "body":("Esta lección reúne **problemas y cuestiones reales de las pruebas de acceso a la universidad "
              "(PAU/Selectividad)** de varias comunidades autónomas (Madrid, Comunidad Valenciana, Andalucía, "
              "Cantabria y Murcia), correspondientes a este bloque.\n\nCada ejercicio está **resuelto paso a paso, "
              "a modo de entrega de examen**: planteamiento, desarrollo con todos los cálculos y respuesta final. "
              "Despliega «Ver solución» solo después de haberlo intentado por tu cuenta.\n\nEl encabezado de cada "
              "ejercicio indica la **comunidad y la convocatoria** de procedencia."),
      "concept_ids":[],"objective_ids":["LO-FPAU-%s-1"%suffix],"provenance":"PAU","scope":"CORE"}
    objs=[
      {"id":"LO-FPAU-%s-1"%suffix,"statement":"Resolver problemas y cuestiones de Selectividad del bloque aplicando el método paso a paso exigido en la corrección de la PAU.","bloom":"aplicar","concept_ids":[]},
      {"id":"LO-FPAU-%s-2"%suffix,"statement":"Plantear las leyes físicas en forma simbólica antes de sustituir, cuidando unidades, vectores y cifras significativas.","bloom":"analizar","concept_ids":[]},
      {"id":"LO-FPAU-%s-3"%suffix,"statement":"Reconocer los tipos de pregunta recurrentes del bloque y los errores típicos que penalizan en el examen.","bloom":"evaluar","concept_ids":[]},
    ]
    summary={"big_idea":"La mejor preparación para la PAU es resolver exámenes reales del bloque y comparar tu desarrollo con una solución modelo.",
      "key_points":["Lee el enunciado y separa los datos (lo conocido) de las incógnitas (lo que pide).",
        "Plantea la ley física en símbolos y despeja antes de sustituir números.",
        "Cuida unidades del SI, carácter vectorial y cifras significativas en el resultado final."],
      "takeaway":"Practicar con problemas reales de distintas comunidades cubre toda la variedad de preguntas del bloque."}
    return {"id":"LPAU","title":TITULO,"subject":"Física","course_label":course_label,
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
    proj=[p for p in cat['projects'] if p['key']=='selectividad_fisica'][0]
    ubd={u['id']:u for u in proj['units']}
    total=0
    for suffix in ORDER:
        p=os.path.join(OUT,"%s.json"%suffix)
        if not os.path.exists(p): report.append("[%s] SIN FICHERO -> omito"%suffix); continue
        exs=json.load(open(p,encoding='utf-8'))
        if not exs: report.append("[%s] 0 ejercicios -> omito"%suffix); continue
        # validacion minima
        seen=set(); verr=[]
        for e in exs:
            for fld in ('id','title','statement','full_solution','answer'):
                if not e.get(fld): verr.append((e.get('id'),'falta',fld))
            if e.get('id') in seen: verr.append((e.get('id'),'dup',''))
            seen.add(e.get('id'))
            for fld in ('statement','full_solution','answer'):
                v=e.get(fld,'')
                if isinstance(v,str) and not balanced(v): verr.append((e.get('id'),'$impar',fld))
        if verr: ok=False; report.append("[%s] FALLOS: %s"%(suffix,verr[:6])); continue
        les=build_lesson(suffix,exs)
        bfn="selectividad_fisica__%s.json"%suffix
        bpath=os.path.join(BUN,bfn)
        b=json.load(open(bpath,encoding='utf-8'))
        b[BKEY]=les
        atomic_write(bpath,b)
        u=ubd[suffix]
        u['lecciones']=[l for l in u['lecciones'] if l.get('bkey')!=BKEY]
        nmax=max([l.get('n',0) for l in u['lecciones']]+[0])
        u['lecciones'].append({"n":nmax+1,"titulo":TITULO,"dificultad":4,"duracion":"variable",
                               "bundle":"bundles/%s"%bfn,"bkey":BKEY})
        total+=len(exs); report.append("[%s] %d ejercicios -> %s"%(suffix,len(exs),bfn))
    atomic_write(CAT,cat)
    print("\n".join(report)); print("TOTAL:",total,"| RESULTADO:","OK" if ok else "CON FALLOS")
    return 0 if ok else 2
if __name__=='__main__': sys.exit(main())
