from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelperHelper
import allure

BASE_URL = "https://ok.ru/"
LOGIN_TEXT = "ismailtester"
PASSWORD_TEXT = "qwerty123"

@allure.suite("Проверка восстановления пользователя")
@allure.title("Переход к восстановлению после нескольких неудачных попыток авторизации")
def test_go_to_recovery_after_many_fails(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.input_login(LOGIN_TEXT)

    for input in range(3):
        LoginPage.input_password(PASSWORD_TEXT)
        LoginPage.click_login()

    LoginPage.click_recovery()
    RecoveryPage = RecoveryPageHelperHelper(browser)

