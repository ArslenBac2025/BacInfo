from numpy import array
from random import randint

M = array([[0] * 5] * 5)
Mres = array([[0] * 5] * 5)

def sum_neighbours(M, i, j, rows, cols):
    if i < 0 or i >= rows or j < 0 or j >= cols:
        return 0

    return M[i, j]

def remplir():
    for i in range(5):
        for j in range(5):
            M[i,j] = randint(1,10)

    print(M)
    print()

    for i in range(5):
        for j in range(5):
            Mres[i, j] += sum_neighbours(M, i - 1, j - 1, 5, 5)
            Mres[i, j] += sum_neighbours(M, i - 1, j, 5, 5)
            Mres[i, j] += sum_neighbours(M, i - 1, j + 1, 5, 5)

            Mres[i, j] += sum_neighbours(M, i, j - 1, 5, 5)
            Mres[i, j] += sum_neighbours(M, i, j + 1, 5, 5)

            Mres[i, j] += sum_neighbours(M, i + 1, j - 1, 5, 5)
            Mres[i, j] += sum_neighbours(M, i + 1, j, 5, 5)
            Mres[i, j] += sum_neighbours(M, i + 1, j + 1, 5, 5)

    print(Mres)

remplir()