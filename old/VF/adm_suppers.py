# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from fn_generic import *
import fn_generic as gen
import adm_main as adm



#############################################################
##              FONCTIONS PROFIL ADMINISTRATIF             ##
#############################################################



def retour() :
    global idusr, fen_SupprPers
    fen_SupprPers.destroy()
    adm.adm_accueil(idusr)

def choix_pers(event) :
    global idusr, fen_SupprPers, fr1, fr2, fr21, fr22, usr_nom, usr_profil
    sp = usr_profil.get()
    data_profils=open('data/data_profils.txt','r')
    dico_profils = gen.decoup_valtuple (data_profils)
    data_profils.close()

    list_usr = dico_profils[sp]
    list_usr.sort()

    # Affichage combobox utilisateurs
    usr_nom = ttk.Combobox(fr22, values=list_usr, state="readonly")
    usr_nom.grid(row=0, column=1)

def save_suppers() :
    global idusr, fen_SupprPers, usr_nom, usr_profil
    spn = usr_nom.get()
    sup_usr = spn.split(' ')
    sup_profil = usr_profil.get()

    # Suppression de l'utilisateur de la base data_profils
    data_profils=open('data/data_profils.txt','r')
    dico_profils = gen.decoup_valtuple (data_profils)
    data_profils.close()
    LU = dico_profils[sup_profil]
    LU.remove(sup_usr)
    del dico_profils[sup_profil]
    dico_profils[sup_profil] = LU
    bdd = 'data/data_profils.txt'
    gen.save_valtuple (bdd, dico_profils)

    # Suppression de l'utilisateur de la base data_pass
    data_pass=open('data/data_pass.txt','r')
    dico_pass = gen.decoup_cletuple (data_pass)
    data_pass.close()
    del dico_pass[tuple(sup_usr)]
    bdd = 'data/data_pass.txt'
    gen.save_cletuple (bdd, dico_pass)

    # Suppression des notes de l'utilisateur dans data_notes
    data_notes=open('data/data_notes.txt','r')
    dico_notes = gen.decoup_cletvalt (data_notes)
    data_notes.close()
    if tuple(sup_usr) in dico_notes :
        del dico_notes[tuple(sup_usr)]
        bdd = 'data/data_notes.txt'
        gen.save_cletvalt (bdd, dico_notes)

    # Suppression de l'utilisateur de la base data_LV1
    data_lv1 = open('data/data_lv1.txt','r')
    dico_lv1 = gen.decoup_valtuple (data_lv1)
    dico_oldlv1 = dico_lv1.copy()
    data_lv1.close()
    for k in dico_oldlv1 :
        L1 = dico_lv1[k]
        if sup_usr in L1 :
            sup_lv1 = k
            LLV1 = dico_lv1[sup_lv1]
            LLV1.remove(sup_usr)
            del dico_lv1[sup_lv1]
            dico_lv1[sup_lv1] = LLV1
            bdd = 'data/data_lv1.txt'
            gen.save_valtuple (bdd, dico_lv1)

    # Suppression de l'utilisateur de la base data_LV2
    data_lv2=open('data/data_lv2.txt','r')
    dico_lv2 = gen.decoup_valtuple (data_lv2)
    dico_oldlv2 = dico_lv2.copy()
    data_lv2.close()
    for k in dico_oldlv2 :
        L2 = dico_lv2[k]
        if sup_usr in L2 :
            sup_lv2 = k
            LLV2 = dico_lv2[sup_lv2]
            LLV2.remove(sup_usr)
            del dico_lv2[sup_lv2]
            dico_lv2[sup_lv2] = LLV2
            bdd = 'data/data_lv2.txt'
            gen.save_valtuple (bdd, dico_lv2)

    # Suppression de l'utilisateur de la base data_SPE
    data_spe=open('data/data_spe.txt','r')
    dico_spe = gen.decoup_valtuple (data_spe)
    dico_oldspe = dico_spe.copy()
    data_spe.close()
    for k in dico_oldspe :
        LS = dico_spe[k]
        if sup_usr in LS :
            sup_spe = k
            LSPE = dico_spe[sup_spe]
            LSPE.remove(sup_usr)
            del dico_spe[sup_spe]
            dico_spe[sup_spe] = LSPE
            bdd = 'data/data_spe.txt'
            gen.save_valtuple (bdd, dico_spe)

    # Suppression de l'utilisateur (Professeur exclusivement) de la base data_com
    data_com=open('data/data_com.txt','r')
    dico_com = gen.decoup_valtuple (data_com)
    dico_oldcom = dico_com.copy()
    data_com.close()
    for k in dico_oldcom :
        LC = dico_com[k]
        if sup_usr in LC :
            sup_com = k
            LCOM = dico_com[sup_com]
            LCOM.remove(sup_usr)
            del dico_com[sup_com]
            dico_com[sup_com] = LCOM
            bdd = 'data/data_com.txt'
            gen.save_valtuple (bdd, dico_com)


    ask = tk.messagebox.askyesno("MERCI", "Cet utilisateur a bien été supprimé.\n Souhaitez-vous en supprimer un autre ?", parent=fen_SupprPers)
    fen_SupprPers.destroy()
    if ask == True :
        del_perso(idusr)                              # retour sur la page d'ajout de personne
    else :
        adm.adm_accueil(idusr)                      # retour sur l'accueil d'admin

def check_suppers() :
    global idusr, fen_SupprPers, usr_nom, usr_profil
    spn = usr_nom.get()
    sup_usr = spn.split(' ')

    if sup_usr == idusr :
        tk.messagebox.showwarning("ATTENTION", "Vous ne pouvez pas vous supprimer vous-même", parent=fen_SupprPers)
        fen_SupprPers.mainloop()
    else :
        ask = tk.messagebox.askyesno("ATTENTION", "Cet opération va supprimer toute référence (notes et autres) à " + spn + " dans la base de données.\nÊtes vous sûr de vouloir continuer ?", parent=fen_SupprPers)
        if ask == True :
            save_suppers()                              # Fin de l'opération (suppression de l'utilisateur dans toutes les BDD)
        else :
            fen_SupprPers.destroy()
            del_perso(idusr)                            # retour sur la page de suppression d'utilisateur
    


#############################################################
##                PROCESS PROFIL PROFESSEUR                ##
#############################################################


def del_perso (nmn) :
    global idusr, fen_SupprPers, fr1, fr2, fr21, fr22, fr23, fr3 , usr_nom, usr_profil
    idusr = nmn

    ## Saisie nouveau nom
    fen_SupprPers = tk.Tk() 
    fen_SupprPers.title("Visual Note") #titre du logiciel
    fen_SupprPers.geometry("700x720") #resolution de la fenetre
    fen_SupprPers.iconbitmap("img/vn_logo_2.ico") #logo en haut a gauche du logiciel
    fen_SupprPers.config(background='white') #couleur du fond

    # créer les boîtes
    fr1=Frame(fen_SupprPers, relief=FLAT, width=540, height=200, bd=0, bg="white")
    fr1.pack(fill=X)
    fr2 = Frame(fen_SupprPers, relief=FLAT, width=540, height=385, bd=0, bg="white")
    fr2.pack(fill=X)
    fr21 = Frame(fr2, relief=FLAT, width=540, height=120, bd=0)
    fr21.pack(fill=X)
    fr22 = Frame(fr2, relief=FLAT, width=540, height=120, bd=0)
    fr22.pack(fill=X)
    fr3 = Frame(fen_SupprPers, relief=FLAT, width=540, height=100, bd=0, bg="white")
    fr3.pack(fill=X)

    # Création du logo
    image = PhotoImage(file="img/logo_vn.png").zoom(15).subsample(15)
    cnvimg = Canvas(fr1, width=600 , height = 180 , bg="white")
    cnvimg.create_image(330, 85, image=image)
    cnvimg.pack(fill=X)

    # Titre
    label_title= Label(fr1, text="Espace Administrateur", font=("Calibri",40), bg="white", fg="black")
    label_title.pack(expand=YES)

    # Message de sous-titre
    label_subtitle= Label(fr1, text="Supression d'un utilisateur ", font=("Calibri",25),bg="white",fg="black")
    label_subtitle.pack(expand=YES)

    # Liste des profils
    txt_profil = tk.Label(fr21, text="Profil de l'utilisateur", font=("Calibri",16), bg="white", fg="black", width = 20)
    usr_profil = ttk.Combobox(fr21, values=['Elève', 'Professeur', 'Administrateur'], state="readonly")
    txt_profil.grid(row=0)
    usr_profil.grid(row=0, column=1)
    usr_profil.bind("<<ComboboxSelected>>", choix_pers)

    # Choix de l'utilisateur
    txt_nom = tk.Label(fr22, text="Nom de l'utilisateur", font=("Calibri",16), bg="white", fg="black", width = 20)
    usr_nom = ttk.Combobox(fr22, values='', state="disabled")
    txt_nom.grid(row=0)
    usr_nom.grid(row=0, column=1)

    # Boutons de validation et retour
    bt_valider = tk.Button(fr3, text='Valider', font = ("Calibri", 15), bg="white", fg="black", command=check_suppers)
    bt_valider.pack(fill=X)
    bt_retour = tk.Button(fr3, text='Retour', font = ("Calibri", 15), bg="white", fg="black", command=retour)
    bt_retour.pack(fill=X)


    fen_SupprPers.mainloop()