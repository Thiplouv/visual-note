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
        C = B[1].split("|")
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



def ajout_dico (dico, tpl, item) :
    if item in dico.keys() :
        dico[item].append(tpl)    # ajout nouvelle entrée dans le dictionnaire si le profil existe
    else :
        dico[item] = [tpl]          # ajout nouvelle entrée dans le dictionnaire si le profil n'existe pas encore
    return dico    



#############################################################
##              FONCTIONS PROFIL ADMINISTRATIF             ##
#############################################################

## Fonction de sauvegarde du mot de passe
def save_pwd (nompn, pwd) :
    ## Découpage des entrées de la BDD (mots de passe) clé / data (élève / password)
    data_pass=open('data/data_pass.txt','r')
    dico_pass = decoup_cletuple (data_pass)
    data_pass.close()
    # Ajout des nouvelles entrées au dictionnaire COM
    ajout_dico(dico_pass, pwd, tuple(nompn))
    # Sauvegarde des dictionnaires dans le fichier texte
    bdd = 'data/data_pass.txt'
    save_cletuple (bdd, dico_pass)





## Fonction de sauvegarde du choix des matières par professeur
def save_matprof () :
    # Récupération des données du formulaire
    ch_com = []
    sel_com = pso_com.curselection()
    for val in sel_com :
        ch_com.append(dico_matieres['com'][val])
    ch_lv1 = []
    sel_lv1 = pso_lv1.curselection()
    for val in sel_lv1 :
        ch_lv1.append(dico_matieres['lv1'][val])
    ch_lv2 = []
    sel_lv2 = pso_lv2.curselection()
    for val in sel_lv2 :
        ch_lv2.append(dico_matieres['lv2'][val])
    ch_spe = []
    sel_spe = pso_spe.curselection()
    for val in sel_spe :
        ch_spe.append(dico_matieres['spe'][val])
    if ch_com != '' :               # test sur la valeur saisie afin de ne pas manipuler un dictionnaire pour lequel il n'y aurait pas de nouvelle entrée
        ## Découpage des entrées de la BDD (COM) clé / data (c.a.d. matière commune / professeur)
        data_com = open('data/data_com.txt','r')
        dico_com = decoup_valtuple (data_com)
        data_com.close()
        # Ajout des nouvelles entrées au dictionnaire COM
        for val in ch_com :
            ajout_dico(dico_com, nompn, val)
        # Sauvegarde des dictionnaires dans le fichier texte
        bdd = 'data/data_com.txt'
        save_valtuple (bdd, dico_com)
    if ch_lv1 != '' :               # test sur la valeur saisie afin de ne pas manipuler un dictionnaire pour lequel il n'y aurait pas de nouvelle entrée
        ## Découpage des entrées de la BDD (LV1) clé / data (c.a.d. LV1 / professeur)
        data_lv1 = open('data/data_lv1.txt','r')
        dico_lv1 = decoup_valtuple (data_lv1)
        data_lv1.close()
        # Ajout des nouvelles entrées au dictionnaire COM
        for val in ch_lv1 :
            ajout_dico(dico_lv1, nompn, val)
        # Sauvegarde des dictionnaires dans le fichier texte
        bdd = 'data/data_lv1.txt'
        save_valtuple (bdd, dico_lv1)
    if ch_lv2 != '' :               # test sur la valeur saisie afin de ne pas manipuler un dictionnaire pour lequel il n'y aurait pas de nouvelle entrée
        ## Découpage des entrées de la BDD (LV1) clé / data (c.a.d. LV1 / professeur)
        data_lv2 = open('data/data_lv2.txt','r')
        dico_lv2 = decoup_valtuple (data_lv2)
        data_lv2.close()
        # Ajout des nouvelles entrées au dictionnaire COM
        for val in ch_lv2 :
            ajout_dico(dico_lv2, nompn, val)
        # Sauvegarde des dictionnaires dans le fichier texte
        bdd = 'data/data_lv2.txt'
        save_valtuple (bdd, dico_lv2)
    if ch_spe != '' :               # test sur la valeur saisie afin de ne pas manipuler un dictionnaire pour lequel il n'y aurait pas de nouvelle entrée
        ## Découpage des entrées de la BDD (LV1) clé / data (c.a.d. LV1 / professeur)
        data_spe = open('data/data_spe.txt','r')
        dico_spe = decoup_valtuple (data_spe)
        data_spe.close()
        # Ajout des nouvelles entrées au dictionnaire COM
        for val in ch_spe :
            ajout_dico(dico_spe, nompn, val)
        # Sauvegarde des dictionnaires dans le fichier texte
        bdd = 'data/data_spe.txt'
        save_valtuple (bdd, dico_spe)


## Fonction de sauvegarde du choix des matières par élève
def save_matelv () :
    global pso_lv1, pso_lv2, pso_spe, nompn
    ch_lv1 = pso_lv1.get()
    ch_lv2 = pso_lv2.get()
    ch_spe = pso_spe.get()
    ## Découpage des entrées de la BDD (LV1) clé / data (c.a.d. langue 1 / élève)
    data_lv1 = open('data/data_lv1.txt','r')
    dico_lv1 = decoup_valtuple (data_lv1)
    data_lv1.close()
    ## Découpage des entrées de la BDD (LV2) clé / data (c.a.d. langue 2 / élève)
    data_lv2 = open('data/data_lv2.txt','r')
    dico_lv2 = decoup_valtuple (data_lv2)
    data_lv2.close()
    ## Découpage des entrées de la BDD (SPE) clé / data (c.a.d. Spécialité / élève)
    data_spe = open('data/data_spe.txt','r')
    dico_spe = decoup_valtuple (data_spe)
    data_spe.close()
    # Ajout des nouvelles entrées aux dictionnaires LV1, LV2 et SPE
    ajout_dico(dico_lv1, nompn, ch_lv1)
    ajout_dico(dico_lv2, nompn, ch_lv2)
    ajout_dico(dico_spe, nompn, ch_spe)
    # Sauvegarde des dictionnaires dans les fichiers textes
    bdd = 'data/data_lv1.txt'
    save_valtuple (bdd, dico_lv1)
    bdd = 'data/data_lv2.txt'
    save_valtuple (bdd, dico_lv2)
    bdd = 'data/data_spe.txt'
    save_valtuple (bdd, dico_spe)

## Fonction de vérification de l'existence de l'élève (redondance nom et prénom) puis sauvegarde dans la BDD
def check() :
    global pso_lv1, pso_lv2, pso_spe, pso_com, nomps, nompn, profil, dico_matieres
    nomps = [pso_nom.get(),pso_prenom.get(),'ISN_2020']  # passage du formulaire (nom, prénom, password) en tuple
    nompn = [pso_nom.get(),pso_prenom.get()]  # passage du formulaire (nom et prénom) en tuple
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
    if nomps in L1 :
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
            pso_com=''
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
            bt_valider = ttk.Button(fen_SaisiePerso, text='Valider', command=save_matelv)
            bt_valider.grid(row=4)
            fen_SaisiePerso.mainloop()
        if profil == 'Professeur' :
            for elt in fen_SaisiePerso.winfo_children() :                    # RAZ de la fenêtre d'affichage
                elt.destroy()
            # Saisie des matières enseignées
            txt_titre = tk.Label(fen_SaisiePerso, text="Saisie des matières enseignées", fg='black')
            txt_titre.grid(row=0)
            # Construction du dictionnaire des matières
            ## Découpage des entrées de la BDD clé / data (c.a.d. type / matière)
            data_matieres=open('data/data_matieres.txt','r')
            dico_matieres = decoup_simple (data_matieres)
            data_matieres.close()
            # Mise en place des listes de choix des matières
            txt_com = ttk.Label(fen_SaisiePerso, text="Matières communes", justify='left')
            pso_com = tk.Listbox(fen_SaisiePerso, height=5, selectmode='multiple', exportselection=0)
            for i in range (0, len(dico_matieres['com'])) :
                pso_com.insert(i, dico_matieres['com'][i])
            txt_com.grid(row=1, column=0)
            pso_com.grid(row=2, column=0)
            txt_lv1 = ttk.Label(fen_SaisiePerso, text="LV1", justify='left')
            pso_lv1 = tk.Listbox(fen_SaisiePerso, height=5, selectmode='multiple', exportselection=0)
            for i in range (0, len(dico_matieres['lv1'])) :
                pso_lv1.insert(i, dico_matieres['lv1'][i])
            txt_lv1.grid(row=1, column=1)
            pso_lv1.grid(row=2, column=1)
            txt_lv2 = ttk.Label(fen_SaisiePerso, text="LV2", justify='left')
            pso_lv2 = tk.Listbox(fen_SaisiePerso, height=5, selectmode='multiple', exportselection=0)
            for i in range (0, len(dico_matieres['lv2'])) :
                pso_lv2.insert(i, dico_matieres['lv2'][i])
            txt_lv2.grid(row=1, column=3)
            pso_lv2.grid(row=2, column=3)
            txt_spe = ttk.Label(fen_SaisiePerso, text="Spécialité", justify='left')
            pso_spe = tk.Listbox(fen_SaisiePerso, height=5, selectmode='multiple', exportselection=0)
            for i in range (0, len(dico_matieres['spe'])) :
                pso_spe.insert(i, dico_matieres['spe'][i])
            txt_spe.grid(row=1, column=4)
            pso_spe.grid(row=2, column=4)
            bt_valider = ttk.Button(fen_SaisiePerso, text='Valider', command=save_matprof)
            bt_valider.grid(row=10)
            fen_SaisiePerso.mainloop()

        # Ajout de la nouvelle entrée au dictionnaire
        ajout_dico (dico_profils, nomps, profil)
    
        # Sauvegarde du dictionnaire dans le fichier texte
        bdd = 'data/data_profils.txt'
        save_valtuple (bdd, dico_profils)
        save_pwd (nompn, 'ISN_2020')




#############################################################
##               PROCESS PROFIL ADMINISTRATIF              ##
#############################################################

##Saisie nouveau nom
fen_SaisiePerso = tk.Tk() 
fen_SaisiePerso.geometry('600x200')

pso_nom = tk.StringVar()
pso_profil = tk.StringVar()
pso_lv1 = tk.StringVar()
pso_lv2 = tk.StringVar()
pso_spe = tk.StringVar()

txt_titre = tk.Label(fen_SaisiePerso, text="Saisie d'une nouvelle personne", fg='black')
txt_nom = tk.Label(fen_SaisiePerso, text="Nom de la personne", justify='left')
txt_prenom = tk.Label(fen_SaisiePerso, text="Prenom de la personne", justify='left')
txt_profil = tk.Label(fen_SaisiePerso, text="Profil de la personne", justify='left')
pso_nom = tk.Entry(textvariable='',width=20)
pso_prenom = tk.StringVar()
pso_prenom = tk.Entry(textvariable='',width=20)
bt_valider = tk.Button(fen_SaisiePerso, text='Valider', command=check)
pso_profil = ttk.Combobox(fen_SaisiePerso, values=["Elève", "Professeur", "Administrateur"])
txt_titre.grid(row=0)
txt_nom.grid(row=1)
txt_prenom.grid(row=2)
txt_profil.grid(row=3)
pso_nom.grid(row=1, column=1)
pso_prenom.grid(row=2, column=1)
pso_profil.grid(row=3, column=1)
pso_profil.current(0)
bt_valider.grid(row=4)

fen_SaisiePerso.mainloop()