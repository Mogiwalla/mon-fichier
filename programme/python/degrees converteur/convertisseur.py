import tkinter as tk

degrees = "celcius"

def convertie(event=None):
    global degrees, calcul
    try:
        if degrees == "celcius":
            celicus = float(inp.get())
            calcul = celicus * 1.8 + 32
            resultat.configure(text=f"ca donne {calcul}°f")
        elif degrees == "faren":
            fahrenheit = float(inp.get())
            calcul = (fahrenheit - 32) / 1.8
            resultat.configure(text=f"ca donne {calcul}°c")
    except:
        resultat.configure(text="Entrez une valeur numérique et valide")

def change():
    global degrees
    if degrees == "celcius":
        degrees = "faren"
        unite.config(text="°f")
    elif degrees == "faren":
        degrees = "celcius"
        unite.config(text="°c")

root = tk.Tk()
root.geometry("600x400")
root.title("Convertisseur")

cadre = tk.Frame(root)
cadre.pack()

unite = tk.Label(cadre, text="°c")
unite.pack()
resultat = tk.Label(root, text="")
resultat.pack(side=tk.RIGHT)

inp = tk.Entry(cadre, width=40)
inp.bind("<Return>", convertie)
inp.pack(side=tk.LEFT)
confirmer = tk.Button(root, text="Confirmer", command=convertie).pack()
switch = tk.Button(root, text="changer", command=change).pack()

root.mainloop()