bekertOra=int(input("Hány óra van most?"))
if (8<=bekertOra<16):
    print(" a bolt nytiva van ")
    print(f"Ennyi órád van még oda érni : {16-bekertOra}")
else: # ha az if feltétel nem igaz ugrik az else ágra
    print("A bolt zárva van ")
    