# Section des imports
import tkinter

# Création de la fenêtre et explications
print("Pour dessiner, déplace ta souris en appuyant sur le bouton gauche.")
print("Pour changer de couleurs, clique sur une des couleurs.")
fenetre = tkinter.Tk()
canvas = tkinter.Canvas(fenetre, width=1920, height=1080, bg= "white")
canvas.pack()

# Dessin
dernierX, dernierY = 0,0
couleur = "black"

def enregistrer_position(event):
    global dernierX, dernierY
    dernierX = event.x
    dernierY = event.y

def quand_cliqué(event):
    enregistrer_position(event)

def quand_déplacé(event):
    canvas.create_line(dernierX, dernierY, event.x, event.y,
                       fill = couleur, width = 3)
    enregistrer_position(event)

canvas.bind("<Button-1>", quand_cliqué)
canvas.bind("<B1-Motion>", quand_déplacé)

# Changement de couleurx

fenetre.mainloop()
