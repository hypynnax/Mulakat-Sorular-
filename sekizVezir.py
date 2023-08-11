import random


uygunYer = True
vezirSayisi = 0

def sagCaprazKontrol(tahta, x, y):
    global uygunYer
    minNumber = min(7 - x, y)
    x += minNumber
    y -= minNumber
    while x >= 0 and y <= 7:
        if tahta[y][x] == 1:
            uygunYer = False
            return False
        x -= 1
        y += 1

def solCaprazKontrol(tahta, x, y):
    global uygunYer
    minNumber = min(x, y)
    x -= minNumber
    y -= minNumber
    while x <= 7 and y <= 7:
        if tahta[y][x] == 1:
            uygunYer = False
            return False
        x += 1
        y += 1

def ustAltKontrol(tahta, x):
    global uygunYer
    for i in range(8):
        if tahta[i][x] == 1:
            uygunYer = False
            return False

def sagSolKontrol(tahta, y):
    global uygunYer
    for i in range(8):
        if tahta[y][i] == 1:
            uygunYer = False
            return False

def sagCaprazDoldur(tahta, x, y, a, b):
    minNumber = min(7 - x, y)
    x += minNumber
    y -= minNumber
    while x >= 0 and y <= 7:
        if tahta[y][x] == 2:
            if x != a and y != b:
                koordinatlar.remove(str(y)+str(x))
            tahta[y][x] = 0
        x -= 1
        y += 1

def solCaprazDoldur(tahta, x, y, a, b):
    minNumber = min(x, y)
    x -= minNumber
    y -= minNumber
    while x <= 7 and y <= 7:
        if tahta[y][x] == 2:
            if x != a and y != b:
                koordinatlar.remove(str(y)+str(x))
            tahta[y][x] = 0
        x += 1
        y += 1

def ustAltDoldur(tahta, x, y):
    for i in range(8):
        if tahta[i][x] == 2:
            if i != y:
                koordinatlar.remove(str(i)+str(x))
            tahta[i][x] = 0

def sagSolDoldur(tahta, x, y):
    for i in range(8):
        if tahta[y][i] == 2:
            if i != x:
                koordinatlar.remove(str(y)+str(i))
            tahta[y][i] = 0

while True:

    if vezirSayisi >= 8:
        break
    else:
        vezirSayisi = 0
        santrancTahtasi = [[2 for x in range(8)]for y in range(8)]
        koordinatlar = ["00" for x in range(64)]
        sira = 0
        for i in range(8):
            for j in range(8):
                koordinatlar[sira] = str(i) + str(j)
                sira += 1

    for i in range(8):
        if len(koordinatlar) != 0:
            koordinatNoktalari = random.choice(koordinatlar)
            y = int(koordinatNoktalari[0])
            x = int(koordinatNoktalari[1])
            sagCaprazKontrol(santrancTahtasi, x, y)
            solCaprazKontrol(santrancTahtasi, x, y)
            ustAltKontrol(santrancTahtasi, x)
            sagSolKontrol(santrancTahtasi, y)
            if uygunYer == True:
                santrancTahtasi[y][x] = 1
                vezirSayisi += 1
                sagCaprazDoldur(santrancTahtasi, x, y, x, y)
                solCaprazDoldur(santrancTahtasi, x, y, x, y)
                ustAltDoldur(santrancTahtasi, x, y)
                sagSolDoldur(santrancTahtasi, x, y)
            else:
                uygunYer = True
            koordinatlar.remove(str(y)+str(x))

print("sonuç")

for i in range(8):
    for j in range(8):
        print("♛" if santrancTahtasi[i][j] == 1 else "♙", end=" ")
    print()
