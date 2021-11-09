from klient import KlientBiznesowy, KlientDetaliczny
from magazyn import Magazyn
from produkt import Produkt
from zamowienie import Zamowienie


magazyn = Magazyn("Okap", "Kozy", "Lomby", 2, 512.23)

produkt = Produkt("Lampa", 1, 21.37, magazyn, "AlamaMater")

klient1 = KlientDetaliczny(
    "Marek", "Karek", 777777777, 12, "Karkołomna 12", 18)
klient2 = KlientBiznesowy(
    "Marek", "Karek", 777777777, 12, "Karkołomna 12", 9996663333212)

zamowienie = Zamowienie()
zamowienie.produkt = produkt
zamowienie.adres_dostawy = "UE Katowice"
zamowienie.klient = klient1
zamowienie.faktura = False
zamowienie.sposob_platnosci = "Przelew BLIK"

print(zamowienie)
