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

def retour() :
    global idusr, fen_SupMat
    fen_SupMat.destroy()
    adm.adm_accueil(idusr)

def choix_mat(event) :
    global idusr, fen_SupMat, fr1, fr2, fr21, fr22, mat_type, mat_mat
    sm = mat_type.get()
    if sm == 'Matière Commune' :
        nt = 'com'
    elif sm == 'Spécialité' :
        nt = 'spe'
    else :
        nt = sm.lower()

    data_matieres=open('data/data_matieres.txt','r')
    dico_matieres = gen.decoup_valtuple (data_matieres)
    data_matieres.close()

    list_mat = []
    for i in range (0, len(dico_matieres[nt])) :
        list_mat.append(dico_matieres[nt][i][0])
    list_mat.sort()

    # Affichage combobox utilisateurs
    mat_mat = ttk.Combobox(fr22, values=list_mat, state="readonly")
    mat_mat.grid(row=0, column=1)


def check_supMat() :
    global idusr, fen_SupMat, mat_type, mat_mat
    sup_mat = mat_mat.get()
    nt = mat_type.get()

    if sup_mat == '' or nt == '' :
        ask = tk.messagebox.showwarning("ATTENTION", "Tous les champs doivent être remplis.\nMerci de corriger.", parent=fen_SupMat)
    else :
        data_not = open ('data/data_notes.txt', 'r')     
        dico_not = gen.decoup_valtuple (data_not)
        data_not.close()
        xy = 'ok'
        for k in dico_not :
            for i in range (0, len(dico_not[k])) :
                if dico_not[k][i][0] == sup_mat :
                    xy = 'ko' 
        if xy != 'ko' :
            ask = tk.messagebox.askyesno("ATTENTION", "Cette opération va supprimer la matière dans TOUTES les bases de données.\nÊtes-vous sûr(e) de vouloir continuer ?", parent=fen_SupMat)
            if ask == True :
                # Suppression de l'utilisateur de la base data_com, data_lv1, data_lv2, data_spe
                if nt == 'Matière Commune' :
                    sup_type = 'com'
                elif nt == 'Spécialité' :
                    sup_type = 'spe'
                else :
                    sup_type = nt.lower()

                tp = 'data/data_' + sup_type + '.txt'
                data_typ = open (tp, 'r')     
                dico_typ = gen.decoup_valtuple (data_typ)
                data_typ.close()

                if sup_mat in dico_typ.keys() :
                    del dico_typ[sup_mat]
                    bdd = 'data/data_' + sup_type + '.txt'
                    gen.save_valtuple (bdd, dico_typ)
            
                # Suppression de l'utilisateur de la base data_matieres
                data_matieres=open('data/data_matieres.txt','r')
                dico_matieres = gen.decoup_valtuple (data_matieres)
                data_matieres.close()
                LM = dico_matieres[sup_type].copy()
                for i in range (0, len(dico_matieres[sup_type])) :
                    if dico_matieres[sup_type][i][0] == sup_mat :
                        LM.remove(dico_matieres[sup_type][i])
                del dico_matieres[sup_type]
                dico_matieres[sup_type] = LM
                bdd = 'data/data_matieres.txt'
                gen.save_valtuple (bdd, dico_matieres)
                ask = tk.messagebox.askyesno("MERCI", "Cette matière a bien été supprimée.\n Souhaitez-vous en supprimer une autre ?", parent=fen_SupMat)
                fen_SupMat.destroy()
                if ask == True :
                    del_mat(idusr)                              # retour sur la page d'ajout de personne
                else :
                    adm.adm_accueil(idusr)                      # retour sur l'accueil d'admin
        else :
            tk.messagebox.showerror("ERREUR", "Des élèves ont des notes dans cette matière.\nVous devez retirer les notes AVANT de supprimer une matière.", parent=fen_SupMat)










#############################################################
##               PROCESS PROFIL ADMINISTRATIF              ##
#############################################################

def del_mat (nmn) :
    global fen_SupMat, idusr,fr1, fr2, fr21, fr22, mat_mat, mat_type
    idusr = nmn

    ##Saisie nouveau nom
    fen_SupMat = tk.Tk() 
    fen_SupMat.title("Visual Note") # titre du logiciel
    fen_SupMat.geometry("700x720") # résolution de la fenetre
    fen_SupMat.iconbitmap("img/vn_logo_2.ico") # logo en haut à gauche du logiciel
    fen_SupMat.config(background='white') # couleur du fond

    # créer les boîtes
    fr1=Frame(fen_SupMat, relief=FLAT, width=540, height=200, bd=0, bg="white")
    fr1.pack(fill=X)
    fr2 = Frame(fen_SupMat, relief=FLAT, width=540, height=385, bd=0, bg="white")
    fr2.pack(fill=X)
    fr21 = Frame(fr2, relief=FLAT, width=540, height=120, bd=0)
    fr21.pack(fill=X)
    fr22 = Frame(fr2, relief=FLAT, width=540, height=120, bd=0)
    fr22.pack(fill=X)
    fr3 = Frame(fen_SupMat, relief=FLAT, width=540, height=100, bd=0, bg="white")
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
    label_subtitle= Label(fr1, text="Supression d'une matière", font=("Calibri",25),bg="white",fg="black")
    label_subtitle.pack(expand=YES)

    # Liste des profils
    txt_type = tk.Label(fr21, text="Type de matière", font=("Calibri",16), bg="white", fg="black", width = 20)
    mat_type = ttk.Combobox(fr21, values=['Matière Commune', 'LV1', 'LV2', 'Spécialité'], state="readonly")
    txt_type.grid(row=0)
    mat_type.grid(row=0, column=1)
    mat_type.bind("<<ComboboxSelected>>", choix_mat)

    # Choix de l'utilisateur
    txt_mat = tk.Label(fr22, text="Matière à supprimer", font=("Calibri",16), bg="white", fg="black", width = 20)
    mat_mat = ttk.Combobox(fr22, values='', state="disabled")
    txt_mat.grid(row=0)
    mat_mat.grid(row=0, column=1)

    # Boutons de validation et retour
    bt_valider = tk.Button(fr3, text='Valider', font = ("Calibri", 15), bg="white", fg="black", command=check_supMat)
    bt_valider.pack(fill=X)
    bt_retour = tk.Button(fr3, text='Retour', font = ("Calibri", 15), bg="white", fg="black", command=retour)
    bt_retour.pack(fill=X)


    fen_SupMat.mainloop()