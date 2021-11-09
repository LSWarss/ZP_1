
class Magazyn:
    def __init__(self, nazwa: str, miejscowosc: str, ulica: str,
                 numer: int, powierzchnia: float):
        self._nazwa = nazwa
        self._miejscowosc = miejscowosc
        self._ulica = ulica
        self._numer = numer
        self._powierzchnia = powierzchnia

    def __str__(self) -> str:
        return f"""Magazyn o nazwe {self._nazwa},
w miejscowosci: {self._miejscowosc},
na ulicy: {self._ulica} {self._numer},
o powierzchni {self._powierzchnia} m^2.
        """

    @property
    def nazwa(self):
        return self._nazwa

    @nazwa.setter
    def nazwa(self, nazwa: str):
        self._nazwa = nazwa

    @property
    def miejscowosc(self):
        return self._miejscowosc

    @miejscowosc.setter
    def miejscowosc(self, miejscowosc: str):
        self._miejscowosc = miejscowosc

    @property
    def ulica(self):
        return self._ulica

    @ulica.setter
    def ulica(self, ulica: str):
        self._ulica = ulica

    @property
    def numer(self):
        return self._numer

    @numer.setter
    def numer(self, numer: int):
        self._numer = numer

    @property
    def powierzchnia(self):
        return self._powierzchnia

    @powierzchnia.setter
    def powierzchnia(self, powierzchnia: str):
        self._powierzchnia = powierzchnia
