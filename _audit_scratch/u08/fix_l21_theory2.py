path = 'bundles/selectividad_quimica__U08_Organica.json'
data = open(path, encoding='utf-8').read()
BS = chr(92) * 2
NL = chr(92) + 'n'

def apply(data, old, new, label, expect=1):
    c = data.count(old)
    if c == expect:
        data = data.replace(old, new)
        print('OK', label, c)
    else:
        print('MISMATCH', label, 'expected', expect, 'got', c)
    return data

old = ('La regla que se ha visto para el eteno es general para cualquier monómero del tipo CH2=CH-R (llamado monómero vinílico): el doble enlace se abre y R queda colgando, sin tocarse, en cada unidad de la cadena. Algunos de los más comunes:' + NL + NL
       + '| Monómero | Reacción | Polímero (usos típicos) |' + NL
       + '|---|---|---|' + NL
       + '| Propeno, CH2=CH-CH3 | n CH2=CH-CH3 → (-CH2-CH(CH3)-)n | Polipropileno (PP): envases, cuerdas, tejidos técnicos |' + NL
       + '| Cloruro de vinilo, CH2=CHCl | n CH2=CHCl → (-CH2-CHCl-)n | Policloruro de vinilo (PVC): tuberías, marcos de ventana |' + NL
       + '| Estireno, C6H5-CH=CH2 | n C6H5-CH=CH2 → (-CH2-CH(C6H5)-)n | Poliestireno (PS): embalajes, aislante térmico |' + NL + NL
       + 'Un cuarto ejemplo que aparece a menudo citado, aunque sin cálculo numérico porque su monómero contiene flúor, es el tetrafluoroeteno (CF2=CF2), cuyo polímero es el politetrafluoretileno (PTFE, más conocido como teflón), usado por su altísima resistencia química y su superficie antiadherente.' + NL + NL
       + 'El patrón es siempre el mismo: localizar el doble enlace C=C del monómero, abrirlo, y escribir exactamente los mismos átomos —ni uno más, ni uno menos— como unidad repetitiva entre paréntesis.')

new = ('La regla que se ha visto para el eteno es general para cualquier monómero del tipo $' + BS + 'mathrm{CH_2{=}CH{-}R}$ (llamado monómero vinílico): el doble enlace se abre y R queda colgando, sin tocarse, en cada unidad de la cadena. Algunos de los más comunes:' + NL + NL
       + '| Monómero | Reacción | Polímero (usos típicos) |' + NL
       + '|---|---|---|' + NL
       + '| Propeno (prop-1-eno), $' + BS + 'mathrm{CH_2{=}CH{-}CH_3}$ | $n' + BS + ',' + BS + 'mathrm{CH_2{=}CH{-}CH_3} ' + BS + 'longrightarrow ' + BS + 'mathrm{({-}CH_2{-}CH(CH_3){-})}_n$ | Polipropileno (PP): envases, cuerdas, tejidos técnicos |' + NL
       + '| Cloruro de vinilo (cloroeteno), $' + BS + 'mathrm{CH_2{=}CHCl}$ | $n' + BS + ',' + BS + 'mathrm{CH_2{=}CHCl} ' + BS + 'longrightarrow ' + BS + 'mathrm{({-}CH_2{-}CHCl{-})}_n$ | Policloruro de vinilo (PVC): tuberías, marcos de ventana |' + NL
       + '| Estireno (etenilbenceno o fenileteno), $' + BS + 'mathrm{C_6H_5{-}CH{=}CH_2}$ | $n' + BS + ',' + BS + 'mathrm{C_6H_5{-}CH{=}CH_2} ' + BS + 'longrightarrow ' + BS + 'mathrm{({-}CH_2{-}CH(C_6H_5){-})}_n$ | Poliestireno (PS): embalajes, aislante térmico |' + NL + NL
       + 'Un cuarto ejemplo citado a menudo es el tetrafluoroeteno, $' + BS + 'mathrm{CF_2{=}CF_2}$, cuyo polímero es el politetrafluoroeteno (PTFE, nombre sistemático; más conocido por su nombre comercial, teflón), usado por su altísima resistencia química y su superficie antiadherente. El cálculo de su masa molar no tiene ningún obstáculo: con $A_r(F)=19{,}00$, $M(' + BS + 'mathrm{C_2F_4})=2' + BS + 'cdot12{,}011+4' + BS + 'cdot19{,}00=100{,}02' + BS + ',' + BS + 'mathrm{g/mol}$, igual que con cualquier otro monómero.' + NL + NL
       + 'El patrón es siempre el mismo: localizar el doble enlace C=C del monómero, abrirlo, y escribir exactamente los mismos átomos —ni uno más, ni uno menos— como unidad repetitiva entre paréntesis.' + NL + NL
       + '**El mecanismo, por etapas (radicalario):** un iniciador con un enlace débil, típicamente un peróxido R' + chr(8211) + 'O' + chr(8211) + 'O' + chr(8211) + 'R, se rompe con el calor en dos radicales libres: $' + BS + 'mathrm{R{-}O{-}O{-}R ' + BS + 'longrightarrow 2' + BS + ',RO' + BS[0] + 'cdot}$. En la **iniciación**, un radical ataca al doble enlace de un monómero: $' + BS + 'mathrm{RO' + BS[0] + 'cdot + CH_2{=}CH_2 ' + BS + 'longrightarrow RO{-}CH_2{-}CH_2' + BS[0] + 'cdot}$. En la **propagación**, el nuevo radical ataca a otro monómero, y así sucesivamente, alargando la cadena un monómero cada vez. En la **terminación**, dos cadenas radicalarias se encuentran y se combinan, formando un enlace entre ellas y dejando ya sin electrón desapareado al producto final; los restos del iniciador quedan como grupos terminales en los dos extremos de la cadena (de ahí que M = n' + BS[0] + 'cdot M_0 sea exacto solo si se desprecian esos extremos).' + NL + NL
       + '**Otros monómeros de adición habituales en PAU:** el acrilonitrilo, $' + BS + 'mathrm{CH_2{=}CH{-}CN}$, da poliacrilonitrilo (PAN, usado en fibras tipo lana sintética); el metacrilato de metilo, $' + BS + 'mathrm{CH_2{=}C(CH_3){-}COOCH_3}$, da poli(metacrilato de metilo) (PMMA, el plexiglás); y los dienos conjugados, con dos dobles enlaces, dan cauchos sintéticos: el isopreno, $' + BS + 'mathrm{CH_2{=}C(CH_3){-}CH{=}CH_2}$, es el monómero del caucho natural (poliisopreno), y el buta-1,3-dieno, $' + BS + 'mathrm{CH_2{=}CH{-}CH{=}CH_2}$, da polibutadieno. Cuando una cadena se forma a partir de dos monómeros distintos mezclados (por ejemplo estireno y butadieno), el producto se llama copolímero, y ya no es una simple repetición de una sola unidad.')

data = apply(data, old, new, 'theory_blocks[2] full rewrite')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
