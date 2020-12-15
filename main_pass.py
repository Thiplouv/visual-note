# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import fn_generic as gen
import elv_main as elv
import prf_main as prf
import adm_main as adm



def retour() :
    global idusr, fen_ChgPass, pfs
    fen_ChgPass.destroy()
    if pfs == 'Elève' :
        elv.elv_accueil(idusr)
    elif pfs == 'Professeur' :
        prf.prf_accueil(idusr)
    else :
        adm.adm_accueil(idusr)

def checkpass() :
    global idusr, fen_ChgPass, ch_mdpold, ch_mdpn1, ch_mdpn2, pfs
    mdpold = ch_mdpold.get()
    mdpn1 = ch_mdpn1.get()
    mdpn2 = ch_mdpn2.get()

    # Construction du dictionnaire de tous les profils
    ## Découpage des entrées de la BDD clé / data (c.a.d. profil / nom-prénom)
    data_pass=open('data/data_pass.txt','r')
    dico_pass = gen.decoup_cletuple(data_pass)
    data_pass.close()

    if mdpold != dico_pass[tuple(idusr)] :
        tk.messagebox.showerror("ATTENTION", "Vous avez fait une erreur dans votre mot de passe actuel.\nMerci de le re-saisir.")
        fen_ChgPass.mainloop()
    elif mdpn1 != mdpn2 :
        tk.messagebox.showerror("ATTENTION", "Les deux mots de passe ne correspondent pas.\nMerci de les re-saisir.")
        fen_ChgPass.mainloop()
    elif mdpold == mdpn1 :
        tk.messagebox.showerror("ERREUR", "Vous ne pouvez pas re-saisir votre ancien mot de passe.\nMerci de corriger.")
        fen_ChgPass.mainloop()
    else :
        dico_pass[tuple(idusr)] = [mdpn1] 
        bdd = 'data/data_pass.txt'
        gen.save_cletuple (bdd, dico_pass)
        tk.messagebox.showinfo("Succès", "Votre nouveau mot de passe a bien été pris en compte.")
        retour()



def chg_pass(n) :
    global idusr, fen_ChgPass, ch_mdpold, ch_mdpn1, ch_mdpn2, pfs

    idusr = n

    # Détermination du profil de l'utilisateur
    data_profils=open('data/data_profils.txt','r')
    dico_profils = gen.decoup_valtuple(data_profils)
    data_profils.close()
    data_pass=open('data/data_pass.txt','r')
    dico_pass = gen.decoup_cletuple(data_pass)
    data_pass.close()
    L1 = []
    L2 = []
    for key in dico_pass.keys() :
        L1 = [key[0], key[1], dico_pass[key]]
        L2.append(L1)
    pfs = gen.find_key (idusr, dico_profils)

    # Affichage de la fenêtre
    fen_ChgPass = tk.Tk()

    fen_ChgPass.title("Visual Note") #titre du logiciel
    fen_ChgPass.geometry("700x720") #resolution de la fenetre
    fen_ChgPass.iconbitmap("img/vn_logo_2.ico") #logo en haut a gauche du logiciel
    fen_ChgPass.config(background='white') #couleur du fond

    ## creer les boites
    fr1=Frame(fen_ChgPass, relief=FLAT, width=540, height=200, bd=0, bg="white")
    fr1.pack(fill=X)
    fr2 = Frame(fen_ChgPass, relief=FLAT, width=540, height=385, bd=0)
    fr2.pack(fill=X)
    fr3 = Frame(fen_ChgPass, relief=FLAT, width=540, height=100, bd=0, bg="white")
    fr3.pack(fill=X)

    ## création du logo
    image = PhotoImage(file="img/logo_vn.png").zoom(15).subsample(15)       #personalisation de l'image en zoomant
    cnvimg = Canvas(fr1, width=600 , height = 180 , bg="white")
    cnvimg.create_image(330, 85, image=image)
    cnvimg.pack(fill=X)

    ## Titre
    label_title= Label(fr1, text="Espace "+pfs, font=("Calibri",40),bg="white",fg="black")
    label_title.pack(expand=YES)

    ## message de sous-titre
    label_subtitle = Label(fr1, text="Modification du mot de passe", font=("Calibri",25),bg="white",fg="black")
    label_subtitle.pack(expand=YES)

    ## Mot de passe actuel
    txt_mdpold = tk.Label(fr2, text="Mot de passe actuel", font=("Calibri",25),bg="white",fg="black")
    ch_mdpold = tk.Entry(fr2, show='*', textvariable='', width=45)
    txt_mdpold.grid(row=0, column=0)
    ch_mdpold.grid(row=0, column=1)
    txt_mdpold = tk.Label(fr2, text="", bg="white",fg="black")              # ligne vide (saut de ligne)
    txt_mdpold.grid(row=1)

    ## Nouveau mot de passe
    txt_mdpn1 = tk.Label(fr2, text="Nouveau mot de passe", font=("Calibri",25),bg="white",fg="black")
    ch_mdpn1 = tk.Entry(fr2, show='*', textvariable='', width=45)
    txt_mdpn1.grid(row=2, column=0)
    ch_mdpn1.grid(row=2, column=1)
    txt_mdpn2 = tk.Label(fr2, text="Saisissez-le à nouveau", font=("Calibri",25),bg="white",fg="black")
    ch_mdpn2 = tk.Entry(fr2, show='*', textvariable='', width=45)
    txt_mdpn2.grid(row=3, column=0)
    ch_mdpn2.grid(row=3, column=1)

    # Boutons de validation et sortie
    bt_valid = tk.Button(fr3, text='Valider', font = ("Calibri", 15), bg="white", fg="black", command=checkpass)
    bt_valid.pack(fill=X)
    bt_retour = tk.Button(fr3, text='Retour', font = ("Calibri", 15), bg="white", fg="black", command=retour)
    bt_retour.pack(fill=X)


    fen_ChgPass.mainloop()
