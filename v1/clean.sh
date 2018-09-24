#!/bin/bash
#
# About: Clean linux automatically
# Author: liberodark
# Project: Linux-Cleaner
# License: GNU GPLv3

# Init

package=(/var/cache/pacman/pkg /var/cache/apt/archives) # /var/cache/yum/$basearch/$releasever
# exeption=($HOME/.cache/pkg $HOME/.cache/archives)
cache="$HOME/.cache"
trash="$HOME/.local/share/Trash/files"
journal="/var/log"
desktop="$HOME/.local/share/applications"
update_source="https://raw.githubusercontent.com/liberodark/Linux-Cleaner/master/clean.sh"
version="0.0.4"

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

# Check Package

  count=$(ls -a $package | sed -e "/\.$/d" | wc -l 2>/dev/null)

  if [[ -z "$count" ]] || [[ $count -eq 0 ]]; then
      echo "Package is empty"
  else
      rm -r $package/*
      echo "Package is cleaned"
  fi

# Check Cache

  count=$(ls -a $cache | sed -e "/\.$/d" | wc -l 2>/dev/null)

  if [[ -z "$count" ]] || [[ $count -eq 0 ]]; then
      echo "Cache is empty"
  else
      #sudo rm -r $cache/*
      echo "Cache is cleaned"
  fi
  
# Check Trash

  count=$(ls -a $trash | sed -e "/\.$/d" | wc -l 2>/dev/null)

  if [[ -z "$count" ]] || [[ $count -eq 0 ]]; then
      echo "Trash is empty"
  else
      rm -r $trash/*
      echo "Trash is cleaned"
  fi

# Check Journal

  count=$(ls -a $journal | sed -e "/\.$/d" | wc -l 2>/dev/null)

  if [[ -z "$count" ]] || [[ $count -eq 0 ]]; then
      echo "Journal is empty"
  else
      rm -r $journal/*
      echo "Journal is cleaned"
  fi
  
# Check Desktop

for files in `ls ${desktop}/*.desktop`
do
        line=`grep '^Exec' $files | tail -1`
        executable=`echo $line | sed 's/^\([^= ]\{4\}\)=\"\{0,1\}\([^= \"]\{1,\}\)\"\{0,1\}.*$/\2/g'`
        which $executable 1>/dev/null 2>/dev/null
        rc=$?
        if [[ -n "$rc" ]] && [[ $rc -ne 0 ]]
        then
                echo "$executable do not exist, $files to remove"
                rm "$files" 2>/dev/null
                echo "Desktop is cleaned"
        fi
done
