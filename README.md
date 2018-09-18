# Linux-Cleaner
Linux-Cleaner

run

```wget -Nnv https://github.com/liberodark/TS3-Update/releases/download/1.9.5/update.sh && chmod +x update.sh; ./update.sh```

Remove old kernels ubuntu / debian :

sudo dpkg --list 'linux-image*'|awk '{ if ($1=="ii") print $2}'|grep -v `uname -r`

`sudo apt-get autoremove`

`sudo apt-get autoclean`

`sudo update-grub`
