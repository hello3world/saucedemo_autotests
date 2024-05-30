import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from login_page import Login_page

# что бы не открывался браузер
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()

# вход на главную страницу
base_url = 'https://www.saucedemo.com/'
browser.get(base_url)
browser.maximize_window()
login_page = Login_page(browser)
login_name = "standard_user"
login_password = "secret_sauce"
login_page.autorization(login_name, login_password)

print("Приветствую тебя в нашем интернет-магазине")
products = browser.find_elements(By.XPATH,
                                 "//div[@class = 'inventory_item_name ']")

# собираем в список названия всех вещей на главной странице
products_names = []
for item in products:
    products_names.append(item.text)

# Предлагаем пользователю выбрать товар для проверки
print(
    "Выбери один из следующих товаров и укажи его номер: ")
for i in range(len(products_names)):
    print(f"{i + 1} - {products_names[i]}")
product_number = input()
print(f"You choose {products_names[int(product_number) - 1]}")

# собираем в список цены всех вещей на главной странице
prices = browser.find_elements(By.XPATH,
                               "//div[@class = 'inventory_item_price']")
products_prices = []
for item in prices:
    products_prices.append(item.text[1:])
print(products_prices)

# собираем в список кнопки "add to cart" всех вещей на главной странице
buttons = browser.find_elements(By.XPATH, "//button[contains(text(), 'Add to cart')]")

# информация о продукте
product_name = products_names[int(product_number) - 1]
product_price = products_prices[int(product_number) - 1]
buttons[int(product_number) - 1].click()

# открываем корзину
basket = browser.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
basket.click()
print('select basket')

# проверяем, что правильный товар добавлен в корзину
chosen_product = browser.find_element(By.XPATH, "//div[@class='inventory_item_name']")
chosen_product_name = chosen_product.text
print(chosen_product_name)
assert chosen_product_name == product_name
print("products names equal")

# проверяем, что цена в корзине соответствует цене на шлавной странице
price_basket_product = browser.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_price_basket_product = price_basket_product.text[1:]
assert value_price_basket_product == product_price
print("products prices equal")

# переходим в форму ввода данных для заказа
checkout = browser.find_element(By.XPATH, "//*[@id='checkout']")
checkout.click()

# заполняем форму
first_name = browser.find_element(By.XPATH, '//*[@id="first-name"]')
first_name.send_keys("Yauheni")
last_name = browser.find_element(By.XPATH, '//*[@id="last-name"]')
last_name.send_keys("Paulovich")
zip_code = browser.find_element(By.XPATH, '//*[@id="postal-code"]')
zip_code.send_keys("220102")
continue_button = browser.find_element(By.XPATH, '//*[@id="continue"]')
continue_button.click()
print("move to Checkout: Overview")

# проверяем страницу проверки правильности оформленного заказа
overview_product = browser.find_element(By.XPATH, "//div[@class='inventory_item_name']")
value_checkout_product = overview_product.text
assert value_checkout_product == product_name
print("overview: products names equal")
checkout_product_price = browser.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_checkout_product_price = checkout_product_price.text[1:]
assert value_checkout_product_price == product_price
print("overview: products prices equal")
price_total = browser.find_element(By.XPATH, '//div[@class="summary_total_label"]').text.split("$")[1]
price_tax = browser.find_element(By.XPATH, '//div[@class="summary_tax_label"]').text.split("$")[1]
assert float(price_total) == (float(price_tax) + float(value_checkout_product_price))
print("prices equal")
time.sleep(5)