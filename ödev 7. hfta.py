kelime = input("Bir kelime girin: ")
tersten = kelime[::-1]
if kelime == tersten:
    print("Palindrom!")
else:
    print("Palindrom değil!")
#----------------------------------------------------
liste = [1, 4, 7, 10, 15, 20, 23, 28, 31]
tek_sayilar = [sayi for sayi in liste if sayi % 2 != 0]
print("Tek sayılar:", tek_sayilar)
#---------------------------------------------------
for sayi in range(2, 101):
    asal = True
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            asal = False
            break
    if asal:
        print(sayi, end=" ")
#---------------------------------------------------
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print('W', end=' ')
        else:
            print('B', end=' ')
    print()
