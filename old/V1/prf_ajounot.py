# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import date, datetime
import locale
locale.setlocale(locale.LC_TIME,'')             # Affichage des dates en Français



#############################################################
##               SOUS-FONCTIONS GENERIQUES                 ##
#############################################################

## Sous-fonctions récurrente de découpage des entrées de la BDD Clé / Data
def decoup_simple (data_txt) :
    dico = dict()
    ligne = data_txt.readline()
    while ligne != "" :             
        A = str(ligne[0:-1])
        B = A.split(":")
        C = B[1].split("|")
        dico[B[0]] = C
        ligne = data_txt.readline()
    return dico

def decoup_valtuple (data_txt) :
    dico = dict()
    ligne = data_txt.readline()
    while ligne != ""  and ligne != "\n" :
        A = str(ligne[0:-1])
        B = A.split(":")
        cle=B[0]
        C = B[1].split("|")
        data = []
    ## Séparation nom et prénom
        for i in range (0, len(C)) :
            data.append(C[i].split(";"))
        dico[cle]=data              # le dictionnaire a maintenant une clé et des items-tuples (nom, prénom)
        ligne = data_txt.readline()
    return dico

def decoup_cletuple (data_txt) :
    dico = dict()
    ligne = data_txt.readline()
    while ligne != "" and ligne != "\n" :             
        A = str(ligne[0:-1])
        B = A.split(":")
        C = B[0].split(";")
        cle = tuple(C)
        D = B[1]
        dico[cle]=D              # le dictionnaire a maintenant une clé-tuples (nom, prénom) et des items
        ligne = data_txt.readline()
    return(dico)

def decoup_cletvalt (data_txt) :
    dico = dict()
    ligne = data_txt.readline()
    while ligne != "" and ligne != "\n" :             
        A = str(ligne[0:-1])
        B = A.split(":")
        C = B[0].split(";")
        cle = tuple(C)
        D = B[1].split("|")
        data = []
        ## Séparation valeurs du tuple
        for i in range (0, len(D)) :
            data.append(D[i].split(";"))
        dico[cle]=data              # le dictionnaire a maintenant une clé et des items (tuples tous les 2)
        ligne = data_txt.readline()
    return(dico)




## Sous-fonctions récurrente de découpage des entrées de la BDD Clé / Data
#def save_simple (data_txt) :


def save_valtuple (bdd, dico) :
    ## Effacement de la BDD précédente
    data_txt=open(bdd,'w')
    data_txt.write('')
    data_txt.close()
    ## Construction et sauvegarde de la nouvelle BDD
    data_txt=open(bdd,'a')
    for (cle,data) in dico.items() :
        data_txt.write(cle+':'+data[0][0]+';'+data[0][1])
        for i in range (1,len(data)) :
            data_txt.write('|'+data[i][0]+';'+data[i][1])
        data_txt.write('\n')
    data_txt.close()

def save_cletuple (bdd,dico) :
    ## Effacement de la BDD précédente
    data_txt=open(bdd,'w')
    data_txt.write('')
    data_txt.close()
    ## Construction et sauvegarde de la nouvelle BDD
    data_txt=open(bdd,'a')
    for (cle,data) in dico.items() :
        dt = ''.join(data)
        data_txt.write(cle[0]+';'+cle[1]+":"+dt)
        data_txt.write('\n')
    data_txt.close()

def save_cletvalt (bdd,dico) :
    ## Effacement de la BDD précédente
    data_txt=open(bdd,'w')
    data_txt.write('')
    data_txt.close()
    ## Construction et sauvegarde de la nouvelle BDD
    data_txt=open(bdd,'a')
    for (cle,data) in dico.items() :
        data_txt.write(cle[0]+';'+cle[1]+":"+data[0][0]+';'+data[0][1]+';'+data[0][2]+';'+data[0][3]+';'+data[0][4]+';'+data[0][5])
        for i in range (1,len(data)) :
            data_txt.write('|'+data[i][0]+';'+data[i][1]+';'+data[i][2]+';'+data[i][3]+';'+data[i][4]+';'+data[i][5])
        data_txt.write('\n')

    data_txt.close()



def ajout_dico (dico, tpl, cle) :
    if cle in dico.keys() :
        dico[cle].append(tpl)    # ajout nouvelle entrée dans le dictionnaire si le profil existe
    else :
        dico[cle] = [tpl]          # ajout nouvelle entrée dans le dictionnaire si le profil n'existe pas encore
    return dico    



#############################################################
##               FONCTIONS PROFIL PROFESSEUR               ##
#############################################################


def checknot() :
    global not_nom, not_mat, not_max, not_coef, not_type, not_not 

    ch_nom = not_nom.get()
    ch_mat = not_mat.get()
    ch_max = not_max.get()
    ch_coef = not_coef.get()
    ch_type = not_type.get()
    ch_not = not_not.get()

    if ch_nom =='' or ch_mat =='' or ch_max =='' or ch_coef =='' or ch_type =='' or ch_not =='' :
        tk.messagebox.showwarning("ATTENTION", "Merci de remplir tous les champs")
        fen_SaisieNote.mainloop()          # retour sur le même écran
    elif float(ch_not) > int(ch_max) :
        tk.messagebox.showwarning("ATTENTION", "Vous avez saisi une note supérieure à la note maximale.\nMerci de corriger")
        fen_SaisieNote.mainloop()          # retour sur le même écran
    else :
        nompn = ch_nom.split(" ")          # Séparation Nom / Prénom
        saisie_note = [ch_mat]
        saisie_note.append(ch_not)
        saisie_note.append(ch_max)
        saisie_note.append(ch_coef)
        saisie_note.append(ch_type)
        yet_dt = datetime.now()            # Sauvegarde de la date du jour
        yet_d = yet_dt.strftime("%d %B")
        saisie_note.append(yet_d)
        
        ## Découpage des entrées de la BDD (mots de passe) clé / data (élève / notes et arguments)
        data_notes=open('data/data_notes.txt','r')
        dico_notes = decoup_cletvalt (data_notes)
        data_notes.close()
        # Ajout des nouvelles entrées au dictionnaire COM
        ajout_dico(dico_notes, tuple(saisie_note), tuple(nompn))
        # Sauvegarde des dictionnaires dans le fichier texte
        bdd = 'data/data_notes.txt'
        save_cletvalt (bdd, dico_notes)







#############################################################
##                PROCESS PROFIL PROFESSEUR                ##
#############################################################

##Saisie nouveau nom
fen_SaisieNote = tk.Tk() 
fen_SaisieNote.geometry('600x200')

# Création de la liste des élèves
data_profil=open('data/data_profils.txt','r')
dico_profil = decoup_valtuple (data_profil)
data_profil.close()
list_noms = []
for i in range (0, len(dico_profil['Elève'])) :
    val = dico_profil['Elève'][i][0]+" "+dico_profil['Elève'][i][1]
    list_noms.append(val)
#Création de la liste des matières
data_matieres=open('data/data_matieres.txt','r')
dico_matieres = decoup_valtuple (data_matieres)
data_matieres.close()
list_mat = []
for i in range (0, len(dico_matieres['com'])) :     # Ajout des matières communes dans la liste
    val = dico_matieres['com'][i][0]
    list_mat.append(val)
for i in range (0, len(dico_matieres['lv1'])) :     # Ajout des matières LV1 dans la liste
    val = dico_matieres['lv1'][i][0] + ' (LV1)'
    list_mat.append(val)
for i in range (0, len(dico_matieres['lv2'])) :     # Ajout des matières LV2 dans la liste
    val = dico_matieres['lv2'][i][0] + ' (LV2)'
    list_mat.append(val)
for i in range (0, len(dico_matieres['spe'])) :     # Ajout des matières SPE dans la liste
    val = dico_matieres['spe'][i][0] + ' (SPE)'
    list_mat.append(val)
#Création des listes pour les coefs, note max et type d'examen
data_bsn=open('data/data_basenotes.txt','r')
dico_bsn = decoup_valtuple (data_bsn)
data_bsn.close()
list_max = []
list_coef = []
list_type = []
for i in range (0, len(dico_bsn['max'])) :     # Ajout des notes max dans la liste
    val = dico_bsn['max'][i][0]
    list_max.append(val)
for i in range (0, len(dico_bsn['coef'])) :     # Ajout des coefs dans la liste
    val = dico_bsn['coef'][i][0]
    list_coef.append(val)
for i in range (0, len(dico_bsn['type'])) :     # Ajout des types dans la liste
    val = dico_bsn['type'][i][0]
    list_type.append(val)

not_nom = tk.StringVar()
not_mat = tk.StringVar()
not_max = tk.StringVar()
not_coef = tk.StringVar()
not_not = tk.StringVar()

txt_titre = tk.Label(fen_SaisieNote, text="Saisie d'une nouvelle note", fg='black')
txt_nom = tk.Label(fen_SaisieNote, text="Nom de l'élève", justify='left')
txt_mat = tk.Label(fen_SaisieNote, text="Matière", justify='left')
txt_not = tk.Label(fen_SaisieNote, text="Note obtenue", justify='left')
txt_coef = tk.Label(fen_SaisieNote, text="Coefficient", justify='left')
txt_max = tk.Label(fen_SaisieNote, text="Note max possible", justify='left')
txt_type = tk.Label(fen_SaisieNote, text="Type d'examen", justify='left')
not_nom = ttk.Combobox(fen_SaisieNote, values=list_noms)
not_mat = ttk.Combobox(fen_SaisieNote, values=list_mat)
not_max = ttk.Combobox(fen_SaisieNote, values=list_max)
not_max.current(2)
not_type = ttk.Combobox(fen_SaisieNote, values=list_type)
not_coef = ttk.Combobox(fen_SaisieNote, values=list_coef)
not_not = tk.Entry(textvariable='',width=5)
bt_valider = ttk.Button(fen_SaisieNote, text='Valider', command=checknot)
txt_titre.grid(row=0)
txt_nom.grid(row=1)
txt_mat.grid(row=2)
txt_max.grid(row=3)
txt_type.grid(row=4)
txt_coef.grid(row=5)
txt_not.grid(row=6)
not_nom.grid(row=1, column=1)
not_mat.grid(row=2, column=1)
not_max.grid(row=3, column=1)
not_type.grid(row=4, column=1)
not_coef.grid(row=5, column=1)
not_not.grid(row=6, column=1)
bt_valider.grid(row=7)

fen_SaisieNote.mainloop()