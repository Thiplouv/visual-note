# -*- coding: utf-8 -*-
from tkinter import *

fen = Tk()

fr1 = Frame(fen,relief=GROOVE,width=500,height=200, bd=5)
can = Canvas(fr1,)
fr2 = Frame(can)
fr3 = Frame(fen,relief=GROOVE,width=500,height=200, bd=10)
fr1.pack()
fr2.pack()
fr3.pack()
mainloop()