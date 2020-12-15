# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from fn_generic import *
import fn_generic as gen
import prf_main as prf





#############################################################
##               FONCTIONS PROFIL PROFESSEUR               ##
#############################################################



def retour() :
    global idusr, fen_SupprNote
    fen_SupprNote.destroy()
    prf.prf_accueil(idusr)


# Fonction de construction et affichage de la combobox 'Matières' en fonction de l'élève
def choix_mat(event) :
    global idusr, not_nom, not_mat, fen_SupprNote, fr22, fr23
    sn = not_nom.get()
    sup_nom = sn.split(' ')
    list_mat = []

    data_matieres = open('data/data_matieres.txt','r')
    dico_matieres = gen.decoup_valtuple (data_matieres)
    data_matieres.close()
    for i in range (0, len(dico_matieres['com'])) :     # Ajout des matières communes dans la liste
        val = dico_matieres['com'][i][0]
        list_mat.append(val)
        data_lv1 = open('data/data_lv1.txt','r')
    data_lv1 = open('data/data_lv1.txt','r')
    dico_lv1 = gen.decoup_valtuple (data_lv1)
    data_lv1.close()
    for k in dico_lv1 :                                 # Ajout des LV1 dans la liste
        for i in range (0, len(dico_lv1[k])) :
            v = dico_lv1[k][i]
            if v == sup_nom :
                key = k + ' LV1'
                list_mat.append(key)
    data_lv2=open('data/data_lv2.txt','r')
    dico_lv2 = gen.decoup_valtuple (data_lv2)
    data_lv2.close()
    for k in dico_lv2 :                                 # Ajout des LV2 dans la liste
        for i in range (0, len(dico_lv2[k])) :
            v = dico_lv2[k][i]
            if v == sup_nom :
                key = k + ' LV2'
                list_mat.append(key)
    data_spe=open('data/data_spe.txt','r')
    dico_spe = gen.decoup_valtuple (data_spe)
    data_spe.close()
    for k in dico_spe :                                 # Ajout des Spécialités dans la liste
        for i in range (0, len(dico_spe[k])) :
            v = dico_spe[k][i]
            if v == sup_nom :
                key = k + ' SPE'
                list_mat.append(key)
    fr23.pack(fill=X)
    not_not = ttk.Combobox(fr23, values='', state="disabled", width=35)
    not_not.grid(row=0, column=1)
    fr22.pack(fill=X)
    not_mat = ttk.Combobox(fr22, values=list_mat, state="readonly")
    not_mat.grid(row=0, column=1)
    not_mat.bind("<<ComboboxSelected>>", choix_not)
    fen_SupprNote.mainloop()

# Fonction de construction et affichage de la combobox 'Notes' en fonction de l'élève et de la matière
def choix_not(event) :
    global idusr, fen_SupprNote, fr22, fr23, not_nom, not_mat, not_not
    snm = not_nom.get()
    sup_nom = snm.split(' ')
    snm = not_mat.get()
    if snm.endswith('LV1') == True or snm.endswith('LV2') == True or snm.endswith('SPE') == True :
        sup_mat = snm[:len(snm)-4]
    else :
        sup_mat = snm
    L1 = []
    L2 = []
    list_not = []

    data_notes=open('data/data_notes.txt','r')
    dico_notes = gen.decoup_cletuple (data_notes)
    data_notes.close()

    if tuple(sup_nom) not in dico_notes :
        tk.messagebox.showinfo("MAUVAIS CHOIX", snm + " n'a aucune note en " + sup_mat + '.')
    else :
        L1 = dico_notes[tuple(sup_nom)].split('|')
        for i in range (0, len(L1)) :
            L2 = L1[i].split(';')
            if L2[0] == sup_mat :
                val = L2[5] + ' : ' + L2[1] + '/' + L2[2] + ' (coef ' + L2[3] + ' - ' + L2[4] + ')'
                list_not.append(val)
        fr23.pack(fill=X)
        not_not = ttk.Combobox(fr23, values=list_not, state="readonly", width=35)
        not_not.grid(row=0, column=1)
    fen_SupprNote.mainloop()

# Fonction de sauvegarde du dictionnaire de notes SANS la valeur supprimée
def save_supnot() :
    global idusr, fen_SupprNote, not_nom, not_mat, not_not
    snm = not_nom.get()
    sup_nom = snm.split(' ')
    snm = not_mat.get()
    if snm.endswith('LV1') == True or snm.endswith('LV2') == True or snm.endswith('SPE') == True :
        sup_mat = snm[:len(snm)-4]
    else :
        sup_mat = snm
    snt0 = not_not.get()
    snt1 = snt0.split(' : ')
    snt2 = snt1[1].split('/')
    snt3 = snt2[1].split(' (coef ')
    snt4 = snt3[1].split(' - ')
    snt5 = snt4[1]
    snt5 = snt5[:len(snt5)-1]
    sup_not = [sup_mat, snt2[0], snt3[0], snt4[0], snt5, snt1[0]]

    data_notes=open('data/data_notes.txt','r')
    dico_notes = gen.decoup_cletvalt (data_notes)
    data_notes.close()
    LN = dico_notes[tuple(sup_nom)]
    LN.remove(sup_not)
    del dico_notes[tuple(sup_nom)]
    dico_notes[tuple(sup_nom)] = LN   
    
    bdd = 'data/data_notes.txt'
    gen.save_cletvalt (bdd, dico_notes)
    ask = tk.messagebox.askyesno("MERCI", "Cette note a bien été supprimée.\n Souhaitez-vous en supprimer une autre ?", parent=fen_SupprNote)
    fen_SupprNote.destroy()
    if ask == True :
        del_note(idusr)                              # retour sur la page d'ajout de personne
    else :
        prf.prf_accueil(idusr)                      # retour sur l'accueil d'admin

    




#############################################################
##                PROCESS PROFIL PROFESSEUR                ##
#############################################################


def del_note (nmn) :
    global idusr, fen_SupprNote, not_nom, not_mat, not_max, not_coef, not_type, not_not, fr1, fr2, fr21, fr22, fr23, fr3 
    idusr = nmn
    ##Saisie nouveau nom
    fen_SupprNote = tk.Tk() 
    fen_SupprNote.title("Visual Note") #titre du logiciel
    fen_SupprNote.geometry("700x720") #resolution de la fenetre
    fen_SupprNote.iconbitmap("img/vn_logo_2.ico") #logo en haut a gauche du logiciel
    fen_SupprNote.config(background='white') #couleur du fond

    #creer les boites
    fr1=Frame(fen_SupprNote, relief=FLAT, width=540, height=200, bd=0, bg="white")
    fr1.pack(fill=X)
    fr2 = Frame(fen_SupprNote, relief=FLAT, width=540, height=385, bd=0)
    fr2.pack(fill=X)
    fr21 = Frame(fr2, relief=FLAT, width=540, height=120, bd=0)
    fr21.pack(fill=X)
    fr22 = Frame(fr2, relief=FLAT, width=540, height=120, bd=0)
    fr22.pack(fill=X)
    fr23 = Frame(fr2, relief=FLAT, width=540, height=120, bd=0)
    fr23.pack(fill=X)
    fr3 = Frame(fen_SupprNote, relief=FLAT, width=540, height=100, bd=0, bg="white")
    fr3.pack(fill=X)

    #creation du logo
    image = PhotoImage(file="img/logo_vn.png").zoom(15).subsample(15)   #personalisation de l'image en zoomant
    cnvimg = Canvas(fr1, width=600 , height = 180 , bg="white")
    cnvimg.create_image(330, 85, image=image)
    cnvimg.pack(fill=X)

    #Titre
    label_title= Label(fr1, text="Espace Professeur", font=("Calibri",40),bg="white",fg="black")
    label_title.pack(expand=YES)

    # message de sous-titre
    label_subtitle= Label(fr1, text="Supression d'une note ", font=("Calibri",25),bg="white",fg="black")
    label_subtitle.pack(expand=YES)


    # Création de la liste des élèves
    data_profil = open('data/data_profils.txt','r')
    dico_profil = gen.decoup_valtuple (data_profil)
    data_profil.close()
    list_noms = []
    list_mat = []
    list_not = []

    for i in range (0, len(dico_profil['Elève'])) :
        val = dico_profil['Elève'][i][0]+" "+dico_profil['Elève'][i][1]
        list_noms.append(val)
    list_noms.sort()
    # Choix de l'élève
    txt_nom = tk.Label(fr21, text="Nom de l'élève", font=("Calibri",16), bg="white", fg="black")
    not_nom = ttk.Combobox(fr21, values=list_noms, state="readonly")
    txt_nom.grid(row=0)
    not_nom.grid(row=0, column=1)
    not_nom.bind("<<ComboboxSelected>>", choix_mat)

    # Choix de la matière
    txt_mat = tk.Label(fr22, text="Matière", font=("Calibri",16), bg="white", fg="black")
    not_mat = ttk.Combobox(fr22, values=list_mat, state="disabled")
    txt_mat.grid(row=0)
    not_mat.grid(row=0, column=1)

    # Choix de la note à supprimer
    list_not = []
    txt_not = tk.Label(fr23, text="Note à supprimer", font=("Calibri",16), bg="white", fg="black")
    not_not = ttk.Combobox(fr23, values=list_not, state="disabled", width=35)
    txt_not.grid(row=0)
    not_not.grid(row=0, column=1)

    # Boutons de validation et retour
    bt_valider = tk.Button(fr3, text='Valider', font = ("Calibri", 15), bg="white", fg="black", command=save_supnot)
    bt_valider.pack(fill=X)
    bt_retour = tk.Button(fr3, text='Retour', font = ("Calibri", 15), bg="white", fg="black", command=retour)
    bt_retour.pack(fill=X)

    fen_SupprNote.mainloop()