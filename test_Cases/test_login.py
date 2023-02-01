import pytest
from selenium import webdriver
from Page_Object.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen

class Test_001_login:
    baseUrl =  Readconfig.getApplicationURL()
    username = Readconfig.getusernamee()
    password = Readconfig.get_password()

    logger = LogGen.loggen()

    def test_homepage(self,setup):
        self.logger.info("*********Test_001_login*********")
        self.logger.info("*******Started******")
        self.logger.debug("***********hello****************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title =self.driver.title
        print(self.driver.title)

        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("*******Pass******")
            assert True

        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_homepage.png")
            self.driver.close()
            self.logger.info("*******Fail******")
            assert False




    def test_login(self,setup):
        self.logger.info("*******verify the login page******")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        print(self.driver.title)
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administratio":
            self.logger.info("*******Pass******")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_login.png")
            self.logger.info("*******Fail******")
            self.driver.close()
            assert False


