$package = /var/cache/pacman/pkg && /var/cache/apt/archives/ && /var/cache/yum/$basearch/$releasever/
$cache = ~/.cache/
$trash = ~/.local/share/Trash/files/
$journal = /var/log/


# Check Journal
ls /var/log/ &> /dev/null

if [ "$?" != 0 ]; then
    echo "Journal is empty"
else
    echo "Journal is cleaned"
    rm -r $journal
fi