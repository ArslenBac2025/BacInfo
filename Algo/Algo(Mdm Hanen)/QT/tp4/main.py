from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

from numpy import array
from pickle import load, dump

def verif(e):
    imc = int(e["imc"])
    if imc == "" or imc <= 0:
        return False

    i = 0
    cond = True
    num_pat = e["n_pat"]

    while i < len(num_pat) and cond:
        if not ("A" <= num_pat[i] <= "Z" or num_pat[i].isnumeric()):
            cond = False
            return cond
        i+=1

    i = 0
    cond = True
    np = e["np"]

    while i < len(np) and cond:
        if not ("A" <= np[i].upper() <= "Z" or np[i] == ' '):
            cond = False
            return cond
        i+=1

    return cond
def ajouter():
    e = dict()
    e["n_pat"] = w.inp_n_pat.text()
    e["np"] = w.inp_np.text()
    e["imc"] = w.inp_imc.text()

    if not verif(e):
        QMessageBox.critical(w ,"invalid input", "please check your inputs")
    else:
        n = w.tab.rowCount()
        w.tab.insertRow(n)
        w.tab.setItem(n, 0, QTableWidgetItem(e["n_pat"]))
        w.tab.setItem(n, 1, QTableWidgetItem(e["np"]))
        w.tab.setItem(n, 2, QTableWidgetItem(e["imc"]))

        w.inp_n_pat.clear()
        w.inp_np.clear()
        w.inp_imc.clear()
def trier():
    e = dict(n_pat = str(), np_pat = str(), imc = int())

    n = w.tab.rowCount()
    T = array([e] * n)

    for i in range(n):
        e = dict()
        n_pat = w.tab.item(i,0)
        np_pat = w.tab.item(i, 1)
        imc = w.tab.item(i, 2)

        e["n_pat"] = n_pat.text()
        e["np"] = np_pat.text()
        e["imc"] = imc.text()

        T[i] = e

    for i in range(1, n):
        j = i
        while j - 1 >= 0 and  int(T[j - 1]["imc"]) < int(T[j]["imc"]):
            T[j - 1], T[j] = T[j], T[j - 1]
            j -= 1

    n = w.tab.rowCount()
    for i in range(n):
        w.tab.setItem(i, 0, QTableWidgetItem(str(T[i]["n_pat"])))
        w.tab.setItem(i, 1, QTableWidgetItem(str(T[i]["np"])))
        w.tab.setItem(i, 2, QTableWidgetItem(str(T[i]["imc"])))


app = QApplication([])
w = loadUi("window.ui")

w.btn_ajt.clicked.connect(ajouter)
w.btn_tri.clicked.connect(trier)

w.show()
app.exec()