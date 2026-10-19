import sys
base = sys.argv[1]  # scratch dir
target = sys.argv[2]  # target json file
old = open(base+"/old.txt", encoding="utf-8").read()
new = open(base+"/new.txt", encoding="utf-8").read()
if old.endswith("\n"): old = old[:-1]
if new.endswith("\n"): new = new[:-1]
data = open(target, encoding="utf-8").read()
n = data.count(old)
print("occurrences:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(target, "w", encoding="utf-8").write(data)
    print("REPLACED OK")
else:
    print("ABORT - adjust old.txt context")
