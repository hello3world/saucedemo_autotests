import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
browser.get(base_url)
browser.maximize_window()

# экземпляр класса ActionChains
action = ActionChains(browser)

price = browser.find_element(By.ID, 'id2')
action.click_and_hold(price).move_by_offset(20,0).release().perform()

time.sleep(10)
