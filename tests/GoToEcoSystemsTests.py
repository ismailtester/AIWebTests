from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.VKEcosystemPage import VKEcosystemPageHelper
import allure

BASE_URL = "https://ok.ru/"

@allure.suite("Проверка тулбара")
@allure.title("Переход к проектам экосистемы VK")
def test_open_vkecosystems(browser):
    BasePage = BasePageHelper(browser)
    BasePage.get_url(BASE_URL)
    BasePage.check_page()
    LoginPage = LoginPageHelper(browser)
    current_window_id = LoginPage.get_windows_id(0)
    LoginPage.click_vk_ecosystems()
    LoginPage.click_more_button()
    new_window = LoginPage.get_windows_id(1)
    LoginPage.switch_window(new_window)
    VKEcosystemPage = VKEcosystemPageHelper(browser)
    VKEcosystemPage.check_page()
    VKEcosystemPage.switch_window(current_window_id)
    LoginPage.check_page()
