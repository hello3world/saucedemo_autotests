# Импорт необходимых модулей из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Создание экземпляра веб-драйвера Chrome
browser = webdriver.Chrome()

# Установка базового URL-адреса для тестируемого веб-сайта
base_url = 'https://www.saucedemo.com/'

# Переход на указанный URL-адрес веб-сайта
browser.get(base_url)

# Максимизация окна браузера для обеспечения полного размера экрана
browser.maximize_window()

# Задержка выполнения скрипта на 2 секунды
time.sleep(2)

# Поиск поля ввода логина на странице по XPath и сохранение его в переменную
# user_name
user_name = browser.find_element(By.XPATH, '//*[@id="user-name"]')

# Ввод текста "standard_user" в поле ввода логина
user_name.send_keys("standard_user")

# Задержка выполнения скрипта на 2 секунды
time.sleep(2)

# Поиск поля ввода пароля на странице по XPath и сохранение его в переменную
# password
password = browser.find_element(By.XPATH, '//*[@id="password"]')

# Ввод текста "secret_sauce" в поле ввода пароля
password.send_keys("secret_sauce")

# Задержка выполнения скрипта на 2 секунды
time.sleep(2)

# Поиск кнопки входа на странице по XPath и сохранение ее в переменную
# button_login
button_login = browser.find_element(By.XPATH, '//*[@id="login-button"]')

# Нажатие на кнопку входа
button_login.click()

# Задержка выполнения скрипта на 10 секунд для того, чтобы убедиться, что
# страница полностью загрузилась и произошла авторизация
time.sleep(10)