from dietetyk import Dietetyk
from osoba import Osoba


from osoba import Osoba
from dieta import Dieta
from dietetyk import Dietetyk

class Pacjent(Osoba):

    def __init__(self, imie: str, nazwisko: str, wiek: int, dietetyk: Dietetyk, waga: float):
        super().__init__(imie, nazwisko, wiek)
        self._dietetyk = dietetyk
        self._waga = waga
    
    def __str__(self) -> str:
        return super().__str__() + f"""
 jest pacjentem, który wazy {self.waga}
 jego dietetykiem jest {self.dietetyk}.
        """

    @property
    def dietetyk(self):
        return self._dietetyk

    @property
    def waga(self):
        return self._waga