from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)


list_repeat = ["cat", "dog"]
i = 1
for el in cycle(list_repeat):
    if i > 10:
        break
    print(el)
    i += 1