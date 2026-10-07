import random

def ertek(kartya):
    if kartya[0] in ['bubi', 'dáma', 'király', 'ász']:
        return 10
    else:
        return int(kartya[0])

szinek = ['kőr', 'káró', 'treff', 'pikk']
szamok = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'bubi', 'dáma', 'király', 'ász']
pakli = [(szam, szin) for szin in szinek for szam in szamok]

random.shuffle(pakli)

jatekos = []
oszto = []

for _ in range(2):
    jatekos.append(pakli.pop())
    oszto.append(pakli.pop())

print("A lapjaid:")
for jatekos_kartyai in jatekos:
    print(', '.join(jatekos_kartyai))
