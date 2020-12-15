# -*- coding: utf-8 -*-
# 1) -  Importation des modules nécessaires
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from fn_generic import *
import fn_generic as gen


data_matieres=open('data/data_matieres.txt','r')
dico_matieres = gen.decoup_valtuple (data_matieres)
data_matieres.close()

LM = []
for k in dico_matieres :
    for i in range (0, len(dico_matieres[k])) :
        LM.append(dico_matieres[k][i][0])
print (LM)