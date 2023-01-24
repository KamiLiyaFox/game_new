def greet():
    print("___________________")
    print("  ~Добро пожаловать  ")
    print("      в игру       ")
    print("  крестики-нолики~  ")
    print("___________________")
    print(" Обозначения: a b ")
    print(" a - номер строки  ")
    print(" b - номер столбца ")


def show():
    print()
    print("      0   1   2   ")
    print("     ___________ ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("    |___|___|___| ")
    print()


def ask():
    while True:
        cords = input("  Введите через пробел координаты клетки: ").split()

        if len(cords) != 2:
            print(" Ты до двух считать умеешь? Координаты должно быть 2! ")
            continue

        a, b = cords

        if not (a.isdigit()) or not (b.isdigit()):
            print(" Нужно вводить цифры, а не что попало! ")
            continue

        a, b = int(a), int(b)

        if 0 > a or a > 2 or 0 > b or b > 2:
            print(" Мимо! Вводите внимательнее, диапазон где-то рядом:)! ")
            continue

        if field[a][b] != " ":
            print(" Занято! Присмотри себе доугое местечко! :) ")
            continue

        return a, b


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print(" Победа присуждается хитрюге - X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Победааааа,  первый приз за - 0!!!")
            return True
    return False


greet()
field = [[" "] * 3 for i in range(3)]
num = 0
while True:
    num += 1
    show()
    if num % 2 == 1:
        print(" Смелее Крестик - твой ход!")
    else:
        print(" Нолик, твоя очередь!")

    a, b = ask()

    if num % 2 == 1:
        field[a][b] = "X"
    else:
        field[a][b] = "0"

    if check_win():
        break

    if num == 9:
        print(" Победила Дружба!")
        break