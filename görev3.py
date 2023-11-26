import json

class Ogrenci:
    def __init__(self, ad, soyad, numara):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.notlar = {}

class OgrenciYonetimSistemi:
    def __init__(self):
        self.ogrenciler = []
        self.dosya_ad = "ogrenci_bilgileri.json"
        self.load_from_file()

    def ogrenci_ekle(self, ogrenci):
        self.ogrenciler.append(ogrenci)
        print(f"{ogrenci.ad} {ogrenci.soyad} kütüphaneye eklendi.")

    def not_gir(self, ogrenci_numara, ders, notlar):
        for ogrenci in self.ogrenciler:
            if ogrenci.numara == ogrenci_numara:
                ogrenci.notlar[ders] = notlar
                print(f"{ogrenci.ad} {ogrenci.soyad}'ın {ders} notları eklendi.")
                break
        else:
            print("Öğrenci bulunamadı.")

    def ogrenci_listele(self):
        for ogrenci in self.ogrenciler:
            print(f"{ogrenci.ad} {ogrenci.soyad} ({ogrenci.numara})")

    def not_listele(self, ogrenci_numara):
        for ogrenci in self.ogrenciler:
            if ogrenci.numara == ogrenci_numara:
                for ders, notlar in ogrenci.notlar.items():
                    print(f"{ogrenci.ad} {ogrenci.soyad} - {ders}: {notlar}")
                break
        else:
            print("Öğrenci bulunamadı.")

    def save_to_file(self):
        with open(self.dosya_ad, 'w') as dosya:
            json.dump([vars(ogrenci) for ogrenci in self.ogrenciler], dosya)

    def load_from_file(self):
        try:
            with open(self.dosya_ad, 'r') as dosya:
                ogrenci_bilgileri = json.load(dosya)
                self.ogrenciler = [Ogrenci(**ogrenci) for ogrenci in ogrenci_bilgileri]
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    yonetim_sistemi = OgrenciYonetimSistemi()

    while True:
        print("\nÖğrenci Yönetim Sistemi")
        print("1. Öğrenci Ekle")
        print("2. Not Girişi Yap")
        print("3. Öğrenci Listele")
        print("4. Notları Listele")
        print("5. Çıkış")

        secim = input("Seçiminizi yapın: ")

        if secim == '1':
            ad = input("Öğrenci Adı: ")
            soyad = input("Öğrenci Soyadı: ")
            numara = input("Öğrenci Numarası: ")
            ogrenci = Ogrenci(ad, soyad, numara)
            yonetim_sistemi.ogrenci_ekle(ogrenci)
        elif secim == '2':
            numara = input("Öğrenci Numarası: ")
            ders = input("Ders Adı: ")
            notlar = input("Notları (virgülle ayırın): ").split(',')
            yonetim_sistemi.not_gir(numara, ders, notlar)
        elif secim == '3':
            yonetim_sistemi.ogrenci_listele()
        elif secim == '4':
            numara = input("Öğrenci Numarası: ")
            yonetim_sistemi.not_listele(numara)
        elif secim == '5':
            yonetim_sistemi.save_to_file()
            print("Programdan çıkılıyor. Güle güle!")
            break
        else:
            print("Geçersiz seçim. Tekrar deneyin.")
