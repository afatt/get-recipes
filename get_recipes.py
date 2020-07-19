#!/usr/bin/env python

'''
This script decodes the QR code from the QR images placed in the images folder.
The QR decoded url is then opened and a pdf of the website is saved in the
/Downloads folder of the user
'''

# standard library
import os
import time
import json

# third party
from PIL import Image
from pyzbar.pyzbar import decode
from selenium import webdriver

# Create a list of images from image types found in /images
image_list = []
for file in os.listdir('.\images'):
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        image_list.append(file)

# Extract the url from the list of images
url_list = []
for image in image_list:
    data = decode(Image.open(r'.\images\{}'.format(image)))

    try:
        url = data[0].data.decode('utf-8')
        url_list.append(url)
        print('Added {} to the url list'.format(url))
    except:
        print('could not load the QR code from {}'.format(image))

# Open the website associated with each url and download a pdf of the pages
for url in url_list:

    chrome_options = webdriver.ChromeOptions()
    settings = {
           "recentDestinations": [{
                "id": "Save as PDF",
                "origin": "local",
                "account": "",
            }],
            "selectedDestinationId": "Save as PDF",
            "version": 2
        }
    prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--kiosk-printing')
    chrome_options.add_argument('--disable-infobars')

    # Modify the path to your chrome driver here
    #CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
    CHROMEDRIVER_PATH = './chromedriver.exe'

    driver = webdriver.Chrome(options=chrome_options,
                              executable_path=CHROMEDRIVER_PATH)
    driver.get(url)
    driver.execute_script('window.print();')

    # Increase this time (sec) if your pdf isnt downloading
    time.sleep(5.0)
    driver.quit()
