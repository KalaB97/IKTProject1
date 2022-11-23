import random

veletlenSzam=random.randrange(1,17)
begepeltSzam=int(input("Adj meg egy számot! "))
if (veletlenSzam>begepeltSzam):
    print(f"A gép nagyobb számra gondolt: {veletlenSzam}")
elif (veletlenSzam<begepeltSzam):
    print(f"A gép kisebb számra gondolt: {veletlenSzam}")
else:
    print(f"Eltaláltad a gép által gondolt számot! {veletlenSzam}")
    