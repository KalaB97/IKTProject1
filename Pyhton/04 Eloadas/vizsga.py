import random

def pontszamGenerator(maxPontszam):
    return random.randrange(0,maxPontszam+1)

def ertekeles(Pontszam):
    if (Pontszam<48):
        return 1
    if (Pontszam<=66):
        return 2
    if (Pontszam<=84):
        return 3 
    if (Pontszam<=102):
        return 4
    return 5              

Diakok=["Csaba","Berta","Zsolt","Kristóf","Attila","Laci","Adri","Tímea","István","Anett","Judit","Zsombor","Gabi"]

pontSzamok=[]
print(len(Diakok))
for i in range (len(Diakok)):
    pontSzamok.append(pontszamGenerator(120))

szum=0
for i in range(len(Diakok)):
    erdemjegy=ertekeles(pontSzamok[i])
    print(f"{Diakok[i]}: {erdemjegy}")
    szum+=erdemjegy
print(f"Osztály átlag : {round(szum/len(Diakok),2)}")

