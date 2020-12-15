# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox




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
        C = B[1].split(",")
        dico[B[0]] = C
        ligne = data_txt.readline()
    return dico

def decoup_valtuple (data_txt) :
    dico = dict()
    ligne = data_txt.readline()
    while ligne != "" :             
        A = str(ligne[0:-1])
        B = A.split(":")
        cle=B[0]
        C = B[1].split(",")
        data = []
    ## Séparation nom et prénom
        for i in range (0, len(C)) :
            data.append(C[i].split(";"))
        dico[cle]=data              # le dictionnaire a maintenant une clé et des items-tuples (nom, prénom)
        ligne = data_txt.readline()
    return dico

#def decoup_cletuple (data_txt) :



## Sous-fonctions récurrente de découpage des entrées de la BDD Clé / Data
#def save_simple (data_txt) :


def save_valtuple (bdd, dico) :
    ## Effacement de la BDD précédente
    data_txt=open(bdd,'w')
    data_txt.write("")
    data_txt.close()
    ## Construction et sauvegarde de la nouvelle BDD
    data_txt=open(bdd,'a')
    for (cle,data) in dico.items() :
        if len(data[0]) == 2 :
            data_txt.write(cle+":"+data[0][0]+';'+data[0][1])
        else :
            data_txt.write(cle+":"+data[0][0]+';'+data[0][1]+';'+data[0][2])
        for i in range (1,len(data)) :
            if len(data[0]) == 2 :
                data_txt.write(","+data[i][0]+';'+data[i][1])
            else :
                data_txt.write(","+data[i][0]+';'+data[i][1]+';'+data[i][2])
        data_txt.write("\n")
    data_txt.close()

#def save_cletuple (data_txt) :



def ajout_dico (dico, tpl, item) :
    if item in dico.keys() :
        dico[item].append(tpl)    # ajout nouvelle entrée dans le dictionnaire si le profil existe
    else :
        dico[item] = [tpl]          # ajout nouvelle entrée dans le dictionnaire si le profil n'existe pas encore
    return dico    



#############################################################
##              FONCTIONS PROFIL ADMINISTRATIF             ##
#############################################################

## Fonction de recherche de la personne puis suppression de la BDD
def actsup() :
    global pso_lv1, pso_lv2, pso_spe, pso_com, nomps, nompn, profil, dico_matieres
    nompn = [pso_nom.get(),pso_prenom.get()]                # passage du formulaire (nom et prénom) en tuple

    # Construction du dictionnaire de tous les profils
    ## Découpage des entrées de la BDD clé / data (c.a.d. profil / nom-prénom)
    data_profils=open('data/data_profils.txt','r')
    dico_profils = decoup_valtuple (data_profils)
    data_profils.close()

    # Vérification de l'existence de l'entrée dans la BDD
    L1 = []
    for key in dico_profils.keys() :        # Création d'une liste de tous les tuples [nom,prénom] pour recherche d'un existant
        L1.extend(dico_profils[key])
    if nomps not in L1 :
        tk.messagebox.showwarning("ATTENTION", "Cette personne n'existe pas dana la base (vérifiez l'orthographe du nom et du prénom")
        fen_SaisiePerso.mainloop()          # retour sur le même écran
    else :









#############################################################
##               PROCESS PROFIL ADMINISTRATIF              ##
#############################################################

##Saisie nom à supprimer
fen_SaisiePerso = tk.Tk() 
fen_SaisiePerso.geometry('600x200')

pso_nom = tk.StringVar()
pso_profil = tk.StringVar()
pso_lv1 = tk.StringVar()
pso_lv2 = tk.StringVar()
pso_spe = tk.StringVar()

txt_titre = tk.Label(fen_SaisiePerso, text="Saisie de la personne à ôter de la base", fg='black')
txt_nom = tk.Label(fen_SaisiePerso, text="Nom de la personne", justify='left')
txt_prenom = tk.Label(fen_SaisiePerso, text="Prenom de la personne", justify='left')
pso_nom = tk.Entry(textvariable='',width=20)
pso_prenom = tk.StringVar()
pso_prenom = tk.Entry(textvariable='',width=20)
bt_valider = tk.Button(fen_SaisiePerso, text='Valider', command=actsup)
txt_titre.grid(row=0)
txt_nom.grid(row=1)
txt_prenom.grid(row=2)
pso_nom.grid(row=1, column=1)
pso_prenom.grid(row=2, column=1)
bt_valider.grid(row=4)

fen_SaisiePerso.mainloop()