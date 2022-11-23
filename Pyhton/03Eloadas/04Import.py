from Kiiras import Kiiras
from Osszehasonlitas import Osszehasonlitas
import random

veletlenSzam=random.randrange(1,17)
begepeltSzam=input("Adj meg egy számot! ")
Kiiras(Osszehasonlitas(veletlenSzam,begepeltSzam))