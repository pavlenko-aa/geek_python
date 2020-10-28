"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
окончании ввода данных свидетельствует пустая строка. """

user_data = open("my_file1.txt", 'w')
while True:
    user_answer = input("Введите данные. Если вы хотите прекратить ввод, просто нажмите Enter. ")
    if user_answer != "":
        user_data.write(user_answer + "\n")
    else:
        break

user_data.close()