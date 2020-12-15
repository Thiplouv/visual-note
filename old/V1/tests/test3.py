# -*- coding: utf-8 -*-
import tkinter as tk

def find_key(v): 
    for k, val in color_dict.items(): 
        print ('00->',val)
        if v in val: 
            return k 
    return "Clé n'existe pas"
  
color_dict ={'Eleve': [['nord', 'n'], ['sud', 's'], ['nini', 'nn']], 'Professeur': [['est', 'e'], ['south', 'qq'], ['west', 'ww']]} 
print(find_key(['nord','n']))  
print(find_key(['south', 'qq'])) 
