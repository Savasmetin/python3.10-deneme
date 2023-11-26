class Hayvan:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def bilgileri_goster(self):
       print(" hayvan bigileri ektedir: ".format(self.isim,self.yas))

class Kopek(Hayvan):
    def __init__(self, isim, yas, tur):
        super().__init__(isim, yas)
        self.tur = tur

    def havla(self):
        return f"{self.isim} havlıyor."
        print("{} havlıyor".format(self.isim))

    def oyun_oyna(self):
        return f"{self.isim} oyun oynuyor."

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f"Tür: {self.tur}")

        print(self.havla())

class Kus(Hayvan):
    def __init__(self, isim, yas, tur):
        super().__init__(isim, yas)
        self.tur = tur

    def uc(self):
        return print("isim: ".format(self.isim))

    def ot(self):
        return f"{self.isim} ötüyor."

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f"Tür: {self.tur}")

        print(self.uc())
        print(self.ot())

class At(Hayvan):
    def __init__(self, isim, yas, cins):
        super().__init__(isim, yas)
        self.cins = cins

    def kos(self):
        return print("koşuyor")

    def zipla(self):
        return f"{self.isim} zıplıyor."

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print("hayvanın cinsi: ".format(self.cins))




kopek = Kopek("Fido", 3, "Golden Retriever")
kus = Kus("Polly", 2, "Muhabbet Kuşu")
at = At("Şahbatur", 5, "Araber")


kopek.bilgiSleri_goster()
kus.bilgileri_goster()
at.bilgileri_goster()
