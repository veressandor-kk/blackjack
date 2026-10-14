'''
Ahol AI volt használva:
.pop() metódus - kártyahúzás a pakliból - 31., 32., 49., 62. sor
pakli = [] lista - a pakli helyes létrehozásához - 23. sor
'''

import random

def ertek(kartya):
    if kartya[0] in ['bubi', 'dáma', 'király', 'ász']:
        return 10
    else:
        return int(kartya[0])

def kez_erteke(kartyak):
    osszeg = 0
    for kartya in kartyak:
        osszeg += ertek(kartya)
    return osszeg

szinek = ['♥', '♦', '♣', '♠']
szamok = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'bubi', 'dáma', 'király', 'ász']
pakli = [(szam, szin) for szam in szamok for szin in szinek]

random.shuffle(pakli)

jatekos = []
oszto = []

for _ in range(2):
    jatekos.append(pakli.pop())
    oszto.append(pakli.pop())

print("A lapjaid:")
for kartya in jatekos:
    print(' '.join(kartya))
jatekos_erteke = kez_erteke(jatekos)
print(f"A pontszámod: {jatekos_erteke}\n")

print("Az osztó lapjai:")
for kartya in oszto:
    print(' '.join(kartya))
oszto_erteke = kez_erteke(oszto)
print(f"Az osztó pontszáma: {oszto_erteke}")

while jatekos_erteke < 21:
    valasz = input("\nKérsz még lapot? (i/n): ")
    if valasz == "i":
        uj_kartya = pakli.pop()
        jatekos.append(uj_kartya)
        print("Az új lapod:", ' '.join(uj_kartya))
        jatekos_erteke = kez_erteke(jatekos)
        print(f"A pontszámod: {jatekos_erteke}")
    elif valasz == "n":
        break
    else:
        print("Kérlek, i vagy n betűt írj be!")

if jatekos_erteke <= 21:
    print("\nAz osztó jön.")
    while oszto_erteke < 17:
        uj_kartya = pakli.pop()
        oszto.append(uj_kartya)
        print("Az osztó új lapja:", ' '.join(uj_kartya))
        oszto_erteke = kez_erteke(oszto)
        print(f"Az osztó pontszáma: {oszto_erteke}")

print("\n--- Végeredmény ---")

if jatekos_erteke == oszto_erteke:
    print(f"A te pontszámod: {jatekos_erteke}\nAz osztó pontszáma: {oszto_erteke}")
    print("\nDöntetlen!")
    
elif jatekos_erteke == 21:
    print(f"A te pontszámod: {jatekos_erteke}\nAz osztó pontszáma: {oszto_erteke}")
    print("\nBlackjack! A pontszámod 21.\nNyertél!")
    
elif oszto_erteke == 21:
    print(f"A te pontszámod: {jatekos_erteke}\nAz osztó pontszáma: {oszto_erteke}")
    print("\nBlackjack! Az osztó pontszáma 21.\nVesztettél!")

elif jatekos_erteke > 21:
    print(f"A te pontszámod: {jatekos_erteke}\nAz osztó pontszáma: {oszto_erteke}")
    print("\nTúllépted a 21 pontot.\nVesztettél!")

elif oszto_erteke > 21:
    print(f"A te pontszámod: {jatekos_erteke}\nAz osztó pontszáma: {oszto_erteke}")
    print("\nAz osztó túllépte a 21 pontot.\nNyertél!")

elif jatekos_erteke > oszto_erteke:
    print(f"A te pontszámod: {jatekos_erteke}\nAz osztó pontszáma: {oszto_erteke}")
    print("\nA te pontszámod közelebb van a 21-hez.\nNyertél!")

else:
    print(f"A te pontszámod: {jatekos_erteke}\nAz osztó pontszáma: {oszto_erteke}")
    print("\nAz osztó pontszáma közelebb van a 21-hez.\nVesztettél!")