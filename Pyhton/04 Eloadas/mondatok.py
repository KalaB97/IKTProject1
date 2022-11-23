import random
def nevelo(szavak):
    maganhangzok="aáeéiíoóöőuúüű"
    if szavak[0].lower()in maganhangzok:
        return "Az"
    else:
         return "A"
       
def jelzo():
    return random.choice(["piros","nagy","könnyed"])

print("Adj meg három főnevet")
for i in range(1,4,1):
    szavak=input(f"{i}. főnév: ")
    print(f"{nevelo(szavak)} {nevelo (szavak)} {jelzo()}")
