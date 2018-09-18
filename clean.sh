#!/bin/bash
#
# About: Clean linux automatically
# Author: liberodark
# Project: Linux-Cleaner
# License: GNU GPLv3

 # Init

package="/var/cache/pacman/pkg && /var/cache/apt/archives/ && /var/cache/yum/$basearch/$releasever/"
cache="~/.cache/*"
trash="~/.local/share/Trash/files/*"
journal="/var/log/*"
desktop="/home/pc/.local/share/applications/*"
update_source="https://raw.githubusercontent.com/liberodark/Linux-Cleaner/master/clean.sh"
version="0.0.1"

echo "Welcome on Linux Cleaner $version"

	# make update if asked
if [ "$1" = "noupdate" ]; then
	update_status="false"
else
	update_status="true"
fi ;

 # update updater
 if [ "$update_status" = "true" ]; then
 	wget -O $0 $update_source
 	$0 noupdate
 	exit 0
fi ;

# ls -a $journal | egrep -v "^\.+$" 

# Check Journal
ls -a $journal | sed -e "/\.$/d" | wc -l &> /dev/null

if [ "$?" != 0 ]; then
    echo "Journal is empty"
else
    sudo rm -r $journal
    echo "Journal is cleaned"
fi