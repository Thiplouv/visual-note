# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import date, datetime
from fn_generic import *
import fn_generic as gen
from elv_main import *
import elv_main as elv



def retour() :
    global idusr, fen_AffNote
    fen_AffNote.destroy()
    elv.elv_accueil(idusr)

def scrollv(event):
    global canvas
    canvas.configure(scrollregion=canvas.bbox("all"),width=510,height=385)



def notes(nmn) :
    global idusr, fen_AffNote, canvas
    # Prérequis : héritage de l'élève concerné
    idusr = nmn
    nom = nmn[0]
    prenom = nmn[1]

    fen_AffNote = Tk()
    fen_AffNote.title("Visualnot'") #titre du logiciel
    fen_AffNote.geometry("630x720") #resolution de la fenetre
    fen_AffNote.iconbitmap("img/vn_logo_2.ico") #logo en haut a gauche du logiciel
    fen_AffNote.config(background='white') #couleur du fond

    fr1=Frame(fen_AffNote, relief=FLAT, width=540, height=200, bd=0, bg="white")
    fr1.pack(fill=X)
    fr2 = Frame(fen_AffNote, relief=FLAT, width=540, height=385, bd=0)
    fr2.pack(fill=X)
    fr3 = Frame(fen_AffNote, relief=FLAT, width=540, height=100, bd=0, bg="white")
    fr3.pack(fill=X)


    canvas=Canvas(fr2)
    frame=Frame(canvas)
    myscrollbar=Scrollbar(fr2,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right",fill="y")
    canvas.pack(side="left")
    canvas.create_window((0,0),window=frame,anchor='nw')
    frame.bind("<Configure>",scrollv)

    #creation du logo
    image = PhotoImage(file="img/logo_vn.png").zoom(15).subsample(15)#personalisation de l'image en zoomant
    cnvimg = Canvas(fr1, width=540 , height = 160 , bg="white")
    cnvimg.create_image(270, 80, image=image)
    cnvimg.pack(fill=X)

    #Titre
    label_title= Label(fr1, text="Espace Elève", font=("Calibri",40),bg="white",fg="black")
    label_title.pack(expand=YES)

    #message de sous-titre
    label_subtitle = Label(fr1, text='Notes et Moyennes de '+prenom+' '+nom, font=("Calibri",25), bg="white",fg="black")
    label_subtitle.pack(fill=X)

    #Création de la liste des matières
    data_matieres=open('data/data_matieres.txt','r')
    dico_matieres = gen.decoup_valtuple (data_matieres)
    data_matieres.close()
    mat_com = []
    coef_com = []
    for i in range (0, len(dico_matieres['com'])) :     # Ajout des matières communes dans la liste
        val = dico_matieres['com'][i][0]
        cof =  dico_matieres['com'][i][1]
        mat_com.append(val)
        coef_com.append(cof)
    ## matières optionnelles de l'élève
    ### LV1
    data_lv1=open('data/data_lv1.txt','r')
    dico_lv1 = gen.decoup_valtuple (data_lv1)
    data_lv1.close()
    for (k) in dico_lv1.keys() :                        # Ajout de LA matière LV1
        if idusr in dico_lv1[k] :
            mat_lv1 = k
    ### LV2
    data_lv2=open('data/data_lv2.txt','r')
    dico_lv2 = gen.decoup_valtuple (data_lv2)
    data_lv2.close()
    for (k) in dico_lv2.keys() :                        # Ajout de LA matière LV2
        if idusr in dico_lv2[k] :
            mat_lv2 = k
    ### SPE
    data_spe=open('data/data_spe.txt','r')
    dico_spe = gen.decoup_valtuple (data_spe)
    data_spe.close()
    for (k) in dico_spe.keys() :                        # Ajout de LA matière SPE
        if idusr in dico_spe[k] :
            mat_spe = k

    # Récupération des notes de l'élève
    data_notes=open('data/data_notes.txt','r')
    dico_notes = gen.decoup_cletvalt (data_notes)
    data_notes.close()
    if tuple(idusr) in dico_notes :
        list_notes = dico_notes[tuple(idusr)]
    else :
        list_notes = []

    # Affichage tableau des notes
    ## Matières
    ### Matières communes
    m_gen = 0
    c_gen = 0
    for i in range (0, len(mat_com)) :
        com = tk.Label(frame, text=mat_com[i], justify='left')
        com.grid(column=0)                  # 1ère colonne : intitulés des matières
        mx = 0
        cf = 0
        for t in range (0, len(list_notes)) :
            if mat_com[i] == list_notes[t][0] :
                mx = mx + float(list_notes[t][1])*20/int(list_notes[t][2])*int(list_notes[t][3])
                cf = cf + int(list_notes[t][3])
                note = tk.Label(frame, text=list_notes[t][5]+' : '+list_notes[t][1]+'/'+list_notes[t][2]+' (coef: '+list_notes[t][3]+', '+list_notes[t][4]+')', justify='left')
                note.grid(column=1)         # 2ème colonne : notes et coefficients...
        if cf == 0 :
            m = 0
            moy = 'NA'                      # Si aucune note (donc pas de cumul de coefs), afficher NA (Non Applicable)
        else :
            m = mx/cf                       # calcul et affichage de la moyenne pour la matière
            moy = '%2.2f' % m
        moyenne = tk.Label(frame, text= 'Moyenne : '+moy+' /20', justify='left')
        moyenne.grid(column=1)
        m_gen = m_gen + m*int(coef_com[i])
        c_gen = c_gen + int(coef_com[i])
    ### LV1
    mx = 0
    cf = 0
    lv1 = tk.Label(frame, text=mat_lv1, justify='left')
    lv1.grid(column=0)                      # 1ère colonne : intitulé de la matière concernée
    for t in range (0, len(list_notes)) :
        if mat_lv1 == list_notes[t][0] :
            mx = mx + float(list_notes[t][1])*20/int(list_notes[t][2])*int(list_notes[t][3])
            cf = cf + int(list_notes[t][3])
            note = tk.Label(frame, text=list_notes[t][5]+' : '+list_notes[t][1]+'/'+list_notes[t][2]+' (coef: '+list_notes[t][3]+', '+list_notes[t][4]+')', justify='left')
            note.grid(column=1)             # 2ème colonne : notes et coefficients...
    if cf == 0 :
        m = 0
        moy = 'NA'                          # Si aucune note (donc pas de cumul de coefs), afficher NA (Non Applicable)
    else :
        m = mx/cf                           # calcul et affichage de la moyenne pour la matière
        moy = '%2.2f' % m
    moyenne = tk.Label(frame, text= 'Moyenne : '+moy+' /20', justify='left')
    moyenne.grid(column=1)
    m_gen = m_gen + m*3
    c_gen = c_gen + 3
    ### LV2
    mx = 0
    cf = 0
    lv2 = tk.Label(frame, text=mat_lv2, justify='left')
    lv2.grid(column=0)                      # 1ère colonne : intitulé de la matière concernée
    for t in range (0, len(list_notes)) :
        if mat_lv2 == list_notes[t][0] :
            mx = mx + float(list_notes[t][1])*20/int(list_notes[t][2])*int(list_notes[t][3])
            cf = cf + int(list_notes[t][3])
            note = tk.Label(frame, text=list_notes[t][5]+' : '+list_notes[t][1]+'/'+list_notes[t][2]+' (coef: '+list_notes[t][3]+', '+list_notes[t][4]+')', justify='left')
            note.grid(column=1)             # 2ème colonne : notes et coefficients...
    if cf == 0 :
        m = 0
        moy = 'NA'                          # Si aucune note (donc pas de cumul de coefs), afficher NA (Non Applicable)
    else :
        m = mx/cf                           # calcul et affichage de la moyenne pour la matière
        moy = '%2.2f' % m
    moyenne = tk.Label(frame, text= 'Moyenne : '+moy+' /20', justify='left')
    moyenne.grid(column=1)
    m_gen = m_gen + m*2
    c_gen = c_gen + 2
    ### Spécialités
    mx = 0
    cf = 0
    spe = tk.Label(frame, text=mat_spe, justify='left')
    spe.grid(column=0)                      # 1ère colonne : intitulé de la matière concernée
    for t in range (0, len(list_notes)) :
        if mat_spe == list_notes[t][0] :
            mx = mx + float(list_notes[t][1])*20/int(list_notes[t][2])*int(list_notes[t][3])
            cf = cf + int(list_notes[t][3])
            note = tk.Label(frame, text=list_notes[t][5]+' : '+list_notes[t][1]+'/'+list_notes[t][2]+' (coef: '+list_notes[t][3]+', '+list_notes[t][4]+')', justify='left')
            note.grid(column=1)             # 2ème colonne : notes et coefficients...
    if cf == 0 :
        m = 0
        moy = 'NA'                          # Si aucune note (donc pas de cumul de coefs), afficher NA (Non Applicable)
    else :
        m = mx/cf                           # calcul et affichage de la moyenne pour la matière
        moy = '%2.2f' % m
    moyenne = tk.Label(frame, text= 'Moyenne : '+moy+' /20', justify='left')
    moyenne.grid(column=1)
    m_gen = m_gen + m*2
    c_gen = c_gen + 2                       # Coef 1 par matière --> A modifier à terme pour avoir un coef par matière
    ### Moyenne générale
    if c_gen == 0 :
        m_gen = 'NA'                        # Si aucune note (donc pas de cumul de coefs), afficher NA (Non Applicable)
    else :
        m = m_gen/c_gen                     # calcul et affichage de la moyenne générale
        moy = '%2.2f' % m
    txt_moy = tk.Label(frame, text= 'Moyenne Générale : ', justify='left')
    txt_moy.grid(column=0)
    not_moy = tk.Label(frame, text= moy +' /20', justify='left')
    not_moy.grid(column=1)

    bt_retour = tk.Button(fr3, text='Retour', font = ("Calibri", 15), bg="white", fg="black", command=retour)
    bt_retour.pack(fill=X)

    fen_AffNote.mainloop()

