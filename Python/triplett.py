import random
gencode = ""

laenge = 60

for i in range(laenge): #schaft einen Gencode (zufällig) (laenge Zeichen lang)
    x = random.randint(0,4)
    if x == 0:
        x = "A"
    elif x == 1:
        x = "C"
    elif x == 2:
        x = "G"
    else:
        x = "T"
    gencode = gencode + x
    if i%3 == 2:
        gencode = gencode + " " #unterteilt den Gencode in einzelne Dreierfolgen
print (gencode)

def tripel_suchen(a): #zählt wie oft der Tripel (das Argument) im Gencode vorkommt
    b = 0
    for i in range(0,len(gencode),4):
        if a == gencode[i:i+3]:
            b = b + 1
    return b

d = {}
tripel = ""

for i in range(4):  #geht alle möglichen Tripel einmal durch u. fügt sie zum Dictionary hinzu (als Schlüssel, kombiniert mit der Häufigkeit dieses Tripels)
    if i == 0:
        tripel = tripel + "A"
    elif i == 1:
        tripel = tripel + "C"
    elif i == 2:
        tripel = tripel + "G"
    else:
        tripel = tripel + "T"
    for j in range(4):
        if j == 0:
            tripel = tripel + "A"
        elif j == 1:
            tripel = tripel + "C"
        elif j == 2:
            tripel = tripel + "G"
        else:
            tripel = tripel + "T"
        for k in range(4):
            if k == 0:
                tripel = tripel + "A"
            elif k == 1:
                tripel = tripel + "C"
            elif k == 2:
                tripel = tripel + "G"
            else:
                tripel = tripel + "T"
            d[tripel] = tripel_suchen(tripel)
            tripel = tripel[:2]
        tripel = tripel[0]
    tripel = ""

x = "Ja"
while x in ["ja","Ja","ok","Ok","OK"]:
    n = input("Nach welchem Tripel aus A, C, G und T soll gesucht werden? ")
    print(d[n])
    x = input("Möchtest Sie noch etwas suchen? ")
"""
Ich nehme hier als Tripel nur immer den ersten bis dritten, den vierten bis sechsten, den siebten bis neunten Buchstaben usw., da ein solches Tripel eine eigene kleine Sinneinheit ist, vergleichbar mit einem Byte. Wenn man 16 Bits häte, würde man ja auch nicht den 1. bis 8., den 2. bis 9., den 3. bis 10. Bit usw. als ein Byte betrachten, sondern lediglich den 1. bis 8. und den 9. bis 16. Bit. (Hier gehe ich von einem Zeichensystem mit 8 Bit für ein Zeichen aus.)
"""