import time

import pytest
from selenium import webdriver
from Page_Object.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
from utilities import XLutils

class Test_002_DDT_login:
    baseUrl =  Readconfig.getApplicationURL()
    path = r"C:\Users\Cliffex-Lead\Documents\Xl test.xlsx"


    logger = LogGen.loggen()

    def test_login_DDT(self,setup):
        self.logger.info("*******verify the login page******")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver)
        self.rows = XLutils.getRowCount(self.path, 'Sheet1')
        print("Numbers of row in excel", self.rows)
        lst_status = []

        for r in range(2, self.rows+1):
            self.user = XLutils.readData(self.path,"Sheet1",r,1)
            self.password = XLutils.readData(self.path,'Sheet1',r,2)
            self.result = XLutils.readData(self.path,'Sheet1',r,3)

            self.lp.set_username(self.user)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(3)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.result =="pass":
                    self.logger.info("************pass")
                    self.lp.click_logout()
                    lst_status.append("pass")

                elif self.result == "Fail":
                    self.logger.info("*****fail")
                    self.lp.click_logout()
                    lst_status.append("fail")

            elif act_title != exp_title:
                if self.result == "Pass":
                    self.logger.info("******fail")
                    # lst_status.append("fail")

                elif self.result =="fail":
                    self.logger.info("*****Passed")
                    lst_status.append("pass")


            if "Fail" not in lst_status:
                self.logger.info("**********login ddt passsed*****")
                self.driver.close()
                assert True
            else:
                self.logger.info("**************fail*****")
                self.driver.close()
                assert False


        self.logger.info("*****end test*******")
        self.logger.info("************Test_002_DDT_login************")







