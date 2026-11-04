#!/usr/bin/env python3
"""Extract every rendered field from the LPAU lessons of the 13 bundles for MathJax lint.
Usage: python3 extract_lint_items.py <bundles_dir> <out_items.json>"""
import json,glob,os,sys
bdir=sys.argv[1]; out=sys.argv[2]; items=[]
for f in sorted(glob.glob(os.path.join(bdir,'selectividad_matematicas__*.json'))):
    b=json.load(open(f,encoding='utf-8'))
    les=b.get('99_Ejercicios_de_selectividad_PAU.json')
    if not les: continue
    for q in les.get('exam_questions',[]):
        qid=q.get('id')
        for fld in ('statement','full_solution','answer'):
            if q.get(fld): items.append({'id':qid,'field':fld,'text':q[fld]})
        for j,k in enumerate(q.get('knowns') or []): items.append({'id':qid,'field':f'knowns[{j}]','text':k})
        for j,k in enumerate(q.get('common_errors') or []): items.append({'id':qid,'field':f'common_errors[{j}]','text':k})
        for j,k in enumerate(q.get('mark_scheme') or []): items.append({'id':qid,'field':f'mark_scheme[{j}]','text':k})
json.dump(items,open(out,'w'),ensure_ascii=False)
print('lint items:',len(items))
