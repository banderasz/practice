"""You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a
wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach
the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down,
and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f], [t, t, f, t], [f, f, f, f], [f, f, f, f]] and start = (3, 0) (bottom left) and end = (0,
0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1,
2) because there is a wall everywhere else on the second row. """
from typing import Tuple

maze = [[False, False, False, False], [True, True, False, True],
        [False, False, False, False], [False, False, False, False]]

start = (3, 0)
end = (0, 0)


def add_path(maze: list, start: Tuple, end: Tuple):
    old_maze = maze.copy()
    here = maze[start[0]][start[1]]
    if start[1] > 0:
        left = maze[start[0]][start[1] - 1]
    else:
        left = None
    if start[1] + 1 < len(maze[0]):
        right = maze[start[0]][start[1] + 1]
    else:
        right = None
    if start[0] + 1 < len(maze):
        up = maze[start[0] + 1][start[1]]
    else:
        up = None
    if start[0] > 0:
        down = maze[start[0] - 1][start[1]]
    else:
        down = None

    if left == False:
        maze[start[0]][start[1] - 1] = here + 1
    if right == False:
        maze[start[0]][start[1] + 1] = here + 1
    if up == False:
        maze[start[0] + 1][start[1]] = here + 1
    if down == False:
        maze[start[0] - 1][start[1]] = here + 1

    if left == False:
        add_path(maze, (start[0], start[1] - 1), end)
    if right == False:
        add_path(maze, (start[0], start[1] + 1), end)
    if up == False:
        add_path(maze, (start[0] + 1, start[1]), end)
    if down == False:
        add_path(maze, (start[0] - 1, start[1]), end)

    if maze[end[0]][end[1]] != False:
        return maze[end[0]][end[1]]
    if old_maze == maze:
        return None


print(add_path(maze, start, end))
