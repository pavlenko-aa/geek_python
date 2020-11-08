class Complex:

    def __init__(self, real: float, img: float):
        self.real = real
        self.img = img

    def __str__(self):
        return str(f"{self.real} + {self.img}i")

    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img)

    def __mul__(self, other):
        new_real = self.real * other.real - self.img * other.img
        new_img = self.real * other.img + self.img * other.real
        return Complex(new_real, new_img)


a = Complex(2, 5)
b = Complex(6, 11)
print(a + b)
print(a * b)
