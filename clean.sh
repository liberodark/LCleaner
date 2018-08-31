package = /var/cache/pacman/pkg && /var/cache/apt/archives/ && /var/cache/yum/$basearch/$releasever/
cache = ~/.cache/
trash = ~/.local/share/Trash/files/
journal = /var/log/


# Check Cuberite
ls /home/cuberite/ &> /dev/null

if [ "$?" != 0 ]; then
    echo "Cuberite not Installed"
    mkdir /home/cuberite/
else
    echo "Cuberite is Installed"
fi