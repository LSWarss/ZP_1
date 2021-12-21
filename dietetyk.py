from osoba import Osoba

class Dietetyk(Osoba):

    def __init__(self, imie: str, nazwisko: str, wiek: int, staz: int, specjalizacja: str):
        super().__init__(imie, nazwisko, wiek)
        self._staz = staz
        self._specjalizacja = specjalizacja
    
    def __str__(self) -> str:
        return super().__str__() + f"""
 jest dietetykiem, który posiada specjalizacje
 w {self.specjalizacja} oraz {self.staz} lat stazu
 w zawodzie.
        """

    @property
    def staz(self):
        return self._staz

    @property
    def specjalizacja(self):
        return self._specjalizacja

