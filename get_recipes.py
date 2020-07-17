import time
from PIL import Image
from pyzbar.pyzbar import decode
from selenium import webdriver
import json

data = decode(Image.open('2217.jpeg'))

try:
    url = data[0].data.decode('utf-8')
    print(url)
except:
    print('could not load the QR code')

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
#CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
CHROMEDRIVER_PATH = './chromedriver.exe'
driver = webdriver.Chrome(options=chrome_options, executable_path=CHROMEDRIVER_PATH)
driver.get(url)
driver.execute_script('window.print();')
time.sleep(5.0)
driver.quit()
