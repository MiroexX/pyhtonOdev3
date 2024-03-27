class Personel:
    def __init__(self, adi, departman, calisma_yili, maas):
        self.adi = adi
        self.departman = departman
        self.calisma_yili = calisma_yili
        self.maas = maas

class Firma:
    def __init__(self, isim):
        self.isim = isim
        self.personel_listesi = []

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)

    def personel_listele(self):
        for personel in self.personel_listesi:
            print(
                f"Adı: {personel.adi}, Departmanı: {personel.departman}, Çalışma Yılı: {personel.calisma_yili}, Maaşı: {personel.maas}")

    def maas_zammi(self, personel, zam_orani):
        for p in self.personel_listesi:
            if p == personel:
                p.maas += p.maas * (zam_orani / 100)

    def personel_cikart(self, personel):
        self.personel_listesi.remove(personel)
