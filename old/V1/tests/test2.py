# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from datetime import date, time, datetime
import locale
locale.setlocale(locale.LC_TIME,'')
import subprocess
from subprocess import Popen, PIPE, run
 
#a = '12.25'
#b = '3'
#d = float(a)/float(b)
#m = '%2.2f' % d

#print ("res : "+m)

#d = datetime.now()
#print (d.strftime("%d %B"))


process = Popen(['python', 'test0.py'])
stdout, stderr = process.communicate()
#print (stdout)

#subprocess.run("start python3 test0.py", check=True, shell=True)