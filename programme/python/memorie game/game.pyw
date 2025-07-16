import random
import tkinter as tk
import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("song.WAV")
pygame.mixer.music.set_volume(1000)
pygame.mixer.music.play(loops=-1)

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

with open("point.txt", "r") as f:
    points = int(f.read())

def starting(n):
    global i, chiffre, chiffre_ensemble, taille, rgb, points, rouge
    rgb = 0
    i = 0
    rouge = 0
    label_point.pack_forget()
    color = rgb_to_hex(rgb, rgb, rgb)
    chiffre = []
    taille = 12

    while i != n:
        chiffre.append(str(random.randint(0, 9)))
        i += 1
    i = 0
    chiffre_ensemble = ''.join(chiffre)
    print(chiffre_ensemble)
    start()

def start():
    global i, taille, chiffre, chiffre_ensemble, rgb, rouge
    if i != len(chiffre):
        inp.delete(0, tk.END)
        rgb += 20
        rouge +=5
        r = rgb + rouge
        color = rgb_to_hex(r, rgb, rgb)
        taille += 2
        label.config(text=chiffre[i], font=("Arial", taille), fg=color)
        root.after(500, start)
        i += 1
    else:
        label.config(text="")
        inp.pack()
    try:
        button_eas.pack_forget()
        button_mid.pack_forget()
        button_hard.pack_forget()
    except:
        pass

def confirm(event=None):
    global i, points
    rep = inp.get()
    if rep == chiffre_ensemble:
        label.config(text="bonne réponse", font=("Arial", 16), fg='black')
        if len(chiffre) == 4:
            points += 2
        elif len(chiffre) == 6:
            points += 5
        elif len(chiffre) == 9:
            points += 10
    else:
        label.config(text="mauvaise réponse", font=("Arial", 16), fg='black')
        if len(chiffre) == 4:
            points -= 20
        elif len(chiffre) == 6:
            points -= 10
        elif len(chiffre) == 9:
            points -= 5
    i = 0
    with open("point.txt", "w") as f:
        if points > 0:
            f.write(str(points))
        else:
            points = 0
            f.write("0")
    label_point.config(text=f'tu as {points} points')
    label_point.pack()
    button_eas.pack()
    button_mid.pack()
    button_hard.pack()
    inp.pack_forget()

root = tk.Tk()
root.geometry("500x500")
root.title("Memorie game")
label_point = tk.Label(root, text=f"tu as {points} points", font=("Arial", 16), fg='black')
label_point.pack()
label = tk.Label(root, text="")
label.pack()
button_eas = tk.Button(root, text="facile", command=lambda: starting(4))
button_mid = tk.Button(root, text="Moyen", command=lambda: starting(6))
button_hard = tk.Button(root, text="difficile", command=lambda: starting(9))
button_eas.pack()
button_mid.pack()
button_hard.pack()
inp = tk.Entry(root)
inp.bind('<Return>', confirm)
root.mainloop()