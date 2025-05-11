import tkinter as tk
import turtle
from datetime import datetime

try:
    from PIL import Image
    PIL_OK = True
except ImportError:
    PIL_OK = False
    print("⚠️ Pillow n'est pas installé. La capture en PNG ne sera pas possible.")

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

# 🎯 Fonction de capture d’écran + conversion PNG si Pillow est dispo
def capture_ecran():
    from datetime import datetime
    base_filename = f"flocon_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    eps_filename = f"{base_filename}.eps"
    png_filename = f"{base_filename}.png"

    fenetre.update_idletasks()
    canvas.update()

    try:
        # 🖼 Capture du canvas (utilisation de _canvas corrigée)
        canvas._canvas.postscript(file=eps_filename)
        print(f"✅ Capture EPS enregistrée : {eps_filename}")
        
        if PIL_OK:
            img = Image.open(eps_filename)
            img.load(scale=1)  # Plus fiable pour .eps
            img = img.convert("RGB")
            img.save(png_filename, "PNG")
            print(f"✅ Image PNG enregistrée : {png_filename}")
        else:
            print("⚠️ Pillow n'est pas installé, seul le fichier EPS a été généré.")

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
