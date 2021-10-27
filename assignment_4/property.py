class Property(): 

    def __init__(self, area : float, rooms: int, price: float, address: str):
        self._area = area
        self._rooms = rooms
        self._price = price
        self._address = address
    
    def __str__(self) -> str:
        return f"Property with area: {self._area}, with {self._rooms} rooms, on {self._address}, costs: {self._price}"