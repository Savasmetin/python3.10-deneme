mesajlar = ["mesajlar.txt","mesajlar2.txt","mesajlar3.txt"]
cevaplar = ["B","B","C"]
index = 0
cevaplar_index = 0
puan = 0
for i in mesajlar:

    f = open(mesajlar[index],"r")
    print(f.read())
    cevap = str(input("cevabnız nedir"))
    if cevaplar[cevaplar_index] == cevap:
        print("soruya doğru bir şekilde cevap verdiniz")
        print("---------------------------------------")
        puan += 10
    else:
        print("cevabınız yanlıştır doğru cevap şu şekildedir: ",cevaplar[cevaplar_index])
        print("---------------------------------------")
    index = index + 1
    cevaplar_index = cevaplar_index + 1
print("puanınız şu şekildedir",puan)

