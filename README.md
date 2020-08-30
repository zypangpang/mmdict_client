## Introduction
This project includes two simple clients for mmDict.
You need to configure your own mmDict daemon server in `configs-example.py`, and then rename this file to `configs.py` to take effect.

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
   
   For simplicity, you can just run `pip3 install --user -r requirements.txt` to install all Python dependencies, 
   but maybe `requirements.txt` file is not updated timely.

## Usage
Simply run `python3 gui_client.py run` to start the gui client, with `-h` to print the help.
