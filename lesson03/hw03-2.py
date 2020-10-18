i = 1
while True:
    print("Введите данные сотрудника. Если вы хотите прекратить ввод данных, введите вместо имени символ #.")
    name_inp = input(f"Введите имя номер {i}: ")
    if name_inp != "#":
        surname_inp = input(f"Введите фамилию номер {i}: ")
        year_inp = input(f"Введите год рождения номер {i}: ")
        city_inp = input(f"Введите город номер {i}: ")
        mail_inp = input(f"Введите email номер {i}: ")
        phone_inp = input(f"Введите телефон номер {i}: ")
        i +=1
    else:
        break

    def resume(name, surname, year, city, mail, phone):
        print(f"Данные сотрудника номер {i-1} : \n"
              f" Имя - {name}, Фамилия - {surname}, Год рождения - {year}, Город - {city}, email - {mail}, телефон - {phone}")


    resume(name=name_inp, surname=surname_inp, year=year_inp, city=city_inp, mail=mail_inp, phone=phone_inp)