number = int(input("Введите целое положительное число:"))
max_numeral = number % 10
number = number // 10
while number > 0:
    if number % 10 > max_numeral:
        max_numeral = number % 10
    number = number // 10
print(max_numeral)

