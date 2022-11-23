import random

def Kiiras(veletlenSzam,begepeltSzam):
    if (veletlenSzam>begepeltSzam):
        print(f"A gép nagyobb számra gondolt: {veletlenSzam}")
    elif (veletlenSzam<begepeltSzam):
        print(f"A gép kisebb számra gondolt: {veletlenSzam}")
    else:
        print(f"Eltaláltad a gép által gondolt számot! {veletlenSzam}")

vSzam=random.randrange(1,17)
bSzam=int(input("Adj meg egy számot! "))
Kiiras(vSzam,bSzam)