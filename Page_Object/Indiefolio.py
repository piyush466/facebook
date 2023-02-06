import time

from selenium.webdriver.common.by import By
from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

class Indie:
    Xpath_login_btn = "//a[@class='nav-link mobile-ipad-none']"
    username_Xpath = "//input[@type='email']"
    username_btn_xpath = "//button[@type='submit']"
    password_textbox_by_xpath = "//input[@type='password']"
    password_btn_xpath = "//button[@type='submit']"
    click_activeproject_xpath = "//a[text()='Active Projects']"
    click_completedproject_xpath = "//a[text()='Completed Projects']"
    Total_completedprojects_xpath = "//div[@id='profile']/div/div/div/div/div/div/div[2]/p"

    def __init__(self, driver):
        self.driver = driver

    def Set_click_login(self):
        self.driver.find_element(By.XPATH, self.Xpath_login_btn).click()
        print("piyush")
        time.sleep(4)

    def Set_username(self,username):
        self.driver.find_element(By.XPATH,self.username_Xpath).send_keys(username)

    def Set_clickon_username_btn(self):
        self.driver.find_element(By.XPATH,self.username_btn_xpath).click()

    def Set_password(self,password):
        self.driver.find_element(By.XPATH, self.password_textbox_by_xpath).send_keys(password)


    def Set_clickon_password_btn(self):
        self.driver.find_element(By.XPATH,self.password_btn_xpath).click()

    def click_active_project(self):
        self.driver.find_element(By.XPATH, self.click_activeproject_xpath).click()

    def click_completed_poject(self):
        self.driver.find_element(By.XPATH,self.click_completedproject_xpath).click()
        print("pass")

    # def total_completed_projects(self):
    #     self.totals = self.driver.find_element(By.XPATH,self.Total_completedprojects_xpath)



