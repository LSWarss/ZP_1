from property import Property


class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str,
                 plot: int):
        super().__init__(area, rooms, price, address)
        self._plot = plot

    def __init__(self, property: Property, plot: int):
        super().__init__(property.area, property.rooms, property.price,
                         property.address)
        self._plot = plot

    def __str__(self) -> str:
        return "House " + super().__str__() + f" with size: {self._plot}"
