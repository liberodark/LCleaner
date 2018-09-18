# Linux-Cleaner
Linux-Cleaner

run

```wget -Nnv https://raw.githubusercontent.com/liberodark/Linux-Cleaner/master/clean.sh && chmod +x clean.sh; ./clean.sh```

Remove old kernels ubuntu / debian :

sudo dpkg --list 'linux-image*'|awk '{ if ($1=="ii") print $2}'|grep -v `uname -r`

`sudo apt-get autoremove`

`sudo apt-get autoclean`

`sudo update-grub`
