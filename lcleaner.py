#!/usr/bin/env python3

# LCleaner : Linux Cleaner
# About: Clean your linux distro simply
# Author: theo546, liberodark, minzord
# License: GNU GPLv3

import os
import sys
import glob
import re
import threading
import datetime
import time
import subprocess
import shutil
from pathlib import Path
import json
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.filedialog import *
from PIL import Image, ImageTk

VERSION = "1.0.0"

class LinuxCleaner:
    def __init__(self, root):
        self.root = root
        self.root.title(f"LCleaner v{VERSION}")
        self.root.geometry("700x500")

        # Try to load icon
        try:
            self.icon = PhotoImage(file="/usr/share/icons/lcleaner.png")
            self.root.tk.call('wm', 'iconphoto', self.root._w, self.icon)
        except:
            pass

        # Define cleaning paths
        self.paths = {
            "package": [
                "/var/cache/pacman/pkg",
                "/var/cache/apt/archives",
                "/var/cache/yum/x86_64/9",
                "/var/cache/yum/x86_64/8",
                "/var/cache/yum/x86_64/7",
                "/var/cache/yum/x86_64/6",
                "/var/cache/yum/i386/9",
                "/var/cache/yum/i386/8",
                "/var/cache/yum/i386/7",
                "/var/cache/yum/i386/6",
                "/var/cache/dnf"
            ],
            "cache": [os.path.expandvars("$HOME/.cache")],
            "trash": [os.path.expandvars("$HOME/.local/share/Trash/files")],
            "journal": ["/var/log"],
            "desktop": [os.path.expandvars("$HOME/.local/share/applications")],
            "temp": ["/tmp"]
        }

        # Exception paths (don't clean these)
        self.exceptions = [
            os.path.expandvars("$HOME/.cache/pkg"),
            os.path.expandvars("$HOME/.cache/archives")
        ]

        # Auto-detect package manager
        self.detect_package_manager()

        # Create the UI
        self.create_ui()

    def detect_package_manager(self):
        """Auto-detect the system's package manager"""
        self.package_manager = None

        # Check for common package managers
        if os.path.exists("/usr/bin/apt") or os.path.exists("/usr/bin/apt-get"):
            self.package_manager = "apt"
        elif os.path.exists("/usr/bin/pacman"):
            self.package_manager = "pacman"
        elif os.path.exists("/usr/bin/dnf"):
            self.package_manager = "dnf"
        elif os.path.exists("/usr/bin/yum"):
            self.package_manager = "yum"

    def create_ui(self):
        """Create the user interface"""
        # Main frame
        main_frame = Frame(self.root)
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Title
        title_label = Label(main_frame, text='Linux Cleaner', fg="blue", font=("Arial", 20))
        title_label.pack(side=TOP, padx=5, pady=3)

        # Subtitle
        subtitle_label = Label(main_frame, text="Clean your Linux system with ease", fg="purple", font=("Arial", 14))
        subtitle_label.pack(side=TOP, padx=5, pady=10)

        # Tabs
        tab_control = ttk.Notebook(main_frame)

        # Main tab
        main_tab = Frame(tab_control)
        tab_control.add(main_tab, text='Main')

        # Checkboxes for what to clean
        self.clean_options = {}
        options_frame = LabelFrame(main_tab, text="Select what to clean")
        options_frame.pack(fill=X, padx=10, pady=10)

        option_types = {
            "package": "Package Caches",
            "cache": "Application Caches",
            "trash": "Trash Bin",
            "journal": "Log Files",
            "desktop": "Invalid Desktop Entries",
            "temp": "Temporary Files"
        }

        self.space_labels = {}

        row = 0
        for key, label in option_types.items():
            var = BooleanVar(value=True)
            self.clean_options[key] = var

            frame = Frame(options_frame)
            frame.pack(fill=X, padx=5, pady=2)

            cb = Checkbutton(frame, text=label, variable=var)
            cb.pack(side=LEFT)

            space_label = Label(frame, text="")
            space_label.pack(side=RIGHT)
            self.space_labels[key] = space_label

            row += 1

        # Button frame
        button_frame = Frame(main_tab)
        button_frame.pack(fill=X, padx=10, pady=10)

        # Clean button
        clean_button = Button(button_frame, text='CLEAN SYSTEM', height=2, command=self.clean_system)
        clean_button.pack(side=LEFT, fill=X, expand=True, padx=5)

        # Analyze button
        analyze_button = Button(button_frame, text='ANALYZE SPACE', height=2, command=self.analyze_space)
        analyze_button.pack(side=RIGHT, fill=X, expand=True, padx=5)

        # Status frame
        status_frame = LabelFrame(main_tab, text="Status")
        status_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Status text
        self.status_text = Text(status_frame, height=10, wrap=WORD)
        self.status_text.pack(fill=BOTH, expand=True, padx=5, pady=5)
        self.status_text.config(state=DISABLED)

        # Advanced tab
        advanced_tab = Frame(tab_control)
        tab_control.add(advanced_tab, text='Advanced')

        # About tab
        about_tab = Frame(tab_control)
        tab_control.add(about_tab, text='About')

        # About content
        about_text = f"""
LCleaner {VERSION}

A simple tool to clean your Linux system safely.

Licensed under GNU GPLv3.

Authors:
- theo546
- liberodark
- minzord

GitHub: https://github.com/liberodark/LCleaner
        """

        about_label = Label(about_tab, text=about_text, justify=LEFT)
        about_label.pack(padx=20, pady=20)

        # Pack the tab control
        tab_control.pack(expand=1, fill=BOTH)

        # Footer status bar
        self.footer_status = Label(main_frame, text='Ready', bd=1, relief=SUNKEN, anchor=W)
        self.footer_status.pack(side=BOTTOM, fill=X)

    def update_status(self, message):
        """Update the status text widget"""
        self.status_text.config(state=NORMAL)
        self.status_text.insert(END, f"{message}\n")
        self.status_text.see(END)
        self.status_text.config(state=DISABLED)
        self.footer_status.config(text=message)
        self.root.update()

    def get_size(self, path):
        """Get the total size of a directory"""
        total_size = 0
        if not os.path.exists(path):
            return 0

        if os.path.isfile(path):
            return os.path.getsize(path)

        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if os.path.exists(fp):
                    total_size += os.path.getsize(fp)

        return total_size

    def human_readable_size(self, size):
        """Convert bytes to human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} PB"

    def analyze_space(self):
        """Analyze space usage for each category"""
        self.update_status("Analyzing disk space usage...")

        total_size = 0

        for key, paths in self.paths.items():
            size = 0
            for path in paths:
                if os.path.exists(path):
                    try:
                        size += self.get_size(path)
                    except:
                        pass

            # Update the label
            readable_size = self.human_readable_size(size)
            self.space_labels[key].config(text=f"({readable_size})")

            self.update_status(f"{key.capitalize()} size: {readable_size}")
            total_size += size

        self.update_status(f"Total space that can be cleaned: {self.human_readable_size(total_size)}")
        self.update_status("Analysis complete.")

    def clean_packages(self):
        """Clean package caches based on detected package manager"""
        if not self.package_manager:
            self.update_status("No package manager detected.")
            return

        try:
            if self.package_manager == "apt":
                self.update_status("Cleaning APT package cache...")
                subprocess.run(["pkexec", "apt-get", "clean"], check=True)
            elif self.package_manager == "pacman":
                self.update_status("Cleaning Pacman package cache...")
                subprocess.run(["pkexec", "pacman", "-Sc", "--noconfirm"], check=True)
            elif self.package_manager == "dnf":
                self.update_status("Cleaning DNF package cache...")
                subprocess.run(["pkexec", "dnf", "clean", "all"], check=True)
            elif self.package_manager == "yum":
                self.update_status("Cleaning YUM package cache...")
                subprocess.run(["pkexec", "yum", "clean", "all"], check=True)

            self.update_status(f"{self.package_manager.upper()} package cache cleaned.")
        except Exception as e:
            self.update_status(f"Error cleaning package cache: {str(e)}")

    def clean_path(self, path, is_system=False):
        """Clean a specific path"""
        if not os.path.exists(path):
            return

        # Skip exception paths
        if path in self.exceptions:
            return

        try:
            if os.path.isfile(path):
                if is_system:
                    subprocess.run(["pkexec", "rm", "-f", path], check=True)
                else:
                    os.remove(path)
            else:
                for item in os.listdir(path):
                    item_path = os.path.join(path, item)
                    if os.path.isdir(item_path):
                        # Skip exception paths
                        if item_path in self.exceptions:
                            continue

                        try:
                            if is_system:
                                subprocess.run(["pkexec", "rm", "-rf", item_path], check=True)
                            else:
                                shutil.rmtree(item_path)
                        except:
                            pass
                    else:
                        try:
                            if is_system:
                                subprocess.run(["pkexec", "rm", "-f", item_path], check=True)
                            else:
                                os.remove(item_path)
                        except:
                            pass
        except Exception as e:
            self.update_status(f"Error cleaning {path}: {str(e)}")

    def clean_desktop_entries(self):
        """Clean invalid desktop entries"""
        if not self.clean_options["desktop"].get():
            return

        self.update_status("Cleaning invalid desktop entries...")

        for path in self.paths["desktop"]:
            if os.path.exists(path):
                for file in glob.glob(f"{path}/*.desktop"):
                    try:
                        with open(file, 'r') as f:
                            content = f.read()

                        # Extract Exec line
                        exec_match = re.search(r'Exec=([^\n]*)', content)
                        if exec_match:
                            exec_line = exec_match.group(1)
                            executable = exec_line.split()[0]

                            # Remove parameters from executable
                            executable = executable.split(' ')[0]

                            # Check if executable exists
                            which_result = subprocess.run(["which", executable], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                            if which_result.returncode != 0:
                                self.update_status(f"Removing invalid desktop entry: {os.path.basename(file)}")
                                os.remove(file)
                    except Exception as e:
                        self.update_status(f"Error processing {file}: {str(e)}")

        self.update_status("Desktop entries cleaned.")

    def clean_system(self):
        """Main cleaning function"""
        if not askyesno('LCleaner', 'Are you sure you want to clean your system? This will remove temporary files and cached data.'):
            return

        self.update_status("Starting cleaning process...")

        # Clean package caches
        if self.clean_options["package"].get():
            self.clean_packages()

        # Clean user cache
        if self.clean_options["cache"].get():
            self.update_status("Cleaning application caches...")
            for path in self.paths["cache"]:
                self.update_status(f"Cleaning {path}...")
                self.clean_path(path)
            self.update_status("Application caches cleaned.")

        # Clean trash
        if self.clean_options["trash"].get():
            self.update_status("Emptying trash...")
            for path in self.paths["trash"]:
                self.update_status(f"Cleaning {path}...")
                self.clean_path(path)
            self.update_status("Trash emptied.")

        # Clean journal/logs
        if self.clean_options["journal"].get():
            self.update_status("Cleaning system logs...")
            for path in self.paths["journal"]:
                self.update_status(f"Cleaning {path}...")
                self.clean_path(path, True)
            self.update_status("System logs cleaned.")

        # Clean desktop entries
        if self.clean_options["desktop"].get():
            self.clean_desktop_entries()

        # Clean temporary files
        if self.clean_options["temp"].get():
            self.update_status("Cleaning temporary files...")
            for path in self.paths["temp"]:
                self.update_status(f"Cleaning {path}...")
                self.clean_path(path, True)
            self.update_status("Temporary files cleaned.")

        self.update_status("Cleaning process completed successfully!")
        showinfo("LCleaner", "Cleaning process completed successfully!")

if __name__ == "__main__":
    root = Tk()
    app = LinuxCleaner(root)
    root.mainloop()
