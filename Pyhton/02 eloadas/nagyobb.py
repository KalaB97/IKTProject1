szam1=int(input("Adj meg egy számot"))
szam2=int(input("Adj meg egy másik számot"))
if (szam1>szam2):
        print("A nagyobb érték",szam1)
        print("A nagyobb érték" +str(szam1)) #számból szöveget készítünk az str függvénnyel 
        print("A nagyobb érték {0}".format(szam1))
        print(f"A nagyobb érték {szam1}") #az f betű formázás jelent be helyetesití a számmal
elif (szam2>szam1):
    print(f"A nagyobb érték {szam2}")
else:
    print ("A két szám egyenlő")
        

        