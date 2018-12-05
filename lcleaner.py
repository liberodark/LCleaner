# LCleaner : Linux Cleaner
# About: Cleaner your linux distro simply
# Author: theo546, liberodark, minzord
# License: GNU GPLv3

import os, sys, glob, re, threading, datetime, time
from PIL import Image
import subprocess
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from PIL import Image, ImageTk

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

windows = Tk()
windows.title("LCleaner v0.0.1")
windows.geometry("620x280")
icon = PhotoImage(file="/usr/share/icons/lcleaner.png")  # link to the window icon
windows.tk.call('wm', 'iconphoto', windows._w, icon)  # window application

TEXTE = Label(windows, text='Linux Cleaner', fg="blue")
TEXTE2 = Label(windows, text="LCleaner clean your linux distro.", fg="purple")
TEXTE.pack(side=TOP, padx=5, pady=3)  # Title of the text application
TEXTE2.pack(side=TOP, padx=5, pady=10)  # Title of the text application

CLEAN = Button(windows, text='CLEAN', height=2, width=30)
RESTORE = Button(windows, text='RESTORE', height=2, width=30)

INFO = Label(windows, text='', fg="black")  # Information that changes according to the button pressed by the user
MESSAGE = Label(windows, text='STATE OF THE PC', fg="blue")

INFO.pack(side=BOTTOM)  # we close the buttons by deciding on their location
MESSAGE.pack(side=BOTTOM)

windows.mainloop()
