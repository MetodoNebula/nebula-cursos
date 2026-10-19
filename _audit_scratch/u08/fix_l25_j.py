import sys, json
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
with open(PATH, "r", encoding="utf-8") as f:
    data = f.read()

i0 = data.find('"25_Polimerización')
i1 = data.find('"26_', i0)
seg = data[i0:i1]

def rep(old, new, expect, label):
    global seg
    c = seg.count(old)
    if c != expect:
        print("MISMATCH", label, "expected", expect, "got", c)
        sys.exit(1)
    seg = seg.replace(old, new)
    print("OK", label, c)

challenge = {
    "id": "CH-Q08-25-1",
    "type": "CHALLENGE",
    "objective_ids": ["LO-Q08-25-4"],
    "concept_ids": ["C-Q08-25-3"],
    "difficulty": 4,
    "statement": "Un oligómero de nailon-6,6, formado por n moléculas de ácido adípico y n moléculas de hexano-1,6-diamina unidas alternadamente, tiene una masa molecular de 2281,22 g/mol. (a) Calcula n. (b) ¿Cuántas moléculas de agua se han liberado en total? (c) Escribe la unidad repetitiva de este oligómero.",
    "hints": [
        "Plantea M = n·M(diácido) + n·M(diamina) - (2n-1)·M(H2O) y despeja n.",
        "Recuerda que con n moléculas de cada monómero hay (2n-1) enlaces, no 2n: los dos extremos de la cadena quedan con un grupo libre sin reaccionar."
    ],
    "answer": "(a) n=10. (b) Se liberan 19 moléculas de agua. (c) [-NH-(CH2)6-NH-CO-(CH2)4-CO-]n.",
    "full_solution": "(a) M = n(146,14+116,21) - (2n-1)(18,015) = 226,32n + 18,015. Igualando a 2281,22: 226,32n = 2263,205, de donde n ≈ 10. (b) Con n=10 moléculas de cada monómero hay (2·10-1)=19 enlaces amida, y por tanto 19 moléculas de agua liberadas. (c) La unidad repetitiva es la misma que la del nailon-6,6 en general, [-NH-(CH2)6-NH-CO-(CH2)4-CO-]n, independientemente de cuántas veces se repita en la cadena.",
    "common_errors": [
        "Calcular (2n) enlaces en vez de (2n-1), olvidando que los dos extremos de la cadena quedan con un grupo libre sin reaccionar."
    ],
    "provenance": "SOURCE_DERIVED"
}

old = '"challenge_questions": [],'
new = '"challenge_questions": [' + json.dumps(challenge, ensure_ascii=False) + '],'
rep(old, new, 1, "F13 challenge_questions add")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE J")
