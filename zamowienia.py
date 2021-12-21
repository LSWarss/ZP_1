
from dieta import Dieta
from dietetyk import Dietetyk
from pacjent import Pacjent


class Zamowienie:

    def __str__(self) -> str:
        return f"""Zamowienie o id {self.identyfikator},
 dla pacjenta : {self.pacjent},
 stworzone przez dietetyka {self.dietetyk},
 w cenie {self.cena} z takimi dietami: {self.diety}
        """

    @property
    def identyfikator(self):
        return self._identifikator

    @identyfikator.setter
    def identyfikator(self, identifikator: str):
        self._identifikator = identifikator

    @property
    def diety(self):
        return self._diety

    @diety.setter
    def diety(self, diety: list):
        self._diety = diety

    @property
    def dietetyk(self):
        return self._dietetyk

    @dietetyk.setter
    def dietetyk(self, dietetyk: Dietetyk):
        self._dietetyk = dietetyk

    @property
    def pacjent(self):
        return self._pacjent

    @pacjent.setter
    def pacjent(self, pacjent: Pacjent):
        self._pacjent = pacjent

    @property
    def cena(self):
        return self.dietsCost() + 100

    def dietsCost(self) -> float:
        cost = 0
        for diet in self.diety:
            cost += diet.cena
        return cost
    
    def dietsCalories(self) -> float:
        cal = 0
        for diet in self.diety:
            cal += diet.kaloryczność
        return cal