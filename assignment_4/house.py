from property import Property


class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str,
                 plot: int):
        super().__init__(area, rooms, price, address)
        self._plot = plot

    def __str__(self) -> str:
        return "House " + super().__str__() + f" with size: {self._plot}"
