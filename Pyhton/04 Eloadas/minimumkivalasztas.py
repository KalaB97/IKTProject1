import random

szamok=[]

for i in range(100):
    generaltSzam=random.randrange(1000)
    szamok.append(generaltSzam)
print(min(szamok))

minimumSzam=szamok[0]
for i in range(1,len(szamok)):
    if (szamok[i]<minimumSzam):
        minimumSzam=szamok[i]
print(minimumSzam)

