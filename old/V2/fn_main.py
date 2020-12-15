# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from fn_generic import *
import fn_generic as gen
from elv_main import *
import elv_main as elv
from prf_main import *
import prf_main as prf
from adm_main import *
import adm_main as adm





#############################################################
##              FONCTIONS MAIN NO PROFIL                   ##
#############################################################


def check() :
    global idusr, fen_Main, pso_nom, pso_prenom, pso_password
    nmpnps = [pso_nom.get(),pso_prenom.get(),pso_password.get()]  # passage du formulaire (nom et prénom) en tuple
    nompn = [pso_nom.get(),pso_prenom.get()]
    idusr = nompn
    nom = pso_nom.get()
    prenom = pso_prenom.get()

    # Construction du dictionnaire de tous les profils
    ## Découpage des entrées de la BDD clé / data (c.a.d. profil / nom-prénom)
    data_profils=open('data/data_profils.txt','r')
    dico_profils = decoup_valtuple(data_profils)
    data_profils.close()
    data_pass=open('data/data_pass.txt','r')
    dico_pass = decoup_cletuple(data_pass)
    data_pass.close()
    L1 = []
    L2 = []
    for key in dico_pass.keys() :
        L1 = [key[0], key[1], dico_pass[key]]
        L2.append(L1)
    if nmpnps in L2 :
        fen_Main.destroy()
        pfs = find_key (nompn, dico_profils)
        if pfs == 'Elève' :
            elv.elv_accueil(nompn)
        elif pfs == 'Professeur' :
            prf.prf_accueil(nompn)
        else :
            adm.adm_accueil(nompn)
    else :
        messagebox.showwarning("ATTENTION", "Il y a une erreur dans votre nom, votre prénom ou le mot de passe.\n Merci de modifier votre saisie et de réessayer.")




#############################################################
##               PROCESS MAIN                              ##
#############################################################

def accmain() :
    global fen_Main, pso_nom, pso_prenom, pso_password
    #creer la fenetre de connection
    fen_Main= Tk()

    #creation du logo
    image = PhotoImage(file="img/logo_vn.png").zoom(15).subsample(15)#personalisation de l'image en zoomant
    cnvimg = Canvas(fen_Main, width=540 , height = 160 , bg="white")
    cnvimg.create_image(270, 80, image=image)


    fen_Main.title("Visual Note") #titre du logiciel
    fen_Main.geometry("630x720") #resolution de la fenetre
    fen_Main.iconbitmap("img/vn_logo_2.ico") #logo en haut a gauche du logiciel
    fen_Main.config(background='white') #couleur du fond

    #creer la boite qui contient titre + message
    frame = Frame(fen_Main , bg = "white")
    fr_prenom = Frame (frame)
    fr_nom = Frame (frame)
    fr_pass = Frame (frame)

    #Titre
    label_title= Label(frame, text="Bienvenue sur Visual Note", font=("Calibri",40),bg="white",fg="black")
    label_title.pack(expand=YES)

    #message pour demander de se connecter
    label_subtitle= Label(frame, text="Veuillez vous connecter", font=("Calibri",25),bg="white",fg="black")
    label_subtitle.pack(expand=YES)


    #creer le prenom d'utilisateur
    txt_prenom = Label(fr_prenom, text="Votre PRENOM", font=("Calibri",16), bg="white", fg="black")
    txt_prenom.grid(row=0, column=0)
    pso_prenom = tk.Entry(fr_prenom, textvariable='',width=66)
    pso_prenom.grid(row=0, column=1)
    fr_prenom.pack(fill=X)

    #creer le nom d'utilisateur
    txt_nom = Label(fr_nom, text="Votre NOM", font=("Calibri",16), bg="white", fg="black")
    txt_nom.grid(row=0, column=0)
    pso_nom = tk.Entry(fr_nom, textvariable='',width=71)
    pso_nom.grid(row=0, column=1)
    fr_nom.pack(fill=X)

    #creer un mot de passe
    txt_password = Label(fr_pass, text="Mot de Passe", font=("Calibri",16), bg="white", fg="black")
    txt_password.grid(row=0, column=0)
    pso_password= tk.Entry(fr_pass, textvariable='', width=68)
    pso_password.grid(row=0, column=1)
    fr_pass.pack(fill=X)


    #ajouter boutton connexion
    cn_button = Button(frame, text= "Se connecter", font = ("Calibri", 15), bg="white", fg="black", command=check)
    cn_button.pack(fill=X)

    #ajouter le logo
    cnvimg.pack(fill=X)

    #ajouter la boite
    frame.pack(fill=X)

    #afficher la fenetre
    fen_Main.mainloop()
