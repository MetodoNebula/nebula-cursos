import sys
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
with open(PATH, "r", encoding="utf-8") as f:
    data = f.read()

i0 = data.find('"24_Propiedades')
i1 = data.find('"25_', i0)
seg = data[i0:i1]

def rep(old, new, expect, label):
    global seg
    c = seg.count(old)
    if c != expect:
        print("MISMATCH", label, "expected", expect, "got", c)
        idx = seg.find(old[:50])
        print("near:", repr(seg[max(0,idx-20):idx+200]))
        sys.exit(1)
    seg = seg.replace(old, new)
    print("OK", label, c)

BS = chr(92)*2
NL = chr(92) + 'n'

# F6: keywords[5].definition — isomer definition including stereoisomers
old = "Compuestos con la misma fórmula molecular pero distinta conectividad, que pueden diferir mucho en sus propiedades físicas y químicas."
new = "Compuestos con la misma fórmula molecular pero distinta estructura (distinta conectividad -isómeros estructurales- o distinta disposición espacial -estereoisómeros-), que pueden diferir mucho en sus propiedades físicas y químicas."
rep(old, new, 1, "F6 keywords[5]")

# F7: theory_blocks[1].body — ácido acético row
old = "| Ácido acético | ácido carboxílico | Sí (O-H, por duplicado) | 60,1 | 117,9°C |"
new = "| Ácido acético | ácido carboxílico | Sí (un O-H; forma dímeros con dos enlaces de H) | 60,1 | 117,9°C |"
rep(old, new, 1, "F7 tabla ácido acético")

# F8/F12: theory_blocks[1].body — añadir filas aldehído/cetona + nombres IUPAC + nota longitud/ramificación
old = '''| Compuesto | Grupo funcional | ¿H unido a O o N? | M (g/mol) | Teb |
|---|---|---|---|---|
| Butano | alcano | No | 58,1 | -0,5°C |
| Metil formiato | éster | No | 60,1 | 31,5°C |
| Propilamina | amina 1ª | Sí (N-H) | 59,1 | 48,0°C |
| Propan-1-ol | alcohol | Sí (O-H) | 60,1 | 97,2°C |
| Ácido acético | ácido carboxílico | Sí (un O-H; forma dímeros con dos enlaces de H) | 60,1 | 117,9°C |'''
new = '''| Compuesto | Grupo funcional | ¿H unido a O o N? | M (g/mol) | Teb |
|---|---|---|---|---|
| Butano | alcano | No | 58,1 | -0,5°C |
| Propanal (aldehído) | aldehído | No | 58,1 | 48°C |
| Propanona (acetona) | cetona | No | 58,1 | 56°C |
| Metil formiato (metanoato de metilo) | éster | No | 60,1 | 31,5°C |
| Propilamina (propan-1-amina) | amina 1ª | Sí (N-H) | 59,1 | 48,0°C |
| Propan-1-ol | alcohol | Sí (O-H) | 60,1 | 97,2°C |
| Ácido acético (ácido etanoico) | ácido carboxílico | Sí (un O-H; forma dímeros con dos enlaces de H) | 60,1 | 117,9°C |

Aldehídos y cetonas tienen un dipolo C=O permanente (más intenso que el de un éter) pero ningún H unido a O: hierven más que un éster o un alcano de masa parecida, pero menos que un alcohol o un ácido, porque no pueden formar enlace de hidrógeno entre ellos. Dentro de una misma serie homóloga, el punto de ebullición sube con la longitud de la cadena (más superficie de contacto, más dispersión de London) y baja con la ramificación (una molécula más compacta tiene menos superficie de contacto con sus vecinas).'''
rep(old, new, 1, "F8 tabla aldehído/cetona")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE B")
