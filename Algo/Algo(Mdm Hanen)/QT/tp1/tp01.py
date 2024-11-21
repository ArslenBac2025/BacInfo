from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
from PyQt5.uic import loadUi  # type: ignore
from pickle import dump, load
from numpy import array

def verif(id):
    cond = True
    i = 0
    while cond and i < len(id):
        if not '0' <= id[i] <= '9':
            cond = False
        i += 1

        
    return cond

def ajouter():
    id = win.inp_id.text()
    if not verif(id) or (not (win.ch_import.isChecked()) and not(win.ch_export.isChecked())) or (not (win.r_homme.isChecked()) and not( win.r_femme.isChecked())) :
        QMessageBox.warning(win, "error", "please enter an id")
    else:
        e = dict()
        e["id"] = id
        if(win.r_homme.isChecked()):
            e["genre"] = "homme"
        else:
            e["genre"] = "femme"
            
        e["type"] = array([0] * 2)
        
        if(win.ch_import.isChecked() and win.ch_export.isChecked()):
            e["type"][0] = 1
            e["type"][1] = 1
        elif win.ch_import.isChecked() and not win.ch_export.isChecked():
            e["type"][0] = 1
            e["type"][1] = 0
            
        elif not win.ch_import.isChecked() and win.ch_export.isChecked():
            e["type"][0] = 0
            e["type"][1] = 1  
            
        f = open("clients.dat", "ab")
        dump(e, f)
        f.close()    
        
def afficher():
    f = open("clients.dat", "rb")
    x = 0 
    while(True):
        try:
            e = load(f)
            if win.com_attributs.currentText() == "Tous":
                win.table_result.setRowCount(x + 1)  
                win.table_result.setItem(x, 0, QTableWidgetItem(e["id"]))
                win.table_result.setItem(x, 1, QTableWidgetItem(e["genre"]))

                type_str = ""
                if e["type"][0] == 1:
                    type_str += "import "
                            
                if e["type"][1] == 1:
                    type_str += "export"
                        
                win.table_result.setItem(x, 2, QTableWidgetItem(type_str))
                x += 1  

            elif win.com_attributs.currentText() == "Homme" and e["genre"] == "homme":
                win.table_result.setRowCount(x + 1)
                win.table_result.setItem(x, 0, QTableWidgetItem(e["id"]))
                win.table_result.setItem(x, 1, QTableWidgetItem(e["genre"]))

                type_str = ""
                if e["type"][0] == 1:
                    type_str += "import "
                            
                if e["type"][1] == 1:
                    type_str += "export"
                        
                win.table_result.setItem(x, 2, QTableWidgetItem(type_str))
                x += 1  

            elif win.com_attributs.currentText() == "Femme" and e["genre"] == "femme":
                win.table_result.setRowCount(x + 1)
                win.table_result.setItem(x, 0, QTableWidgetItem(e["id"]))
                win.table_result.setItem(x, 1, QTableWidgetItem(e["genre"]))

                type_str = ""
                if e["type"][0] == 1:
                    type_str += "import "
                            
                if e["type"][1] == 1:
                    type_str += "export"
                        
                win.table_result.setItem(x, 2, QTableWidgetItem(type_str))
                x += 1  

            elif win.com_attributs.currentText() == "Export" and e["type"][1] == 1 and e["type"][0] == 0:
                win.table_result.setRowCount(x + 1)
                win.table_result.setItem(x, 0, QTableWidgetItem(e["id"]))
                win.table_result.setItem(x, 1, QTableWidgetItem(e["genre"]))

                type_str = ""
                if e["type"][0] == 1:
                    type_str += "import "
                            
                if e["type"][1] == 1:
                    type_str += "export"
                        
                win.table_result.setItem(x, 2, QTableWidgetItem(type_str))
                x += 1  

            elif win.com_attributs.currentText() == "Import" and e["type"][0] == 1 and e["type"][1] == 0:
                win.table_result.setRowCount(x + 1)
                win.table_result.setItem(x, 0, QTableWidgetItem(e["id"]))
                win.table_result.setItem(x, 1, QTableWidgetItem(e["genre"]))

                type_str = ""
                if e["type"][0] == 1:
                    type_str += "import "
                            
                if e["type"][1] == 1:
                    type_str += "export"
                        
                win.table_result.setItem(x, 2, QTableWidgetItem(type_str))
                x += 1  

            elif win.com_attributs.currentText() == "Import/Export" and e["type"][0] == 1 and e["type"][1] == 1:
                win.table_result.setRowCount(x + 1)
                win.table_result.setItem(x, 0, QTableWidgetItem(e["id"]))
                win.table_result.setItem(x, 1, QTableWidgetItem(e["genre"]))

                type_str = ""
                if e["type"][0] == 1:
                    type_str += "import "
                            
                if e["type"][1] == 1:
                    type_str += "export"
                        
                win.table_result.setItem(x, 2, QTableWidgetItem(type_str))
                x += 1
            else:
                win.table_result.setRowCount(0)
        except EOFError:
            break
        
    f.close()
     
f = open("clients.dat", "wb")
f.close()

def reset():
    win.inp_id.clear()
    win.ch_import.setChecked(False)
    win.ch_export.setChecked(False)
    win.r_homme.setChecked(False)
    win.r_femme.setChecked(False)
    win.table_result.clear()
    win.table_result.setRowCount(0)
    f = open("clients.dat", "wb")
    f.close()

app = QApplication([])
win = loadUi("main.ui")
win.btn_add.clicked.connect(ajouter)
win.btn_select.clicked.connect(afficher)
win.btn_reset.clicked.connect(reset)
win.show()
app.exec()