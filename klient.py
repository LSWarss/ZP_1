class Klient:
    def __init__(self, imie: str, nazwisko: str, numer: int,
                 ilosc_zamowien: int, adres: str):
        self._imie = imie
        self._nazwisko = nazwisko
        self._numer = numer
        self._ilosc_zamowien = ilosc_zamowien
        self._adres = adres

    def __str__(self) -> str:
        return f"""Klient {self._imie} {self._nazwisko},
z: {self._adres},
o ilosci zamowien: {self._ilosc_zamowien},
oraz numerze: {self._numer}
"""

    @property
    def imie(self):
        return self._imie

    @imie.setter
    def nazwa(self, imie: str):
        self._imie = imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, nazwisko: str):
        self._nazwisko = nazwisko

    @property
    def adres(self):
        return self._ulica

    @adres.setter
    def adres(self, adres: str):
        self._adres = adres

    @property
    def numer(self):
        return self._numer

    @numer.setter
    def numer(self, numer: int):
        self._numer = numer

    @property
    def ilosc_zamowien(self):
        return self._ilosc_zamowien

    @ilosc_zamowien.setter
    def ilosc_zamowien(self, ilosc_zamowien: int):
        self._ilosc_zamowien = ilosc_zamowien


class KlientDetaliczny(Klient):

    def __init__(self, imie: str, nazwisko: str, numer: int,
                 ilosc_zamowien: int, adres: str, wiek: int):
        super().__init__(imie, nazwisko, numer, ilosc_zamowien, adres)
        self._wiek = wiek

    @property
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self, wiek: int):
        self._wiek = wiek

    def __str__(self) -> str:
        prefix = super().__str__()
        return '{}oraz wieku: {}'.format(prefix, self._wiek)


class KlientBiznesowy(Klient):

    def __init__(self, imie: str, nazwisko: str, numer: int,
                 ilosc_zamowien: int, adres: str, nip: int):
        super().__init__(imie, nazwisko, numer, ilosc_zamowien, adres)
        self._nip = nip

    @property
    def nip(self):
        return self._nip

    @nip.setter
    def nip(self, nip: int):
        self._nip = nip

    def __str__(self) -> str:
        prefix = super().__str__()
        return '{}oraz nipie: {}'.format(prefix, self._nip)
