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


class Warehouse:
    presence: dict
    outcoming: dict

    def __init__(self) -> None:
        self.presence = {}
        self.outcoming = {}

    def tech_incoming(self, tech: Technics, count: int):
        if tech in self.presence:
            self.presence.update({tech: self.presence.get(tech) + count})
        else:
            self.presence.update({tech: count})

    def to_division(self, div: str, tech: Technics):
        if div in self.outcoming:
            list_of_tech = self.outcoming.get(div)
            list_of_tech.append(tech)
            self.outcoming.update({div: list_of_tech})
        else:
            self.outcoming.update({div: tech})

    def __str__(self) -> str:
        result = "Поступили на склад:\n"
        for key in self.presence:
            result += f"{key}: {self.presence.get(key)} \n"

        result += f"\n"

        for key in self.outcoming:
            result += f"В подразделение {key} отправлено: {str(self.outcoming.get(key))}  \n"
        return result


printer1 = Printer("Canon", "Grey", 1000, "laser")
printer2 = Printer("Canon", "Grey", 5000, "laser")
fax1 = Fax("Samsung", "White", 500, 50)

store = Warehouse()
store.tech_incoming(printer1, 2)
store.tech_incoming(printer1, 3)
store.tech_incoming(printer2, 10)
store.tech_incoming(fax1, 25)
store.to_division("Бухгалтерия", printer1)
store.to_division("Серетариат", fax1)
print(store)
