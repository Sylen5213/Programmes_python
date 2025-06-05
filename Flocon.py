# Sections des imports
import tkinter as tk
import turtle
from datetime import datetime
from PIL import ImageGrab  # Utilisation de PIL pour capturer l'écran

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Création de flocons")
fenetre.attributes('-fullscreen', True)
fenetre.bind("<Escape>", lambda e: fenetre.attributes('-fullscreen', False))

# Cadre principal
cadre_global = tk.Frame(fenetre)
cadre_global.pack(fill=tk.BOTH, expand=True)

# Cadre boutons
cadre_boutons = tk.Frame(cadre_global, bg="lightgrey", width=300)
cadre_boutons.pack(side=tk.LEFT, fill=tk.Y)

# Canvas pour turtle
canvas = turtle.ScrolledCanvas(cadre_global)
canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Turtle
t = turtle.RawTurtle(canvas)
t.speed(10)
t.pensize(3)
t.color("white")
t.screen.bgcolor("turquoise")
t.shape("turtle")

# Fonctions de dessin
def formev():
    t.right(25)
    t.forward(50)
    t.backward(50)
    t.left(50)
    t.forward(50)
    t.backward(50)
    t.right(25)

def brancheFlocon():
    for _ in range(4):
        t.forward(30)
        formev()
    t.backward(120)

def flocon(nb_branches):
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()
    for _ in range(nb_branches):
        brancheFlocon()
        t.right(360 / nb_branches)

# 🎯 Fonction de capture d’écran + conversion PNG avec Pillow
def capture_ecran():
    base_filename = f"flocon_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    png_filename = f"{base_filename}.png"

    fenetre.update_idletasks()  # Mettre à jour l'écran
    canvas.update()  # Mettre à jour le canevas

    # Capturer l'image à partir du canvas Tkinter (prend un "rectangle" autour du canevas)
    try:
        # Utilisation de ImageGrab pour capturer le canvas
        x = fenetre.winfo_rootx() + canvas.winfo_x()
        y = fenetre.winfo_rooty() + canvas.winfo_y()
        width = canvas.winfo_width()
        height = canvas.winfo_height()

        # Prendre la capture d'écran dans la zone du canvas
        img = ImageGrab.grab(bbox=(x, y, x + width, y + height))
        img.save(png_filename, "PNG")
        print(f"✅ Image PNG enregistrée : {png_filename}")
    except Exception as e:
        print(f"❌ Erreur lors de la capture : {e}")

# 🧭 Boutons
tk.Label(cadre_boutons, text="Choisis une action :", bg="lightgrey", font=("Arial", 14)).pack(pady=20)

tk.Button(cadre_boutons, text="1. Flocon à 6 branches", width=25, command=lambda: flocon(6)).pack(pady=10)
tk.Button(cadre_boutons, text="2. Flocon à 10 branches", width=25, command=lambda: flocon(10)).pack(pady=10)
tk.Button(cadre_boutons, text="3. Flocon à 18 branches", width=25, command=lambda: flocon(18)).pack(pady=10)
tk.Button(cadre_boutons, text="4. Capture d’écran", width=25, command=capture_ecran).pack(pady=30)
tk.Button(cadre_boutons, text="5. Quitter", width=25, command=fenetre.destroy).pack(pady=10)

# Lancement
fenetre.mainloop()
