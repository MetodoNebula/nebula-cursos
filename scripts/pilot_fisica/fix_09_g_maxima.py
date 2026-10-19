# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__campo_gravitatorio.json")
d = json.load(open(fp, encoding="utf-8"))
lesson = d["04_El_campo_gravitatorio_terrestre_variación_de_g.json"]

# 1) objectives[2].statement
old = lesson["objectives"][2]["statement"]
assert "máximo en la superficie" in old, old
if "modelo de Tierra homogénea" not in old:
    new = old.replace(
        "que el valor de $g$ es **máximo en la superficie**",
        "que, en el modelo de Tierra homogénea, el valor de $g$ es **máximo en la superficie**"
    )
    assert new != old, repr(old)
    lesson["objectives"][2]["statement"] = new
    print("objectives[2] OK")
else:
    print("objectives[2] already scoped, skipped")

# 2) summary.key_points[4]
old = lesson["summary"]["key_points"][4]
assert "máximo de g está en la superficie" in old or "máximo de $g$ está en la superficie" in old, repr(old)
if "modelo de Tierra homogénea" not in old and "modelo homogéneo" not in old:
    for target in ("**El máximo de g está en la superficie.**", "**El máximo de $g$ está en la superficie.**"):
        if target in old:
            new = old.replace(target, "**En el modelo de Tierra homogénea, el máximo de g está en la superficie.**" if "g$" not in target else "**En el modelo de Tierra homogénea, el máximo de $g$ está en la superficie.**")
            break
    else:
        raise AssertionError("pattern not found: " + repr(old))
    assert new != old
    lesson["summary"]["key_points"][4] = new
    print("key_points[4] OK")
else:
    print("key_points[4] already scoped, skipped")

# 3) summary.what_to_remember_if_nothing_else
old = lesson["summary"]["what_to_remember_if_nothing_else"]
assert "máximo de g está en la superficie" in old or "máximo de $g$ está en la superficie" in old, repr(old)
if "modelo" not in old:
    for target in ("el máximo de g está en la superficie, no en el centro", "el máximo de $g$ está en la superficie, no en el centro"):
        if target in old:
            repl = target.replace("el máximo", "en el modelo de Tierra homogénea (el que se usa en Selectividad) el máximo")
            new = old.replace(target, repl)
            break
    else:
        raise AssertionError("pattern not found: " + repr(old))
    assert new != old
    lesson["summary"]["what_to_remember_if_nothing_else"] = new
    print("what_to_remember OK")
else:
    print("what_to_remember already scoped, skipped")

json.dump(d, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("SAVED")
