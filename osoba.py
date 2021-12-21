class Osoba: 
    
    def __init__(self, imie, nazwisko, wiek): 
        self._imie = imie
        self._nazwisko = nazwisko
        self._wiek = wiek
    
    def __str__(self) -> str:
        return f"""Osoba o imieniu {self.imie},
i nazwisku {self.nazwisko}, ma {self.wiek} lat"""

    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def wiek(self):
        return self._wiek