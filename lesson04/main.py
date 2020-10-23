"""Ввод переменных черех параметры последовательно: Фамилия, часы, ставка, бонус"""

import sys

from lesson04 import hw04_1

try:
    file, name, hours, wage, bonus = sys.argv
except ValueError:
    print("Invalid args")
    exit()

hw04_1.worker(name)
print(hw04_1.calculate(int(hours), int(wage), int(bonus)))
