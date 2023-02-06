import time

from Page_Object.Indiefolio import Indie
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_indifolio:
    url = "http://cliffex:Cliffex@98765@dev.getcreator.in/"
    username = "piyusha@cliffex.com"
    password = "Piyush@123"




    def test_login_Homepage(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        time.sleep(3)
        self.Ind = Indie(self.driver)
        self.Ind.Set_click_login()
        self.Ind.Set_username(self.username)
        self.Ind.Set_clickon_username_btn()
        time.sleep(2)
        self.Ind.Set_password(self.password)
        time.sleep(3)
        self.Ind.Set_clickon_password_btn()
        # self.driver.close()



    def test_title(self,setup):
        self.test_login_Homepage(setup)
        time.sleep(4)
        self.Ind.click_active_project()
        time.sleep(1)
        self.Ind.click_completed_poject()
        time.sleep(15)
        # self.Ind.total_completed_projects()

        # Total_completedprojects_xpath = "//div[@id='profile']/div/div/div/div/div/div/div[2]/p"
        self.totalcp= self.driver.find_elements(By.XPATH,"//div[@id='profile']/div/div/div/div/div/div/div[2]/p")
        for total in self.totalcp:
            print(total)























