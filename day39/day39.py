"""Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead
or alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.
"""

from random import random
import matplotlib.pyplot as plt
import copy

class Cell:
    def __init__(self, x: int, y: int, status: bool):
        self.x = x
        self.y = y
        self.status = status
        self.neighbours = list()

    def calc_neighbouts(self, population):
        for cell in population:
            if abs(cell.x - self.x) <= 1 and abs(cell.y-self.y) <= 1 and cell != self:
                self.neighbours.append(cell)

    def iterate(self):
        live_neighbours = 0
        for neighbour in self.neighbours:
            if neighbour.status:
                live_neighbours += 1
        if live_neighbours < 2:
            return False
        elif live_neighbours > 3:
            return False
        elif live_neighbours == 3:
            return True
        elif live_neighbours == 2:
            return self.status

population = []
p = 0.5
N = 200
X = 100
Y = 100

for i in range(X):
    for j in range(Y):
        if random() < p and ( 40 <i< 60 and 40 <j< 60):
            population.append(Cell(i, j, True))
        else:
            population.append(Cell(i, j, False))

# list_of_life = [(10,10), (10,11), (11,11), (10,12)]
#
# for cell in population:
#     if (cell.x, cell.y) in list_of_life:
#         cell.status = True


def plot(population: list):
    deadx = list()
    deady = list()
    livex = list()
    livey = list()
    for cell in population:
        if cell.status:
            livex.append(cell.x)
            livey.append(cell.y)
        else:
            deadx.append(cell.x)
            deady.append(cell.y)

    plt.scatter(deadx, deady, c='r', marker='.', label='dead')
    plt.scatter(livex, livey, c='g', marker='.', label='live')
    plt.legend(loc='upper left')
    plt.show()

for cell in population:
    cell.calc_neighbouts(population)

for i in range(N):
    plot(population)
    status_change = list()
    for cell in population:
        status_change.append(cell.iterate())
    for i in range(len(population)):
        population[i].status = status_change[i]