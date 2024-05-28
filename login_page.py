from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login_page:
    def __init__(self, browser):
        self.browser = browser

    def autorization(self, login_name, login_password):
        # поле логина
        login_name = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="user-name"]')))
        login_name.send_keys("standard_user")
        # поле пароля
        login_password = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
        login_password.send_keys("secret_sauce")
        # кнопка для входа
        button_login = WebDriverWait(self.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))
        button_login.click()