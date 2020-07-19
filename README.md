# get-recipes

## Pre-Requisits

#### Install Git-Bash
If using on Windows you need to install git bash for windows https://gitforwindows.org/

#### Install Python 3.7.3
Install python version 3.7.3 from this link https://www.python.org/downloads/release/python-373/
  - choose the 'Windows x86-64 executable installer' option under Files
  - Run the exectuable and make sure to check the 'Add Python 3.7 to PATH' checkbox

#### Getting the right Chrome Driver
Check your version of chrome using the following instrucions:

1. Open Chrome and open the Chrome settings. Click 'Help' > 'About Google Chrome'. A new window will appear with your Version of google chrome.

  ![](https://github.com/afatt/get-recipes/blob/master/google_settings.png)

2. This script uses Chrome Version (84.0.4147.89) as its chromedriver.exe. If your Chrome version is older than (84.0.4147.89), then update Chrome or find the chromedriver.exe that matches your Version here https://chromedriver.chromium.org/downloads

  - If you downloaded a new chromedriver.exe find it and replace the chromedriver.exe in /get-recipes after following the Getting Started instructions below

## Getting Started

1. Open your file explorer and navigate to where you would like to install the repository (I chose the Documents folder). Right click and chose "Git Bash Here"

2. Type the following command in the terminal: ```git clone https://github.com/afatt/get-recipes.git```
  
3. Navigate into the get-recipes folder: ```cd get-recipes```

4. Then install the python dependencies: ```python setup.py install```

## How to Use

1. Make sure you have images of your QR codes in get-recipes/images folder
2. Open git bash in the same directory as the get-recipes folder with by right clicking and choosing "Git Bash Here"
3. Run the script using: ```python get_recipes.py```
4. The pdfs will be installed in the Downloads folder of your computer
