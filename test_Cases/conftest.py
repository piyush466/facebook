from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


@pytest.fixture()
def setup(browser):
    # driver = webdriver.Firefox(executable_path=r"C:\Users\Cliffex-Lead\Desktop\chrome123\geckodriver.exe")
    # global driver
    if browser=="chrome":

        # object = Service(r"C://Users//Cliffex-Lead//Desktop//piyush//chromedriver.exe")
        # driver = webdriver.Chrome(service=object)
        driver= webdriver.Chrome(executable_path=r"C:\Users\Cliffex-Lead\Desktop\piyush\chromedriver.exe")
        print("Lauching the chrome browser........")
        driver.maximize_window()

    elif browser=="firefox":
        driver = webdriver.Chrome(executable_path=r"C:\Users\Cliffex-Lead\Desktop\piyush\chromedriver.exe")
        print("Lauching the firefox browser........")
        driver.maximize_window()

    else:
        # object = Service(r"C://Users//Cliffex-Lead//Desktop//piyush//chromedriver.exe")
        # driver = webdriver.Chrome(service=object)
        driver = webdriver.Chrome(executable_path=r"C:\Users\Cliffex-Lead\Desktop\piyush\chromedriver.exe")
        print("Lauching the chrome browser........")
        driver.maximize_window()


    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



###############pytest HTML reports###################

#hook for adding environment info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Facebook home page'
    config._metadata['Module Name'] = 'facebook'
    config._metadata['Tester'] = 'Piyush'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

