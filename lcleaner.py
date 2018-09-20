# LCleaner : Linux Cleaner
# About: Cleaner your linux distro simply
# Author: theo546, liberodark
# License: GNU GPLv3

import os
import sys
from PIL import Image
import subprocess
from tkinter import *

if sys.version_info[0] == 3:
    from tkinter import messagebox
else:
    import tkMessageBox as messagebox

#os.system("xrdb -load /dev/null") # loading data with xrdb

# Folders

# Centos / Redhat
releasever = "7 6"
basearch = "x86_64 i386"
package = "/var/cache/pacman/pkg /var/cache/apt/archives /var/cache/yum/$basearch/$releasever"
# exeption=($HOME/.cache/pkg $HOME/.cache/archives)
cache = "$HOME/.cache"
trash = "$HOME/.local/share/Trash/files"
journal = "/var/log"
desktop = "$HOME/.local/share/applications"
pacmanfichier = "/etc/pacman.conf"

try:
    #On suppose d'abord qu'AMAR est désactivé. On met donc etatamar = 0 au départ.
    etatamar = 0
    with open(pacmanfichier, 'r') as searchfile:
        for line in searchfile:
            #Si la chaîne '[AMAR]' est écrit quelque part dans pacman.conf, alors le dépôt est activé et on met etatamar = 1.
            if 'amar.conf' in line:
                etatamar = 1
    searchfile.close()
except OSError:
    print("cache inaccessible, give the path to your folder")
    sys.exit(1)

configamar = "\n#Do not disable AMAR manually if you use the app\nInclude = /etc/pacman.d/amar.conf\n"

def pressA():
    A.config(state=DISABLED)
    B.config(state=ACTIVE)
    try:
        with open(pacmanfichier, "a") as ecrire:
            ecrire.write(configamar)
            ecrire.close()
            os.system("sudo pacman -Syy")
            INFO.config(text="Actif", fg="green")  # on active le depot AMAR, donc on ecrit sur le fichier.
            etatamar = 1
            ecrire.close()
    except OSError:
        messagebox.showerror("Error", "Ficher pacman.conf non accessible en écrture\nVérifier vos droit et relancer"
                                       " le script\nVérifier aussi que vous ne faite une mise à jours en même temps")


def pressB():
    A.config(state=ACTIVE)
    B.config(state=DISABLED)
    try:
        with open((pacmanfichier), "r") as f:
            lines = f.readlines()
            lines.remove("#Do not disable AMAR manually if you use the app\n")
            lines.remove("Include = /etc/pacman.d/amar.conf\n")
        with open((pacmanfichier), "w") as new_f:
            for line in lines:
                new_f.write(line)
        os.system ("sudo pacman -Syy")
        INFO.config(text="Inactif", fg="red")  # on active le depot AMAR, donc on ecrit sur le fichier.
        etatamar = 0
        f.close()
        new_f.close()
    except OSError:
        messagebox.showerror("Error", "Ficher pacman.conf non accessible en écrture\nVérifier vos droit et relancer"
                                       " le script\nVérifier aussi que vous ne faite une mise à jours en même temps")


win = Tk()
win.title("LCleaner v0.0.1")
win.geometry("620x280")
tux = PhotoImage(file="/usr/share/icons/lcleaner.png")  # link to the window icon
win.tk.call('wm', 'iconphoto', win._w, tux)  # window application

TEXTE = Label(win, text='Linux Cleaner', fg="blue")
TEXTE2 = Label(win, text="LCleaner clean your linux distro.", fg="purple")
TEXTE.pack(side=TOP, padx=5, pady=3)  # Title of the text application
TEXTE2.pack(side=TOP, padx=5, pady=10)  # Title of the text application

A = Button(win, text='CLEAN', height=2, width=30, command=pressA)
B = Button(win, text='RESTORE', height=2, width=30, command=pressB)

INFO = Label(win, text='', fg="black")  # Information that changes according to the button pressed by the user
MESSAGE = Label(win, text='STATE OF THE PC', fg="blue")

INFO.pack(side=BOTTOM)  # we close the buttons by deciding on their location
MESSAGE.pack(side=BOTTOM)

if etatamar:
    A.pack()
    A.config(state=DISABLED)
    B.pack()
    B.config(state=ACTIVE)
else:
    A.pack()
    A.config(state=ACTIVE)
    B.pack()
    B.config(state=DISABLED)

if etatamar == 0:
    INFO.config(text="Bad", fg="red")  # on active le depot AMAR, donc on ecrit sur le fichier.
else:
    INFO.config(text="Good", fg="green")  # on active le depot AMAR, donc on ecrit sur le fichier.

win.mainloop()
