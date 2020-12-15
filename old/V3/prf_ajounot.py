# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import date, datetime
import locale
locale.setlocale(locale.LC_TIME,'')             # Affichage des dates en Français
from fn_generic import *
import fn_generic as gen
from prf_main import *
import prf_main as prf



#############################################################
##               FONCTIONS PROFIL PROFESSEUR               ##
#############################################################


def checknot() :
    global idusr, not_nom, not_mat, not_max, not_coef, not_type, not_not 

    ch_nom = not_nom.get()
    ch_mat = not_mat.get()
    ch_max = not_max.get()
    ch_coef = not_coef.get()
    ch_type = not_type.get()
    ch_not = not_not.get()

    if ch_nom =='' or ch_mat =='' or ch_max =='' or ch_coef =='' or ch_type =='' or ch_not =='' :
        tk.messagebox.showwarning("ATTENTION", "Merci de remplir tous les champs")
        fen_SaisieNote.mainloop()          # retour sur le même écran
    elif float(ch_not) > int(ch_max) or float(ch_not) < 0 :
        tk.messagebox.showwarning("ATTENTION", "Vous avez saisi une note négative ou supérieure à la note maximale.\nMerci de corriger")
        fen_SaisieNote.mainloop()          # retour sur le même écran
    else :
        nompn = ch_nom.split(" ")          # Séparation Nom / Prénom
        saisie_note = [ch_mat]
        saisie_note.append(ch_not)
        saisie_note.append(ch_max)
        saisie_note.append(ch_coef)
        saisie_note.append(ch_type)
        yet_dt = datetime.now()            # Sauvegarde de la date du jour
        yet_d = yet_dt.strftime("%d %B")
        saisie_note.append(yet_d)
        
        ## Découpage des entrées de la BDD (mots de passe) clé / data (élève / notes et arguments)
        data_notes=open('data/data_notes.txt','r')
        dico_notes = gen.decoup_cletvalt (data_notes)
        data_notes.close()
        # Ajout des nouvelles entrées au dictionnaire COM
        gen.ajout_dico(dico_notes, tuple(saisie_note), tuple(nompn))
        # Sauvegarde des dictionnaires dans le fichier texte
        bdd = 'data/data_notes.txt'
        gen.save_cletvalt (bdd, dico_notes)
        ask = tk.messagebox.askyesno("MERCI", "Cette note a bien été enregistrée(e) pour "+ch_nom+".\n Souhaitez-vous ajouter une autre note ?", parent=fen_SaisieNote)
        fen_SaisieNote.destroy()
        if ask == True :
            addnote(idusr)                              # retour sur la page d'ajout de personne
        else :
            prf.prf_accueil(idusr)                      # retour sur l'accueil d'admin


def retour() :
    global idusr, fen_SaisieNote
    fen_SaisieNote.destroy()
    prf.prf_accueil(idusr)






#############################################################
##                PROCESS PROFIL PROFESSEUR                ##
#############################################################

def addnote (nmn) :
    global idusr, fen_SaisieNote, not_nom, not_mat, not_max, not_coef, not_type, not_not 
    idusr = nmn
    ##Saisie nouveau nom
    fen_SaisieNote = tk.Tk() 
    fen_SaisieNote.geometry('600x200')
    fen_SaisieNote.title("Visualnot'") #titre du logiciel
    fen_SaisieNote.geometry("630x720") #resolution de la fenetre
    fen_SaisieNote.iconbitmap("img/vn_logo_2.ico") #logo en haut a gauche du logiciel
    fen_SaisieNote.config(background='white') #couleur du fond

    #creer les boites
    fr1=Frame(fen_SaisieNote, relief=FLAT, width=540, height=200, bd=0, bg="white")
    fr1.pack(fill=X)
    fr2 = Frame(fen_SaisieNote, relief=FLAT, width=540, height=385, bd=0)
    fr2.pack(fill=X)
    fr3 = Frame(fen_SaisieNote, relief=FLAT, width=540, height=100, bd=0, bg="white")
    fr3.pack(fill=X)

    #creation du logo
    image = PhotoImage(file="img/logo_vn.png").zoom(15).subsample(15)#personalisation de l'image en zoomant
    cnvimg = Canvas(fr1, width=540 , height = 160 , bg="white")
    cnvimg.create_image(270, 80, image=image)
    cnvimg.pack(fill=X)

    #Titre
    label_title= Label(fr1, text="Espace Professeur", font=("Calibri",40),bg="white",fg="black")
    label_title.pack(expand=YES)

    # message de sous-itre
    label_subtitle= Label(fr1, text="Saisie d'une nouvelle note ", font=("Calibri",25),bg="white",fg="black")
    label_subtitle.pack(expand=YES)


    # Création de la liste des élèves
    data_profil=open('data/data_profils.txt','r')
    dico_profil = gen.decoup_valtuple (data_profil)
    data_profil.close()
    list_noms = []
    for i in range (0, len(dico_profil['Elève'])) :
        val = dico_profil['Elève'][i][0]+" "+dico_profil['Elève'][i][1]
        list_noms.append(val)
    list_noms.sort()
    #Création de la liste des matières
    data_matieres=open('data/data_matieres.txt','r')
    dico_matieres = gen.decoup_valtuple (data_matieres)
    data_matieres.close()
    list_mat = []
    for i in range (0, len(dico_matieres['com'])) :     # Ajout des matières communes dans la liste
        val = dico_matieres['com'][i][0]
        list_mat.append(val)
    for i in range (0, len(dico_matieres['lv1'])) :     # Ajout des matières LV1 dans la liste
        val = dico_matieres['lv1'][i][0] + ' (LV1)'
        list_mat.append(val)
    for i in range (0, len(dico_matieres['lv2'])) :     # Ajout des matières LV2 dans la liste
        val = dico_matieres['lv2'][i][0] + ' (LV2)'
        list_mat.append(val)
    for i in range (0, len(dico_matieres['spe'])) :     # Ajout des matières SPE dans la liste
        val = dico_matieres['spe'][i][0] + ' (SPE)'
        list_mat.append(val)
    #Création des listes pour les coefs, note max et type d'examen
    data_bsn=open('data/data_basenotes.txt','r')
    dico_bsn = gen.decoup_valtuple (data_bsn)
    data_bsn.close()
    list_max = []
    list_coef = []
    list_type = []
    for i in range (0, len(dico_bsn['max'])) :     # Ajout des notes max dans la liste
        val = dico_bsn['max'][i][0]
        list_max.append(val)
    for i in range (0, len(dico_bsn['coef'])) :     # Ajout des coefs dans la liste
        val = dico_bsn['coef'][i][0]
        list_coef.append(val)
    for i in range (0, len(dico_bsn['type'])) :     # Ajout des types dans la liste
        val = dico_bsn['type'][i][0]
        list_type.append(val)

    not_nom = tk.StringVar()
    not_mat = tk.StringVar()
    not_max = tk.StringVar()
    not_coef = tk.StringVar()
    not_not = tk.StringVar()

    txt_nom = tk.Label(fr2, text="Nom de l'élève", font=("Calibri",16), bg="white", fg="black")
    txt_mat = tk.Label(fr2, text="Matière", font=("Calibri",16), bg="white", fg="black")
    txt_not = tk.Label(fr2, text="Note obtenue", font=("Calibri",16), bg="white", fg="black")
    txt_coef = tk.Label(fr2, text="Coefficient", font=("Calibri",16), bg="white", fg="black")
    txt_max = tk.Label(fr2, text="Note max possible", font=("Calibri",16), bg="white", fg="black")
    txt_type = tk.Label(fr2, text="Type d'examen", font=("Calibri",16), bg="white", fg="black")
    not_nom = ttk.Combobox(fr2, values=list_noms, state="readonly")
    not_mat = ttk.Combobox(fr2, values=list_mat, state="readonly")
    not_max = ttk.Combobox(fr2, values=list_max)
    not_max.current(2)
    not_type = ttk.Combobox(fr2, values=list_type, state="readonly")
    not_coef = ttk.Combobox(fr2, values=list_coef,state="readonly")
    not_not = tk.Entry(fr2, textvariable='',width=5)
    txt_nom.grid(row=1)
    txt_mat.grid(row=2)
    txt_max.grid(row=3)
    txt_type.grid(row=4)
    txt_coef.grid(row=5)
    txt_not.grid(row=6)
    not_nom.grid(row=1, column=1)
    not_mat.grid(row=2, column=1)
    not_max.grid(row=3, column=1)
    not_type.grid(row=4, column=1)
    not_coef.grid(row=5, column=1)
    not_not.grid(row=6, column=1)

    bt_valider = tk.Button(fr3, text='Valider', font = ("Calibri", 15), bg="white", fg="black", command=checknot)
    bt_valider.pack(fill=X)
    bt_retour = tk.Button(fr3, text='Retour', font = ("Calibri", 15), bg="white", fg="black", command=retour)
    bt_retour.pack(fill=X)



    # Afficher la fenêtre
    fen_SaisieNote.mainloop()