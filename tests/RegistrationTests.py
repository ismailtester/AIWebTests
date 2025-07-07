from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.RegistrationPage import RegistrationPageHeler
from pages.LoginPage import LoginPageHelper
import allure


BASE_URL = "https://ok.ru/"




def test_registration_random_country(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_registration()
    RegistrationPage = RegistrationPageHeler(browser)
    selected_country_code = RegistrationPage.select_random_country()
    actual_country_code =  RegistrationPage.get_phone_field_value()
    print(selected_country_code, actual_country_code)
    assert selected_country_code == actual_country_code
