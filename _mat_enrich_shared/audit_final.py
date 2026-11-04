import json, glob, os, hashlib

BND="bundles"; BK="bundles/_backup_mat_enrich_20261104_002419"
bundles=sorted(b for b in glob.glob(f"{BND}/eso_matematicas__*.json") if not b.endswith(".regen.json"))
def load(p):
    with open(p,encoding="utf-8") as f: return json.load(f)

def lesson_concepts(L):
    c={k.get("concept_id") for k in (L.get("keywords") or []) if isinstance(k,dict)}
    for o in (L.get("objectives") or []):
        c|=set(o.get("concept_ids") or [])
    return {x for x in c if x}

def lesson_assets(L):
    # list of (id, tikz_hash) across theory_blocks
    out=[]
    for tb in (L.get("theory_blocks") or []):
        for a in (tb.get("assets") or []):
            tk=a.get("tikz","") or ""
            out.append((a.get("id",""), hashlib.md5(tk.encode()).hexdigest()[:8]))
    return out

report=[]; all_ids={}; problems=[]
T={"tot":0,"new":0,"ast":0,"astbk":0}
for bp in bundles:
    name=os.path.basename(bp).replace("eso_matematicas__","").replace(".json","")
    try: data=load(bp)
    except Exception as e: problems.append(f"[JSON FAIL] {name}: {e}"); continue
    bkp=os.path.join(BK,os.path.basename(bp)); bk=load(bkp) if os.path.exists(bkp) else None
    u_tot=u_new=u_ast=u_astbk=0
    for lk,L in data.items():
        if not isinstance(L,dict): continue
        exs=L.get("exercises",[]) or []; u_tot+=len(exs)
        vobj={o.get("id") for o in (L.get("objectives") or []) if isinstance(o,dict)}
        vcon=lesson_concepts(L)
        a_now=lesson_assets(L); u_ast+=len(a_now)
        if bk and lk in bk:
            a_bk=lesson_assets(bk[lk]); u_astbk+=len(a_bk)
            # tikz content changed? (exercise agents must NOT have touched figures)
            if {x[0] for x in a_now}!={x[0] for x in a_bk}:
                problems.append(f"[ASSET SET CHANGED] {name}/{lk}")
        for ex in exs:
            exid=ex.get("id",""); all_ids.setdefault(exid,[]).append(f"{name}/{lk}")
            if ex.get("provenance","")=="SOURCE_DERIVED":
                u_new+=1
                for oid in ex.get("objective_ids",[]) or []:
                    if vobj and oid not in vobj: problems.append(f"[BAD OBJ] {name}/{lk}/{exid}: {oid}")
                for cid in ex.get("concept_ids",[]) or []:
                    if vcon and cid not in vcon: problems.append(f"[BAD CONCEPT] {name}/{lk}/{exid}: {cid}")
                fs=ex.get("full_solution","") or ""; st=ex.get("statement","") or ""
                if len(fs)<60: problems.append(f"[SHORT SOL] {name}/{lk}/{exid}: len={len(fs)}")
                if (fs.count('$')%2) or (st.count('$')%2): problems.append(f"[UNBALANCED $] {name}/{lk}/{exid}")
    report.append((name,u_tot,u_new,u_ast,u_astbk))
    T["tot"]+=u_tot;T["new"]+=u_new;T["ast"]+=u_ast;T["astbk"]+=u_astbk
for k,v in all_ids.items():
    if len(v)>1 and k: problems.append(f"[DUP ID] {k}: {v}")
print(f"{'UNIT':36s} {'TOT':>4} {'NEW':>4} {'AST(now/bk)':>12}")
for name,tot,new,a,abk in report:
    fl="" if a==abk else "  <-- DIFF"
    print(f"{name:36s} {tot:4d} {new:4d} {a:5d}/{abk:<5d}{fl}")
print("-"*62)
print(f"{'TOTAL '+str(len(report)):36s} {T['tot']:4d} {T['new']:4d} {T['ast']:5d}/{T['astbk']:<5d}")
print(f"\nPROBLEMS: {len(problems)}")
for p in problems[:60]: print("  "+p)
