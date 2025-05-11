import tkinter
fenêtre = tkinter.Tk()
bouton = tkinter.Button(fenêtre, text="Appuie sur le bouton pour dessiner un flocon de neige.", width=40)
bouton.pack(padx=10, pady=10)
compteclics = 0
def quandcliqué(event):
    global compteclics
    compteclics = compteclics + 1
    if compteclics == 1:
        bouton.configure(text="Vraiment ? N'appuie. Pas. Dessus.")
    elif compteclics == 2:
        bouton.configure(text="La prochaine fois, plus de bouton.")
    else:
        bouton.pack_forget()
bouton.bind("<ButtonRelease-1>", quandcliqué)
fenêtre.mainloop()
