# Импорт необходимых модулей из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# для применения явного ожидание
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем класс для тестирования
class TestBuyProduct:
    """Класс включающий сценарий покупки товара"""
    def test_select_product(self):
        browser = webdriver.Chrome()
        base_url = 'https://www.saucedemo.com/'
        browser.get(base_url)
        browser.maximize_window()
        print("Start test")
        # поле логина
        user_name = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="user-name"]')))
        user_name.send_keys("standard_user")
        # поле пароля
        password = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
        password.send_keys("secret_sauce")
        # кнопка для входа
        button_login = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))
        button_login.click()
        # продукт
        select_product = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')))
        select_product.click()
        print("Select product")
        # корзина
        shopping_cart = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="shopping_cart_link"]')))
        shopping_cart.click()
        print("Transition to cart")
        header_product = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="inventory_item_name"]')))
        value_header_product = header_product.text
        assert value_header_product == "Sauce Labs Backpack"
        print("Successful Finish test")
        time.sleep(10)
test = TestBuyProduct()  # Создание экземпляра класса
test.test_select_product()  # Вызов метода с тестом
