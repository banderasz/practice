"""You are given an array of non-negative integers that represents a two-dimensional elevation map where each element
is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth
index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water. """

def calc_water(array: list):
    forward = list()
    backward = list()
    max = array[0]
    for i in range(len(array)):
        if i > 0 and i+1 < len(array):
            if array[i] < max:
                forward.append(max - array[i])
            else:
                max = array[i]
                forward.append(0)
        else:
            forward.append(0)
    array.reverse()
    max = array[0]
    for i in range(len(array)):
        if i > 0 and i+1 < len(array):
            if array[i] < max:
                backward.append(max - array[i])
            else:
                max = array[i]
                backward.append(0)
        else:
            backward.append(0)
    backward.reverse()
    return sum([min(x,y) for x,y in zip(forward, backward)])

print(calc_water([3, 0, 1, 3, 1, 2]))