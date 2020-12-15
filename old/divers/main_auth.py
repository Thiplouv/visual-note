# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
from tkinter import messagebox




#############################################################
##               SOUS-FONCTIONS GENERIQUES                 ##
#############################################################

## Sous-fonctions récurrente de découpage des entrées de la BDD Clé / Data
def decoup_simple (data_txt) :
    dico = dict()
    ligne = data_txt.readline()
    while ligne != "" :             
        A = str(ligne[0:-1])
        B = A.split(":")
        C = B[1].split("|")
        dico[B[0]] = C
        ligne = data_txt.readline()
    return dico

def decoup_valtuple (data_txt) :
    dico = dict()
    ligne = data_txt.readline()
    while ligne != "" :             
        A = str(ligne[0:-1])
        B = A.split(":")
        cle=B[0]
        C = B[1].split("|")
        data = []
    ## Séparation nom et prénom
        for i in range (0, len(C)) :
            data.append(C[i].split(";"))
        dico[cle]=data              # le dictionnaire a maintenant une clé et des items-tuples (nom, prénom)
        ligne = data_txt.readline()
    return dico

def decoup_cletuple (data_txt) :
    dico = dict()
    ligne = data_txt.readline()
    while ligne != "" and ligne != "\n" :             
        A = str(ligne[0:-1])
        B = A.split(":")
        C = B[0].split(";")
        cle = tuple(C)
        D = B[1]
        dico[cle]=D              # le dictionnaire a maintenant une clé-tuples (nom, prénom) et des items
        ligne = data_txt.readline()
    return(dico)




## Sous-fonctions récurrente de découpage des entrées de la BDD Clé / Data
#def save_simple (data_txt) :


def save_valtuple (bdd, dico) :
    ## Effacement de la BDD précédente
    data_txt=open(bdd,'w')
    data_txt.write('')
    data_txt.close()
    ## Construction et sauvegarde de la nouvelle BDD
    data_txt=open(bdd,'a')
    for (cle,data) in dico.items() :
        data_txt.write(cle+':'+data[0][0]+';'+data[0][1])
        for i in range (1,len(data)) :
            data_txt.write('|'+data[i][0]+';'+data[i][1])
        data_txt.write('\n')
    data_txt.close()

def save_cletuple (bdd,dico) :
    ## Effacement de la BDD précédente
    data_txt=open(bdd,'w')
    data_txt.write('')
    data_txt.close()
    ## Construction et sauvegarde de la nouvelle BDD
    data_txt=open(bdd,'a')
    for (cle,data) in dico.items() :
        dt = ''.join(data)
        data_txt.write(cle[0]+';'+cle[1]+":"+dt)
        data_txt.write('\n')
    data_txt.close()



def ajout_dico (dico, tpl, item) :
    if item in dico.keys() :
        dico[item].append(tpl)    # ajout nouvelle entrée dans le dictionnaire si le profil existe
    else :
        dico[item] = [tpl]          # ajout nouvelle entrée dans le dictionnaire si le profil n'existe pas encore
    return dico    




#############################################################
##              FONCTIONS MAIN NO PROFIL                   ##
#############################################################


def check() :
   global pso_nom, pso_profil, nom, profil
   nom = [pso_nom.get(),pso_prenom.get()]  # passage du formulaire (nom et prénom) en tuple
    
   # Construction du dictionnaire de tous les profils
   ## Découpage des entrées de la BDD clé / data (c.a.d. profil / nom-prénom)
   data_profils=open('data/data_profils.txt','r')
   dico_profils = decoup_valtuple (data_profils)
   data_profils.close()
   L1 = []
   for key in dico_profils.keys() :        # Création d'une liste de tous les tuples [nom,prénom] pour recherche d'un existant
      L1.extend(dico_profils[key])
   if nom in L1 :
      check_password()
   else :
      messagebox.showwarning("ATTENTION", "le pseudo n'est pas correct")
      window.mainloop()          # retour sur le même écran

def check_password():
   global pso_nom, pso_profil,pso_password, nom, profil , password
   password=[pso_nom.get(),pso_prenom.get(),pso_password.get()]
   data_pass=open('data/data_pass.txt','r')
   dico_pass = decoup_valtuple (data_pass)
   data_pass.close()
   L2 = []
   print ('01->',L2)
   for key in dico_pass.keys() :        # Création d'une liste de tous les tuples [nom,prénom, mdp] pour recherche d'un existant
      L2.extend(dico_pass[key])
      if password in L2 and password =="ISN_2020" :
         messagebox.askquestion("Bienvenue", "ceci est votre premiere connexion veuillez changer votre mdp")
         if answer == 'yes':
            open(changeurdemotdepasse)
      elif password in L2:
         messagebox.showwarning("Bienvenue", "connexion............")
      else :
         messagebox.showwarning("ATTENTION", "le mot de passe n'est pas correct")
         window.mainloop()          # retour sur le même écran
   





#############################################################
##               PROCESS MAIN                              ##
#############################################################


#creer la fenetre de connection
window= Tk()

#creation du logo
width = 470
height = 200
image = PhotoImage(file="img/logo_vn.png").zoom(15).subsample(15)#personalisation de l'image en zoomant
canvas = Canvas(window, width=width , height = height , bg="white")
canvas.create_image(width/2, height/2, image=image)


window.title("Visualnot'") #titre du logiciel
window.geometry("1080x720") #resolution de la fenetre
window.iconbitmap("img/vn_logo_2.ico") #logo en haut a gauche du logiciel
window.config(background='white') #couleur du fond

#creer la boite qui contient titre + message
frame=Frame(window , bg = "white")

#Titre
label_title= Label(frame, text="Bienvenue sur Visualnot'", font=("Calibri",40),bg="white",fg="black")
label_title.pack(expand=YES)

#message pour demander de se connecter
label_subtitle= Label(frame, text="Veuillez vous connecter", font=("Calibri",25),bg="white",fg="black")
label_subtitle.pack(expand=YES)


#creer le prenom d'utilisateur
pso_prenom = tk.Entry(frame, textvariable='',width=20)
pso_prenom.pack(fill=X)

#creer le prenom d'utilisateur
pso_nom = tk.Entry(frame, textvariable='',width=20)
pso_nom.pack(fill=X)

#creer un mot de passe
pso_password= tk.Entry(frame, textvariable='',width=20)
pso_password.pack(fill=X)


#ajouter boutton connexion
cn_button = Button(frame, text= "Se connecter" , font = ("Calibri", 15), bg="white", fg="black",command=check)
cn_button.pack(fill=X)

#ajouter le logo
canvas.grid(row=0, column=0, sticky=N)

#ajouter la boite
frame.grid(row=1, column=0, sticky=W)

#afficher la fenetre
window.mainloop()
