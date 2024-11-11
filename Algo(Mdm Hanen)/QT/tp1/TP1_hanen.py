from PyQt5.QtWidgets import *
from PyQt5.uic import *
from numpy import*
from pickle import*
matiere=dict(
                libelle=str(),
                DC=float(),
                DS=float())
e=dict(num=int(),
        nom=str(),
        prenom=str(),
        genre=str(),
        classe=str(),
        option=array([int]*4),
        Tmat=array([matiere]*10)
           )
global taille
taille=0
def verif(ch):
    i=0
    test=True
    while(not((test==False)or(i>len(ch)-1))):
        if ("A"<=ch[i].upper()<="Z"):
            i=i+1
        else:
            test=False
    return test
def ajouter():
    num=fen.num.text()
    if not(num.isnumeric())or(len(num)!=4):
        QMessageBox.critical(fen,"Erreur","le numéro d'inscription doit être un nombre de 4 chiffres")
    else:
        e["num"]=int(num)
        nom=fen.nom.text()
        if (nom=="")or(not(verif(nom))):
            QMessageBox.critical(fen,"Erreur","le nom est une chaine non vide totalement alphabétique")
        else:
            e["nom"]=nom
            prenom=fen.prenom.text()
            if (prenom=="")or(not(verif(prenom))):
                QMessageBox.critical(fen,"Erreur","le prenom est une chaine non vide totalement alphabétique")
            else:
                e["prenom"]=prenom
                if not(fen.m.isChecked())and not(fen.f.isChecked()):
                    QMessageBox.critical(fen,"Erreur","vous devez sélectionné un genre")
                else:
                    if (fen.m.isChecked()):
                        e["genre"]="M"
                    elif (fen.f.isChecked()):
                        e["genre"]="F"
                    if (fen.music.isChecked()):
                        e["option"][0]=1
                    else:
                        e["option"][0]=0
                       
                    if (fen.theatre.isChecked()):
                        e["option"][1]=1
                    else:
                        e["option"][1]=0
                    
                    if (fen.dessin.isChecked()):
                        e["option"][2]=1
                    else:
                        e["option"][2]=0
                        
                    if (fen.sport.isChecked()):
                        e["option"][3]=1
                    else:
                        e["option"][3]=0
                    e["classe"]=fen.classe.currentText()
                    f=open("eleve.dat","ab")
                    dump(e,f)
                    QMessageBox.information(fen,"Ajout","Ajout avec succes")
                    f.close()
                    
def ajoutnotes():
    global taille
    dc=fen.dc.text()
    ds=fen.ds.text()
    if (not(dc.isnumeric()) or (not(ds.isnumeric()))):
        QMessageBox.critical(fen,"Erreur","les notes doivent être numérique")
    else:
        x=fen.notes.rowCount()
        fen.notes.insertRow(x)
        fen.notes.setItem(x,0,QTableWidgetItem(fen.matiere.currentText()))
        mat=dict()
        mat["libelle"]=fen.matiere.currentText()
        fen.notes.setItem(x,1,QTableWidgetItem(dc))
        mat["dc"]=float(dc)
        fen.notes.setItem(x,2,QTableWidgetItem(ds))
        mat["ds"]=float(ds)
        e["Tmat"][taille]=mat
        taille=taille+1

                        


f=open("eleve.dat","wb")
f.close()                          
                        
                       
app=QApplication([]) #Instance d’application QTDesigner
fen=loadUi("TP1.ui ")#Nom de la fenêtre
fen.ajout.clicked.connect(ajouter)#lorsqu’on clique sur le bouton le module associé au bouton s’exécute
fen.ajoutnotes.clicked.connect(ajoutnotes)#lorsqu’on clique sur le bouton le module associé au bouton s’exécute

fen.show()#Instruction pour charger la fenêtre nommée
app.exec_()#Instruction pour l’exécution d’application
