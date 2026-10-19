# -*- coding: utf-8 -*-
"""
Verificador numerico propio (Fase 2).

Busca, dentro de los campos de solucion/respuesta de cada pieza (worked_examples,
guided_exercises, exercises, exam_questions, challenge_questions), expresiones
LaTeX del tipo  <expresion aritmetica concreta> = <numero>  y recalcula el lado
izquierdo para comprobar que coincide con el lado derecho dentro de una
tolerancia razonable (errores de redondeo intermedio, cifras significativas).

A diferencia de equality_mismatches_candidates.csv (que confunde variables de
una letra como "E" o "e" con el numero de Euler, y no entiende \dfrac/sen/\cdot),
este script:
  - Solo evalua el LHS cuando es una expresion puramente numerica (digitos,
    operadores, \cdot, \dfrac, \frac, \sqrt, sen/cos/tg y sus inversas, potencias,
    paréntesis, notación científica con coma decimal). Si el LHS contiene
    cualquier letra que no sea el nombre de una función reconocida, se descarta
    (no es una "ecuación resuelta", es una fórmula simbólica).
  - Convierte la coma decimal española a punto antes de evaluar.
  - Tolera un error relativo de hasta el 3% (arrastre de redondeos en cadenas
    de varios pasos) antes de marcar discrepancia.
"""
import json, re, os, math, sys

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web")
PILOT = os.path.join(BASE, "pilot/selectividad_fisica_v2")
UNITS = ["campo_gravitatorio","mas","ondas","electromagnetismo","optica",
         "relatividad","cuantica","nuclear"]

SOLUTION_FIELDS = ["answer", "solution", "full_solution"]
CONTAINER_KEYS = ["worked_examples","guided_exercises","exercises",
                  "exam_questions","challenge_questions"]

# --- tokenizer / evaluator for a restricted numeric LaTeX subset ---

FUNC_MAP = {
    "sen": "math.sin", "cos": "math.cos", "tg": "math.tan", "tan": "math.tan",
    "arcsen": "math.asin", "arccos": "math.acos", "arctg": "math.atan",
    "log": "math.log10", "ln": "math.log", "sqrt": "math.sqrt",
}

def strip_latex_wrappers(s):
    s = s.replace("\\,", " ").replace("\\;", " ").replace("\\!", "")
    s = s.replace("\\left", "").replace("\\right", "")
    s = s.replace("\\boxed", "")
    s = s.replace("\\mathrm{m/s^2}", "").replace("\\text", "")
    return s

def latex_to_py(expr):
    e = expr
    # \dfrac{a}{b} and \frac{a}{b} -> (a)/(b)  (handle nesting via regex loop)
    for _ in range(6):
        e2 = re.sub(r"\\d?frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", e)
        if e2 == e:
            break
        e = e2
    # \sqrt{a} -> math.sqrt(a)
    for _ in range(6):
        e2 = re.sub(r"\\sqrt\{([^{}]*)\}", r"math.sqrt(\1)", e)
        if e2 == e:
            break
        e = e2
    # function names followed by a number/paren: sen 30^\circ, cos(x), log(x)
    for name, py in FUNC_MAP.items():
        e = re.sub(r"\\?%s\s*\{([^{}]*)\}" % re.escape(name), r"%s(\1)" % py, e)
    e = e.replace("\\cdot", "*").replace("\\times", "*")
    e = e.replace("^\\circ", "*DEGSENTINEL")  # mark degree, handled below crudely
    e = e.replace("{", "(").replace("}", ")")
    e = e.replace("^", "**")
    # Spanish decimal comma -> point, but only between digits (avoid touching real commas)
    e = re.sub(r"(?<=\d),(?=\d)", ".", e)
    # remove leftover latex spacing commands and stray backslashes before letters we don't know
    e = e.replace("\\", "")
    e = e.replace("DEGSENTINEL", "")
    return e

NUMERIC_ALLOWED_RE = re.compile(
    r"^[0-9\.\,\+\-\*\/\(\)\s\^\{\}\\a-zA-Z_]*$"
)
# whitelist of identifiers allowed to appear (functions); anything else with letters => reject
ALLOWED_WORDS = set(["sen","cos","tg","tan","arcsen","arccos","arctg","log","ln",
                      "sqrt","dfrac","frac","cdot","times","circ","left","right",
                      "boxed","text","mathrm","s","m","kg","N","J","W","Hz","Pa",
                      "pi","e"])

def is_pure_numeric_expr(expr):
    words = re.findall(r"[A-Za-z]+", expr)
    for w in words:
        if w.lower() not in ALLOWED_WORDS:
            return False
    return True

def safe_eval(py_expr):
    py_expr = py_expr.replace("pi", "math.pi")
    # bare 'e' as Euler's number only if isolated and not part of a longer identifier (already handled by regex word-split)
    allowed_globals = {"math": math, "__builtins__": {}}
    return eval(py_expr, allowed_globals, {})

EQ_RE = re.compile(r"\$\$?([^$]{3,200}?)=\s*([\-0-9][0-9\.\,\\cdot\{\}\^\s\*/a-zA-Z]{0,60}?)\$\$?")

def extract_equations(text):
    """Find LHS = RHS pairs inside $...$ or $$...$$ math segments."""
    out = []
    for seg in re.findall(r"\$\$(.*?)\$\$|\$(.*?)\$", text, re.DOTALL):
        math_str = seg[0] or seg[1]
        if "=" not in math_str:
            continue
        parts = math_str.split("=")
        if len(parts) < 2:
            continue
        lhs = parts[-2].strip()
        rhs = parts[-1].strip()
        out.append((lhs, rhs, math_str))
    return out

def try_parse_number(rhs_raw):
    r = rhs_raw.strip()
    r = re.sub(r"\\,", "", r)
    r = r.rstrip("\\;., ")
    r = latex_to_py(r)
    r = r.strip()
    if not is_pure_numeric_expr(r):
        return None
    try:
        val = safe_eval(r)
        if isinstance(val, (int, float)) and not isinstance(val, bool):
            return float(val)
    except Exception:
        return None
    return None

def check_lesson(course_json, unit, bkey, lesson, report):
    for ck in CONTAINER_KEYS:
        items = lesson.get(ck, [])
        if not isinstance(items, list):
            continue
        for idx, item in enumerate(items):
            if not isinstance(item, dict):
                continue
            for field in SOLUTION_FIELDS:
                val = item.get(field)
                texts = []
                if isinstance(val, str):
                    texts = [val]
                elif isinstance(val, list):
                    texts = [v for v in val if isinstance(v, str)]
                for text in texts:
                    text2 = strip_latex_wrappers(text)
                    for lhs, rhs, mstr in extract_equations(text2):
                        if not is_pure_numeric_expr(lhs) or len(re.findall(r"[0-9]", lhs)) == 0:
                            continue
                        lhs_py = latex_to_py(lhs)
                        try:
                            lhs_val = safe_eval(lhs_py)
                        except Exception:
                            continue
                        if not isinstance(lhs_val, (int, float)) or isinstance(lhs_val, bool):
                            continue
                        rhs_val = try_parse_number(rhs)
                        if rhs_val is None:
                            continue
                        if rhs_val == 0 and abs(lhs_val) < 1e-9:
                            continue
                        denom = max(abs(rhs_val), 1e-12)
                        rel_err = abs(lhs_val - rhs_val) / denom
                        if rel_err > 0.03:
                            report.append({
                                "unit": unit, "bkey": bkey, "container": ck, "idx": idx,
                                "field": field, "lhs": lhs, "rhs": rhs,
                                "lhs_val": lhs_val, "rhs_val": rhs_val,
                                "rel_err": round(rel_err, 4),
                                "context": mstr[:160],
                            })

def main():
    all_report = []
    for unit in UNITS:
        fp = os.path.join(PILOT, f"selectividad_fisica__{unit}.json")
        d = json.load(open(fp, encoding="utf-8"))
        for bkey, lesson in d.items():
            check_lesson(d, unit, bkey, lesson, all_report)
    out_fp = os.path.join(BASE, "scripts/pilot_fisica/numeric_qa_report.json")
    json.dump(all_report, open(out_fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"Total candidate mismatches: {len(all_report)}")
    for r in all_report:
        print(f"[{r['unit']}/{r['bkey']}] {r['container']}[{r['idx']}].{r['field']}: "
              f"{r['lhs']} = {r['lhs_val']:.6g}  vs declared {r['rhs']} = {r['rhs_val']:.6g}  "
              f"(rel_err={r['rel_err']})")

if __name__ == "__main__":
    main()
