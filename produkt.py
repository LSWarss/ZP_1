from magazyn import Magazyn


class Produkt:
    def __init__(self, nazwa: str, ilosc: int, cena: float,
                 miejsce_skladowania: Magazyn, producent: str):
        self._nazwa = nazwa
        self._ilosc = ilosc
        self._cena = cena
        self._miejsce_skladowania = miejsce_skladowania
        self._producent = producent

    def __str__(self) -> str:
        return f"""Produkto o nazwe {self._nazwa},
wyprodukowany przez: {self._producent},
jest umieszony w {self._miejsce_skladowania},
w ilości {self._ilosc} oraz cenie {self._cena}.
        """

    @property
    def nazwa(self):
        return self._nazwa

    @nazwa.setter
    def nazwa(self, nazwa: str):
        self._nazwa = nazwa

    @property
    def ilosc(self):
        return self._ilosc

    @ilosc.setter
    def ilosc(self, ilosc: int):
        self._ilosc = ilosc

    @property
    def cena(self):
        return self._cena

    @cena.setter
    def cena(self, cena: float):
        self._cena = cena

    @property
    def miejsce_skladowania(self):
        return self._miejsce_skladowania

    @miejsce_skladowania.setter
    def miejsce_skladowania(self, miejsce_skladowania: Magazyn):
        self._miejsce_skladowania = miejsce_skladowania

    @property
    def producent(self):
        return self._producent

    @producent.setter
    def producent(self, producent: str):
        self._producent = producent
