import random

def main():             # Основная функция для игры
    field = ["-"] * 9
    symbols = ["X", "O"]
    player_idx = random.randint(0, 1)
    player_symbol = symbols[player_idx]
    computer_symbol = symbols[1 - player_idx]
    print('''Правила игры:
- Вам нужно выстроить свои символы в линию из 3 штук.
- Линии могут быть вертикальными, горизонтальными и диагональными.
- Также вам нужно не дать победить компьютеру.
    
Вы будете ходить ''' + player_symbol)
    if player_symbol == 'O':
        get_computer_move(computer_symbol, field)
    draw_board(field)

    while True:
        get_player_move(player_symbol, field)
        check_win_response = check_win(field)       # Получаем ответ о статусе партии
        if  check_win_response == player_symbol:    # Выводим ответ
            print("Вы победили!!!")
            break
        elif check_win_response == computer_symbol:
            print("Победил компьютер!!!")
            break
        elif check_win_response == '=':
            print("Ничья")
            break
        
        get_computer_move(computer_symbol, field) 
        draw_board(field)
        check_win_response = check_win(field)       # Получаем ответ о статусе партии
        if check_win_response == player_symbol:     # Выводим ответ
            print("Вы победили!!!")
            break
        elif check_win_response == computer_symbol:
            print("Победил компьютер!!!")
            break
        elif check_win_response == '=':
            print("Ничья")
            break

def draw_board(field):       # Функция для создания игрового поля
    print(f'''y
∧
|
3 | {field[0]} | {field[1]} | {field[2]} |
2 | {field[3]} | {field[4]} | {field[5]} |
1 | {field[6]} | {field[7]} | {field[8]} |
0   1   2   3 —> x''')

def get_player_move(player_symbol, field):         # Ход игрока
    x = int(input('Введите координату по оси x: '))
    y = int(input('Введите координату по оси y: '))
    while True:
        if (x not in [1, 2, 3]) or (y not in [1, 2, 3]):        # Повторный ввод координат, если есть числа, выходящие за пределы радиуса
            print('Некорректный ввод, попробуйте ещё раз')
            x = int(input('Введите координату по оси x: '))
            y = int(input('Введите координату по оси y: '))
        elif field[(3 - y) * 3 + x - 1] != '-':                 # Повторный ввод координат, если клетка занята
            print('Здесь уже занято, попробуйте ещё раз')
            x = int(input('Введите координату по оси x: '))
            y = int(input('Введите координату по оси y: '))
        else:
            break
    field[(3 - y) * 3 + x - 1] = player_symbol
    return field

def get_computer_move(computer_symbol, field):      # Ход компьютера. Рандомный выбор ячейки поля для осуществления компьютером хода
    x = random.randint(1, 3)
    y = random.randint(1, 3)
    while True:
        if field[(3 - y) * 3 + x - 1] != '-':      # Повторный рандомный выбор ячейки, если предыдущие значения были заняты
            x = random.randint(1, 3)
            y = random.randint(1, 3)
        else:
            break
    field[(3 - y) * 3 + x - 1] = computer_symbol
    return field

def check_win(field):      # Проверка победы одного из участников
    for i in range(3):     # Проверка по горизонтали
        if field[i*3] == field[i*3+1] == field[i*3+2] and field[i*3] != '-':
            return field[i*3]
    for i in range(3):      # Проверка по вертикали
        if field[i] == field[i+3] == field[i+6] and field[i] != '-':
            return field[i]

    if field[0] == field[4] == field[8] and field[0] != '-':
        return field[0]                                         # Проверка горизонталей
    if field[2] == field[4] == field[6] and field[2] != '-':
        return field[2]

    if '-' not in field:        # Проверка на ничью
        return '='
    else:
        return '-'

main()      # Запуск игры