from selenium.webdriver.common.by import By
from test.pages.page import Page

class LoginPage(Page):
    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')
    locator_csdn = (By.XPATH, '//a[@class = "favurl"]')

    def search01(self,data):
        self.driver.find_element(*LoginPage.locator_kw).send_keys(data)
        self.driver.find_element(*LoginPage.locator_su).click()