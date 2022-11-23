print=(" Add meg 5 kutya nevét!")
kutyak=[]
for i in range (1,6):
    kutyaNev=input(f"{i}. kutya neve: ")
    kutyak.append(kutyaNev)
    
for egyKutya in kutyak:
    print(egyKutya)

for i in range (len(kutyak)):
    print(kutyak[i])

i=0
while (i<len(kutyak)):
    print(kutyak(i))
    i+=1

print("2 betűs kutyák")
for egyKutya in kutyak:
    if (len(egyKutya)==2):
        print(egyKutya)
