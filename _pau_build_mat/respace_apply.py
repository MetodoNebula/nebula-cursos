#!/usr/bin/env python3
"""Respace (add paragraph breaks to) full_solution of LPAU exam_questions, in place,
atomically. Non-destructive: only whitespace/paragraph breaks added. Verifies balanced $
and that non-whitespace content is unchanged before writing.
Usage: python3 respace_apply.py <bundles_glob_prefix>   e.g. 'bundles/selectividad_matematicas_ccss__'
"""
import re, json, glob, os, sys, tempfile
MATH = re.compile(r'\$\$(?:\\.|[\s\S])+?\$\$|\$(?:\\.|[^$\n])+\$')
BOUND = re.compile(r'(?<=[.?!])\s+(?=[A-ZÁÉÍÓÚÑ¿¡0-9*\x00])')
ABBR  = re.compile(r'(?:\bp\.\s?ej|\betc|\baprox|\bnúm|\bSr|\bSra|\bDra?|\bvs|\bcf|\bfig|\bec|\bpág|\bmáx|\bmín)\.$', re.I)
STRUCT = re.compile(r'^\s*(?:[-*•]\s|\d+[.)]\s|\||#{1,4}\s|>)')
def _struct(block): return any(STRUCT.match(l) for l in block.split('\n') if l.strip())
def space_solution(fs):
    if not fs or '\x00' in fs: return fs
    out=[]
    for blk in re.split(r'\n{2,}', fs):
        s=blk.strip()
        if not s: continue
        if '$$' in s or _struct(s): out.append(s); continue
        ph=[]
        def prot(m): ph.append(m.group(0)); return '\x00%d\x00'%(len(ph)-1)
        t=MATH.sub(prot, s)
        merged=[]
        for p in BOUND.split(t):
            vis=re.sub(r'\x00\d+\x00','',merged[-1]).strip() if merged else ''
            if merged and ABBR.search(vis): merged[-1]=merged[-1]+' '+p
            else: merged.append(p)
        rest=lambda x: re.sub(r'\x00(\d+)\x00', lambda mm: ph[int(mm.group(1))], x)
        out.extend(rest(p.strip()) for p in merged if p.strip())
    return '\n\n'.join(out)
def dollars(s):
    n=0;i=0
    while i<len(s):
        if s[i]=='\\':i+=2;continue
        if s[i]=='$':n+=1
        i+=1
    return n
def main():
    pref=sys.argv[1]; changed=0; bad=0
    for f in sorted(glob.glob(pref+'*.json')):
        b=json.load(open(f,encoding='utf-8')); les=b.get('99_Ejercicios_de_selectividad_PAU.json')
        if not les: continue
        ch=False
        for q in les.get('exam_questions',[]):
            fs=q.get('full_solution')
            if not fs: continue
            new=space_solution(fs)
            if re.sub(r'\s+','',new)!=re.sub(r'\s+','',fs) or dollars(new)%2:
                bad+=1; continue   # safety: skip if anything off
            if new!=fs: q['full_solution']=new; ch=True; changed+=1
        if ch:
            fd,tmp=tempfile.mkstemp(dir=os.path.dirname(f),suffix='.tmp'); os.close(fd)
            open(tmp,'w',encoding='utf-8').write(json.dumps(b,ensure_ascii=False,indent=1)); os.replace(tmp,f)
    print(f'respaced {changed} solutions; skipped(unsafe) {bad}')
if __name__=='__main__': main()
