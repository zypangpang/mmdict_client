## Introduction
This project includes two simple clients for [mmDict](https://github.com/zypangpang/mmdict_daemon).

A config file will be created at the first running. The default config file path is `$HOME/.mmdict_client/configs.ini`. 
Then you need to change it accordingly.

## Installation
Just git clone this repo. No need more steps.

## Dependencies
1. System dependencies.

    You need install **Python3.6+, qt5 and qtwebengine** in your system. For different Linux distros, the names may be different.
    
    For example, in Arch, simply run `pacman -S python qt5-base qt5-webengine`. 
    In Gentoo, run `emerge -a python qtcore qtwebengine`.
    Note that usually you don't need to explicitly install qt5, other software using qt will pull it automatically.

2. Python dependencies are listed in `Pipfile`, i.e.
    * pyqt5 
    * pyqtwebengine 
    * beautifulsoup4 
    * lxml 
    * requests
    * fire
    
   **Recommend** using `pip3 install --user <package>` to install above packages seperately.

## Usage
Simply run `python3 gui_main.py run` to start the gui client, with `-h` to print the help.
