mot=input("Saisir un mot : ")
d=int(input("Saisir le nombre de lettres à décaler : "))
decal=""
for l in mot:
  if (ord(l)<=ord("Z")):
    decal+=chr((ord(l)+d-ord('A'))%26+ord('A'))
  else:
    decal+=chr((ord(l)+d-ord('a'))%26+ord('a'))
print(decal)
