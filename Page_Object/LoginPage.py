from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id ="Email"
    textbox_password_id="Password"
    Button_Login_Xpath="//button"
    logout_butn_LinkText="Logout"

    def __init__(self,driver):
        self.driver=driver

    def set_username(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)


    def set_password(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.Button_Login_Xpath).click()


    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT,self.logout_butn_LinkText).click()