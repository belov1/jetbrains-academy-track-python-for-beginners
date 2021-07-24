
grid = [[' ' for _ in range(0, 3)] for _ in range(0,3)]
player = ''


def output():
    print('---------')
    for row in range(3):
        print('|', ' '.join(grid[row]), '|')
    print('---------')


def is_winner(symbol):
    if any(row.count(symbol) == 3 for row in grid):
        return True
    for col in range(3):
        if [grid[row][col] for row in range(0, 3)].count(symbol) == 3:
            return True
    row1 = [grid[i][i] for i in range(0, 3)]
    row2 = [grid[2 - i][i] for i in range(0, 3)]
    if any([row1.count(symbol) == 3, row2.count(symbol) == 3]):
        return True
    return False


def process():
    flat_grid = [x for row in grid for x in row]
    if abs(flat_grid.count('X') - flat_grid.count('O')) > 1:
        print('Impossible')
        quit()
    elif is_winner('X') and is_winner('O'):
        print('Impossible')
        quit()

    if is_winner('X'):
        print('X wins')
        quit()
    elif is_winner('O'):
        print('O wins')
        quit()
    elif all(row.count(' ') == 0 for row in grid):
        print('Draw')


output()

while any(row.count(' ') for row in grid):
    player = 'O' if player == 'X' else 'X'

    while True:
        user_input = input('Enter the coordinates').split()

        if any(not x.isdigit() for x in user_input):
            print('You should enter numbers!')
            continue
        coordinates = [int(x) for x in user_input]

        if any(x < 1 or x > 3 for x in coordinates):
            print('Coordinates should be from 1 to 3!')
            continue
        x, y = coordinates[0] - 1, coordinates[1] - 1

        if grid[x][y] != ' ':
            print('This cell is occupied! Choose another one!')
            continue
        grid[x][y] = player
        output()
        process()
        break