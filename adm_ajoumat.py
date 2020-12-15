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
    global idusr, fen_SaisieMat
    fen_SaisieMat.destroy()
    adm.adm_accueil(idusr)

def check_num (ch) :
    global idusr, fen_SaisieMat
    num = ['1','2','3','4','5','6','7','8','9', '0']
    
    msg = 'ok'
    for i in range (0, len(ch)) :
        if ch[i] not in num :
            msg = 'Merci de saisir un coeffficient valide (entier numérique).'
    return (msg)

def check_alpha (ch) :
    global idusr, fen_SaisiePerso
    alpha_min = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','à','â','é','è','ë','ê','ô','ï','î','ç',' ']
    alpha_maj = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    msg = 'ok'
    chsp = ch.split('-')
    if chsp[0][0] not in alpha_maj :
        msg = 'Les initiales doivent être en majuscule.\nMerci de corriger.'
    elif len (chsp) == 1 :
        for i in range (1, len(chsp[0])) :
            if chsp[0][i] not in alpha_min and chsp[0][i] not in alpha_maj :
                msg = 'Merci de ne saisir que des caractères alphabétiques.'
    else :
            if chsp[1][0] not in alpha_maj :
                msg = 'Les initiales doivent être en majuscule.\nMerci de corriger.'      
            else :
                for i in range (1, len(chsp[1])) :
                    if chsp[1][i] not in alpha_min and chsp[1][i] not in alpha_maj :
                        msg = 'Merci de ne saisir que des caractères alphabétiques.'
    return (msg)


def checkmat() :
    global idusr, fen_SaisieMat, mat_coef, mat_nom, mat_prf
    chm_nom = mat_nom.get()
    chm_prf = mat_prf.get()
    chm_coef = mat_coef.get()
    
    ## Découpage des entrées de la BDD (mots de passe) clé / data (élève / notes et arguments)
    data_matieres=open('data/data_matieres.txt','r')
    dico_matieres = gen.decoup_valtuple (data_matieres)
    data_matieres.close()

    LM = []
    for k in dico_matieres :
        for i in range (0, len(dico_matieres[k])) :
            LM.append(dico_matieres[k][i][0])
        
    if chm_nom == '' or chm_prf == '' or chm_coef == '' :
        tk.messagebox.showwarning('ATTENTION', 'Tous les champs doivent être remplis !\nMerci de corriger.', parent = fen_SaisieMat)
    else :
        ret = check_num (chm_coef)
        res = check_alpha (chm_nom)
        if ret != 'ok' :
            tk.messagebox.showwarning('ATTENTION', ret, parent = fen_SaisieMat)
        elif int(chm_coef) < 1 or int(chm_coef) > 20 :
            tk.messagebox.showwarning('ATTENTION', 'Merci de saisir un coeffficient valide (compris entre 1 et 20).', parent = fen_SaisieMat)
        elif res != 'ok' :
            tk.messagebox.showwarning('ATTENTION', res, parent = fen_SaisieMat)
        elif chm_nom in LM :
            tk.messagebox.showwarning('ATTENTION', 'Cette matière existe déjà.\nMerci de corriger.', parent = fen_SaisieMat)
        else :
            if chm_prf == 'Matière Commune' :
                key = 'com'
            elif chm_prf == 'LV1' :
                key = 'lv1'
            elif chm_prf == 'LV2' :
                key = 'lv2'
            else :
                key = 'spe'
            
            val = [chm_nom, chm_coef]

            # Ajout des nouvelles entrées au dictionnaire Matières
            gen.ajout_dico(dico_matieres, val, key)
            # Sauvegarde des dictionnaires dans le fichier texte
            bdd = 'data/data_matieres.txt'
            gen.save_valtuple (bdd, dico_matieres)
            ask = tk.messagebox.askyesno("MERCI", "Cette matière a bien été ajoutée.\nSouhaitez-vous en ajouter une autre ?", parent=fen_SaisieMat)
            fen_SaisieMat.destroy()
            if ask == True :
                addmat(idusr)                              # retour sur la page d'ajout de personne
            else :
                adm.adm_accueil(idusr)                      # retour sur l'accueil d'admin





#############################################################
##               PROCESS PROFIL ADMINISTRATIF              ##
#############################################################

def addmat (nmn) :
    global fen_SaisieMat, idusr, mat_prf, mat_nom, mat_coef
    idusr = nmn

    ##Saisie nouveau nom
    fen_SaisieMat = tk.Tk() 
    fen_SaisieMat.title("Visual Note") # titre du logiciel
    fen_SaisieMat.geometry("700x720") # resolution de la fenetre
    fen_SaisieMat.iconbitmap("img/vn_logo_2.ico") # logo en haut a gauche du logiciel
    fen_SaisieMat.config(background='white') # couleur du fond

    #creer les boites
    fr1=Frame(fen_SaisieMat, relief=FLAT, width=540, height=200, bd=0, bg="white")
    fr1.pack(fill=X)
    fr2 = Frame(fen_SaisieMat, relief=FLAT, width=540, height=385, bd=4)
    fr2.pack(fill=X)
    fr3 = Frame(fen_SaisieMat, relief=FLAT, width=540, height=100, bd=0, bg="white")
    fr3.pack(fill=X)

    #creation du logo
    image = PhotoImage(file="img/logo_vn.png").zoom(15).subsample(15)   # personalisation de l'image en zoomant
    cnvimg = Canvas(fr1, width=600 , height = 180 , bg="white")
    cnvimg.create_image(330, 85, image=image)
    cnvimg.pack(fill=X)

    #Titre
    label_title= Label(fr1, text="Espace Administrateur", font=("Calibri",40),bg="white",fg="black")
    label_title.pack(expand=YES)

    # message de sous-itre
    label_subtitle= Label(fr1, text="Saisie d'une nouvelle matière ", font=("Calibri",25),bg="white",fg="black")
    label_subtitle.pack(expand=YES)

    mat_nom = tk.StringVar()
    mat_coef = tk.StringVar()

    txt_nom = tk.Label(fr2, text="Intitulé de la matière", font=("Calibri",16), bg="white", fg="black", width=22)
    mat_nom = tk.Entry(fr2, textvariable='',width=20)
    txt_nom.grid(row=0, column=0)
    mat_nom.grid(row=0, column=1)

    txt_prf = tk.Label(fr2, text="Type de matière", font=("Calibri",16), bg="white", fg="black", width=22)
    mat_prf = ttk.Combobox(fr2, values=["Matière Commune", "LV1", "LV2", "Spécialité"], state="readonly")
    mat_prf.current(0)
    txt_prf.grid(row=1, column=0)
    mat_prf.grid(row=1, column=1)

    txt_coef = tk.Label(fr2, text="Coefficient de la matière", font=("Calibri",16), bg="white", fg="black", width=22)
    mat_coef = tk.Entry(fr2, textvariable='',width=3)
    txt_coef.grid(row=2, column=0)
    mat_coef.grid(row=2, column=1)

    bt_valider = tk.Button(fr3, text='Valider', font = ("Calibri", 15), bg="white", fg="black", command=checkmat)
    bt_valider.pack(fill=X)
    bt_retour = tk.Button(fr3, text='Retour', font = ("Calibri", 15), bg="white", fg="black", command=retour)
    bt_retour.pack(fill=X)

    fen_SaisieMat.mainloop()