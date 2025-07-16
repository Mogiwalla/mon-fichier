import tkinter as tk
from math import sqrt, cos, sin, tan, pi, e, factorial, radians, degrees

root = tk.Tk()
root.geometry("420x600")
root.title("Calculatrice")

nombre = "0"
i = 0

label = tk.Label(root, text=nombre)
label.config(font=("Arial", 16))

def calcul():
    global nombre
    nombre = nombre.replace("X", "*")
    nombre = nombre.replace("^", "**")
    nombre = nombre.replace("√", "sqrt")
    nombre = nombre.replace("π", "pi")
    nombre = nombre.replace("fac", "factorial")
    nombre = nombre.replace("rad", "radians")
    nombre = nombre.replace("deg", "degrees")
    nombre = nombre.replace(",", ".")
    nombre = str(eval(nombre))
    nombre = nombre.replace(".", ",")
    label.config(text=nombre)

def ajouter(x):
    global nombre

    if nombre == "0" and x is not ",":
        nombre = x
        label.config(text=nombre)
    else:
        nombre += x
        label.config(text=nombre)

def reset():
    global nombre
    nombre = "0"
    label.config(text=nombre)

def reset1():
    global nombre
    nombre = nombre[:-1]
    if nombre == "":
        nombre = "0"
    label.config(text=nombre)


button_options = {"width": 5, "height": 2, "font": ("Arial", 14)}

tk.Button(text="1", **button_options, command=lambda: ajouter("1") ).place(x=20,  y=350)
tk.Button(text="2", **button_options, command=lambda: ajouter("2")).place(x=100, y=350)
tk.Button(text="3", **button_options, command=lambda: ajouter("3")).place(x=180, y=350)

tk.Button(text="4", **button_options, command=lambda: ajouter("4")).place(x=20,  y=280)
tk.Button(text="5", **button_options, command=lambda: ajouter("5")).place(x=100, y=280)
tk.Button(text="6", **button_options, command=lambda: ajouter("6")).place(x=180, y=280)

tk.Button(text="7", **button_options, command=lambda: ajouter("7")).place(x=20,  y=210)
tk.Button(text="8", **button_options, command=lambda: ajouter("8")).place(x=100, y=210)
tk.Button(text="9", **button_options, command=lambda: ajouter("9")).place(x=180, y=210)

tk.Button(text="0", **button_options, command=lambda: ajouter("0")).place(x=20,  y=420)

tk.Button(text="(", **button_options, command=lambda: ajouter("(")).place(x=100, y=420)
tk.Button(text=")", **button_options, command=lambda: ajouter(")")).place(x=180, y=420)
tk.Button(text="Ce", **button_options, command=reset).place(x=180,  y=140)
tk.Button(text="C", **button_options, command=reset1).place(x=260,  y=140)

tk.Button(text="sin", **button_options, command=lambda: ajouter("sin(")).place(x=20,  y=490)
tk.Button(text="tan", **button_options, command=lambda: ajouter("tan(")).place(x=180,  y=490)
tk.Button(text="cos", **button_options, command=lambda: ajouter("cos(")).place(x=100,  y=490)
tk.Button(text="=", **button_options, command=calcul).place(x=340, y=140)

tk.Button(text="+", **button_options, command=lambda: ajouter("+")).place(x=260, y=420)
tk.Button(text="-", **button_options, command=lambda: ajouter("-")).place(x=260, y=350)
tk.Button(text="X", **button_options, command=lambda: ajouter("X")).place(x=260, y=280)
tk.Button(text="^", **button_options, command=lambda: ajouter("^")).place(x=20,  y=140)
tk.Button(text="√", **button_options, command=lambda: ajouter("√(")).place(x=100,  y=140)
tk.Button(text="/", **button_options, command=lambda: ajouter("/")).place(x=260, y=210)

tk.Button(text="π", **button_options, command=lambda: ajouter("π")).place(x=260, y=490)
tk.Button(text="e", **button_options, command=lambda: ajouter("e")).place(x=340, y=210)
tk.Button(text="abs", **button_options, command=lambda: ajouter("abs(")).place(x=340, y=280)
tk.Button(text=",", **button_options, command=lambda: ajouter(",")).place(x=340, y=350)
tk.Button(text="deg", **button_options, command=lambda: ajouter("deg(")).place(x=340, y=420)
tk.Button(text="rad", **button_options, command=lambda: ajouter("rad(")).place(x=340, y=490)

label.pack()
root.mainloop()
