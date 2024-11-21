
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.uic import loadUi
from numpy import array

def verif(ch):
    if(len(ch) < 3): return False
    i = 0
    cond = True
    while(not((cond == False) and (i > len(ch)))):
        if(not 'A' <= (ch[i]).upper() <= 'Z'):
            cond = False
        i+=1
    return cond

def ajout():
    e = dict(
        num=str(),
        nom=str(),
        pre=str(),
        genre=str(),
        option=array([int] * 4)
    )
    num = doc.num.text()
    if(not(num.isnumeric()) or len(num) != 4):
        QMessageBox.critical(doc, "error", "enter num of length 4 and numeric")
    else:
        e["num"] = num
        nom = doc.nom.text()
        pre = doc.pre.text()

        if(not(verif(pre) and verif(nom))):
            QMessageBox.critical(doc, "error", "entrer votre nom et prenom cv")
        else:
            e["nom"] = nom
            e["pre"] = pre

            if(doc.M.isChecked() or doc.F.isChecked()):
                if(doc.M.isChecked()):
                    e["genre"] = "M"
                else:
                    e["genre"] = "F"

                #or just do 0 for correct usage
                e["option"] = array([int()] * 4)
                i = 0

                if(doc.music_cb.isChecked()):
                    e["option"][0] = 1
                else:
                    e["option"][0] = 0

                if(doc.theater_cb.isChecked()):
                    e["option"][1] = 1
                else:
                    e["option"][1] = 0

                if(doc.sports_cb.isChecked()):
                    e["option"][2] = 1
                else:
                    e["option"][2] = 0

                if(doc.dessin_cb.isChecked()):
                    e["option"][3] = 1
                else:
                    e["option"][3] = 0

            else:
                QMessageBox.critical(doc, "error", "selectionner votre genre cv")

app = QApplication([])
doc = loadUi("window.ui")
doc.show()
doc.submit.clicked.connect(ajout)
app.exec()