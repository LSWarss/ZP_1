class Property(): 

    def __init__(self, area : float, rooms: int, price: float, address: str):
        self._area = area
        self._rooms = rooms
        self._price = price
        self._address = address
    
    @property
    def area(self):
        return self._area

    @property
    def rooms(self):
        return self._rooms

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value: float):
        self._price = value

    @property
    def address(self):
        return self._price

    @address.setter
    def address(self, value: str): 
        self._address = value


    def __str__(self) -> str:
        return f"Property with area: {self._area}, with {self._rooms} rooms, on {self._address}, costs: {self._price}"