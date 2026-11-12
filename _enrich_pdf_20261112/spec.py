import json,sys
u=sys.argv[1]; d=json.load(open(f'bundles/eso_matematicas__{u}.json',encoding='utf-8'))
only=sys.argv[2] if len(sys.argv)>2 else None
for k,L in d.items():
    if only and not k.startswith(only): continue
    print(f"\n##### KEY: {k}   id={L['id']}")
    print("OBJ:", "; ".join(f"{o['id']}={o['statement'][:95]}" for o in L.get('objectives',[])))
    cs=set()
    for e in L.get('exercises',[]): cs|=set(e.get('concept_ids',[]))
    for w in L.get('keywords',[]):
        if w.get('concept_id'): cs.add(w['concept_id'])
    print("CONCEPTS:", ", ".join(f"{w.get('concept_id')}:{w.get('term')}" for w in L.get('keywords',[]) if w.get('concept_id')))
    print("CONCEPT_IDS_VALIDOS:", sorted(cs))
    ms=L.get('misconceptions',[])
    print("MISCONCEPTIONS:", "; ".join((m if isinstance(m,str) else (m.get('misconception') or m.get('statement') or m.get('text') or json.dumps(m,ensure_ascii=False)))[:130] for m in ms))
    print("EJERCICIOS EXISTENTES:")
    for e in L.get('exercises',[]):
        print(f"  [{e['id']} d{e.get('difficulty')}] {e['statement'][:125]}")
