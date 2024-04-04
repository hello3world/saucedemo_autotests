from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

# что бы не открывался браузер
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# browser = webdriver.Chrome(options=options)

browser = webdriver.Chrome()

base_url = 'https://demoqa.com/buttons'
browser.get(base_url)
browser.maximize_window()

action = ActionChains(browser)
double_button = browser.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
action.double_click(double_button).perform()

right_button = browser.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
action.context_click(right_button).perform()


time.sleep(5)