import random

def Osszehasonlitas(veletlenSzam,begepeltSzam):
    if (veletlenSzam>begepeltSzam):
        return f"A gép nagyobb számra gondolt:{veletlenSzam}"
    elif (veletlenSzam<begepeltSzam): 
        return f"A gép kisebb számra gondolt : {veletlenSzam}"
    else:
        return f"Eltaláltad a gép által gondolt számot {veletlenSzam}"

veletlenSzam=random.randrange(1,17)
begepeltSzam=int(input("ajd meg egy számot"))
print(Osszehasonlitas(veletlenSzam,begepeltSzam))
uzenet=Osszehasonlitas(veletlenSzam,begepeltSzam)
print(uzenet)
for betu in uzenet:
    print (betu,end=betu)
print("")