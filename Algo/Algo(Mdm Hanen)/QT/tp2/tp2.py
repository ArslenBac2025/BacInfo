from PyQt5.QtWidgets import *
from PyQt5.uic import *
from numpy import array
from pickle import load, dump
from random import randint

def enregistrer():
    e = dict()
    e["prog"] = array([""] * 6, dtype="<U20")
    n = 0

    if not w.m.isChecked() and not w.mille.isChecked() and not w.mme.isChecked():
        QMessageBox.critical(w, "error", "please check your gender");
    else:
        if w.inp_np.text() == "" or w.inp_mail.text() == "":
            QMessageBox.critical(w, "error", "please enter your inputs")
        else:
            if w.m.isChecked():
                e["genre"] = "m"
            if w.mille.isChecked():
                e["genre"] = "mille"
            if w.mme.isChecked():
                e["genre"] = "mme"

            e["np"] = w.inp_np.text()
            e["email"] = w.inp_mail.text()
            e["langue"] = w.combo_langue.currentText()
            if not w.ch_cpp.isChecked() and not w.ch_java.isChecked() and not w.ch_py.isChecked() and not w.ch_php.isChecked() and not w.ch_js.isChecked() and not w.ch_autres.isChecked():
                QMessageBox.critical(w, "error", "please pick at least a language")
            else:
                n = 0
                if w.ch_cpp.isChecked():
                    e["prog"][n] = "C++"
                    n+=1
                if w.ch_java.isChecked():
                    e["prog"][n] = "Java"
                    n+=1
                if w.ch_py.isChecked():
                    e["prog"][n] = "Python"
                    n+=1
                if w.ch_php.isChecked():
                    e["prog"][n] = "PHP"
                    n+=1
                if w.ch_js.isChecked():
                    e["prog"][n] = "JavaScript"
                    n+=1
                if w.ch_autres.isChecked():
                    e["prog"][n] = "Autre"
                    i+=1

                e["length"] = n

                f = open("clients.dat", "wb")
                dump(e, f)
                f.close()

def afficher():
    f = open("clients.dat", "rb")
    EOF = False
    while not EOF:
        try:
            e = load(f)
            print(e)
            x = w.tb_affich.rowCount()
            w.tb_affich.insertRow(x)
            mystr = ""
            for i in range(e["length"]):
                mystr += e["prog"][i] + "//"
            print(mystr)
            w.tb_affich.setItem(x, 0, QTableWidgetItem(mystr))
            w.tb_affich.setItem(x, 1, QTableWidgetItem(e["genre"]))
            w.tb_affich.setItem(x, 2, QTableWidgetItem(e["np"]))
            w.tb_affich.setItem(x, 3, QTableWidgetItem(e["langue"]))
        except:
            EOF = True

    f.close()

def effacer():
    w.inp_np.clear()
    w.inp_mail.clear()
    w.ch_py.setChecked(False)
    w.ch_java.setChecked(False)
    w.ch_cpp.setChecked(False)
    w.ch_php.setChecked(False)
    w.ch_autres.setChecked(False)
    w.ch_js.setChecked(False)

def quitter():
    app.quit()

app = QApplication([])
w = loadUi("tp2.ui")
w.show()
w.btn_enreg.clicked.connect(enregistrer)
w.btn_afficher.clicked.connect(afficher)
w.btn_eff.clicked.connect(effacer)
w.btn_quitter.clicked.connect(quitter)
app.exec()