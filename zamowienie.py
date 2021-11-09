from magazyn import Magazyn
from klient import Klient
from produkt import Produkt


class Zamowienie:
    def __init__(self):
        self._produkt = None
        self._adres_dostawy = None
        self._sposob_platnosci = None
        self._faktura = None
        self._wartosc = None
        self._klient = None
        self._do_klienta = None

    def __str__(self) -> str:
        return f"""
Zamowienie produktu: {self._produkt},
na adres: {self._adres_dostawy},
opłacone: {self._sposob_platnosci},
przez: {self._klient},
o wartości: {self.wartosc()},
na fakture: {self._faktura}
"""

    @ property
    def produkt(self):
        return self._produkt

    @ produkt.setter
    def produkt(self, produkt: Produkt):
        self._produkt = produkt

    @property
    def adres_dostawy(self):
        return self._adres_dostawy

    @adres_dostawy.setter
    def adres_dostawy(self, adres_dostawy: str):
        if self.do_klienta:
            self._adres_dostawy = self.zamownie_na_adres_klienta()
        else:
            self._adres_dostawy = adres_dostawy

    @property
    def klient(self):
        return self._klient

    @klient.setter
    def klient(self, klient: Klient):
        self._klient = klient

    @property
    def faktura(self):
        return self._faktura

    @faktura.setter
    def faktura(self, faktura: bool):
        self._faktura = faktura

    @property
    def do_klienta(self):
        return self._do_klienta

    @do_klienta.setter
    def do_klienta(self, do_klienta: bool):
        self._do_klienta = do_klienta

    def wartosc(self):
        return round(self.produkt.ilosc * self.produkt.cena, 2)

    def zamownie_na_adres_klienta(self):
        return self.klient.adres

    @property
    def sposob_platnosci(self):
        return self._sposob_platnosci

    @sposob_platnosci.setter
    def sposob_platnosci(self, sposob_platnosci: str):
        self._sposob_platnosci = sposob_platnosci
