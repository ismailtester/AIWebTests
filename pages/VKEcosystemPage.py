import allure
from selenium.webdriver import ActionChains
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By


class VKEcosystemPageLocators:
    VK_LOGO = (By.ID, 'header-logo')
    ABOUT_BUTTON = (By.XPATH, '//*[contains(@class, "Header_menuList")]/a[contains(@href, "/company/about/")]')
    PROJECTS_BUTTON = (By.XPATH, '//*[contains(@class, "Header_menuList")]/a[contains(@href, "/projects")]')
    FOR_BUSINESS_BUTTON = (By.XPATH, '//*[contains(@class, "Header_menuList")]/a[contains(@href, "/business")]')
    VK_CAREER = (By.XPATH, '//*[contains(@class, "Header_menuList")]/a[@href="https://team.vk.company/"]')
    PRESS_BUTTON = (By.XPATH, '//*[contains(@class, "Header_menuList")]/a[contains(@href, "/press/releases")]')
    INVESTORS_BUTTON = (By.XPATH, '//*[contains(@class, "Header_menuList")]/a[contains(@href, "/investors")]')
    ESG_BUTTON = (By.XPATH, '//*[contains(@class, "Header_menuList")]/a[contains(@href, "/esg")]')
    EVENTS_BUTTON = (By.XPATH, '//*[contains(@class, "Header_menuList")]/a[contains(@href, "/press/events")]')
    SEARCH_BUTTON = (By.XPATH, '//*[@href="/search/"]')
    CHANGE_LANGUAGE_BUTTON = (By.XPATH, '//button[@aria-label="English"]')


class VKEcosystemPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(VKEcosystemPageLocators.VK_LOGO)
        self.find_element(VKEcosystemPageLocators.ABOUT_BUTTON)
        self.find_element(VKEcosystemPageLocators.PROJECTS_BUTTON)
        self.find_element(VKEcosystemPageLocators.FOR_BUSINESS_BUTTON)
        self.find_element(VKEcosystemPageLocators.VK_CAREER)
        self.find_element(VKEcosystemPageLocators.PRESS_BUTTON)
        self.find_element(VKEcosystemPageLocators.INVESTORS_BUTTON)
        self.find_element(VKEcosystemPageLocators.ESG_BUTTON)
        self.find_element(VKEcosystemPageLocators.EVENTS_BUTTON)
        self.find_element(VKEcosystemPageLocators.SEARCH_BUTTON)
        self.find_element(VKEcosystemPageLocators.CHANGE_LANGUAGE_BUTTON)



