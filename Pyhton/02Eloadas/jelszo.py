from time import sleep

jelszo="Kando"

marad=3
while(marad>0):
    bekertJelszo=input("Kérem a jelszót: ")
    if (bekertJelszo==jelszo):
        print("Sikeres bejelentkezés.")
        marad=0
    if (marad==1):
        print("10 másodperc várakozás....")
        sleep(10)
        marad=4
    marad-=1
print("Dolgozhat")