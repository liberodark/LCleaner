# LCleaner is Linux Cleaner

Is simple gui to clean your linux distro and secure cleaning



# Run :
```sudo pip install pycrypto```
```wget -Nnv https://raw.githubusercontent.com/liberodark/Linux-Cleaner/master/lcleaner.sh && sudo python3 lcleaner.py```

# Build :
Stadalone : ```nuitka3 --standalone --recurse-on --python-version=3.7 lcleaner.py```
Normal : ```nuitka3 --recurse-on --python-version=3.7 lcleaner.py```

# Run Bash
```wget -Nnv https://raw.githubusercontent.com/liberodark/Linux-Cleaner/master/clean.sh && chmod +x clean.sh; ./clean.sh```

## Fonction Support
- [x] Remove cache apps.
- [x] Remove Trash.
- [x] Remove journal apps.
- [x] Remove empty or old desktop entry.
- [x] Auto Update.

## OS Support
- [X] Ubuntu
- [X] Arch Linux / Manjaro
- [ ] Other need to test



## Roadmap
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
- [ ] Add one bouton to clean (1 Click to clean)
- [ ] Add Auto Clean
- [x] Add Auto Detecte your Package Manager
- [ ] Add better clean options
