#!/usr/bin/env python3
"""Insert LPAU lessons into the 13 selectividad_matematicas bundles and add catalog
entries. Idempotent (safe to re-run). Atomic writes (tmp+os.replace). Does NOT run
rebuild_catalog (caller does). Run from Nebula_Cursos_Web root.
Usage: python3 insert_pau.py _pau_build_mat/lessons_all.json
"""
import json, os, sys, tempfile

ROOT=os.path.abspath('.')
assert os.path.exists(os.path.join(ROOT,'catalog.json')), 'run from Nebula_Cursos_Web root'
BKEY='99_Ejercicios_de_selectividad_PAU.json'

def atomic_write(path,obj):
    fd,tmp=tempfile.mkstemp(dir=os.path.dirname(path),suffix='.tmp'); os.close(fd)
    open(tmp,'w',encoding='utf-8').write(json.dumps(obj,ensure_ascii=False,indent=1))
    os.replace(tmp,path)

def first_lesson(bundle):
    for k,v in bundle.items():
        if isinstance(v,dict) and v.get('id'): return v
    return None

def main():
    lessons=json.load(open(sys.argv[1],encoding='utf-8'))
    report={}
    for block,lesson in lessons.items():
        bpath=os.path.join(ROOT,'bundles',f'selectividad_matematicas__{block}.json')
        if not os.path.exists(bpath):
            print('  SKIP (no bundle):',block); continue
        bundle=json.load(open(bpath,encoding='utf-8'))
        fl=first_lesson(bundle)
        les=dict(lesson)
        les['subject']=fl.get('subject'); les['course_label']=fl.get('course_label'); les['unit_id']=fl.get('unit_id')
        # insert/replace LPAU key (place at end)
        bundle.pop(BKEY,None)
        bundle[BKEY]=les
        atomic_write(bpath,bundle)
        report[block]=len(les.get('exam_questions',[]))
    # catalog
    cat=json.load(open(os.path.join(ROOT,'catalog.json'),encoding='utf-8'))
    proj=None
    for p in cat['projects']:
        if p.get('key')=='selectividad_matematicas': proj=p; break
    assert proj, 'selectividad_matematicas project not found'
    bundle_rel={block:f'bundles/selectividad_matematicas__{block}.json' for block in lessons}
    for block,lesson in lessons.items():
        rel=bundle_rel[block]
        # find the unit whose lecciones already reference this bundle
        unit=None
        for u in proj['units']:
            for l in u.get('lecciones',[]):
                if l.get('bundle')==rel: unit=u; break
            if unit: break
        if unit is None:
            # fallback: match unit id == block
            for u in proj['units']:
                if u.get('id')==block: unit=u; break
        if unit is None:
            print('  WARN: no catalog unit for',block); continue
        lecs=unit.setdefault('lecciones',[])
        lecs[:]=[l for l in lecs if l.get('bkey')!=BKEY]  # drop existing LPAU
        nmax=max([l.get('n',0) for l in lecs] or [0])
        lecs.append({'n':nmax+1,'titulo':'Ejercicios de selectividad (PAU)','dificultad':3,
                     'duracion':lesson.get('estimated_length','2 h'),'contenido':{},
                     'bundle':rel,'bkey':BKEY})
    atomic_write(os.path.join(ROOT,'catalog.json'),cat)
    print('INSERTED LPAU into %d bundles + catalog entries:'%len(report))
    for b,n in sorted(report.items()): print(f'  {b:24s} {n} exam_questions')

if __name__=='__main__': main()
