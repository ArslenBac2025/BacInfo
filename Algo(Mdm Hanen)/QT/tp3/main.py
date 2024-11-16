from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

from random import randint
from numpy import array

def remplir():
    global l
    global c
    global M

    dimension = w.taille.text()
    if len(dimension) < 3:
        QMessageBox.critical(w, "error", "invalid dimensions")

    find_x = dimension.find("x")
    l = int(dimension[: find_x])
    c = int(dimension[find_x + 1:])

    M = array([[int] * c] * l)

    w.ava.setRowCount(l)
    w.ava.setColumnCount(c)

    for i in range(l):
        for j in range(c):
            num = randint(10, 99)
            w.ava.setItem(i, j, QTableWidgetItem(str(num)))
            M[i,j] = num


def tri():
    global l
    global c

    n = c * l

    T = array([int()] * n)

    k = 0
    for i in range(l):
        for j in range(c):
            T[j + k] = M[i,j]
        k += c


    for i in range(1, n):
        temp = T[i]
        j = i
        while j > 0 and T[j - 1] > temp:
            T[j] = T[j - 1]
            j-=1
        T[j] = temp

    print(T)

    k = 0
    w.apres.setRowCount(l)
    w.apres.setColumnCount(c)
    for i in range(l):
        for j in range(c):
            w.apres.setItem(i, j , QTableWidgetItem(str(T[j + k])))
        k += c

app = QApplication([])
w = loadUi("TPTri.ui")


l = 0
c = 0

w.remplir.clicked.connect(remplir)
w.tri.clicked.connect(tri)

w.show()
app.exec()