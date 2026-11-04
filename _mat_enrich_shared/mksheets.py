#!/usr/bin/env python3
"""mksheets.py <outdir>  -> hojas de contacto por lección en <outdir>/sheets/"""
import json,os,subprocess,collections,sys
outdir=sys.argv[1]; res=json.load(open(os.path.join(outdir,'result.json')))
sh=os.path.join(outdir,'sheets'); os.makedirs(sh,exist_ok=True)
by=collections.OrderedDict()
for r in res:
    if not r['compiled']:continue
    p=os.path.join(outdir,'png',r['png'])
    if not os.path.exists(p):continue
    by.setdefault(r['lesson'][:38],[]).append((r['id'],p))
for i,(les,items) in enumerate(sorted(by.items()),1):
    args=['montage']
    for fid,p in items: args+=['-label',fid,p]
    args+=['-tile','3x','-geometry','380x270+6+8','-background','white','-pointsize','14',os.path.join(sh,'L%02d.png'%i)]
    subprocess.run(args,check=True); print('L%02d'%i,les[:30],[f for f,_ in items])
