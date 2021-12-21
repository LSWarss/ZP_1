from dietetyk import Dietetyk

class Dieta:
    def __init__(self, nazwa: str, cena: float,
                 dietetyk: Dietetyk, wariant: str, kaloryczność: float):
        self._nazwa = nazwa
        self._kaloryczność = kaloryczność
        self._cena = cena
        self._dietetyk = dietetyk
        self._wariant = wariant

    def __str__(self) -> str:
        return f"""Dieta o nazwe {self.nazwa},
 stworzona przez: {self.dietetyk},
 w wariancie {self.wariant}, 
 kaloryczności {self.kaloryczność}
 oraz cenie {self.cena}.
        """

    @property
    def nazwa(self):
        return self._nazwa

    @property
    def dietetyk(self):
        return self._dietetyk

    @property
    def cena(self):
        return self._cena

    @property
    def kaloryczność(self):
        return self._kaloryczność

    @property
    def wariant(self):
        return self._wariant
