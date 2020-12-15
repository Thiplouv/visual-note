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


def chx_mat(event) :
    global idusr, not_nom, not_mat, fen_SaisieNote, fr22
    sn = not_nom.get()
    sup_nom = sn.split(' ')
    list_mat = []

    data_matieres=open('data/data_matieres.txt','r')
    dico_matieres = gen.decoup_valtuple (data_matieres)
    data_matieres.close()
    for i in range (0, len(dico_matieres['com'])) :     # Ajout des matières communes dans la liste
        val = dico_matieres['com'][i][0]
        list_mat.append(val)
        data_lv1=open('data/data_lv1.txt','r')
    data_lv1=open('data/data_lv1.txt','r')
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
    fr22.pack(fill=X)
    not_mat = ttk.Combobox(fr22, values=list_mat, state="readonly")
    not_mat.grid(row=0, column=1)
    fen_SaisieNote.mainloop()
   

def check_num (ch,tp) :
    global idusr, fen_SaisieNote
    num = ['1','2','3','4','5','6','7','8','9','0','.']
    
    msg = 'ok'
    for i in range (0, len(ch)) :
        if ch[i] not in num :
            msg = 'Merci de saisir une ' + tp + ' valide.'
    return (msg)

def checknot() :
    global idusr, not_nom, not_mat, not_max, not_coef, not_type, not_not 

    ch_nom = not_nom.get()
    snm = not_mat.get()
    ch_max = not_max.get()
    ch_coef = not_coef.get()
    ch_type = not_type.get()
    ch_not = not_not.get()
    if snm.endswith('LV1') == True or snm.endswith('LV2') == True or snm.endswith('SPE') == True :
        ch_mat = snm[:len(snm)-4]
    else :
        ch_mat = snm

    res = check_num (ch_max, 'note maximale')
    ret = check_num (ch_not, 'note')
    if ch_nom =='' or ch_mat =='' or ch_max =='' or ch_coef =='' or ch_type =='' or ch_not =='' :
        tk.messagebox.showwarning("ATTENTION", "Merci de remplir tous les champs.")
    elif res != 'ok' :
        tk.messagebox.showerror('ERREUR', res, parent=fen_SaisieNote)
    elif ret != 'ok' :
        tk.messagebox.showerror('ERREUR', ret, parent=fen_SaisieNote)
    elif float(ch_not) > int(ch_max) or float(ch_not) < 0 :
        tk.messagebox.showwarning("ATTENTION", "Vous avez saisi une note négative ou supérieure à la note maximale.\nMerci de corriger")
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
        ask = tk.messagebox.askyesno("MERCI", "Cette note a bien été enregistrée pour "+ch_nom+".\nSouhaitez-vous ajouter une autre note ?", parent=fen_SaisieNote)
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
    global idusr, fen_SaisieNote, not_nom, not_mat, not_max, not_coef, not_type, not_not, fr22
    idusr = nmn
    ##Saisie nouveau nom
    fen_SaisieNote = tk.Tk() 
    fen_SaisieNote.title("Visual Note") #titre du logiciel
    fen_SaisieNote.geometry("700x720") #resolution de la fenetre
    fen_SaisieNote.iconbitmap("img/vn_logo_2.ico") #logo en haut a gauche du logiciel
    fen_SaisieNote.config(background='white') #couleur du fond

    # Créer les boites
    fr1=Frame(fen_SaisieNote, relief=FLAT, width=540, height=200, bd=0, bg="white")
    fr1.pack(fill=X)
    fr2 = Frame(fen_SaisieNote, relief=FLAT, width=540, height=385, bd=0)
    fr2.pack(fill=X)
    fr21 = Frame(fr2, relief=FLAT, width=540, height=100, bd=0)
    fr21.pack(fill=X)
    fr22 = Frame(fr2, relief=FLAT, width=540, height=285, bd=0)
    fr22.pack(fill=X)
    fr23 = Frame(fr2, relief=FLAT, width=540, height=285, bd=0)
    fr23.pack(fill=X)
    fr3 = Frame(fen_SaisieNote, relief=FLAT, width=540, height=100, bd=0, bg="white")
    fr3.pack(fill=X)

    #creation du logo
    image = PhotoImage(file="img/logo_vn.png").zoom(15).subsample(15)#personalisation de l'image en zoomant
    cnvimg = Canvas(fr1, width=600 , height = 180 , bg="white")
    cnvimg.create_image(330, 85, image=image)
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

    # Choix de l'élève
    txt_nom = tk.Label(fr21, text="Nom de l'élève", font=("Calibri",16), bg="white", fg="black", width=25)
    not_nom = ttk.Combobox(fr21, values=list_noms, state="readonly")
    txt_nom.grid(row=0)
    not_nom.grid(row=0, column=1)
    not_nom.bind("<<ComboboxSelected>>", chx_mat)

    # Choix de la matière
    txt_mat = tk.Label(fr22, text="Matière", font=("Calibri",16), bg="white", fg="black", width=25)
    not_mat = ttk.Combobox(fr22, values='', state="disabled")
    txt_mat.grid(row=0)
    not_mat.grid(row=0, column=1)

    # Choix de la note max, du coef, du type et de le note attribuée
    txt_max = tk.Label(fr23, text="Note max possible", font=("Calibri",16), bg="white", fg="black", width=25)
    not_max = ttk.Combobox(fr23, values=list_max)
    not_max.current(2)
    txt_max.grid(row=0)
    not_max.grid(row=0, column=1)

    txt_type = tk.Label(fr23, text="Type d'examen", font=("Calibri",16), bg="white", fg="black", width=25)
    not_type = ttk.Combobox(fr23, values=list_type, state="readonly")
    txt_type.grid(row=1)
    not_type.grid(row=1, column=1)

    txt_coef = tk.Label(fr23, text="Coefficient", font=("Calibri",16), bg="white", fg="black", width=25)
    not_coef = ttk.Combobox(fr23, values=list_coef,state="readonly")
    txt_coef.grid(row=2)
    not_coef.grid(row=2, column=1)

    txt_not = tk.Label(fr23, text="Note obtenue", font=("Calibri",16), bg="white", fg="black", width=25)
    not_not = tk.Entry(fr23, textvariable='', width=5)
    txt_not.grid(row=3)
    not_not.grid(row=3, column=1)

    bt_valider = tk.Button(fr3, text='Valider', font = ("Calibri", 15), bg="white", fg="black", command=checknot)
    bt_valider.pack(fill=X)
    bt_retour = tk.Button(fr3, text='Retour', font = ("Calibri", 15), bg="white", fg="black", command=retour)
    bt_retour.pack(fill=X)



    # Afficher la fenêtre
    fen_SaisieNote.mainloop()