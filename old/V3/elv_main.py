# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import elv_notes as en
import fn_main as fmn
import main_pass as pas


def deconnect() :
    fen_AccElv.destroy()
    fmn.accmain()

def elv_notes () :
    global idusr, fen_AccElv
    fen_AccElv.destroy() 
    en.notes(idusr)

def modif_pass () :
    global idusr, fen_AccElv
    fen_AccElv.destroy()
    pas.chg_pass(idusr)


def elv_accueil (nmn) :
    global idusr, fen_AccElv
    idusr = nmn
    #creer la fenetre de connection
    fen_AccElv= Tk()

    #creation du logo
    image = PhotoImage(file="img/logo_vn.png").zoom(15).subsample(15)#personalisation de l'image en zoomant
    cnvimg = Canvas(fen_AccElv, width=540 , height = 160 , bg="white")
    cnvimg.create_image(270, 80, image=image)

    fen_AccElv.title("Visual Note") #titre du logiciel
    fen_AccElv.geometry("630x720") #resolution de la fenetre
    fen_AccElv.iconbitmap("img/vn_logo_2.ico") #logo en haut a gauche du logiciel
    fen_AccElv.config(background='white') #couleur du fond

    #creer la boite qui contient titre + message
    frame=Frame(fen_AccElv, bg = "white")

    #Titre
    label_title= Label(frame, text="Espace Elève", font=("Calibri",40),bg="white",fg="black")
    label_title.pack(expand=YES)

    #message pour demander de se connecter
    label_subtitle= Label(frame, text="Bienvenue " + idusr[1] + " " + idusr[0], font=("Calibri",25),bg="white",fg="black")
    label_subtitle.pack(expand=YES)


    #ajouter boutton Ajout de notes
    cn_button = Button(frame, text= "Consulter le bulletin" , font = ("Calibri", 15), bg="white", fg="black",command=elv_notes)
    cn_button.pack(fill=X)

    #ajouter boutton Suppression de note
    cn_button = Button(frame, text= "Modifier le mot de passe" , font = ("Calibri", 15), bg="white", fg="black",command=modif_pass)
    cn_button.pack(fill=X)

    #ajouter boutton Déconnexion
    cn_button = Button(frame, text= "Se déconnecter" , font = ("Calibri", 15), bg="white", fg="black",command=deconnect)
    cn_button.pack(fill=X)

    #ajouter le logo
    cnvimg.pack(fill=X)

    #ajouter la boite
    frame.pack(fill=X)

    #afficher la fenetre
    fen_AccElv.mainloop()
