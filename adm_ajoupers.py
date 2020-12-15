# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from fn_generic import *
import fn_generic as gen
from adm_main import *
import adm_main as adm




#############################################################
##              FONCTIONS PROFIL ADMINISTRATIF             ##
#############################################################

## Fonction de vérification du nom et du prénom (caractères alphabétiques)
def check_alpha (ch) :
    global idusr, fen_SaisiePerso
    alpha_min = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','à','â','é','è','ë','ê','ô','ï','î','ç']
    alpha_maj = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    msg = 'ok'
    chsp = ch.split('-')
    if chsp[0][0] not in alpha_maj :
        msg = 'Les initiales doivent être en majuscule.\nMerci de corriger.'
    elif len (chsp) == 1 :
        for i in range (1, len(chsp[0])) :
            if chsp[0][i] in alpha_maj :
                msg = 'Seules les initiales doivent être en majuscule.\nMerci de corriger.'
            elif chsp[0][i] not in alpha_min :
                msg = 'Merci de ne saisir que des caractères alphabétiques.'
    else :
            if chsp[1][0] not in alpha_maj :
                msg = 'Les initiales doivent être en majuscule.\nMerci de corriger.'      
            else :
                for i in range (1, len(chsp[1])) :
                    if chsp[1][i] in alpha_maj :
                        msg = 'Seules les initiales doivent être en majuscule.\nMerci de corriger.'
                    elif chsp[1][i] not in alpha_min :
                        msg = 'Merci de ne saisir que des caractères alphabétiques.'
    return (msg)


## Fonction de sauvegarde du mot de passe
def save_pwd (nompn, pwd) :
    global idusr
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
    global idusr, fen_SaisiePerso, nompn, dico_profils
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
            ajout_dico(dico_com, nompn, val[0])
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
            ajout_dico(dico_lv1, nompn, val[0])
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
            ajout_dico(dico_lv2, nompn, val[0])
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
            ajout_dico(dico_spe, nompn, val[0])
        # Sauvegarde des dictionnaires dans le fichier texte
        bdd = 'data/data_spe.txt'
        save_valtuple (bdd, dico_spe)
    # Ajout de la nouvelle entrée au dictionnaire
    ajout_dico (dico_profils, nomps, profil)
    # Sauvegarde du dictionnaire dans le fichier texte
    bdd = 'data/data_profils.txt'
    save_valtuple (bdd, dico_profils)
    save_pwd (nompn, 'ISN_2020')
    # Message de fin
    ask = tk.messagebox.askyesno("MERCI", nompn[1]+" "+nompn[0]+" a bien été enregistrée(e) dans la base.\n Souhaitez-vous ajouter une autre personne ?", parent=fen_SaisiePerso)
    fen_SaisiePerso.destroy()
    if ask == True :
        addpers(idusr)                              # retour sur la page d'ajout de personne
    else :
        adm.adm_accueil(idusr)                      # retour sur l'accueil d'admin


## Fonction de sauvegarde du choix des matières par élève
def save_matelv () :
    global idusr, fen_SaisiePerso, pso_lv1, pso_lv2, pso_spe, nompn, nomps, dico_profils
    ch_lv1 = pso_lv1.get()
    ch_lv2 = pso_lv2.get()
    ch_spe = pso_spe.get()

    if ch_lv1 == ch_lv2 :
        tk.messagebox.showerror("ERREUR", "Un élève ne peut pas faire " + ch_lv1 + " en LV1 et LV2.\nMerci de corriger.", parent=fen_SaisiePerso)
    else :
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
        # Ajout de la nouvelle entrée au dictionnaire
        ajout_dico (dico_profils, nomps, profil)
        # Sauvegarde du dictionnaire dans le fichier texte
        bdd = 'data/data_profils.txt'
        save_valtuple (bdd, dico_profils)
        save_pwd (nompn, 'ISN_2020')
        # Message de fin
        ask = tk.messagebox.askyesno("MERCI", nompn[1]+" "+nompn[0]+" a bien été enregistrée(e) dans la base.\n Souhaitez-vous ajouter une autre personne ?", parent=fen_SaisiePerso)
        fen_SaisiePerso.destroy()
        if ask == True :
            addpers(idusr)                              # retour sur la page d'ajout de personne
        else :
            adm.adm_accueil(idusr)                      # retour sur l'accueil d'admin



## Fonction de vérification de l'existence de l'élève (redondance nom et prénom) puis sauvegarde dans la BDD
def checkpers() :
    global idusr, fen_SaisiePerso, fr1, fr2, fr3, pso_lv1, pso_lv2, pso_spe, pso_com, pso_profil, nomps, nompn, profil, dico_matieres, dico_profils
    nomps = [pso_nom.get(),pso_prenom.get(),'ISN_2020']  # passage du formulaire (nom, prénom, password) en tuple
    nompn = [pso_nom.get(),pso_prenom.get()]  # passage du formulaire (nom et prénom) en tuple
    profil = pso_profil.get()               # passage du formulaire (profil) en variables
    
    # Vérification des caractères alphabétiques dans la saisie
    res = check_alpha(nompn[0])
    if res != 'ok' :
        tk.messagebox.showwarning('ATTENTION', res, parent = fen_SaisiePerso)
    else :
        ret = check_alpha(nompn[1])
        if ret != 'ok' :
            tk.messagebox.showwarning('ATTENTION', ret, parent = fen_SaisiePerso)
        else :
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
                tk.messagebox.showwarning("ATTENTION", "Cette personne est déjà enregistrée", parent=fen_SaisiePerso)
                fen_SaisiePerso.mainloop()          # retour sur le même écran
            else :
                if profil == 'Elève' :
                    for elt in fr2.winfo_children() :                    # RAZ de la fenêtre d'affichage
                        elt.destroy()
                    for elt in fr3.winfo_children() :                    # RAZ de la fenêtre d'affichage
                        elt.destroy()
                    fr2.pack(fill=X)
                    fr3.pack(fill=X)
                    # Saisie des LV1, LV2 et SPE
                    txt_titre = tk.Label(fr2, text="Saisie des matières optionnelles", font=("Calibri",18), bg="white", fg="black")
                    txt_titre.grid(row=0)
                    # Construction du dictionnaire des matières
                    ## Découpage des entrées de la BDD clé / data (c.a.d. type / matière)
                    data_matieres=open('data/data_matieres.txt','r')
                    dico_matieres = decoup_valtuple (data_matieres)
                    data_matieres.close()
                    # Mise en place des combobox de choix des matières
                    pso_com=''
                    lst_lv1 =[]
                    for i in range (0, len(dico_matieres['lv1'])) :
                        val = dico_matieres['lv1'][i][0]
                        lst_lv1.append(val)
                    lst_lv2 =[]
                    for i in range (0, len(dico_matieres['lv2'])) :
                        val = dico_matieres['lv2'][i][0]
                        lst_lv2.append(val)
                    lst_spe =[]
                    for i in range (0, len(dico_matieres['spe'])) :
                        val = dico_matieres['spe'][i][0]
                        lst_spe.append(val)
                    txt_lv1 = tk.Label(fr2, text="LV1", font=("Calibri",16), bg="white", fg="black")
                    pso_lv1 = ttk.Combobox(fr2, values=lst_lv1, state="readonly")
                    txt_lv1.grid(row=1)
                    pso_lv1.current(0)                      # Anglais par défaut
                    pso_lv1.grid(row=1, column=1)
                    txt_lv2 = tk.Label(fr2, text="LV2", font=("Calibri",16), bg="white", fg="black")
                    pso_lv2 = ttk.Combobox(fr2, values=lst_lv2, state="readonly")
                    pso_lv2.current(1)                      # Espagnol par défaut
                    txt_lv2.grid(row=2)
                    pso_lv2.grid(row=2, column=1)
                    txt_spe = tk.Label(fr2, text="Spécialité", font=("Calibri",16), bg="white", fg="black")
                    pso_spe = ttk.Combobox(fr2, values=lst_spe, state="readonly")
                    txt_spe.grid(row=3)                     # Pas de spécialité par défaut
                    pso_spe.grid(row=3, column=1)
                    bt_valider = tk.Button(fr3, text='Valider', font = ("Calibri", 15), bg="white", fg="black", command=save_matelv)
                    bt_valider.pack(fill=X)
                    bt_annuler = tk.Button(fr3, text='Annuler', font = ("Calibri", 15), bg="white", fg="black", command=annuler)
                    bt_annuler.pack(fill=X)
                    fen_SaisiePerso.mainloop()
                elif profil == 'Professeur' :
                    for elt in fr2.winfo_children() :                    # RAZ de la fenêtre d'affichage
                        elt.destroy()
                    for elt in fr3.winfo_children() :                    # RAZ de la fenêtre d'affichage
                        elt.destroy()
                    fr2.pack(fill=X)
                    fr3.pack(fill=X)
                    # Saisie des matières enseignées
                    txt_titre = tk.Label(fr2, text="Saisie des matières enseignées", font = ("Calibri", 18), bg="white", fg="black")
                    txt_titre.grid(row=0)
                    # Construction du dictionnaire des matières
                    ## Découpage des entrées de la BDD clé / data (c.a.d. type / matière)
                    data_matieres=open('data/data_matieres.txt','r')
                    dico_matieres = decoup_valtuple (data_matieres)
                    data_matieres.close()
                    # Mise en place des listes de choix des matières
                    txt_com = tk.Label(fr2, text="Matières communes", font = ("Calibri", 15), bg="white", fg="black")
                    pso_com = tk.Listbox(fr2, height=5, selectmode='multiple', exportselection=0)
                    for i in range (0, len(dico_matieres['com'])) :
                        pso_com.insert(i, dico_matieres['com'][i][0])
                    txt_com.grid(row=1, column=0)
                    pso_com.grid(row=2, column=0)
                    txt_lv1 = tk.Label(fr2, text="LV1", font = ("Calibri", 15), bg="white", fg="black")
                    pso_lv1 = tk.Listbox(fr2, height=5, selectmode='multiple', exportselection=0)
                    for i in range (0, len(dico_matieres['lv1'])) :
                        pso_lv1.insert(i, dico_matieres['lv1'][i][0])
                    txt_lv1.grid(row=1, column=1)
                    pso_lv1.grid(row=2, column=1)
                    txt_lv2 = tk.Label(fr2, text="LV2", font = ("Calibri", 15), bg="white", fg="black")
                    pso_lv2 = tk.Listbox(fr2, height=5, selectmode='multiple', exportselection=0)
                    for i in range (0, len(dico_matieres['lv2'])) :
                        pso_lv2.insert(i, dico_matieres['lv2'][i][0])
                    txt_lv2.grid(row=1, column=3)
                    pso_lv2.grid(row=2, column=3)
                    txt_spe = tk.Label(fr2, text="Spécialité", font = ("Calibri", 15), bg="white", fg="black")
                    pso_spe = tk.Listbox(fr2, height=5, selectmode='multiple', exportselection=0)
                    for i in range (0, len(dico_matieres['spe'])) :
                        pso_spe.insert(i, dico_matieres['spe'][i][0])
                    txt_spe.grid(row=1, column=4)
                    pso_spe.grid(row=2, column=4)
                    bt_valider = tk.Button(fr3, text='Valider', font = ("Calibri", 15), bg="white", fg="black", command=save_matprof)
                    bt_valider.pack(fill=X)
                    bt_annuler = tk.Button(fr3, text='Annuler', font = ("Calibri", 15), bg="white", fg="black", command=annuler)
                    bt_annuler.pack(fill=X)
                    fen_SaisiePerso.mainloop()

                else :
                    # Ajout de la nouvelle entrée au dictionnaire
                    ajout_dico (dico_profils, nomps, profil)
                
                    # Sauvegarde du dictionnaire dans le fichier texte
                    bdd = 'data/data_profils.txt'
                    save_valtuple (bdd, dico_profils)
                    save_pwd (nompn, 'ISN_2020')

                    ask = tk.messagebox.askyesno("MERCI", nompn[1]+" "+nompn[0]+" a bien été enregistrée(e) dans la base.\n Souhaitez-vous ajouter une autre personne ?", parent=fen_SaisiePerso)
                    fen_SaisiePerso.destroy()
                    if ask == True :
                        addpers(idusr)                              # retour sur la page d'ajout de personne
                    else :
                        adm.adm_accueil(idusr)                      # retour sur l'accueil d'admin


def retour() :
    global idusr, fen_SaisiePerso
    fen_SaisiePerso.destroy()
    adm.adm_accueil(idusr)

def annuler() :
    global idusr, fen_SaisiePerso
    fen_SaisiePerso.destroy()
    addpers(idusr)



#############################################################
##               PROCESS PROFIL ADMINISTRATIF              ##
#############################################################

def addpers(nmn) :
    global idusr, fen_SaisiePerso, fr1, fr2, fr3, pso_nom, pso_prenom, pso_profil
    idusr = nmn
    ##Saisie nouveau nom
    fen_SaisiePerso = tk.Tk() 
    fen_SaisiePerso.geometry('700x720') # résolution de la fenêtre
    fen_SaisiePerso.title("Visual Note") #titre du logiciel
    fen_SaisiePerso.iconbitmap("img/vn_logo_2.ico") #logo en haut a gauche du logiciel
    fen_SaisiePerso.config(background='white') #couleur du fond

    #creer les boites
    fr1=Frame(fen_SaisiePerso, relief=FLAT, width=600, height=200, bd=0, bg="white")
    fr1.pack(fill=X)
    fr2 = Frame(fen_SaisiePerso, relief=FLAT, width=600, height=385, bd=4)
    fr2.pack(fill=X)
    fr3 = Frame(fen_SaisiePerso, relief=FLAT, width=600, height=100, bd=0, bg="white")
    fr3.pack(fill=X)

    #creation du logo
    image = PhotoImage(file="img/logo_vn.png").zoom(15).subsample(15)#personalisation de l'image en zoomant
    cnvimg = Canvas(fr1, width=600 , height = 180 , bg="white")
    cnvimg.create_image(330, 85, image=image)
    cnvimg.pack(fill=X)

    #Titre
    label_title= Label(fr1, text="Espace Administrateur", font=("Calibri",40),bg="white",fg="black")
    label_title.pack(expand=YES)

    # message de sous-itre
    label_subtitle= Label(fr1, text="Saisie d'une nouvelle personne ", font=("Calibri",25),bg="white",fg="black")
    label_subtitle.pack(expand=YES)

    pso_nom = tk.StringVar()
    pso_profil = tk.StringVar()
    pso_lv1 = tk.StringVar()
    pso_lv2 = tk.StringVar()
    pso_spe = tk.StringVar()

    txt_nom = tk.Label(fr2, text="Nom de la personne", font=("Calibri",16), bg="white", fg="black")
    txt_prenom = tk.Label(fr2, text="Prenom de la personne", font=("Calibri",16), bg="white", fg="black")
    txt_profil = tk.Label(fr2, text="Profil de la personne", font=("Calibri",16), bg="white", fg="black")
    pso_nom = tk.Entry(fr2, textvariable='',width=20)
    pso_prenom = tk.StringVar()
    pso_prenom = tk.Entry(fr2, textvariable='',width=20)
    pso_profil = ttk.Combobox(fr2, values=["Elève", "Professeur", "Administrateur"], state="readonly")
    txt_nom.grid(row=0)
    txt_prenom.grid(row=1)
    txt_profil.grid(row=2)
    pso_nom.grid(row=0, column=1)
    pso_prenom.grid(row=1, column=1)
    pso_profil.grid(row=2, column=1)
    pso_profil.current(0)

    bt_valider = tk.Button(fr3, text='Valider', font = ("Calibri", 15), bg="white", fg="black", command=checkpers)
    bt_valider.pack(fill=X)
    bt_retour = tk.Button(fr3, text='Retour', font = ("Calibri", 15), bg="white", fg="black", command=retour)
    bt_retour.pack(fill=X)

    fen_SaisiePerso.mainloop()