from datetime import date

class Employee(): 

    def __init__(self, first_name : str, last_name : str, hire_date : date, birth_date : date, city : str, street: str, zip_code: str, phone: str):
        self._first_name = first_name
        self._last_name = last_name
        self._hire_date = hire_date
        self._birth_date = birth_date
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._phone = phone
    
    def __str__(self) -> str:
        hire_str = self._hire_date.strftime("%x")
        birth_str = self._birth_date.strftime("%x")
        return f"Employee: {self._first_name} {self._last_name} hired on: {hire_str}, born on: {birth_str} living in city: {self._city}, on street {self._street}, {self._zip_code}, phone: {self._phone}"