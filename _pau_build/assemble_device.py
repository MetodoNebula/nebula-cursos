# -*- coding: utf-8 -*-
"""Ensambla (EN EL DISPOSITIVO) la lección 'Ejercicios de selectividad (PAU)'
en cada bundle de selectividad_quimica y añade la entrada al catalog.json.
Escribe los ficheros EN SITIO de forma atómica. Idempotente."""
import json, os, sys, glob, re, tempfile

ROOT="/home/%s/mnt/Nebula_GPT_Cowork/Nebula_Cursos_Web"%os.environ.get('USER','')
# fallback: deducir ROOT desde este script (está en ROOT/_pau_build)
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.dirname(HERE)
BUN=os.path.join(ROOT,'bundles')
OUT=os.path.join(HERE,'out')
CAT=os.path.join(ROOT,'catalog.json')

META={
 'U00':('U00_Fundamentos','U00_Fundamentos','Química · 2º Bachillerato · Fundamentos'),
 'U01':('U01_Estequiometria','U-QUI-01-ESTEQUIOMETRIA','Química · 2º Bachillerato · Estequiometría'),
 'U02':('U02_Estructura_Atomica','U-QUI-02-ESTRUCTURA-ATOMICA','Química · 2º Bachillerato · Estructura atómica y clasificación periódica'),
 'U03':('U03_Enlace','U-QUI-03-ENLACE','Química · 2º Bachillerato · Enlace químico y propiedades de las sustancias'),
 'U04':('U04_Termoquimica','U-QUI-04-TERMOQUIMICA','Química · 2º Bachillerato · Transformaciones energéticas y espontaneidad'),
 'U05':('U05_Equilibrio','U-QUI-05-EQUILIBRIO','Química · 2º Bachillerato · Cinética y equilibrio químico'),
 'U06':('U06_Acido_Base','U-QUI-06-ACIDO-BASE','Química · 2º Bachillerato · Ácidos y bases'),
 'U07':('U07_Electroquimica','U-QUI-07-ELECTROQUIMICA','Química · 2º Bachillerato · Electroquímica'),
 'U08':('U08_Organica','U-QUI-08-ORGANICA','Química · 2º Bachillerato · Química del carbono e isomería'),
}
TITULO="Ejercicios de selectividad (PAU)"
BKEY="99_Ejercicios_de_selectividad_PAU.json"
ORDER=['U00','U01','U02','U03','U04','U05','U06','U07','U08']

def balanced_dollars(s):
    return len(re.findall(r'(?<!\\)\$',s))%2==0

def load_block_exercises(code):
    parts=sorted(glob.glob(os.path.join(OUT,"%s_part*of*.json"%code)),
                 key=lambda p:int(re.search(r'part(\d+)of',p).group(1)))
    ex=[]
    for p in parts: ex.extend(json.load(open(p,encoding='utf-8')))
    return ex,parts

def build_lesson(code,exs):
    unit_dir,unit_id,course_label=META[code]
    intro={"id":"TH-QPAU-%s-1"%code,"type":"intuition",
      "title":"Cómo usar este banco de problemas de Selectividad",
      "body":("Esta lección reúne **problemas y cuestiones reales de las pruebas de acceso a la universidad "
              "(PAU/Selectividad)** de varias comunidades autónomas (Andalucía, Madrid, Comunidad Valenciana "
              "y Aragón), correspondientes a este bloque.\n\nCada ejercicio está **resuelto paso a paso, a modo "
              "de entrega de examen**: planteamiento, desarrollo con todos los cálculos y respuesta final. "
              "Despliega «Ver solución» solo después de haberlo intentado por tu cuenta.\n\nEl encabezado de cada "
              "ejercicio indica la **comunidad y la convocatoria** de procedencia."),
      "concept_ids":[],"objective_ids":["LO-QPAU-%s-1"%code],"provenance":"PAU","scope":"CORE"}
    objs=[
      {"id":"LO-QPAU-%s-1"%code,"statement":"Resolver problemas y cuestiones de Selectividad del bloque aplicando el método paso a paso exigido en la corrección de la PAU.","bloom":"aplicar","concept_ids":[]},
      {"id":"LO-QPAU-%s-2"%code,"statement":"Justificar cada resultado con el razonamiento químico y las unidades correctas, identificando los datos relevantes del enunciado.","bloom":"analizar","concept_ids":[]},
      {"id":"LO-QPAU-%s-3"%code,"statement":"Reconocer los tipos de pregunta recurrentes del bloque y los errores típicos que penalizan en el examen.","bloom":"evaluar","concept_ids":[]},
    ]
    summary={"big_idea":"La mejor preparación para la PAU es resolver exámenes reales del bloque y comparar tu desarrollo con una solución modelo.",
      "key_points":["Lee el enunciado y separa datos (lo conocido) de incógnitas (lo que pide).",
        "Plantea la reacción o ecuación ajustada antes de calcular.",
        "Cuida unidades, cifras significativas y la coherencia del resultado final."],
      "takeaway":"Practicar con problemas reales de distintas comunidades cubre toda la variedad de preguntas del bloque."}
    return {"id":"LPAU","title":TITULO,"subject":"Química","course_label":course_label,
      "unit_id":unit_id,"estimated_length":"variable","estimated_difficulty":4,
      "objectives":objs,"prerequisites":[],"diagnostic_items":[],
      "theory_blocks":[intro],"keywords":[],
      "worked_examples":[],"guided_exercises":[],"exercises":[],
      "exam_questions":exs,"challenge_questions":[],"mcq":[],"flashcards":[],
      "misconceptions":[],"common_mistakes":[],"exam_notes":[],
      "summary":summary,"lang":"es","provenance":"PAU"}

def atomic_write(path,obj):
    s=json.dumps(obj,ensure_ascii=False,indent=1)
    json.loads(s)  # valida
    fd,tmp=tempfile.mkstemp(dir=os.path.dirname(path),suffix='.tmp'); os.close(fd)
    open(tmp,'w',encoding='utf-8').write(s); os.replace(tmp,path)

def main():
    report=[]; ok=True
    cat=json.load(open(CAT,encoding='utf-8'))
    if not (isinstance(cat,dict) and isinstance(cat.get('projects'),list)):
        sys.exit("catalog.json no tiene estructura {projects:[...]} — aborto por seguridad")
    proj=[p for p in cat['projects'] if p['key']=='selectividad_quimica'][0]
    ubd={u['id']:u for u in proj['units']}
    total_ex=0
    for code in ORDER:
        unit_dir,unit_id,course_label=META[code]
        exs,parts=load_block_exercises(code)
        if not exs:
            report.append("[%s] SIN EJERCICIOS -> omito"%code); continue
        # validación
        seen=set(); verr=[]
        for e in exs:
            for fld in ('id','title','statement','full_solution','answer'):
                if not e.get(fld): verr.append((e.get('id'),'falta',fld))
            if e.get('id') in seen: verr.append((e.get('id'),'dup',''))
            seen.add(e.get('id'))
            for fld in ('statement','full_solution','answer'):
                v=e.get(fld,'')
                if isinstance(v,str) and not balanced_dollars(v): verr.append((e.get('id'),'$',fld))
        if verr:
            ok=False; report.append("[%s] FALLOS: %s"%(code,verr[:4])); continue
        les=build_lesson(code,exs)
        bfn="selectividad_quimica__%s.json"%unit_dir
        bpath=os.path.join(BUN,bfn)
        b=json.load(open(bpath,encoding='utf-8'))
        b[BKEY]=les
        atomic_write(bpath,b)
        # catalog
        u=ubd[unit_dir]
        u['lecciones']=[l for l in u['lecciones'] if l.get('bkey')!=BKEY]
        nmax=max([l.get('n',0) for l in u['lecciones']]+[0])
        u['lecciones'].append({"n":nmax+1,"titulo":TITULO,"dificultad":4,"duracion":"variable",
                               "bundle":"bundles/%s"%bfn,"bkey":BKEY})
        total_ex+=len(exs)
        report.append("[%s] %d ejercicios insertados en %s"%(code,len(exs),bfn))
    atomic_write(CAT,cat)
    print("\n".join(report))
    print("TOTAL ejercicios insertados:",total_ex)
    print("RESULTADO:", "OK" if ok else "CON FALLOS")
    return 0 if ok else 2

if __name__=='__main__': sys.exit(main())
