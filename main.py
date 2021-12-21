from pacjent import Pacjent
from dieta import Dieta
from dietetyk import Dietetyk
from zamowienia import Zamowienie

dietetyk_Marek = Dietetyk("Marek", "Skarbonka", 32, 7, "Vege")
pacjent = Pacjent("Lukasz", "Jordan", 24, dietetyk_Marek, 78)
dieta_vege = Dieta("Vege+", 1200.69, dietetyk_Marek, "vege", 2300)
dieta_jarosz = Dieta("Jarosz", 1000.21, dietetyk_Marek, "jaro", 2000)
zamowienie = Zamowienie()

zamowienie.dietetyk = dietetyk_Marek
zamowienie.identyfikator = "420Diets"
zamowienie.pacjent = pacjent
zamowienie.diety = [dieta_vege, dieta_jarosz]
print(zamowienie)
print(zamowienie.dietsCost())
print(zamowienie.dietsCalories())