#Operátorok
#Értékadó operátor - =
from asyncio.windows_events import NULL
from tkinter import E


szoveg1="Kutya"
szoveg2='Kutya'#ne használjuk
valosSzam1=123.56
egeszSzam1=245
logikaiValtozo1=True
logikaiValtozo2=False
#logikaiValtozo3=NULL
print(szoveg1,szoveg2,valosSzam1,egeszSzam1,logikaiValtozo1,logikaiValtozo2)
#Műveleti operátorok --- +,-,*,/,%-mod,//-div,**-hatványozás
eredmeny1=valosSzam1+egeszSzam1
print(eredmeny1)
eredmeny1=valosSzam1-egeszSzam1
print(eredmeny1)
eredmeny1=valosSzam1/egeszSzam1
print(eredmeny1)
eredmeny1=valosSzam1*egeszSzam1
print(eredmeny1)
eredmeny2=10/3
print(eredmeny2)
eredmeny2=10//3
print(eredmeny2)
eredmeny2=10%3
print(eredmeny2)
eredmeny3=2**8
print(eredmeny3)
szovegesEredmeny1=szoveg1+szoveg2
print(szovegesEredmeny1)
szovegesEredmeny2=szoveg1*5
print(szovegesEredmeny2)
#értéknövelő operátorok - +=,-=
darab=0
print(darab)
darab+=1 #darab=darab+1
print(darab)
darab-=1 #darab=darab-1
print(darab)
#Összehasonlító operátorok - <,>,<=,>=,!=,==
#Egyszerű egyirányú elágazás - if
if (valosSzam1<1000):
    print("A valosSzam1 változó értéke kisebb mint 1000.")
    print("Vizsgálat vége.")
#Összetett kétirányú elágazás - if-else
if (egeszSzam1>500):
    print("Az egeszSzam1 változó értéke nagyobb mint 500.")
else:
    print("Az egészSzam1 változó értéke kisebb vagy egyenlő mint 500.")
#Összetett több irányú elágazás - if-elif-else
if (egeszSzam1==245):
    print("Az egeszSzam1 értéke 245.")
elif (egeszSzam1>245):
    print("Az egeszSzam1 értéke nagyobb mint 245.")
else:
    print("Az egeszSzam1 értéke kisebb mint 245.")
if (szoveg1==szoveg2):
    print("Azonos a két szöveg.")

#Logikai operátorok - or,and,not
# or   |  and  | not
#A B E | A B E | A E
#0 0 0 | 0 0 0 | 0 1
#0 1 1 | 0 1 0 | 1 0
#1 0 1 | 1 0 0
#1 1 1 | 1 1 1

egeszSzam2=246
if (egeszSzam1>=245 and egeszSzam2<=246):
    print("fsdjfsdhkfskf")
if (szoveg1=="Kutyaa" or egeszSzam1>100):
    print("kfldfdfkdlfsdf")
if (logikaiValtozo1):
    print("sdwwewe")
if (not logikaiValtozo2):
    print("lkésdjlskdhasfjdl")