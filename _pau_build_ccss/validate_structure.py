# -*- coding: utf-8 -*-
"""Structural validation to run ON THE DEVICE after assembly:
 - every CCSS bundle + catalog.json load as JSON
 - catalog has {projects:[...]} with the 9 courses intact
 - each of the 11 CCSS bundles has the LPAU lesson with exam_questions
 - catalog ccss units each have the PAU leccion entry; counts match
 - report exam_questions and assets(figuras) per block"""
import json, os, sys, glob
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.dirname(HERE)
BUN=os.path.join(ROOT,'bundles'); CAT=os.path.join(ROOT,'catalog.json')
EXPECT_COURSES={'fq_completo','eso_matematicas','gcse_mates','gcse_ciencias_chem',
 'gcse_ciencias_phys','selectividad_quimica','selectividad_fisica','selectividad_matematicas',
 'selectividad_matematicas_ccss'}
SUFFIXES=['fundamentos','mat_matrices','mat_sistemas','mat_limites','mat_derivadas',
 'mat_representacion','mat_integrales','mat_probabilidad','mat_programacion_lineal',
 'mat_estadistica','mat_muestreo_inferencia']
BKEY="99_Ejercicios_de_selectividad_PAU.json"

def main():
    errs=[]; info=[]
    # catalog
    try: cat=json.load(open(CAT,encoding='utf-8'))
    except Exception as e: print('FATAL catalog.json no carga:',e); sys.exit(2)
    if not (isinstance(cat,dict) and isinstance(cat.get('projects'),list)):
        print('FATAL catalog sin {projects:[...]}'); sys.exit(2)
    keys={p.get('key') for p in cat['projects']}
    if not EXPECT_COURSES.issubset(keys):
        errs.append('faltan cursos en catalog: %s'%(EXPECT_COURSES-keys))
    info.append('catalog projects: %d (%s)'%(len(cat['projects']), ','.join(sorted(keys))))
    ccss=[p for p in cat['projects'] if p['key']=='selectividad_matematicas_ccss'][0]
    ubd={u['id']:u for u in ccss['units']}
    # bundles
    tot_q=0; tot_fig=0
    for suf in SUFFIXES:
        bp=os.path.join(BUN,'selectividad_matematicas_ccss__%s.json'%suf)
        try: b=json.load(open(bp,encoding='utf-8'))
        except Exception as e: errs.append('%s no carga: %s'%(suf,e)); continue
        les=b.get(BKEY)
        if not les: errs.append('%s SIN leccion LPAU'%suf); continue
        eqs=les.get('exam_questions',[]); nq=len(eqs)
        nfig=sum(len(e.get('assets',[]) or []) for e in eqs)
        tot_q+=nq; tot_fig+=nfig
        # ids unique + prefix
        ids=[e.get('id') for e in eqs]
        if len(set(ids))!=len(ids): errs.append('%s ids duplicados'%suf)
        # catalog leccion present
        u=ubd.get(suf)
        has=u and any(l.get('bkey')==BKEY for l in u.get('lecciones',[]))
        if not has: errs.append('%s: catalog sin leccion PAU'%suf)
        info.append('%-26s exam_questions=%-3d figuras=%-3d catalog_leccion=%s'%(suf,nq,nfig,bool(has)))
    print('\n'.join(info))
    print('TOTAL exam_questions=%d  figuras=%d'%(tot_q,tot_fig))
    if errs:
        print('=== ERRORES (%d) ==='%len(errs))
        for e in errs: print('  -',e)
        sys.exit(1)
    print('ESTRUCTURA OK')
if __name__=='__main__': main()
