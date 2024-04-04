from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# что бы не открывался браузер
options = webdriver.ChromeOptions()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)

# browser = webdriver.Chrome()

base_url = 'https://www.saucedemo.com/'
browser.get(base_url)
browser.maximize_window()
# поле логина
user_name = browser.find_element(By.XPATH, '//*[@id="user-name"]')
user_name.send_keys("standard_user")
# поле пароля
password = browser.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("secret_sauce")
# кнопка
button_login = browser.find_element(By.XPATH, '//*[@id="login-button"]')
button_login.click()

"""INFO PRODUCT #1"""
print("INFO PRODUCT #1")
product_1 = browser.find_element(By.XPATH, "//*[@id='item_4_title_link']/div")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = browser.find_element(By.XPATH, "//*[@id='inventory_container"
                                           "']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

"""Bring product #1 to basket"""
select_product_1 = browser.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print('select_product_1')

"""Delete product from basket"""
select_product_1 = browser.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
select_product_1.click()
print('product_1 delete from basket')

"""Bring product #1 to basket"""
select_product_1 = browser.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print('select_product_1')

"""INFO PRODUCT #2"""
print("INFO PRODUCT #2")
product_2 = browser.find_element(By.XPATH, '//*[@id="item_1_title_link"]/div')
value_product_2 = product_2.text
print(value_product_2)

price_product_2 = browser.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div')
value_price_product_2 = price_product_2.text
print(value_price_product_2)

"""Bring product #2 to basket"""
select_product_2 = browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
select_product_2.click()
print('select_product_2')

"""Open basket"""
basket = browser.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
basket.click()
print('select basket')

"""INFO basket PRODUCT #1"""
print("INFO basket PRODUCT #1")
basket_product_1 = browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
value_basket_product_1 = basket_product_1.text
print(value_product_1)
print("value_basket_product_1", value_basket_product_1)
assert value_product_1 == value_basket_product_1
print("products names equal")

price_basket_product_1 = browser.find_element(By.XPATH, "//*[@id='cart_contents_container']"
                                              "/div/div[1]/div[3]/div[2]/div[2]/div")
value_basket_price_product_1 = price_basket_product_1.text
print(value_basket_price_product_1)
assert value_price_product_1 == value_basket_price_product_1
print("products prices equal")

"""Checkout"""
Checkout = browser.find_element(By.XPATH, "//*[@id='checkout']")
Checkout.click()


"""Checkout: Your Information"""
first_name = browser.find_element(By.XPATH, '//*[@id="first-name"]')
first_name.send_keys("Yauheni")
last_name = browser.find_element(By.XPATH, '//*[@id="last-name"]')
last_name.send_keys("Paulovich")
zip_code = browser.find_element(By.XPATH, '//*[@id="postal-code"]')
zip_code.send_keys("220102")

continue_button = browser.find_element(By.XPATH, '//*[@id="continue"]')
continue_button.click()
print("select continue_button")


"""Checkout: Overview products"""
checkout_product_1 = browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
checkout_value_product_1 = checkout_product_1.text
assert checkout_value_product_1 == value_product_1

checkout_product_2 = browser.find_element(By.XPATH, '//*[@id="item_1_title_link"]/div')
checkout_value_product_2 = checkout_product_2.text
assert checkout_value_product_2 == value_product_2

"""Checkout: Overview prices"""
checkout_price_product_1 = browser.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_checkout_price_product_1 = checkout_price_product_1.text
assert value_checkout_price_product_1 == value_price_product_1

checkout_price_product_2 = browser.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_checkout_price_product_2 = checkout_price_product_2.text
assert value_checkout_price_product_2 == value_price_product_2
print("Checkout: Overview - prices and product equal")

"""Checking prices"""
price_total = browser.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]').text.split("$")[1]

assert float(price_total) == (float(value_checkout_price_product_1[1:]) + float(value_checkout_price_product_2[1:]))
print("prices equal")

time.sleep(5)