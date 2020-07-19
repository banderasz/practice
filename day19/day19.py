"""A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing
cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
return the minimum cost which achieves this goal. """

"""
Backtracking
"""
from typing import Tuple, List

from day19_matrix import read_matrix

matrix = read_matrix("test.xlsx")


class House:
    id = 0

    def __init__(self, colors: List[Tuple]):
        self.chosen_color = None # to avoid to check for None every time
        self.dif = None
        self.dif_before = None
        self.dif_after = None
        self.colors = colors
        self.id = House.id
        House.id += 1


def choose_color(i, color):
    if not color is None:
        current = houses[i]
        last_color = houses[i - 1].chosen_color if i > 0 else None
        next_color = houses[i + 1].chosen_color if i+1 < len(houses) else None
        old_color = current.chosen_color
        current.chosen_color = color
        current_value = current.colors[color][1]

        current.dif = current_value - min_color_value(current.colors, [last_color, color, next_color])[1]
        current.dif_before = current_value - min_color_value(current.colors, [last_color, color])[1]
        current.dif_after = current_value - min_color_value(current.colors, [color, next_color])[1]
        if old_color != color:
            choose_color(i - 1, last_color)
            choose_color(i + 1, next_color)


def min_color_value(color: list, forbidden: list):
    free_color = list()
    for i in range(len(color)):
        if not i in forbidden:
            free_color.append(color[i])
    sorted_colors = sorted(free_color, key=lambda x: x[1])
    return sorted_colors[0]

def iterate(i):
    if i < len(houses):
        current = houses[i]
        last = houses[i-1]
        if i+1 < len(houses):
            next = houses[i+1]
        else:
            next = House(None)
        sorted_colors = sorted(current.colors, key=lambda x: x[1])

        free_min = min_color_value(current.colors, [last.chosen_color, next.chosen_color])
        free_back = min_color_value(current.colors, [next.chosen_color])
        free_forward = min_color_value(current.colors, [last.chosen_color])

        last_dif = last.dif_before or 0
        next_dif = next.dif_after or 0

        if sorted_colors[0][1] == free_min[1]:
            choose_color(i, free_min[0])
            iterate(i + 1)
        elif free_min[1] > free_forward[1] - next_dif:
            choose_color(i, free_forward[0])
            iterate(i + 1)
        elif free_min[1] > free_back[1] - last_dif:
            choose_color(i, free_back[0])
            iterate(i - 1)
        else:
            choose_color(i, free_min[0])
            iterate(i + 1)



list_of_edges = list(matrix.T.to_dict().values())

houses = list()
for house in list_of_edges:
    houses.append(House(list(house.items())))

iterate(0)

sum = 0
for house in houses:
    sum += house.colors[house.chosen_color][1]
    print(house.chosen_color)

print(sum)

