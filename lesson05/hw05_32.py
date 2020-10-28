"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл. """

my_sequence = open("my_file32.txt", "r")
out_f = open("my_file321.txt", "w")
dict_val = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
for line in my_sequence:
    out_f.write(line.replace(line.split()[0], dict_val.get(line.split()[0])))
my_sequence.close()
