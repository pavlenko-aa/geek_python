class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"У вас в руках {self.title}. Запуск отрисовки ручкой.")

class Pencil(Stationery):
    def draw(self):
        print(f"У вас в руках {self.title}. Запуск отрисовки карандашом.")

class Handle(Stationery):
    def draw(self):
        print(f"У вас в руках {self.title}. Запуск отрисовки маркером.")


pensil = Pencil("карандаш")
pen = Pen("ручка")
handle = Handle("маркер")
pensil.draw()
pen.draw()
handle.draw()
