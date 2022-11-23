bekertOra=int(input("Hány órás visszaszámlálást tervezünk? "))
kesleltetes=0
for i in range(bekertOra):
    print(f"Visszaszámlálás: {bekertOra-i}")
    felfuggesztes=input("Fel kell függeszteni a visszaszámlálást (i/n)?")
    if (felfuggesztes.upper()=="I"):
        kesleltetes+=1
print(f"A rakéta a visszaszámlálást követően ennyi órával indult: {bekertOra+kesleltetes}")


#for i in range(bekertOra,0,-1):
#    print(f"Visszaszámlálás: {i}")
