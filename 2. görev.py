import json

class Film:
    def __init__(self, ad, yonetmen, yil, izlendi=False):
        self.ad = ad
        self.yonetmen = yonetmen
        self.yil = yil
        self.izlendi = izlendi

class FilmKutuphanesi:
    def __init__(self):
        self.filmler = []
        self.dosya_ad = "film_kutuphanesi.json"
        self.load_from_file()

    def film_ekle(self, film):
        self.filmler.append(film)
        print(f"{film.ad} kütüphaneye eklendi.")

    def film_izlendi_olarak_isaretle(self, film_ad):
        for film in self.filmler:
            if film.ad == film_ad:
                film.izlendi = True
                print(f"{film.ad} izlendi olarak işaretlendi.")
                break
        else:
            print("Film bulunamadı.")

    def film_listele(self):
        for film in self.filmler:
            izlendi_durumu = "İzlendi" if film.izlendi else "İzlenmedi"
            print(f"{film.ad} - {film.yonetmen} ({film.yil}) - {izlendi_durumu}")

    def save_to_file(self):
        with open(self.dosya_ad, 'w') as dosya:
            json.dump([vars(film) for film in self.filmler], dosya)

    def load_from_file(self):
        try:
            with open(self.dosya_ad, 'r') as dosya:
                film_bilgileri = json.load(dosya)
                self.filmler = [Film(**film) for film in film_bilgileri]
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    kutuphane = FilmKutuphanesi()

    while True:
        print("\nFilm Kütüphanesi Yönetim Sistemi")
        print("1. Film Ekle")
        print("2. Film İzlendi Olarak İşaretle")
        print("3. Film Listele")
        print("4. Çıkış")

        secim = input("Seçiminizi yapın: ")

        if secim == '1':
            ad = input("Film Adı: ")
            yonetmen = input("Yönetmen: ")
            yil = input("Yıl: ")
            film = Film(ad, yonetmen, yil)
            kutuphane.film_ekle(film)
        elif secim == '2':
            film_ad = input("İzlendi olarak işaretlenecek film adı: ")
            kutuphane.film_izlendi_olarak_isaretle(film_ad)
        elif secim == '3':
            kutuphane.film_listele()
        elif secim == '4':
            kutuphane.save_to_file()
            print("Programdan çıkılıyor. Güle güle!")
            break
        else:
            print("Geçersiz seçim. Tekrar deneyin.")
