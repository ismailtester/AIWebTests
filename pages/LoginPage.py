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
    REGISTER_BY_PHONE_BUTTON = (By.XPATH, '//a[@class="button-pro __sec mb-3x __wide"]')
    VK_REGISTER_BUTTON = (By.XPATH, '//*[@data-l="t,vkc"]')
    MAILRU_REGISTER_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_REGISTER_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')


class LoginPageHelper:
    pass