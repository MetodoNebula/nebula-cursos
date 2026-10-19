import json, sys
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"

tikz = (
"\\begin{tikzpicture}[scale=0.85]"
"\\draw[nbaxis] (-0.3,0) -- (9.5,0);\\node[font=\\scriptsize] at (9.8,0.05) {$E$};"
"\\draw[nbaxis] (-0.3,0) -- (-0.3,2.6);\\node[font=\\scriptsize,align=center] at (-0.3,2.9) {fracción de\\\\moléculas};"
"\\fill[NebulaGold,opacity=0.25] plot[smooth] coordinates {(6,0)(6,0.88)(6.5,0.72)(7,0.58)(7.5,0.46)(8,0.36)(8.5,0.28)(9,0.21)} -- (9,0) -- cycle;"
"\\fill[NebulaNavy,opacity=0.3] plot[smooth] coordinates {(6,0)(6,0.38)(6.5,0.25)(7,0.16)(7.5,0.10)(8,0.06)(8.5,0.03)(9,0.01)} -- (9,0) -- cycle;"
"\\draw[NebulaGold,thick] plot[smooth] coordinates {(0,0)(0.5,0.15)(1,0.45)(1.5,0.8)(2,1.1)(2.5,1.35)(3,1.5)(3.5,1.55)(4,1.5)(4.5,1.4)(5,1.25)(5.5,1.05)(6,0.88)(6.5,0.72)(7,0.58)(7.5,0.46)(8,0.36)(8.5,0.28)(9,0.21)};"
"\\node[font=\\scriptsize,NebulaGold] at (4.3,1.75) {$T_2>T_1$};"
"\\draw[nbline,thick] plot[smooth] coordinates {(0,0)(0.5,0.3)(1,0.9)(1.5,1.6)(2,2.1)(2.5,2.3)(3,2.2)(3.5,1.9)(4,1.5)(4.5,1.1)(5,0.8)(5.5,0.55)(6,0.38)(6.5,0.25)(7,0.16)(7.5,0.10)(8,0.06)(8.5,0.03)(9,0.01)};"
"\\node[font=\\scriptsize,NebulaNavy] at (2.0,2.5) {$T_1$};"
"\\draw[nbdash,thick] (6,0) -- (6,1.1);\\node[font=\\scriptsize] at (6,-0.3) {$E_a$};"
"\\node[font=\\scriptsize,align=left] at (7.7,1.3) {área sombreada $\\propto$\\\\fracción con $E\\ge E_a$};"
"\\end{tikzpicture}"
)

new_obj = {
  "id": "TH-Q05-08-1B",
  "type": "intuition",
  "title": "La distribución de energías y la fracción con E ≥ Ea",
  "body": "A una temperatura dada, las moléculas no tienen todas la misma energía cinética: se reparten según una distribución de energías (curva de Maxwell-Boltzmann). El área bajo la curva a la derecha de $E_a$ representa la fracción de choques con energía suficiente para reaccionar. Al subir la temperatura (de $T_1$ a $T_2$), la curva se ensancha y su máximo se desplaza hacia energías mayores: aunque la curva a $T_2$ parece más baja cerca del origen, el área a la derecha de $E_a$ es mucho mayor que a $T_1$. Esta es la causa microscópica de que $k$ crezca tan deprisa con la temperatura, y es exactamente la misma idea con la que un catalizador consigue acelerar una reacción sin cambiar $T$: al reducir $E_a$, desplaza la línea vertical hacia la izquierda, de modo que una fracción mayor de la misma curva queda por encima de ella.",
  "concept_ids": ["C-Q05-08-1"],
  "objective_ids": ["LO-Q05-08-2"],
  "provenance": "SOURCE_DERIVED",
  "assets": [
    {
      "id": "AS-Q05-08-1",
      "type": "tikz",
      "caption": "Distribución de energías de las moléculas a dos temperaturas ($T_2>T_1$). El área sombreada a la derecha de $E_a$ es la fracción de choques con energía suficiente para reaccionar: crece mucho al pasar de $T_1$ a $T_2$.",
      "tikz": tikz
    }
  ]
}

block_text = json.dumps(new_obj, ensure_ascii=False, indent=2)
prefixed = "\n".join(("      " + line if line.strip() else line) for line in block_text.split("\n"))

old_frag = '"provenance": "SOURCE_DERIVED"\n      },\n      {\n        "id": "TH-Q05-08-2",'
new_frag = '"provenance": "SOURCE_DERIVED"\n      },\n' + prefixed + ',\n      {\n        "id": "TH-Q05-08-2",'

data = open(PATH, encoding="utf-8").read()
n = data.count(old_frag)
print("occurrences:", n)
if n == 1:
    data = data.replace(old_frag, new_frag, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("INSERTED OK")
else:
    print("ABORT")
