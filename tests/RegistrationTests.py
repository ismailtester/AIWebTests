from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.RegistrationPage import RegistrationPageHelperHeler
from pages.LoginPage import LoginPageHelper


BASE_URL = "https://ok.ru/"




def test_registration_random_country(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_registration()
    RegistrationPage = RegistrationPageHelperHeler(browser)
    selected_country_code = RegistrationPage.select_random_country()
    actual_country_code =  RegistrationPage.get_phone_field_value()
    assert selected_country_code == actual_country_code
