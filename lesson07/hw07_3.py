class Cell:
    part = int

    def __init__(self, part):
        self.part = part

    def __str__(self):
        return str(self.part)

    def __add__(self, other):
        return Cell(self.part + other.part)

    def __sub__(self, other):
        if self.part > other.part:
            return Cell(self.part - other.part)
        else:
            return f"Вычитание невозможно, получится отрицательное значение."

    def __mul__(self, other):
        return Cell(self.part * other.part)

    def __truediv__(self, other):
        if self.part > other.part:
            return Cell(self.part // other.part)
        else:
            return f"Целочисленное деление невозможно."

    def make_order(self):
        lines = self.part // numb
        left = "*" * (self.part % numb)
        res = ""
        j = 0
        while j < lines:
            b = ""
            i = 0
            while i < numb:
                i += 1
                b += "*"
            else:
                b += "\\n"
            res += b
            j += 1
        else:
            res += left
        return res


first = Cell(25)
second = Cell(30)
third = Cell(5)
forth = Cell(100)

print(first + second)
print(second - third)
print(second * third)
print(third / second)
numb = int(input("Введите число: "))
print(second.make_order())
