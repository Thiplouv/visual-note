# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


data_txt=open('test_pass.txt','r')
dico = dict()
ligne = data_txt.readline()
while ligne != "\n" :             
    A = str(ligne[0:-1])
    print('00->',A)
    B = A.split(":")
    print('01->',B)
    C = B[0].split(";")
    print('02->',C)
    cle = tuple(C)
    print('03->',cle)
    D = B[1]
    print('04->',D)
    dico[cle]=D              # le dictionnaire a maintenant une clé et des items-tuples (nom, prénom)
    ligne = data_txt.readline()
print(dico)
