import sys, os

bundle = os.path.join(os.environ['HOME'], 'mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json')
old_path = sys.argv[1]
new_path = sys.argv[2]

with open(old_path, encoding='utf-8') as f:
    old = f.read()
with open(new_path, encoding='utf-8') as f:
    new = f.read()
# strip a single trailing newline added by heredoc, keep internal content intact
if old.endswith('\n'):
    old = old[:-1]
if new.endswith('\n'):
    new = new[:-1]

with open(bundle, encoding='utf-8') as f:
    data = f.read()

count = data.count(old)
if count != 1:
    print(f'ABORT: old string found {count} times (expected 1). File: {old_path}')
    sys.exit(1)

data2 = data.replace(old, new, 1)
with open(bundle, 'w', encoding='utf-8') as f:
    f.write(data2)
print(f'OK: replaced 1 occurrence. File: {old_path}')
