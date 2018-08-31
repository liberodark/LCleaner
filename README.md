# Linux-Cleaner
Linux-Cleaner

Remove old kernels ubuntu / debian :
`sudo dpkg --list 'linux-image*'|awk '{ if ($1=="ii") print $2}'|grep -v `uname -r``

`sudo apt-get autoremove`

`sudo apt-get autoclean`

`sudo update-grub`
