import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_TAB_BUTTON = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QR_TAB_BUTTON  = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    SIGNIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    QR_SIGNIN_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    RESTORE_PASSWORD_BUTTON = (By.XPATH, '//*[@data-l="t,restore"]')
    REGISTER_BY_PHONE_BUTTON = (By.XPATH, '//div[@class="external-oauth-login-footer"]/a[@data-l="t,register"]')
    VK_REGISTER_BUTTON = (By.XPATH, '//*[@data-l="t,vkc"]')
    MAILRU_REGISTER_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_REGISTER_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')
    RETURN_BUTTON = (By.XPATH, '//*[@data-l="t,cancel"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@role="button"]/*[@class="external-oauth-login_title-tx"]')
    RESTORE_PROFILE_BUTTON = (By.XPATH, '//*[@class="form-actions"]/*[@data-l="t,restore"]')




class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_TAB_BUTTON)
        self.find_element(LoginPageLocators.QR_TAB_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.SIGNIN_BUTTON)
        self.find_element(LoginPageLocators.QR_SIGNIN_BUTTON)
        self.find_element(LoginPageLocators.RESTORE_PASSWORD_BUTTON)
        self.find_element(LoginPageLocators.REGISTER_BY_PHONE_BUTTON)
        self.find_element(LoginPageLocators.VK_REGISTER_BUTTON)
        self.find_element(LoginPageLocators.MAILRU_REGISTER_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_REGISTER_BUTTON)

    @allure.step("Нажимаем на кнопку 'Войти'")
    def click_login(self):
        self.find_element(LoginPageLocators.SIGNIN_BUTTON).click()
        self.attach_screenshot()

    @allure.step("Получаем текст ошибки")
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text


    @allure.step("Вводим логин")
    def input_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()


    @allure.step("Вводим пароль")
    def input_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()


    @allure.step("Переходим к восстановлению")
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RESTORE_PROFILE_BUTTON).click()


