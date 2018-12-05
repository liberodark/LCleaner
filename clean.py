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



windows.mainloop()
