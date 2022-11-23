import random

maxSzam=90
hanyasLotto=5
sajatSzamok=[]
print("Add meg a saját számaidat (ötöslottó)")
for i in range(5):
    szam=int(input(f"{i+1}. szám: "))
    sajatSzamok.append(szam)
sorsoltSzamok=[]
while(len(sorsoltSzamok)<hanyasLotto):
    sorsoltSzam=random.randrange(1,maxSzam+1)
    if(sorsoltSzam not in sorsoltSzamok):
        sorsoltSzamok.append(sorsoltSzam)
print(sorsoltSzamok)
talatokSzama=0
for egySajatSzam in sajatSzamok:
    if (egySajatSzam in sorsoltSzamok):
        talatokSzama+=1
print (f"Találatok száma :{talatokSzama}")

