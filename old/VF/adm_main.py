# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import adm_ajoupers as adp
import fn_main as fmn
import main_pass as pas
import adm_suppers as spp
import adm_ajoumat as ajm
import adm_supmat as spm



#############################################################
##              FONCTIONS PROFIL ADMINISTRATIF             ##
#############################################################

def deconnect() :
    fen_AccAdmin.destroy()
    fmn.accmain()

def adm_addpers () :
    global idusr, fen_AccAdmin
    fen_AccAdmin.destroy()
    adp.addpers(idusr)

def adm_suppers () :
    global idusr, fen_AccAdmin
    fen_AccAdmin.destroy()
    spp.del_perso(idusr)
 
def modif_pass () :
    global idusr, fen_AccAdmin
    fen_AccAdmin.destroy()
    pas.chg_pass(idusr)

def adm_ajoumat () :
    global idusr, fen_AccAdmin
    fen_AccAdmin.destroy()
    ajm.addmat(idusr)

def adm_supmat () :
    global idusr, fen_AccAdmin
    fen_AccAdmin.destroy()
    spm.del_mat(idusr)




#############################################################
##               PROCESS PROFIL ADMINISTRATIF              ##
#############################################################

def adm_accueil (nmn) :
    global idusr, fen_AccAdmin
    idusr = nmn
    
    # Créer la fenetre de connection
    fen_AccAdmin = Tk()

    # Création du logo
    image = PhotoImage(file="img/logo_vn.png").zoom(15).subsample(15)#personalisation de l'image en zoomant
    cnvimg = Canvas(fen_AccAdmin, width=600 , height = 180 , bg="white")
    cnvimg.create_image(330, 85, image=image)

    fen_AccAdmin.title("Visual Note") #titre du logiciel
    fen_AccAdmin.geometry("700x720") #resolution de la fenetre
    fen_AccAdmin.iconbitmap("img/vn_logo_2.ico") #logo en haut a gauche du logiciel
    fen_AccAdmin.config(background='white') #couleur du fond

    # Créer la boite qui contient titre + message
    frame=Frame(fen_AccAdmin , bg = "white")

    # Titre
    label_title = Label(frame, text="Bienvenue sur Visual Note", font=("Calibri",40),bg="white",fg="black")
    label_title.pack(expand=YES)

    # Message pour demander de se connecter
    label_subtitle= Label(frame, text="Bienvenue " + idusr[1] + " " + idusr[0], font=("Calibri",25),bg="white",fg="black")
    label_subtitle.pack(expand=YES)


    # Ajouter bouton Ajout d'un utilisateur
    cn_button = Button(frame, text= "Ajouter des utilisateurs" , font = ("Calibri", 15), bg="white", fg="black",command=adm_addpers)
    cn_button.pack(fill=X)

    # Ajouter bouton Suppression un utilisateur
    cn_button = Button(frame, text= "Supprimer des utilisateurs" , font = ("Calibri", 15), bg="white", fg="black",command=adm_suppers)
    cn_button.pack(fill=X)

    # Ajouter bouton Ajout de matière
    cn_button = Button(frame, text= "Ajouter une matière" , font = ("Calibri", 15), bg="white", fg="black",command=adm_ajoumat)
    cn_button.pack(fill=X)

    # Ajouter bouton Suppression de matière
    cn_button = Button(frame, text= "Supprimer une matière" , font = ("Calibri", 15), bg="white", fg="black",command=adm_supmat)
    cn_button.pack(fill=X)

    # Ajouter bouton Modification de mot de passe
    cn_button = Button(frame, text= "Modifier le mot de passe" , font = ("Calibri", 15), bg="white", fg="black",command=modif_pass)
    cn_button.pack(fill=X)

    # Ajouter bouton Déconnexion
    cn_button = Button(frame, text= "Se déconnecter" , font = ("Calibri", 15), bg="white", fg="black",command=deconnect)
    cn_button.pack(fill=X)

    # Ajouter le logo
    cnvimg.pack(fill=X)

    # Ajouter la boîte
    frame.pack(fill=X)

    # Afficher la fenêtre
    fen_AccAdmin.mainloop()
