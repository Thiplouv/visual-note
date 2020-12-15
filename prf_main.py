# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import prf_ajounot as adn
import prf_supnot as dln
import fn_main as fmn
import main_pass as pas



#############################################################
##              FONCTIONS PROFIL ADMINISTRATIF             ##
#############################################################

def deconnect() :
    fen_AccProf.destroy()
    fmn.accmain()

def prf_addnote () :
    global idusr, fen_AccProf
    fen_AccProf.destroy()
    adn.addnote(idusr)

def prf_supnote () :
    global idusr, fen_AccProf
    fen_AccProf.destroy()
    dln.del_note(idusr)

def modif_pass () :
    global idusr, fen_AccProf
    fen_AccProf.destroy()
    pas.chg_pass(idusr)






#############################################################
##               PROCESS PROFIL ADMINISTRATIF              ##
#############################################################

def prf_accueil (nmn) :
    global idusr, fen_AccProf
    idusr = nmn

    # creer la fenetre de connection
    fen_AccProf = Tk()

    # creation du logo
    image = PhotoImage(file="img/logo_vn.png").zoom(15).subsample(15)#personalisation de l'image en zoomant
    cnvimg = Canvas(fen_AccProf, width=600 , height = 180 , bg="white")
    cnvimg.create_image(330, 85, image=image)

    fen_AccProf.title("Visual Note") #titre du logiciel
    fen_AccProf.geometry("700x720") #resolution de la fenetre
    fen_AccProf.iconbitmap("img/vn_logo_2.ico") #logo en haut a gauche du logiciel
    fen_AccProf.config(background='white') #couleur du fond

    # creer la boite qui contient titre + message
    frame=Frame(fen_AccProf , bg = "white")

    # Titre
    label_title= Label(frame, text="Espace Professeur", font=("Calibri",40),bg="white",fg="black")
    label_title.pack(expand=YES)

    # message de bienvenue
    label_subtitle= Label(frame, text="Bienvenue " + nmn[1] + " " + nmn[0], font=("Calibri",25),bg="white",fg="black")
    label_subtitle.pack(expand=YES)


    # ajouter bouton Ajout de notes
    cn_button = Button(frame, text= "Ajouter des notes" , font = ("Calibri", 15), bg="white", fg="black",command=prf_addnote)
    cn_button.pack(fill=X)

    # ajouter bouton Suppression de note
    cn_button = Button(frame, text= "Supprimer des notes" , font = ("Calibri", 15), bg="white", fg="black",command=prf_supnote)
    cn_button.pack(fill=X)

    #ajouter bouton Suppression de note
    cn_button = Button(frame, text= "Modifier le mot de passe" , font = ("Calibri", 15), bg="white", fg="black",command=modif_pass)
    cn_button.pack(fill=X)

    #ajouter boutton Déconnexion
    cn_button = Button(frame, text= "Se déconnecter" , font = ("Calibri", 15), bg="white", fg="black",command=deconnect)
    cn_button.pack(fill=X)

    # ajouter le logo
    cnvimg.pack(fill=X)

    # ajouter la boite
    frame.pack(fill=X)

    # afficher la fenetre
    fen_AccProf.mainloop()
