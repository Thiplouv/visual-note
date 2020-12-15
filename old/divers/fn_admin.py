# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functools import partial
from fn_generic import *


#############################################################
##              FONCTIONS PROFIL ADMINISTRATIF             ##
#############################################################

## Fonction de sauvegarde du choix des matières par élève
def save_mat () :
    global pso_lv1, pso_lv2, pso_spe, nom, profil
    ch_lv1 = pso_lv1.get()
    ch_lv2 = pso_lv2.get()
    ch_spe = pso_spe.get()
    # Construction des dictionnaire LV1, LV2, SPE
    ## Découpage des entrées de la BDD (LV1) clé / data (c.a.d. langue 1 / élève)
    data_lv1=open('data/data_lv1.txt','r')
    dico_lv1 = decoup_valtuple (data_lv1)
    data_lv1.close()
    ## Découpage des entrées de la BDD (LV2) clé / data (c.a.d. langue 2 / élève)
    data_lv2=open('data/data_lv2.txt','r')
    dico_lv2 = decoup_valtuple (data_lv2)
    data_lv2.close()
    ## Découpage des entrées de la BDD (SPE) clé / data (c.a.d. Spécialité / élève)
    data_spe=open('data/data_lv2.txt','r')
    dico_spe = decoup_valtuple (data_spe)
    data_spe.close()
    # Ajout des nouvelles entrées aux dictionnaires LV1, LV2 et SPE
    ajout_dico(dico_lv1, nom, ch_lv1)
    ajout_dico(dico_lv2, nom, ch_lv2)
    ajout_dico(dico_spe, nom, ch_spe)
    # Sauvegarde des dictionnaire dans les fichiers textes
    bdd = 'data/data_lv1.txt'
    save_valtuple (bdd, dico_lv1)
    bdd = 'data/data_lv2.txt'
    save_valtuple (bdd, dico_lv2)
    bdd = 'data/data_spe.txt'
    save_valtuple (bdd, dico_spe)

## Fonction de vérification de l'existence de l'élève (redondance nom et prénom) puis sauvegarde dans la BDD
def check() :
    global pso_lv1, pso_lv2, pso_spe, pso_nom, pso_profil, nom, profil
    nom = [pso_nom.get(),pso_prenom.get()]  # passage du formulaire (nom et prénom) en tuple
    profil = pso_profil.get()               # passage du formulaire (profil) en variables
    
    # Construction du dictionnaire de tous les profils
    ## Découpage des entrées de la BDD clé / data (c.a.d. profil / nom-prénom)
    data_profils=open('data/data_profils.txt','r')
    dico_profils = decoup_valtuple (data_profils)
    data_profils.close()
    
    # Vérification de l'existence de la nouvelle entrée dans la BDD
    L1 = []
    for key in dico_profils.keys() :        # Création d'une liste de tous les tuples [nom,prénom] pour recherche d'un existant
        L1.extend(dico_profils[key])
    if nom in L1 :
        tk.messagebox.showwarning("ATTENTION", "Cette personne est déjà enregistrée")
        fen_SaisiePerso.mainloop()          # retour sur le même écran
    else :
        if profil == 'Elève' :
            for elt in fen_SaisiePerso.winfo_children() :                    # RAZ de la fenêtre d'affichage
                elt.destroy()
            # Saisie des LV1, LV2 et SPE
            txt_titre = tk.Label(fen_SaisiePerso, text="Saisie des matières optionnelles", fg='black')
            txt_titre.grid(row=0)
            # Construction du dictionnaire des matières
            ## Découpage des entrées de la BDD clé / data (c.a.d. type / matière)
            data_matieres=open('data/data_matieres.txt','r')
            dico_matieres = decoup_simple (data_matieres)
            data_matieres.close()
            # Mise en place des combobox de choix des matières
            txt_titre = tk.Label(fen_SaisiePerso, text="Saisie des matières optionnelles", fg='black')
            txt_lv1 = ttk.Label(fen_SaisiePerso, text="LV1", justify='left')
            pso_lv1 = ttk.Combobox(fen_SaisiePerso, values=dico_matieres['lv1'])
            txt_lv1.grid(row=1)
            pso_lv1.current(0)                      # Anglais par défaut
            pso_lv1.grid(row=1, column=1)
            txt_lv2 = ttk.Label(fen_SaisiePerso, text="LV2", justify='left')
            pso_lv2 = ttk.Combobox(fen_SaisiePerso, values=dico_matieres['lv2'])
            pso_lv2.current(1)                      # Espagnol par défaut
            txt_lv2.grid(row=2)
            pso_lv2.grid(row=2, column=1)
            txt_spe = ttk.Label(fen_SaisiePerso, text="Spécialité", justify='left')
            pso_spe = ttk.Combobox(fen_SaisiePerso, values=dico_matieres['spe'])
            txt_spe.grid(row=3)                     # Pas de spécialité par défaut
            pso_spe.grid(row=3, column=1)
            bt_valider = ttk.Button(fen_SaisiePerso, text='Valider', command=save_mat)
            bt_valider.grid(row=4)
            fen_SaisiePerso.mainloop()

        # Ajout de la nouvelle entrée au dictionnaire
        ajout_dico (dico_profils, nom, profil)
    
        # Sauvegarde du dictionnaire dans le fichier texte
        bdd = 'data/data_profils.txt'
        save_valtuple (bdd, dico_profils)
