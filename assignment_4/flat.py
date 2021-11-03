from property import Property


class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str,
                 floor: int):
        super().__init__(area, rooms, price, address)
        self._floor = floor

    def __init__(self, property: Property, floor: int):
        super().__init__(property.area,property.rooms, property.price, property.address)
        self._floor = floor

    def __str__(self) -> str:
        return "Flat " + super().__str__() + f"on floor {self._floor}"
