jelszo="Kando"

marad=3
while(marad>0):
    bekertJelszo=input("kérem a jelszót: ")
    if (bekertJelszo==jelszo):
        print("sikeres bejelenkezés.")
        marad=0
    marad-=1
if(marad==-1):
            print("dolgozhat")
else:
    print("sikertelen bejelentkezés. 10 perc múlva újra próbálkozhat!")


    jelszo="kando"

    marad=3
    while(marad>0):
        bekertJelszo=input ("Kérem a jelszót: ")
        if (bekertJelszo==jelszo)
            print("Sikeres bejelentkezés")
            marad=0
        if (Marad==1):
            print("10 másodperc várás..") 
            sleep(10)
            marad=4
        marad-=1
print("Dolgozhat")  