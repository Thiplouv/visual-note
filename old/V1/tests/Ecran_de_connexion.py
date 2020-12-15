from tkinter import *
import webbrowser #pour rediriger vers une page internet (que l'on enlevera apres)

def open_ecran_daccueil():
   webbrowser.open_new(" https://0921484n.index-education.net/pronote/eleve.html")#creation commande pour redirection 
    

#creer la fenetre de connection
window= Tk()

#creation du logo
width = 200
height = 200
image = PhotoImage(file="download.png").zoom(35).subsample(32)#personalisation de l'image en zoomant
canvas = Canvas(window, width=width , height = height , bg="white")
canvas.create_image(width/2, height/2, image=image)


window.title("Visualnot'") #titre du logiciel
window.geometry("1080x720") #resolution de la fenetre
#window.iconbitmap("download.ico") #logo en haut a gauche du logiciel
window.config(background='white') #couleur du fond

#creer la boite qui contient titre + message
frame=Frame(window , bg = "white")


#Titre
label_title= Label(frame, text="Bienvenue sur Visualnot'", font=("Calibri",40),bg="white",fg="black")
label_title.pack(expand=YES)

#message pour demander de se connecter
label_subtitle= Label(frame, text="Veuillez vous connecter", font=("Calibri",25),bg="white",fg="black")
label_subtitle.pack(expand=YES)

#creer un nom d'utilisateur
pseudo_entry= Entry(frame, text="Pseudo", font=("Calibri",10),bg="white",fg="black")
pseudo_entry.pack(fill=X)

#creer un mot de passe
password_entry= Entry(frame, text="mot de passe'", font=("Calibri",10),bg="white",fg="black")
password_entry.pack(fill=X)


#ajouter boutton connexion
cn_button = Button(frame, text= "Se connecter" , font = ("Calibri", 15), bg="white", fg="black",command=open_ecran_daccueil)#redirige pour l'instant au vrai pronote
cn_button.pack(fill=X)

#ajouter le logo
canvas.grid(row=0, column=0, sticky=N)


#ajouter la boite
frame.grid(row=1, column=0, sticky=W)



#afficher la fenetre
window.mainloop()
