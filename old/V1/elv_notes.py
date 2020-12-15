# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import date, datetime



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
    while ligne != ""  and ligne != "\n" :
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

def decoup_cletvalt (data_txt) :
    dico = dict()
    ligne = data_txt.readline()
    while ligne != "" and ligne != "\n" :             
        A = str(ligne[0:-1])
        B = A.split(":")
        C = B[0].split(";")
        cle = tuple(C)
        D = B[1].split("|")
        data = []
        ## Séparation valeurs du tuple
        for i in range (0, len(D)) :
            data.append(D[i].split(";"))
        dico[cle]=data              # le dictionnaire a maintenant une clé et des items (tuples tous les 2)
        ligne = data_txt.readline()
    return(dico)



#############################################################
##               FONCTIONS PROFIL ELEVE                    ##
#############################################################






#############################################################
##                PROCESS PROFIL ELEVE                     ##
#############################################################

global nompn
print ('00->',nompn)
# Prérequis : héritage de l'élève concerné
nom = "Pl00"                # Nom et prénom fixes, à remplacer par l'héritage quand l'authentification sera prête
prenom = "Th00"             # idem
nompn = [nom,prenom]
print ('01->',nompn)

fen_AffNote = tk.Tk() 
fen_AffNote.geometry('450x600')

#Création de la liste des matières
data_matieres=open('data/data_matieres.txt','r')
dico_matieres = decoup_valtuple (data_matieres)
data_matieres.close()
mat_com = []
for i in range (0, len(dico_matieres['com'])) :     # Ajout des matières communes dans la liste
    val = dico_matieres['com'][i][0]
    mat_com.append(val)
## matières optionnelles de l'élève
### LV1
data_lv1=open('data/data_lv1.txt','r')
dico_lv1 = decoup_valtuple (data_lv1)
data_lv1.close()
for (k) in dico_lv1.keys() :                        # Ajout de LA matière LV1
    if nompn in dico_lv1[k] :
        mat_lv1 = k
### LV2
data_lv2=open('data/data_lv2.txt','r')
dico_lv2 = decoup_valtuple (data_lv2)
data_lv2.close()
for (k) in dico_lv2.keys() :                        # Ajout de LA matière LV2
    if nompn in dico_lv2[k] :
        mat_lv2 = k
### SPE
data_spe=open('data/data_spe.txt','r')
dico_spe = decoup_valtuple (data_spe)
data_spe.close()
for (k) in dico_spe.keys() :                        # Ajout de LA matière SPE
    if nompn in dico_spe[k] :
        mat_spe = k

# Récupération des notes de l'élève
data_notes=open('data/data_notes.txt','r')
dico_notes = decoup_cletvalt (data_notes)
data_notes.close()
list_notes = dico_notes[tuple(nompn)]

# Affichage tableau des notes
titre = tk.Label(fen_AffNote, text='Notes et Moyennes de '+prenom+' '+nom, justify='left')
titre.grid(row=0)
## Matières
### Matières communes
m_gen = 0
c_gen = 0
for i in range (0, len(mat_com)) :
    com = tk.Label(fen_AffNote, text=mat_com[i], justify='left')
    com.grid(column=0)                  # 1ère colonne : intitulés des matières
    mx = 0
    cf = 0
    for t in range (0, len(list_notes)) :
        if mat_com[i] == list_notes[t][0] :
            mx = mx + float(list_notes[t][1])*20/int(list_notes[t][2])*int(list_notes[t][3])
            cf = cf + int(list_notes[t][3])
            note = tk.Label(fen_AffNote, text=list_notes[t][5]+' : '+list_notes[t][1]+'/'+list_notes[t][2]+' (coef: '+list_notes[t][3]+', '+list_notes[t][4]+')', justify='left')
            note.grid(column=1)         # 2ème colonne : notes et coefficients...
    if cf == 0 :
        moy = 'NA'                      # Si aucune note (donc pas de cumul de coefs), afficher NA (Non Applicable)
    else :
        m = mx/cf                       # calcul et affichage de la moyenne pour la matière
        moy = '%2.2f' % m
    moyenne = tk.Label(fen_AffNote, text= 'Moyenne : '+moy+' /20', justify='left')
    moyenne.grid(column=1)
    m_gen = m_gen + m
    c_gen = c_gen + 1
### LV1
mx = 0
cf = 0
lv1 = tk.Label(fen_AffNote, text=mat_lv1, justify='left')
lv1.grid(column=0)                      # 1ère colonne : intitulé de la matière concernée
for t in range (0, len(list_notes)) :
    if mat_lv1 == list_notes[t][0] :
        mx = mx + float(list_notes[t][1])*20/int(list_notes[t][2])*int(list_notes[t][3])
        cf = cf + int(list_notes[t][3])
        note = tk.Label(fen_AffNote, text=list_notes[t][5]+' : '+list_notes[t][1]+'/'+list_notes[t][2]+' (coef: '+list_notes[t][3]+', '+list_notes[t][4]+')', justify='left')
        note.grid(column=1)             # 2ème colonne : notes et coefficients...
if cf == 0 :
    moy = 'NA'                          # Si aucune note (donc pas de cumul de coefs), afficher NA (Non Applicable)
else :
    m = mx/cf                           # calcul et affichage de la moyenne pour la matière
    moy = '%2.2f' % m
moyenne = tk.Label(fen_AffNote, text= 'Moyenne : '+moy+' /20', justify='left')
moyenne.grid(column=1)
m_gen = m_gen + m
c_gen = c_gen + 1
### LV2
mx = 0
cf = 0
lv2 = tk.Label(fen_AffNote, text=mat_lv2, justify='left')
lv2.grid(column=0)                      # 1ère colonne : intitulé de la matière concernée
for t in range (0, len(list_notes)) :
    if mat_lv2 == list_notes[t][0] :
        mx = mx + float(list_notes[t][1])*20/int(list_notes[t][2])*int(list_notes[t][3])
        cf = cf + int(list_notes[t][3])
        note = tk.Label(fen_AffNote, text=list_notes[t][5]+' : '+list_notes[t][1]+'/'+list_notes[t][2]+' (coef: '+list_notes[t][3]+', '+list_notes[t][4]+')', justify='left')
        note.grid(column=1)             # 2ème colonne : notes et coefficients...
if cf == 0 :
    moy = 'NA'                          # Si aucune note (donc pas de cumul de coefs), afficher NA (Non Applicable)
else :
    m = mx/cf                           # calcul et affichage de la moyenne pour la matière
    moy = '%2.2f' % m
moyenne = tk.Label(fen_AffNote, text= 'Moyenne : '+moy+' /20', justify='left')
moyenne.grid(column=1)
m_gen = m_gen + m
c_gen = c_gen + 1
### Spécialités
mx = 0
cf = 0
spe = tk.Label(fen_AffNote, text=mat_spe, justify='left')
spe.grid(column=0)                      # 1ère colonne : intitulé de la matière concernée
for t in range (0, len(list_notes)) :
    if mat_spe == list_notes[t][0] :
        mx = mx + float(list_notes[t][1])*20/int(list_notes[t][2])*int(list_notes[t][3])
        cf = cf + int(list_notes[t][3])
        note = tk.Label(fen_AffNote, text=list_notes[t][5]+' : '+list_notes[t][1]+'/'+list_notes[t][2]+' (coef: '+list_notes[t][3]+', '+list_notes[t][4]+')', justify='left')
        note.grid(column=1)             # 2ème colonne : notes et coefficients...
if cf == 0 :
    moy = 'NA'                          # Si aucune note (donc pas de cumul de coefs), afficher NA (Non Applicable)
else :
    m = mx/cf                           # calcul et affichage de la moyenne pour la matière
    moy = '%2.2f' % m
moyenne = tk.Label(fen_AffNote, text= 'Moyenne : '+moy+' /20', justify='left')
moyenne.grid(column=1)
m_gen = m_gen + m
c_gen = c_gen + 1                       # Coef 1 par matière --> A modifier à terme pour avoir un coef par matière
### Moyenne générale
if c_gen == 0 :
    m_gen = 'NA'                        # Si aucune note (donc pas de cumul de coefs), afficher NA (Non Applicable)
else :
    m = m_gen/c_gen                     # calcul et affichage de la moyenne générale
    moy = '%2.2f' % m
txt_moy = tk.Label(fen_AffNote, text= 'Moyenne Générale : ', justify='left')
txt_moy.grid(column=0)
not_moy = tk.Label(fen_AffNote, text= moy +' /20', justify='left')
not_moy.grid(column=1)


fen_AffNote.mainloop()

