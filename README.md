
<img src="https://github.com/liberodark/LCleaner/raw/master/lcleaner.png"> <b>LCleaner is Linux Cleaner</b>

Is simple gui to clean your linux distro and secure cleaning



# Run :
```sudo pip install PyQt5```

```wget -Nnv https://raw.githubusercontent.com/liberodark/Linux-Cleaner/master/lcleaner.sh && sudo python3 lcleaner.py```

# Build :
Stadalone : ```nuitka3 --standalone --recurse-on --python-version=3.7 lcleaner.py```

Normal : ```nuitka3 --recurse-on --python-version=3.7 lcleaner.py```

# How to use :
lcleaner --clean : Clean All

lcleaner -cache : Clean Cache

lcleaner -trash : Clean Trash

lcleaner -journal : Clean Journal

lcleaner -desktop : Clean Desktop

lcleaner --help : show help

# Exemples :
lcleaner --clean (To Clean All)

lcleaner -cache -trash (To Clean Trash and Cache)

# Run Bash
```wget -Nnv https://raw.githubusercontent.com/liberodark/LCleaner/master/v1/clean.sh && chmod +x clean.sh; ./clean.sh```

## Fonction Support in Bash
- [x] Remove cache apps.
- [x] Remove Trash.
- [x] Remove journal apps.
- [x] Remove empty or old desktop entry.

## OS Support
- [X] Ubuntu
- [X] Arch Linux / Manjaro
- [ ] Other need to test

## Roadmap to v2
- [x] Make GUI
- [x] Go to python 3
- [ ] Add terminal commands (```--clean all``` or ```--clean cache```)
- [ ] Add Visibility to gain space
- [ ] Add clean to find for clean apps removed
- [ ] Add clean to space or memory
- [ ] Add clean to system file
- [ ] Add clean for old kernels (ubuntu / debian)
- [ ] Add clean to apps
- [ ] Add selection for clean
- [x] Add one bouton to clean (1 Click to clean)
- [ ] Add Auto Clean
- [x] Add Auto Detecte your Package Manager (pacman, yum, apt)
- [ ] Add better clean options
