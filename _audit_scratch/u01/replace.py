import sys
old_path, new_path, bundle_path = sys.argv[1], sys.argv[2], sys.argv[3]
old = open(old_path, encoding="utf-8").read()
new = open(new_path, encoding="utf-8").read()
if old.endswith("\n"): old = old[:-1]
if new.endswith("\n"): new = new[:-1]
data = open(bundle_path, encoding="utf-8").read()
n = data.count(old)
print("occurrences:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(bundle_path, "w", encoding="utf-8").write(data)
    print("REPLACED OK")
else:
    print("ABORT - ajusta el contexto en old.txt")
