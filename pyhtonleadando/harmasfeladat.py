def harmasfeladat():
    bekertszam=int(input("Adjon meg egy pozitív egész számot!: "))
    for i in range (bekertszam):
        if (i%2==0):
            print("0")
        else:
            print("1")
    

harmasfeladat()