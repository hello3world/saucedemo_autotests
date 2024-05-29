import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_page:
    def __init__(self, browser):
        self.browser = browser

    def autorization(self, login_name, login_password):
        # поле логина
        login_name_field = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="user-name"]')))
        login_name_field.send_keys(login_name)

        # поле пароля
        login_password_field = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
        login_password_field.send_keys(login_password)

        # кнопка для входа
        button_login = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="login-button"]')))
        if login_name == "performance_glitch_user":
            time.sleep(5)
        button_login.click()
