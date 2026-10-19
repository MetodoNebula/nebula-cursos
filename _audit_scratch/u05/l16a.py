# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

# H1 + H4: rewrite theory_blocks[0] (TH-Q05-16-1)
edits.append(("H1_H4_TH1", r'''"title": "Sales «insolubles» que en realidad se disuelven un poco",
        "body": "Cuando dos o más sales tienen **la misma estequiometría de disociación** (p. ej., todas $AB$ con $K_{sp}=s^2$, o todas $AB_2$ con $K_{sp}=4s^3$), basta comparar sus $K_{sp}$ para ordenarlas por solubilidad: menor $K_{sp}$ implica menor $s$. Sin embargo, esta comparación directa **no es válida** entre sales de tipos distintos (por ejemplo, $AB$ frente a $AB_2$), porque la relación entre $s$ y $K_{sp}$ varía con el tipo: una sal $AB_2$ con $K_{sp}$ algo mayor que una $AB$ puede ser menos soluble. Para comparar esos casos hay que calcular $s$ explícitamente en cada caso.",''',
r'''"title": "Disolución saturada y equilibrio dinámico",
        "body": "Ninguna sal es totalmente insoluble. Al echar $AgCl$ en agua, se disuelve una cantidad pequeñísima hasta que la disolución queda saturada; a partir de ese momento, los iones se disuelven y precipitan a la misma velocidad: es un equilibrio dinámico entre el sólido y sus iones en disolución, igual que cualquier otro equilibrio químico.\n\nLa concentración de sal disuelta en la disolución saturada se llama solubilidad molar, $s$ (en mol/L), y es la incógnita que casi siempre se busca en los problemas de esta lección. Tanto $K_{sp}$ como $s$ dependen de la temperatura, igual que cualquier constante de equilibrio.",'''
))

# H2 + H1 example: rewrite theory_blocks[4] (TH-Q05-16-5)
edits.append(("H2_TH5", r'''"body": "Un error habitual es decir «esta sal tiene Ksp más pequeño, luego es más soluble que la otra» sin fijarse en que son de distinta estequiometría. Como la relación entre Ksp y s cambia con la estequiometría (potencia 2 para AB, potencia 1/3 con factor 4 para AB2/A2B), **dos sales con Ksp parecido pueden tener solubilidades molares muy distintas**, y solo se pueden comparar directamente por Ksp si son del mismo tipo estequiométrico.",''',
r'''"body": "Un error habitual es decir «esta sal tiene un $K_{sp}$ más pequeño, luego es menos soluble» sin fijarse en que las sales pueden tener distinta estequiometría. La relación entre $K_{sp}$ y $s$ cambia con el tipo de sal: $s=\\sqrt{K_{sp}}$ para sales tipo $AB$, pero $s=\\sqrt[3]{K_{sp}/4}$ para sales tipo $AB_2$ o $A_2B$. Por eso, una sal $A_2B$ o $AB_2$ con $K_{sp}$ MENOR que una sal $AB$ puede ser, en realidad, MÁS soluble. Ejemplo real: $K_{sp}(Ag_2CrO_4)=1{,}1\\cdot10^{-12}<K_{sp}(AgCl)=1{,}8\\cdot10^{-10}$, y sin embargo $s(Ag_2CrO_4)=6{,}5\\cdot10^{-5}$ M es MAYOR que $s(AgCl)=1{,}34\\cdot10^{-5}$ M. Dos sales solo se pueden comparar directamente por su $K_{sp}$ si son del mismo tipo estequiométrico; si no, hay que calcular $s$ explícitamente en cada caso.",'''
))

results = []
ok_all = True
for label, old, new in edits:
    n = data.count(old)
    results.append((label, n))
    if n == 1:
        data = data.replace(old, new, 1)
    else:
        ok_all = False
for lb, cnt in results:
    print(lb, cnt)
if ok_all:
    open(PATH, "w", encoding="utf-8").write(data)
    print("ALL WRITTEN")
else:
    print("ABORT")
