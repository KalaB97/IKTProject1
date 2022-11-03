bekertOra=int(input("hány órás visszaszámlálást tervezzünk? "))
kesleltetes=0
for i in range (bekertOra):
    print(f"Visszaszámlálás: {bekertOra-i}")
    felfuggesztes=input("Fel kell függeszteni a vissza számlálást (i/n)?")
    if (felfuggesztes=="i"):
        kesleltetes+=1
print(f"A rakéta a vissza számlálást követően ennyi órával indult : {bekertOra+kesleltetes}")