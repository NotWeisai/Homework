s_al = input('Кто решил задачу по алгебре: ').split()
s_geom = input('Кто решил задачу по геометрии: ').split()
s_trig = input('Кто решил задачу по тригонометрии: ').split()
al = set()
geom = set()
trig = set()

for i in s_al:
    al.add(i)
for i in s_geom:
    geom.add(i)
for i in s_trig:
    trig.add(i)

res = al.intersection(geom, trig)
if len(res) == 0:
    print('Никто не решил все три задачи.')
else:
    print('Все три задачи решил: ', res)