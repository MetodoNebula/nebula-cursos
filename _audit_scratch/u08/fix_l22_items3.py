path = 'bundles/selectividad_quimica__U08_Organica.json'
data = open(path, encoding='utf-8').read()

def apply(data, old, new, label, expect=1):
    c = data.count(old)
    if c == expect:
        data = data.replace(old, new)
        print('OK', label, c)
    else:
        print('MISMATCH', label, 'expected', expect, 'got', c)
    return data

# Finding 12a: worked_examples[2].solution
old12a = '(a) n_etanol=50,0/46,069=1,09 mol. (b) n_O2=3·1,09=3,26 mol ⇒ m_O2=3,26·31,998=104 g. (c) n_CO2=2·1,09=2,17 mol ⇒ m_CO2=2,17·44,009=95,5 g; n_H2O=3·1,09=3,26 mol ⇒ m_H2O=3,26·18,015=58,7 g.'
new12a = '(a) n_etanol=50,0/46,069=1,085 mol. (b) n_O2=3·1,085=3,256 mol ⇒ m_O2=3,256·31,998=104 g. (c) n_CO2=2·1,085=2,171 mol ⇒ m_CO2=2,171·44,009=95,5 g; n_H2O=3·1,085=3,256 mol ⇒ m_H2O=3,256·18,015=58,7 g.'
data = apply(data, old12a, new12a, 'worked_examples[2].solution')

# Finding 12b: exercises[0].full_solution
old12b = 'n_octano=100,0/114,232=0,875 mol. n_O2=12,5·0,875=10,9 mol ⇒ m_O2=10,9·31,998=350 g.'
new12b = 'n_octano=100,0/114,232=0,8754 mol. n_O2=12,5·0,8754=10,94 mol ⇒ m_O2=10,94·31,998=350 g.'
data = apply(data, old12b, new12b, 'exercises[0].full_solution')

# Finding 13: mcq[1].stem
old13 = 'Se queman 10,0 g de un hidrocarburo con 15,0 g de O2, y resulta que el O2 se agota antes de que reaccione todo el combustible. ¿Qué parte de la ecuación general sirve para decidir esto?'
new13 = 'Se queman 10,0 g de un hidrocarburo con 15,0 g de O2. ¿Cómo se decide cuál de los dos es el reactivo limitante?'
data = apply(data, old13, new13, 'mcq[1].stem')

# Finding 14: exercises[1].statement
old14 = 'Se queman 20,0 g de propano con oxígeno en exceso, pero el rendimiento real del proceso (fracción de propano que realmente se transforma en CO2) es del 92,0%. Calcula la masa de CO2 que se obtiene realmente.'
new14 = 'Se queman 20,0 g de propano (M=44,097 g/mol) con oxígeno en exceso; M(CO2)=44,009 g/mol. Por pérdidas en la recogida del gas, solo se consigue recuperar el 92,0% del CO2 producido. Calcula la masa de CO2 que realmente se recoge.'
data = apply(data, old14, new14, 'exercises[1].statement')

old14b = 'm_CO2,real=55,1 g (frente a 59,9 g en el caso teórico).'
new14b = 'm_CO2,recogido=55,1 g (frente a 59,9 g producidos realmente, de los que se pierde un 8,0% en la recogida).'
data = apply(data, old14b, new14b, 'exercises[1].answer')

old14c = 'n_propano=20,0/44,097=0,454 mol. Con rendimiento del 100%: n_CO2=3·0,454=1,36 mol ⇒ m_CO2,teo=1,36·44,009=59,9 g. Con rendimiento real del 92,0%: m_CO2,real=59,9·0,920=55,1 g.'
new14c = 'n_propano=20,0/44,097=0,454 mol. Todo el propano se quema (hay oxígeno en exceso): n_CO2=3·0,454=1,36 mol ⇒ m_CO2,producido=1,36·44,009=59,9 g, que es el CO2 realmente generado por la combustión. De esos 59,9 g, solo se recoge el 92,0%: m_CO2,recogido=59,9·0,920=55,1 g.'
data = apply(data, old14c, new14c, 'exercises[1].full_solution')

# Finding 15: mcq[4].stem
old15 = 'Se queman completamente x gramos de un hidrocarburo puro (CaHb, sin oxígeno propio) con oxígeno en exceso. Si se repite el mismo experimento quemando la misma masa x de un compuesto oxigenado con igual número de C y de H que el hidrocarburo anterior, ¿qué cantidad de O2 se necesitará, en comparación?'
new15 = 'Se queman completamente una masa m de un hidrocarburo puro (CaHb, sin oxígeno propio) con oxígeno en exceso. Si se repite el mismo experimento quemando la misma masa m de un compuesto oxigenado con igual número de C y de H que el hidrocarburo anterior, ¿qué cantidad de O2 se necesitará, en comparación?'
data = apply(data, old15, new15, 'mcq[4].stem')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
