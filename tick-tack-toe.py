def intro():
    print('  Игра крестики-нолики')
    print('')
    print('Введите две координаты X и Y')
    print(' X - это номер строки')
    print(' Y - это номер столбца')


def playing_space():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  ——————————————— ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  ——————————————— ")
    print()


def ask():
    while True:
        coords = input(' Введите координаты через пробел  ').split()

        if len(coords) != 2:
            print(' Введитие ДВЕ координаты ')
            continue

        x, y = coords

        if not (x.isdigit() or y.isdigit()):
            print(' Введите цифры ')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def check_win():
    win_coord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for coord in win_coord:
        symbols = []
        for c in coord:
            symbols.append(field[c[0]][c[1]])

        if symbols == ["X", "X", "X"]:
            print("Победил крестик!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Победил нолик!")
            return True
    return False


intro()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    playing_space()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break
