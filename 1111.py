import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import simpledialog, messagebox
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

class FilmArayuzu:
    def __init__(self, root):
        self.root = root
        self.root.title("Film Kütüphanesi")
        self.root.geometry("400x300")

        self.kutuphane = FilmKutuphanesi()

        self.create_widgets()

    def create_widgets(self):
        self.menu_frame = ttk.Frame(self.root)
        self.menu_frame.pack(pady=10)

        ttk.Button(self.menu_frame, text="Film Ekle", command=self.film_ekle).grid(row=0, column=0, padx=5)
        ttk.Button(self.menu_frame, text="Film İzlendi Olarak İşaretle", command=self.film_izlendi).grid(row=0, column=1, padx=5)
        ttk.Button(self.menu_frame, text="Film Listele", command=self.film_listele).grid(row=0, column=2, padx=5)
        ttk.Button(self.menu_frame, text="Çıkış", command=self.cikis).grid(row=0, column=3, padx=5)

        self.liste_frame = ttk.Frame(self.root)
        self.liste_frame.pack(pady=10)

        self.film_listesi = ttk.Treeview(self.liste_frame, columns=("Ad", "Yönetmen", "Yıl", "İzlendi"))
        self.film_listesi.heading("#0", text="Ad")
        self.film_listesi.heading("Ad", text="Ad")
        self.film_listesi.heading("Yönetmen", text="Yönetmen")
        self.film_listesi.heading("Yıl", text="Yıl")
        self.film_listesi.heading("İzlendi", text="İzlendi")
        self.film_listesi.column("#0", width=0, stretch=tk.NO)
        self.film_listesi.column("Ad", anchor=tk.W, width=100)
        self.film_listesi.column("Yönetmen", anchor=tk.W, width=100)
        self.film_listesi.column("Yıl", anchor=tk.W, width=50)
        self.film_listesi.column("İzlendi", anchor=tk.W, width=50)
        self.film_listesi.grid(row=0, column=0)

    def film_ekle(self):
        ad = simpledialog.askstring("Film Ekle", "Film Adı:")
        yonetmen = simpledialog.askstring("Film Ekle", "Yönetmen:")
        yil = simpledialog.askstring("Film Ekle", "Yıl:")
        film = Film(ad, yonetmen, yil)
        self.kutuphane.film_ekle(film)
        self.update_film_listesi()

    def film_izlendi(self):
        film_ad = simpledialog.askstring("İzlendi Olarak İşaretle", "İzlendi olarak işaretlenecek film adı:")
        self.kutuphane.film_izlendi_olarak_isaretle(film_ad)
        self.update_film_listesi()

    def film_listele(self):
        self.update_film_listesi()

    def cikis(self):
        self.kutuphane.save_to_file()
        self.root.destroy()

    def update_film_listesi(self):
        self.film_listesi.delete(*self.film_listesi.get_children())
        for film in self.kutuphane.filmler:
            izlendi_durumu = "Evet" if film.izlendi else "Hayır"
            self.film_listesi.insert("", "end", values=(film.ad, film.yonetmen, film.yil, izlendi_durumu))

if __name__ == "__main__":
    root = ThemedTk(theme="equilux")  # Tema adını değiştirebilirsiniz.
    app = FilmArayuzu(root)
    root.mainloop()
