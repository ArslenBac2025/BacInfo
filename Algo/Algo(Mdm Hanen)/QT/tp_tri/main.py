from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer

from numpy import array
from pickle import load, dump

i = 0

def show_message(message, timeout = 2000):
    w.output.setText(message)

    QTimer.singleShot(timeout, lambda: w.output.clear())


def bubble_sort(arr, n):
    type = w.type.currentText()

    cond = True
    while cond:
        cond = False
        for i in range(n - 1):
            if arr[i] < arr[i + 1] and type == "descending":
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                cond = True
            elif arr[i] > arr[i + 1] and type == "ascending":
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                cond = True


def run():
    global i

    if i >= w.res.columnCount():
        w.res.setColumnCount(i + 1)

    num = int(w.inp.text())

    w.res.setItem(0, i, QTableWidgetItem(str(num)))

    w.inp.clear()

    i+=1

def sort():
    global i

    n = w.res.columnCount()
    arr = array([0] * n)


    for j in range(0, n):
        arr[j] = w.res.item(0, j).text()

    bubble_sort(arr, n)

    for j in range(0, n):
        w.res.setItem(0, j, QTableWidgetItem(str(arr[j])))


def manage_f():
    file_name = w.filename.text()

    if w.filetype.currentText() == "export":
        f = open(file_name, "wb")

        n = w.res.columnCount()


        for i in range(n):
            item = int(w.res.item(0, i).text())
            dump(item, f)

        show_message("successfully exported!")
        f.close()
    else:
        file_name = w.filename.text()
        f = open(file_name, "rb")

        arr = []

        while True:
            try:
                x = load(f)
                arr.append(x)
            except EOFError:
                break

        w.res.clear()
        for i in range(len(arr)):
            w.res.setColumnCount(i + 1)
            w.res.setItem(0, i ,QTableWidgetItem(str(arr[i])))

        show_message("successfully imported!")


app = QApplication([])
w = loadUi("interface.ui")

w.res.setRowCount(1)

w.submit.clicked.connect(run)
w.sort.clicked.connect(sort)
w.filesubmit.clicked.connect(manage_f)

w.show()
app.exec()