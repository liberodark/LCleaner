<img src="https://github.com/liberodark/LCleaner/raw/master/lcleaner.png"> <b>LCleaner is Linux Cleaner</b>

A simple GUI to clean your Linux distro with an intuitive interface and powerful cleaning features.

## Run :
```sudo pip install PyQt5 pillow```

```wget -Nnv https://raw.githubusercontent.com/liberodark/LCleaner/master/lcleaner.py && sudo python3 lcleaner.py```

## Build :
Standalone : ```nuitka3 --standalone --recurse-on --python-version=3.7 lcleaner.py```

Normal : ```nuitka3 --recurse-on --python-version=3.7 lcleaner.py```

## Installing Dependencies by Distribution

#### NixOS
```nix
shell-nix
```

#### Debian/Ubuntu
```bash
sudo apt-get update
sudo apt-get install -y python3-tk python3-pil python3 policykit-1
```

#### Fedora/RHEL/CentOS
```bash
sudo dnf install -y python3-tkinter python3-pillow python3 polkit
```

#### Arch Linux
```bash
sudo pacman -S tk python-pillow python polkit
```

#### openSUSE
```bash
sudo zypper install python3-tk python3-Pillow python3 polkit
```

#### Alpine Linux
```bash
sudo apk add py3-tk py3-pillow python3 polkit
```

## Package Installation (Arch Linux) :
```bash
git clone https://github.com/liberodark/LCleaner.git
cd LCleaner
makepkg -si
```

## Manual Run
```bash
git clone https://github.com/liberodark/LCleaner
cd LCleaner
python lcleaner.py
```

## Debug
```bash
python -m tkinter
python -c "from PIL import Image, ImageTk; print('Pillow Work')"
```

## How to use :
lcleaner --clean : Clean All

lcleaner -cache : Clean Cache

lcleaner -trash : Clean Trash

lcleaner -journal : Clean Journal

lcleaner -desktop : Clean Desktop

lcleaner --analyze : Analyze disk space usage

lcleaner --help : show help

## Examples :
lcleaner --clean (To Clean All)

lcleaner -cache -trash (To Clean Trash and Cache)

## GUI Features
The graphical interface now provides:
- Option to select which components to clean
- Space analysis to see how much space can be freed
- Status updates during cleaning operations
- Package manager auto-detection
- Tabbed interface with Main, Advanced, and About sections

## Function Support in GUI
- [x] Remove cache apps
- [x] Remove Trash
- [x] Remove journal apps
- [x] Remove empty or old desktop entries
- [x] Package manager auto-detection
- [x] Space analysis
- [x] One-click cleaning
- [x] Modern tabbed interface

## OS Support
- [X] Ubuntu
- [X] Arch Linux / Manjaro
- [X] Fedora / RHEL / CentOS
- [X] OpenSUSE
- [ ] Other distros need testing

## Roadmap to v1.1
- [x] Modern GUI with tabs
- [x] Python 3 support
- [x] Command-line arguments
- [x] Space analysis
- [x] Package manager auto-detection
- [x] One-button cleaning
- [ ] System file cleaning
- [ ] Auto-clean scheduling
- [ ] Old kernel cleanup (Ubuntu/Debian)
- [ ] Detailed application cache cleaning
- [ ] Backup/restore functionality
- [ ] System optimization options
- [ ] Translation support
