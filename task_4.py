# Импорт необходимых модулей из библиотеки Selenium
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time
from login_page import Login_page
# для применения явного ожидания
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# список usernames для тестирования
users = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"]
# пароль для входа
user_login_password = "secret_sauce"
# Создаем класс для тестирования страницы
class TestBuyLoginPage:
    """Класс включающий сценарий проверки страницы аутентификации"""

    def test_login_page(self, user_login_name, user_login_password):
        browser = webdriver.Chrome()
        base_url = 'https://www.saucedemo.com/'
        browser.get(base_url)
        browser.maximize_window()
        print("Start test")
        # создаем экземпляр класса страницы аутентификации
        login = Login_page(browser)
        try:
            login.autorization(user_login_name, user_login_password)
            print(f"Authorization complete for {user_login_name}")
            # проверка перехода на главную страницу
            header_logo = WebDriverWait(browser, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@class="app_logo"]')))
            value_header_logo = header_logo.text
            assert value_header_logo == "Swag Labs"
            print(f"Test passed successfully for {user_login_name}")
        except TimeoutException:
            print(
                f"TimeoutException: Authorization failed for user {user_login_name}")
            screenshot_name = f"screenshot_{user_login_name}.png"
            browser.save_screenshot('.\\errors_screens\\' + screenshot_name)
            print(f"Screenshot saved to {screenshot_name}")
        time.sleep(3)

test = TestBuyLoginPage()  # Создание экземпляра класса

for user in users:
    print("user = ", user)
    test.test_login_page(user, user_login_password)  # Вызов метода с тестом для каждого пользователя