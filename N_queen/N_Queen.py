from Cell import Cell

n = 5

cells = list()
queens = list()
for i in range(n):
    for j in range(n):
        cells.append(Cell(i, j))


def choose_queen():
    any_free = False

    for cell in cells:
        if cell.free and not cell.tried:
            any_free = True
            queens.append(cell)
            cell.queen = True
            cell_queen_check(cell.x, cell.y)
    if not any_free:
        triedcell = queens.pop()
        triedcell.tried = len(queens)+1
        triedcell.queen = False
        for cell in cells:
            cell.free = True
            if cell.tried > (len(queens)+1):
                cell.tried = 0
        for queen in queens:
            cell_queen_check(queen.x, queen.y)



def search_cell(x, y):
    for cell in cells:
        if cell.y == y and cell.x == x:
            return cell


def cell_queen_check(x, y):
    for cell in cells:
        if cell.x == x or cell.y == y or abs(cell.x - x) == abs(cell.y - y):
            cell.free = False


def board():
    out = ""
    for cell in cells:
        if cell.free:
            out += "O "
        else:
            if cell.queen:
                out += "I "
            else:
                out += "X "
        if cell.y == n - 1:
            out += "\n"
    print(out)


while len(queens) < n:
    choose_queen()
    board()