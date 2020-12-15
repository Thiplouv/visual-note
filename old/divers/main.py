# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from fn_generic import *
from fn_admin import *

 
##Fonction de vérification de l'existence de l'élève (redondance nom et prénom) puis sauvegarde dans la BDD
def check() :
    data_profils=open('data/data_profils.txt','r')
    # Construction du dictionnaire de tous les profils
    dico_profils =dict()
    ligne = data_profils.readline()
    ## Découpage des entrées de la BDD clé / data (c.a.d. profil / nom-prénom)
    while ligne != "" :             
        A = str(ligne[0:-1])
        B = A.split(":")
        cle=B[0]
        C = B[1].split(",")
        data = []
    ## Séparation nom et prénom
        for i in range (0, len(C)) :
            data.append(C[i].split(";"))
        
        dico_profils[cle]=data              # le dictionnaire a maintenant une clé (profil) et des items-tuples (nom, prénom)
        ligne = data_profils.readline()
    nom = [pso_nom.get(),pso_prenom.get()]  # passage du formulaire (nom et prénom) en tuple
    profil = pso_profil.get()               # passage du formulaire (profil) en variables
    
    # Vérification de l'existence de la nouvelle entrée dans la BDD
    L1 = []
    for key in dico_profils.keys() :        # Création d'une liste de tous les tuples [nom,prénom] pour recherche d'un existant
        L1.extend(dico_profils[key])
    if nom in L1 :
        tk.messagebox.showwarning("ATTENTION", "Cette personne est déjà enregistrée")
        fen_SaisiePerso.mainloop()          # retour sur le même écran
    else :
        # Ajout de la nouvelle entrée au dictionnaire
        prev_profils = dico_profils             # sauvegarde de l'ancien dictionnaire (avant update)
        if profil in prev_profils.keys() :
            dico_profils[profil].append(nom)    # ajout nouvelle entrée dans le dictionnaire si le profil existe
        else :
            dico_profils[profil] = [nom]          # ajout nouvelle entrée dans le dictionnaire si le profil n'existe pas encore
    
        # Sauvegarde du dictionnaire dans le fichier texte
        ## Effacement de la BDD précédente
        data_profils=open('data/data_profils.txt','w')
        data_profils.write("")
        data_profils.close()
        ## Construction et sauvegarde de la nouvelle BDD
        data_profils=open('data/data_profils.txt','a')
        for (cle,data) in dico_profils.items() :
            data_profils.write(cle+":"+data[0][0]+";"+data[0][1])
            for i in range (1,len(data)):
                data_profils.write(","+data[i][0]+";"+data[i][1])
            data_profils.write("\n")
        data_profils.close()


##Saisie nouveau nom
fen_SaisiePerso = tk.Tk() 
fen_SaisiePerso.geometry('400x150')

pso_nom = tk.StringVar()
pso_nom.set("")
pso_prenom = tk.StringVar()
pso_prenom.set("")
txt_titre = tk.Label(fen_SaisiePerso, text="Saisie d'une nouvelle personne", fg='black')
txt_nom = ttk.Label(fen_SaisiePerso, text="Nom de la personne", justify='left')
txt_prenom = ttk.Label(fen_SaisiePerso, text="Prenom de la personne", justify='left')
txt_profil = ttk.Label(fen_SaisiePerso, text="Profil de la personne", justify='left')
pso_nom = ttk.Entry(textvariable=pso_nom,width=20)
pso_prenom = ttk.Entry(textvariable=pso_prenom,width=20)
bt_valider = ttk.Button(fen_SaisiePerso, text='Valider', command=check)

pso_profil = ttk.Combobox(fen_SaisiePerso, 
                            values=[
                                    "Elève", 
                                    "Professeur",
                                    "Administrateur"])
#print(dict(comboExample)) 
txt_titre.grid(row=0)
txt_nom.grid(row=1)
txt_prenom.grid(row=2)
txt_profil.grid(row=3)
pso_nom.grid(row=1, column=1)
pso_prenom.grid(row=2, column=1)
pso_profil.grid(row=3, column=1)
pso_profil.current(0)
bt_valider.grid(row=4)

#print(comboExample.current(), comboExample.get())

fen_SaisiePerso.mainloop()