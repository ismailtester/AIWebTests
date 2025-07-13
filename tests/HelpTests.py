import allure
from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageLocators, HelpPageHelperHeler
from pages.AdvertisementCabinetHelp import AdvertisementPageHelperHelper

BASE_URL = "https://ok.ru/help"



@allure.suite("Проверка страницы помощи")
@allure.title("Переход к странице 'Рекламный кабинет'")
def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelperHeler(browser)
    HelpPage.scrollToitem(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementPageHelperHelper(browser)
