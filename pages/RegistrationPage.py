import allure
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
from random import randint

class RegistrationPageLocators:
    PHONE_FIELD = (By.ID, 'field_phone')
    COUNTRY_LIST = (By.XPATH, '//div[@data-l="t,country"]')
    COUNTRY_ITEM = (By.XPATH, '//div[@class="country-select_code"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@data-l="t,submit"]')
    AGREEMENT_BUTTON = (By.XPATH, '//*[@data-l="t,agreement"]')
    PRIVACY_BUTTON = (By.XPATH, '//*[@data-l="t,privacy"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@data-l="t,support"]')


class RegistrationPageHelperHeler(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(RegistrationPageLocators.PHONE_FIELD)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST)
        self.find_element(RegistrationPageLocators.SUBMIT_BUTTON)
        self.find_element(RegistrationPageLocators.AGREEMENT_BUTTON)
        self.find_element(RegistrationPageLocators.PRIVACY_BUTTON)
        self.find_element(RegistrationPageLocators.SUBMIT_BUTTON)

    @allure.step("Выбираем рандомную страну в выпадающем списке")
    def select_random_country(self):
        random_number = randint(0, 212)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
        selected_country = country_items[random_number].text
        country_items[random_number].click()
        self.attach_screenshot()
        return selected_country

    @allure.step("Получаем код страны из поля ввода телефона")
    def get_phone_field_value(self):
        return self.find_element(RegistrationPageLocators.PHONE_FIELD).get_attribute("value")