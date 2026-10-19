# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"solution": "$x=0{,}1696 \\Rightarrow [H_2]_{eq}=0{,}500-0{,}1696=0{,}330$ M; $[I_2]_{eq}=0{,}200-0{,}1696=0{,}0304$ M; $[HI]_{eq}=0{,}400+2\\cdot0{,}1696=0{,}739$ M",'''

new = r'''"solution": "$54{,}3=\\dfrac{(0{,}400+2x)^2}{(0{,}500-x)(0{,}200-x)}\\Rightarrow(0{,}400+2x)^2=54{,}3(0{,}100-0{,}700x+x^2)\\Rightarrow50{,}3x^2-39{,}61x+5{,}27=0\\Rightarrow x=\\dfrac{39{,}61\\pm\\sqrt{39{,}61^2-4\\cdot50{,}3\\cdot5{,}27}}{2\\cdot50{,}3}$: $x_1=0{,}170$, $x_2=0{,}618$ (se descarta: $0{,}200-0{,}618<0$). $x=0{,}1696 \\Rightarrow [H_2]_{eq}=0{,}500-0{,}1696=0{,}330$ M; $[I_2]_{eq}=0{,}200-0{,}1696=0{,}0304$ M; $[HI]_{eq}=0{,}400+2\\cdot0{,}1696=0{,}739$ M",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
