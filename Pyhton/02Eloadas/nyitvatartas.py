bekertOra=int(input("Hány óra van most? "))
if (8<=bekertOra<16):
    print("A bolt nyitva van.")
    print(f"Ennyi órád van még odaérni: {16-bekertOra}")
else:
    print("A bolt zárva van.")