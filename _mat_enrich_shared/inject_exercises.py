#!/usr/bin/env python3
"""inject_exercises.py <bundle.json> <exercises_module.py>
El módulo debe definir EX = { "<clave_leccion>": [ {ejercicio}, ... ] } y,
opcionalmente, una función val() que lance asserts numéricos.
Comprueba integridad (ids únicos, objective/concept válidos, $ balanceados,
solución no trivial, sin \\n), normaliza texto e inyecta en exercises[]."""
import json,sys,importlib.util,re
def clean(s):
    s=s.replace('\\n',' ').replace('\n',' '); s=re.sub(r'  +',' ',s).strip(); return s
def main():
    bundle,mod=sys.argv[1],sys.argv[2]
    d=json.load(open(bundle,encoding='utf-8'))
    spec=importlib.util.spec_from_file_location('exmod',mod);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    if hasattr(m,'val'): m.val(); print('val() OK')
    prob=[]; total=0
    for lk,news in m.EX.items():
        if lk not in d: prob.append(f"clave de lección inexistente: {lk}"); continue
        les=d[lk]
        valid_lo={o['id'] for o in les.get('objectives',[])}
        valid_c=set()
        for e in les.get('exercises',[]): valid_c|=set(e.get('concept_ids',[]))
        for k in les.get('keywords',[]):
            if k.get('concept_id'): valid_c.add(k['concept_id'])
        ids={e['id'] for e in les.get('exercises',[])}
        for e in news:
            for f in('statement','answer','full_solution'): e[f]=clean(e[f])
            e['hints']=[clean(h) for h in e.get('hints',[])]
            e['common_errors']=[clean(c) for c in e.get('common_errors',[])]
            if e['id'] in ids: prob.append(f"{lk}: id duplicado {e['id']}")
            ids.add(e['id'])
            for lo in e.get('objective_ids',[]):
                if lo not in valid_lo: prob.append(f"{lk}/{e['id']}: objective_id inválido {lo} (válidos {sorted(valid_lo)})")
            for c in e.get('concept_ids',[]):
                if c not in valid_c: prob.append(f"{lk}/{e['id']}: concept_id no visto {c}")
            for f in('statement','answer','full_solution'):
                if e[f].count('$')%2: prob.append(f"{lk}/{e['id']}: $ desbalanceado en {f}")
            if len(e['full_solution'])<60: prob.append(f"{lk}/{e['id']}: solución demasiado corta")
            if e.get('provenance')!='SOURCE_DERIVED': prob.append(f"{lk}/{e['id']}: provenance debe ser SOURCE_DERIVED")
            total+=1
    if prob:
        print("PROBLEMAS (no se inyecta nada):"); [print("  -",p) for p in prob]; sys.exit(1)
    for lk,news in m.EX.items(): d[lk]['exercises'].extend(news)
    out=json.dumps(d,ensure_ascii=False,indent=2); json.loads(out)
    open(bundle,'w',encoding='utf-8').write(out)
    print(f"INYECTADOS {total} ejercicios OK")
    for lk in m.EX: print(f"  {lk[:42]}: {len(d[lk]['exercises'])} ejercicios")
if __name__=='__main__': main()
