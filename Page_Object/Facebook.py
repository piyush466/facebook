from selenium.webdriver.common.by import By
from selenium import webdriver


class FacebookLogin1:
    username_Name = "email"
    passwod_Name = "pass"
    click_on_Login_Id = "loginbutton"
    print_msg_valid_xpath = "//div[@class='_9ay7']"

    def __init__(self,driver):
        self.driver = driver

    def Set_username_fb(self,username):
        self.driver.find_element(By.NAME,self.username_Name).clear()
        self.driver.find_element(By.NAME,self.username_Name).send_keys(username)

    def Set_password_fb(self,password):
        self.driver.find_element(By.NAME,self.passwod_Name).clear()
        self.driver.find_element(By.NAME,self.passwod_Name).send_keys(password)

    def Set_Click_Login(self):
        self.driver.find_element(By.ID,self.click_on_Login_Id).click()

    def print_msg(self):
        self.p = self.driver.find_element(By.XPATH, self.print_msg_valid_xpath)
        print(self.p.text)
