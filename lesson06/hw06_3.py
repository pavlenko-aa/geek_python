class Worker:
    name: str
    surname: str
    position: str
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income["wage"] = wage
        self._income["bonus"] = bonus


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, wage, bonus)
        self.position = position

    def get_full_name(self):
        return f"Полное имя: {self.name} {self.surname}"

    def get_total_income(self):
        b = self._income["wage"] + self._income["bonus"]
        return f"Доход с учётом премии: {b}"


john = Position("John", "Smith", "plumber", 10, 35)
print(john.get_full_name())
print(john.get_total_income())

jane = Position("Jane", "Eyre", "secretary", 35, 100)
print(jane.get_full_name())
print(jane.get_total_income())
