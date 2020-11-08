class Store:
    pass


class Technics:
    title: str
    colour: str
    price: float

    def __init__(self, title, colour, price):
        self.title = title
        self.colour = colour
        self.price = price

    def __str__(self) -> str:
        return str(f"Фирма: {self.title}. Цвет: {self.colour}. Цена: {self.price}.")


class Printer(Technics):
    kind: str

    def __init__(self, title, colour, price, kind):
        super().__init__(title, colour, price)
        self.kind = kind

    def __str__(self) -> str:
        return str(f"Принтер. {super().__str__()} Тип: {self.kind}.")


class Fax(Technics):
    speed: int

    def __init__(self, title, colour, price, speed):
        super().__init__(title, colour, price)
        self.speed = speed

    def __str__(self) -> str:
        return str(f"Факс. {super().__str__()} Скорость: {self.speed} стр/мин.")


class Copier(Technics):
    resolution: int

    def __init__(self, title, colour, price, resolution):
        super().__init__(title, colour, price)
        self.resolution = resolution

    def __str__(self) -> str:
        return str(f"Копир. {super().__str__()} Разрешение: {self.resolution} dpi.")


print(Printer("Canon", "Grey", 1000, "laser"))
print(Fax("Samsung", "White", 500, 50))
print(Copier("Xerox", "Black", 5000, 800))
