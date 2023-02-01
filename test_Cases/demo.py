from selenium import webdriver


import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

test = Service(r"C:\Users\Cliffex-Lead\Desktop\piyush\chromedriver.exe")

driver = webdriver.Chrome(service=test)
driver.maximize_window()

# driver = webdriver.Chrome(executable_path=r"C:\Users\Cliffex-Lead\Desktop\piyush\chromedriver.exe")
driver.get("https://dev.mmabetclub.com/login")