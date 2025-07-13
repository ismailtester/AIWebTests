import allure
from selenium.webdriver import ActionChains
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By

class AdvertisementPageLocators:
    TITLE = (By.XPATH, '//span[text()="Рекламный кабинет"]')


class AdvertisementPageHelperHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(AdvertisementPageLocators.TITLE)
