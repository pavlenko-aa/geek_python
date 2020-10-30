class Road:
    _length: int
    _width: int
    mass: int
    height: int

    def __init__(self, width, length, mass=25, height=5):
        self._width = width
        self._length = length
        self.height = height
        self.mass = mass
        res = int((self._width * self._length * self.height * self.mass) / 1000)
        print(f"Масса асфальта для покрытия дорожного полотна длиной {self._length}м и шириной {self._width}м составляет {res}т")


user_width = int(input("Введите ширину дорожного полотна: "))
user_length = int(input("Введите длину дорожного полотна: "))
a = Road(user_width, user_length)
