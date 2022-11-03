#Operátorok
#Értékadó operátor =
szoveg1="Kutya"
szoveg2="Kutya"
valoszSzam1=123.56
egeszSzam1=245
logikaiValtozo1=True
logikaiValtozo2=False
print(szoveg1,szoveg2,valoszSzam1,egeszSzam1,logikaiValtozo1,logikaiValtozo2)
#Műveleti operátorok - +, -,*,/,%-mod,//-div,**-hatványozás
eredmeny1=valoszSzam1+egeszSzam1
print(eredmeny1)
eredmeny1=valoszSzam1-egeszSzam1
print(eredmeny1)
eredmeny1=valoszSzam1/egeszSzam1
print(eredmeny1)
eredmeny1=valoszSzam1*egeszSzam1
print(eredmeny1)
eredmeny2=10/3
print(eredmeny2)
eredmeny2=10/3
print(eredmeny2)
eredmeny2=10//3
print(eredmeny2)
eredmeny2=10%3
print(eredmeny2)
eredmeny3=2**8
print(eredmeny3)
szovegeseredmeny=szoveg1+szoveg2
print(szovegeseredmeny)
szovegeseredmeny2=szoveg1*5
print(szovegeseredmeny2)
#értéknövelő operátorok - +=,-=
darab=0 #&darab=darab+1
print(darab)
darab+=1 #darab=darab-1
print(darab)
darab-=1
print(darab)
#összehasonlitó operátorok -< ,> <=,>=,!=,==
#egyszerű egyirányú elágazás
if (valoszSzam1<1000):
        print("A valoszSzam1 változó értéke kisebb mint 1000.")
        print("vizsgálat vége.")
#összetett kétirányú elágazás
if (egeszSzam1>500):
    print("Az egészszám változó értékenagyobb mint 500")
else:
    print("Az egyeszSzam1 változó értéke kisebb mint vagy egyenlő mint 500")
#összetett több irányú elágazás
if (egeszSzam1==245):
    print("Az egeszSzam1 értéke 245.")
elif (egeszSzam1>245):
    print("Az egeszSzam1 értéke nagyobb mint 245.")
else:
    print("Az egeszSzam1 ertéke kisebb mint 245")
if (szoveg1==szoveg2):
    print("azonos a két szöveg")  
#Logikai Operátorok - and,or,not

egeszSzam2=246
if (egeszSzam1>=245 and egeszSzam2<=246):
    print("jjb")   
if (szoveg1=="kutya" or egeszSzam1>1000):
    print("kgjghn")
if (logikaiValtozo1==True):
    print("nbknfknh")
if ( not logikaiValtozo2):
    print("knjb")        


 
