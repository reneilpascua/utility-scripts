import os
from sys import argv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

dirname = os.path.dirname(__file__)
DRIVER_PATH = os.path.join(dirname, 'driver/chromedriver')

options = Options()
options.headless = True
# options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
print('hello world')
driver.get(argv[1])
print(driver.page_source)
driver.quit()

