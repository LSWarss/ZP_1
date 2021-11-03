class Library:
    def __init__(self, city: str, street: str, open_hours: str, phone: str):
        self._city = city
        self._street = street
        self._open_hours = open_hours
        self._phone = phone

    def __str__(self) -> str:
        return f"""Library in {self._city}, on street: {self._street}, with
        open hours: {self._open_hours} and phone number: {self._phone}"""
