class OwnError(Exception):
    def __init(self, txt):
        self.txt = txt


print(
    "Вводите элементы списка по одному, нажимая Enter после каждого добавленного числа.\n"
    "Когда введете все необходимые элементы, введите слово stop.\n")
res = []
while True:
    ask = input("Введите число: ")
    if ask == "stop":
        break
    try:
        if ask.isdigit():
            res.append(int(ask))
        else:
            raise OwnError("Вы ввели не число! Попробуйте ещё раз")
    except OwnError as err:
        print(err)

print(res)
