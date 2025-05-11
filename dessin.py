import tkinter
print("Pour dessiner, déplace ta souris en appuyant sur le bouton gauche.")
print("Pour changer de couleur, clique sur une des couleurs.")
fenêtre = tkinter.Tk()
canvas = tkinter.Canvas(fenêtre, width=750, height=500, bg="white")
canvas.pack()
dernierX, dernierY = 0,0
couleur = "black"

def enregistrer_position(event):
    global dernierX, dernierY
    dernierX = event.x
    dernierY = event.y
    
def quand_cliqué(event):
    enregistrer_position(event)
    
def quand_déplacé(event):
    canvas.create_line(dernierX, dernierY, event.x, event.y, fill = couleur, width = 3)
    enregister_position(event)
canvas.bind("Button-1", quand_cliqué)
canvas.bind("B1-Motion", quand_cliqué)
fenêtre.mainloop()
