#!/bin/bash
#
# About: Clean linux automatically
# Author: liberodark
# Thanks : Fanch The System
# License: GNU GPLv3

version="0.0.8"

echo "Welcome on LCleaner Script $version"

#=================================================
# RETRIEVE ARGUMENTS FROM THE MANIFEST AND VAR
#=================================================

# ls -a $journal | egrep -v "^\.+$" 
#remove="find -mtime +1 -delete"
package=(/var/cache/pacman/pkg /var/cache/apt/archives /var/cache/yum/x86_64/6server /var/cache/yum/x86_64/7server /var/cache/yum/i386/6server /var/cache/yum/i386/7server)
exeption=($HOME/.cache/pkg $HOME/.cache/archives)
cache="$HOME/.cache"
trash="$HOME/.local/share/Trash/files"
journal="/var/log"
desktop="$HOME/.local/share/applications"
temp="/tmp"

# Make config file
echo "$package" >> "$config"
echo "$cache" >> "$config"
echo "$trash" >> "$config"
echo $journal >> "$config"
echo "$desktop" >> "$config"

if [ -f "$config" ]
then
    for i in $(cat "$config")
    do
        if [ -d "$i" ]
        then 
            cnt=$(ls "$i"| wc -l)
            echo "Nombre d'element dans $i : $cnt"
        fi
    done
fi

      echo "Welcome on Linux Cleaner $version"

    # Check Package

    echo -n "Do you want to remove packages (y/n)? "
    read -r answer
  
    if [ "$answer" != "${answer#[Yy]}" ] ;then
        echo Yes
          count=$(ls -a "$package" | sed -e "/\.$/d" | wc -l 2>/dev/null)

      if [[ -z "$count" ]] || [[ $count -eq 0 ]]; then
          echo "Package is empty"
      else
          sudo rm -rf "$package"/*
          echo "Package is cleaned"
      fi
    else
        echo No
    fi

    # Check Cache

    echo -n "Do you want to remove cache (y/n)? "
    read -r answer
  
    if [ "$answer" != "${answer#[Yy]}" ] ;then
        echo Yes
          count=$(ls -a "$cache" | sed -e "/\.$/d" | wc -l 2>/dev/null)

      if [[ -z "$count" ]] || [[ $count -eq 0 ]]; then
          echo "Cache is empty"
      else
          #sudo rm -rf $cache/*
          echo "Cache is cleaned"
      fi
    else
        echo No
    fi
  
    # Check Trash


    echo -n "Do you want to remove trash (y/n)? "
    read -r answer

    if [ "$answer" != "${answer#[Yy]}" ] ;then
        echo Yes
          count=$(ls -a "$trash" | sed -e "/\.$/d" | wc -l 2>/dev/null)

      if [[ -z "$count" ]] || [[ $count -eq 0 ]]; then
          echo "Trash is empty"
      else
          sudo rm -rf "$trash"/*
          echo "Trash is cleaned"
      fi
    else
        echo No
    fi

    # Check Journal

    echo -n "Do you want to remove journal (y/n)? "
    read -r answer

    if [ "$answer" != "${answer#[Yy]}" ] ;then
        echo Yes
          count=$(ls -a $journal | sed -e "/\.$/d" | wc -l 2>/dev/null)

      if [[ -z "$count" ]] || [[ $count -eq 0 ]]; then
          echo "Journal is empty"
      else
          sudo rm -rf $journal/*
          echo "Journal is cleaned"
      fi
    else
        echo No
    fi
  
    # Check Desktop

    echo -n "Do you want to remove desktop (y/n)? "
    read -r answer

    if [ "$answer" != "${answer#[Yy]}" ] ;then
        echo Yes
        for files in $desktop/*.desktop
    do
            line=$(grep '^Exec' "$files" | tail -1)
            executable=$(echo "$line" | sed 's/^\([^= ]\{4\}\)=\"\{0,1\}\([^= \"]\{1,\}\)\"\{0,1\}.*$/\2/g')
            which "$executable" 1>/dev/null 2>/dev/null
            rc=$?
            if [[ -n "$rc" ]] && [[ $rc -ne 0 ]]
            then
                    echo "$executable do not exist, $files to remove"
                    rm -f "$files" 2>/dev/null
                    echo "Desktop is cleaned"
            fi
    done
    else
        echo No
    fi
