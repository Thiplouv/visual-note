# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk


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
        C = B[1].split(",")
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
        C = B[1].split(",")
        data = []
    ## Séparation nom et prénom
        for i in range (0, len(C)) :
            data.append(C[i].split(";"))
        dico[cle]=data              # le dictionnaire a maintenant une clé et des items-tuples (nom, prénom)
        ligne = data_txt.readline()
    return dico

#def decoup_cletuple (data_txt) :


## Sous-fonctions récurrente de découpage des entrées de la BDD Clé / Data
#def save_simple (data_txt) :


def save_valtuple (bdd, dico) :
    ## Effacement de la BDD précédente
    data_txt=open(bdd,'w')
    data_txt.write("")
    data_txt.close()
    ## Construction et sauvegarde de la nouvelle BDD
    data_txt=open(bdd,'a')
    for (cle,data) in dico.items() :
        data_txt.write(cle+":"+data[0][0]+";"+data[0][1])
        for i in range (1,len(data)):
            data_txt.write(","+data[i][0]+";"+data[i][1])
        data_txt.write("\n")
    data_txt.close()

#def save_cletuple (data_txt) :

def ajout_dico (dico, nom, item) :
    if item in dico.keys() :
        dico[item].append(nom)    # ajout nouvelle entrée dans le dictionnaire si le profil existe
    else :
        dico[item] = [nom]          # ajout nouvelle entrée dans le dictionnaire si le profil n'existe pas encore
    return dico    
