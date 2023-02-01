from selenium.webdriver.common.by import By

from Page_Object.Facebook import FacebookLogin1
from selenium import webdriver
class Test_FB_login:
    Url = "https://www.facebook.com/login/"
    username = "piyushdravyakar@gmail.com"
    password = "piyush1234"

    def test_login_Homepage(self,setup):
        self.driver = setup
        self.driver.get(self.Url)
        act_title = self.driver.title
        print(self.driver.title)

        if act_title == "Log in to Facebook":
            print("Your test is pass")
            assert True
            self.driver.close()
        else:
            print("your test is fail")
            self.driver.close()
            assert False


    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.Url)
        self.fb = FacebookLogin1(self.driver)
        self.fb.Set_username_fb(self.username)
        self.fb.Set_password_fb(self.password)
        self.fb.Set_Click_Login()
        self.fb.print_msg()
        self.driver.close()







