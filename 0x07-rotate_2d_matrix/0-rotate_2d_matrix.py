#!/usr/bin/python3
"""
2D matrix rotation, rotate it 90 degrees clockwise
Args: Matrix (list) - 2d square matrix, Return: none
"""


def rotate_2d_matrix(matrix):
    x = len(matrix)
    for i in range(x):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(x):
        for j in range(int(x / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][x-1-j]
            matrix[i][x-1-j] = temp
