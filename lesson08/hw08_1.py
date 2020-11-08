class Data:

    @staticmethod
    def make_int(param):
        date = []
        for el in param.split("-"):
            date.append(int(el))
        return date

    @classmethod
    def val_data(cls, param):
        date = cls.make_int(param)
        if int(date[0]) < 1 or int(date[0]) > 31:
            print("Дата введена неверно.")
            return
        if int(date[1]) < 1 or int(date[1]) > 12:
            print("Месяц введен неверно.")
            return
        if int(date[2]) < 1:
            print("Год введен неверно.")
            return
        print(f"Вы ввели все верно. Ваша дата: {param}")


user_data = input("Введите дату в формате ДД-ММ-ГГГГ: ")
Data.make_int(user_data)
Data.val_data(user_data)