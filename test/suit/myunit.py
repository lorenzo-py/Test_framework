import unittest
from selenium import webdriver
from utils.config import Config


class BaseTest(unittest.TestCase):
    def setUp(self):
        URL = Config().myget('URL')
        browser = Config().myget('browser')
        driverpath = Config().myget('driver_path')
        if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome(executable_path=driverpath)
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
        self.driver.implicitly_wait(20)
        self.driver.get(URL)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()