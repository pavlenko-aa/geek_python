class Car:
    speed: int
    colour: str
    name: str
    is_police: bool

    def __init__(self, name, colour, speed, is_police=False):
        self.name = name
        self.colour = colour
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.speed}")

    def __str__(self) -> str:
        return f"{self.name} {self.colour} {self.is_police}"


class TownCar(Car):
    def show_speed(self):
        if self.speed < 60:
            print(f"Текущая скорость автомобиля {self.speed}")
        else:
            print("Превышение скорости!")


class WorkCar(Car):
    def show_speed(self):
        if self.speed < 40:
            print(f"Текущая скорость автомобиля {self.speed}")
        else:
            print("Превышение скорости!")

class PoliceCar(Car):
    pass

class SportCar(Car):
    pass


a = WorkCar("Peugeot", "красный", 50)
a.show_speed()
a.stop()
a.turn("налево")
b = PoliceCar("Ford", "синий", 150, True)
print(b)
b.show_speed()
