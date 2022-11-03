szo1=input("Adj meg egy szót!")
szo2=input ("Adj meg egy másik szót!")
szo1Hossza=len(szo1)#len függvény megmondja hogy hány angol abc betűből áll
szo2Hossza=len(szo2)
if (szo1Hossza>szo2Hossza):
    print(f"A hosszabb szó: {szo1}")
elif (szo2Hossza>szo1Hossza):
    print(f"Hosszabb szó : {szo2}")
else: 
    print(" A két szó egyforma hosszú")    
    