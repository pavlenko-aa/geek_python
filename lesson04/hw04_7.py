from functools import reduce


def generator(n):
    for el in range(1, n+1):
        yield reduce(lambda x, y: x * y, [el1 for el1 in range(1, el + 1)])


i = 1
for numb in generator(int(input("Введите число, для которого надо вычислить факториал: "))):
    print(f"{i}! = {numb}")
    i += 1
