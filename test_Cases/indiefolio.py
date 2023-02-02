import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

driver = webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe")
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.get('http://dev.getcreator.in/')
driver.get('http://cliffex:Cliffex@98765@dev.getcreator.in/')
driver.implicitly_wait(5)
title= driver.title
print(title)
if(title == "IndieFolio || Hire The Best Freelancers For Your Creative Needs"):
    print("Test Passed")
else:
     print("Test failed")

time.sleep(10)
get_url = driver.current_url

print("The current url is:"+str(get_url))



