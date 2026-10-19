path = 'bundles/selectividad_quimica__U08_Organica.json'
data = open(path, encoding='utf-8').read()

i0 = data.find('"21_Polimerización_por_adición.json"')
i1 = data.find('"22_', i0)
seg = data[i0:i1]

c_m0 = seg.count('M0')
seg = seg.replace('M0', 'M$_0$')

old_nh2 = chr(8211) + 'NH2)'
new_nh2 = chr(8211) + 'NH$_2$)'
c_nh2 = seg.count(old_nh2)
seg = seg.replace(old_nh2, new_nh2)

old_h2o = 'pequeña (H2O, HCl)'
new_h2o = 'pequeña (H$_2$O, HCl)'
c_h2o = seg.count(old_h2o)
seg = seg.replace(old_h2o, new_h2o)

print('M0', c_m0, 'NH2)', c_nh2, 'H2O,HCl', c_h2o)

data = data[:i0] + seg + data[i1:]
open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
