import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Создание экземпляра веб-драйвера Chrome
browser = webdriver.Chrome()

# Установка базового URL-адреса для тестируемого веб-сайта
base_url = 'https://demoqa.com/date-picker'

# Переход на указанный URL-адрес веб-сайта
browser.get(base_url)

# Максимизация окна браузера для обеспечения полного размера экрана
browser.maximize_window()

# Ожидание загрузки страницы
time.sleep(2)

# Находим поле даты
date_input = browser.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
time.sleep(2)
date_input.click()
time.sleep(2)

# Очищаем поле даты
date_input.send_keys(Keys.CONTROL + 'a')
date_input.send_keys(Keys.BACKSPACE)
time.sleep(2)

# Получаем текущую дату и добавляем 10 дней
current_date = datetime.datetime.now()
new_date = current_date + datetime.timedelta(days=10)

# Преобразуем новую дату в нужный формат
new_date_str = new_date.strftime("%m/%d/%Y")

# Вводим новую дату в поле
date_input.send_keys(new_date_str)
date_input.send_keys(Keys.ENTER)

# Печатаем текущую и новую дату для проверки
print("Current date:", current_date.strftime("%m/%d/%Y"))
print("New date (10 days later):", new_date_str)

# Закрытие браузера
time.sleep(5)
browser.quit()