import sys
base = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u04/"
path = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U04_Termoquimica.json"
old = open(base+"old.txt", encoding="utf-8").read()
new = open(base+"new.txt", encoding="utf-8").read()
if old.endswith("\n"): old = old[:-1]
if new.endswith("\n"): new = new[:-1]
data = open(path, encoding="utf-8").read()
n = data.count(old)
print("occurrences:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(path, "w", encoding="utf-8").write(data)
    print("REPLACED OK")
else:
    print("ABORT - ajusta el contexto en old.txt")
