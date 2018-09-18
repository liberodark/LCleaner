#!/bin/bash
#
# About: Clean linux automatically
# Author: liberodark
# Project: Linux-Cleaner
# License: GNU GPLv3

# Init

package="/var/cache/pacman/pkg && /var/cache/apt/archives/ && /var/cache/yum/$basearch/$releasever/"
cache="~/.cache"
trash="$HOME/.local/share/Trash/files"
journal="/var/log"
desktop="$HOME/.local/share/applications"
update_source="https://raw.githubusercontent.com/liberodark/Linux-Cleaner/master/clean.sh"
version="0.0.2"

  echo "Welcome on Linux Cleaner $version"

# make update if asked

  if [ "$1" = "noupdate" ]; then
  	update_status="false"
  else
  	update_status="true"
  fi ;

# update updater

   if [ "$update_status" = "false" ]; then # update off
   	wget -O $0 $update_source
   	$0 noupdate
   	exit 0
  fi ;

  # ls -a $journal | egrep -v "^\.+$" 

# Check Trash

  count=$(ls -a $trash | sed -e "/\.$/d" | wc -l 2>/dev/null)

  if [[ -z "$count" ]] || [[ $count -eq 0 ]]; then
      echo "Trash is empty"
  else
      sudo rm -r $trash/*
      echo "Trash is cleaned"
  fi

# Check Journal

  count=$(ls -a $journal | sed -e "/\.$/d" | wc -l 2>/dev/null)

  if [[ -z "$count" ]] || [[ $count -eq 0 ]]; then
      echo "Journal is empty"
  else
      sudo rm -r $journal/*
      echo "Journal is cleaned"
  fi
  
# Check Desktop

  ls ${desktop}/*.desktop 2>/dev/null

  if [[ -z "$count" ]] || [[ $count -eq 0 ]]; then
      echo "Desktop is OK"
  else
      #sudo rm -r $desktop/*
      echo "Desktop is cleaned"
  fi
  
  # desktop
for fichier in `ls ${desktop}/*.desktop`
do
ligne=` grep '^Exec' $fichier | tail -1`
executable=`echo $ligne | cut -d "=" -f2`
echo $executable
which $executable
echo $?
done
