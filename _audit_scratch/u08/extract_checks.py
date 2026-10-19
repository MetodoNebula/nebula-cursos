import re, sys

audit_path = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u08_full.md"
bundle_path = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"

text = open(audit_path, encoding="utf-8").read()
bundle = open(bundle_path, encoding="utf-8").read()

lesson_re = re.compile(r'^####\s+Lección\s+(\d+)\s+—\s+(.+)$', re.M)
matches = list(lesson_re.finditer(text))
lessons = []
for i, m in enumerate(matches):
    start = m.end()
    end = matches[i+1].start() if i+1 < len(matches) else len(text)
    lessons.append((m.group(1), m.group(2), text[start:end]))

only = sys.argv[1] if len(sys.argv) > 1 else None

texto_re = re.compile(r'\*Texto actual:\*\s*(.+?)(?=\n\s*-\s*\*Arreglo|\n\d+\.\s+\*\*\[|\Z)', re.S)

def clean_frag(s):
    s = s.strip()
    s = s.strip('«»').strip()
    # if it contains a separator indicating multiple sub-quotes glued by the audit, take first part
    for sep in [' / ', '» / «', '»/«']:
        if sep in s:
            s = s.split(sep)[0]
    s = s.strip('«»').strip()
    # cut at first backslash or $ sign (latex), keep enough context
    frag = re.split(r'[\\$]', s)[0].strip()
    frag = frag.strip('«»').strip()
    if len(frag) < 12:
        frag = s[:90]
    return frag[:100]

for num, title, body in lessons:
    if only and num != only:
        continue
    print(f"\n===== Lección {num} — {title} =====")
    items = re.split(r'\n(?=\d+\.\s+\*\*\[)', body)
    for item in items:
        fm = re.match(r'(\d+)\.\s+\*\*\[(\w+)\s*·\s*(\w+)\]\*\*\s+`([^`]+)`', item)
        if not fm:
            continue
        idx, sev, cat, field = fm.groups()
        tm = texto_re.search(item)
        if not tm:
            print(f"  #{idx} [{sev}·{cat}] {field} -- (sin 'Texto actual' citado)")
            continue
        raw = tm.group(1).strip()
        frag = clean_frag(raw)
        cnt = bundle.count(frag)
        status = "FOUND(%d)" % cnt if cnt else "NOT-FOUND"
        print(f"  #{idx} [{sev}·{cat}] {field} :: frag={frag!r} -> {status}")
