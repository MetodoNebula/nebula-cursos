PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = '''Dar por buena una aproximación sin calcular el error relativo que introduce.",
        "why": "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.",
        "how_to_avoid": "Resolver siempre, al menos la primera vez, también sin aproximar, y comparar ambos resultados antes de decidir si la aproximación vale.'''

new = '''Dar por buena una aproximación sin calcular el error relativo que introduce.",
        "why": "Se recuerda la regla «Kc pequeña, se puede aproximar» como automática, sin comprobar después que x_aprox/c0 sea realmente menor del 5%.",
        "how_to_avoid": "Calcular siempre x_aprox/c0 tras aproximar; si no es menor del 5%, resolver también la ecuación completa, sin aproximar.'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT - not unique")
