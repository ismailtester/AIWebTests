import allure
from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelpPage import HelpPageLocators, HelpPageHeler
from pages.AdvertisementCabinetHelp import AdvertisementPageHelper

BASE_URL = "https://ok.ru/help"



@allure.suite("Проверка страницы помощи")
@allure.title("Переход к странице 'Рекламный кабинет'")
def test_help_test(browser):
    BasePage(browser).get_url(BASE_URL)
    HelpPage = HelpPageHeler(browser)
    HelpPage.scrollToitem(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementPageHelper(browser)
