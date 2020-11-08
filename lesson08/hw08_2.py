class OwnError(Exception):
    def __init(self, txt):
        self.txt = txt


try:
    first = int(input("Введите делимое: "))
    second = int(input("Введите делитель: "))
    if second == 0:
        raise OwnError("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Ваш результат деления: {first / second}")
