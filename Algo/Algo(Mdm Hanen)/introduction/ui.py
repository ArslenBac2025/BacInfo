from PyQt5.QtWidgets import * # type: ignore
from PyQt5.uic import loadUi # type: ignore


app = QApplication([])
w = loadUi("interface.ui")

def factoriel(n):
    if n == 0:
        return 1
    
    return n * factoriel(n - 1)

def execute():
    w.res.setText(str(factoriel(int(w.inp.text()))))

w.btn.clicked.connect(execute)

w.show()
app.exec()