#!/usr/bin/python3
"""
Create a function def island_perimeter(grid);
that returns the perimeter of the island described in grid.
"""


def island_perimeter(grid):
    """
    grid is a list of list of integers:
    0 represents water, 1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    x = len(grid)
    for i, row in enumerate(grid):
        y = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == y - 1 or (y > j + 1 and row[j + 1] == 0),
                i == x - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
