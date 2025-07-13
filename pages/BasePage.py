from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import allure

class BasePageLocators:
    TOOLBAR_LOGO = (By.ID, 'nohook_logo_link')
    TOOLBAR_SEARCH = (By.XPATH, '//input[@data-tsid="toolbar-search-input"]')
    VK_ECOSYSTEM = (By.XPATH, '//*[@data-module="VkEcosystem"]')
    MORE_BUTTON = (By.XPATH, '//*[@data-l="t,more"]')



class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver

    def check_page(self):
        self.find_element(BasePageLocators.TOOLBAR_LOGO)
        self.find_element(BasePageLocators.VK_ECOSYSTEM)

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator), message=f"Не удалось найти элемент {locator}")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_all_elements_located(locator), message=f"Не удалось найти элементы {locator}")

    @allure.step("Открываем страницу")
    def get_url(self, url):
        return self.driver.get(url)

    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), "скриншот", allure.attachment_type.PNG)

    @allure.step("Нажимаем на кнопку экосистемы")
    def click_vk_ecosystems(self):
        self.find_element(BasePageLocators.VK_ECOSYSTEM).click()

    @allure.step("Нажимаем на кнопку 'еще'")
    def click_more_button(self):
        self.find_element(BasePageLocators.MORE_BUTTON).click()

    def get_windows_id(self, index):
        return self.driver.window_handles[index]

    @allure.step('Переключаемся на другую вкладку')
    def switch_window(self, window_id):
        self.driver.switch_to.window(window_id)



