sequence = [2, 2, 2, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_sequence = [el for el in sequence if sequence.count(el) == 1]

print(new_sequence)