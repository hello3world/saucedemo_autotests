# Импорт необходимых модулей из библиотеки Selenium
from datetime import datetime

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time
from login_page import Login_page
# для применения явного ожидания
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Создаем класс для тестирования страницы
class TestBuyLoginPage:
    """Класс включающий сценарий проверки страницы аутентификации"""

    def test_login_page(self):
        browser = webdriver.Chrome()
        base_url = 'https://www.saucedemo.com/'
        browser.get(base_url)
        browser.maximize_window()
        print("Start testing")

        # создаем экземпляр класса страницы аутентификации
        login = Login_page(browser)

        # список usernames для тестирования
        users = ["standard_user", "locked_out_user", "problem_user",
                 "performance_glitch_user"]

        # пароль для входа
        user_login_password = "secret_sauce"

        for user in users:
            print("-" * 30)
            print("user = ", user)
            try:
                login.autorization(user, user_login_password)
                print(f"Authorization complete for {user}")
                # проверка перехода на главную страницу
                header_logo = WebDriverWait(browser, 30).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//*[@class="app_logo"]')))
                value_header_logo = header_logo.text
                assert value_header_logo == "Swag Labs"
                print(f"Test passed successfully for {user}")
                browser.back()
            except Exception as E:
                print(
                    f"{E}: Authorization failed for user {user}")
                current_date = datetime.now()
                str_current_date = current_date.strftime("%m.%d.%Y")
                screenshot_name = f"screenshot_{user}_{str_current_date}.png"
                browser.save_screenshot('.\\errors_screens\\' + screenshot_name)
                print(f"Screenshot saved to {screenshot_name}")
            finally:
                browser.refresh()

test = TestBuyLoginPage()  # Создание экземпляра класса
test.test_login_page()