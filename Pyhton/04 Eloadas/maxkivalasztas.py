import random

szamok=[]

for i in range(100):
    generaltSzam=random.randrange(1000)
    szamok.append(generaltSzam)

#maximum kivalasztas tetele
maxSzam=szamok[0]
for i in range(1,len(szamok)):
    if (szamok[i]>maxSzam):
        maxSzam=szamok[i]
print(maxSzam)


