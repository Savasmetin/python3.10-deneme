sorular = ["Türkiye'nin ilk Cumhurbaşkanı kimdir ?"
    , "2014 Dünya Kupası şampiyonu hangi takımdır?"
    , "Mustafa Kemal Atatürk hangi yıl vefat etmiştir ?"]

soru_1_cevaplar = ["A) Mustafa Kemal Atatürk", "B) İsmet İnönü", "C) Recep Tayyip Erdoğan", "D) Cemal Gürsel"]
soru_2_cevaplar = ["A) Hollanda", "B) Almanya", "C) Arjantin", "D) Türkiye"]
soru_3_cevaplar = ["A) 1928", "B) 2022", "C) 1920", "D) 1938"]

dogru_cevaplar = ["a", "b", "d"]

def sor():
    puan = 0

    print("Soru 1:", sorular[0])

    for x in soru_1_cevaplar:
        print(x)

    cevap_1 = input("Cevabınız Nedir: ")

    if (cevap_1.lower() == dogru_cevaplar[0]):

        print("Tebrikler soruyu doğru bildiniz. Bir sonraki soru için hazırsınız :)")

        puan += 1

    else:

        print("Cevabınız yanlış. Doğru Cevap Mustafa Kemal Atatürk'tür.")

    print("-" * 50)

    print("Soru 2:", sorular[1])

    for x in soru_2_cevaplar:
        print(x)

    cevap_2 = input("Cevabınız Nedir: ")

    if (cevap_2.lower() ==  dogru_cevaplar[1]):

        print("Tebrikler soruyu doğru bildiniz. Bir sonraki soru için hazırsınız :)")

        puan += 1

    else:

        print("Cevabınız yanlış. Doğru cevap Almanya Milli Takımıdır.")

    print("-" * 50)

    print("Soru 3:", sorular[2])

    for x in soru_3_cevaplar:
        print(x)

    cevap_3 = input("Cevabınız Nedir: ")

    if (cevap_3.lower() == dogru_cevaplar[2]):

        print("Tebrikler son soruyu doğru bildiniz.")

        puan += 1

    else:

        print("Cevabınız yanlış doğru cevap 1938 yılıdır.")

    print("-" * 50)

    print("Bilgi yarışmamız bitmiştir. Katılımınız için minnettarız. Toplamda {} soruya doğru cevap verdiniz.".format(puan))




sor()
