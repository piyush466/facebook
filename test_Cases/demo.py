from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path=r"C:\Users\Cliffex-Lead\Desktop\piyush\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get('https://ultimateqa.com/dummy-automation-websites/')
print(driver.current_url)

driver.find_element(By.XPATH,"(//span[@class='lwptoc_item_label'])[1]").click()

est = driver.current_url
print("after click button:-"+est)

