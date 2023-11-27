def fio():
    fio = input('Введите имя, фамилию, отчество и возраст: ')
    Fio = fio.split()
    name = Fio[0]
    surname = Fio[1]
    patronymic = Fio[2]
    age = Fio[3]
    YearOfBirth = int(age)
    print(f"{surname} {name} {patronymic} {2023 - YearOfBirth} г.р. зарегистрирован(-а)")

fio()