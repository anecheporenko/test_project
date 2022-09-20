# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из
# библиотеки expected_conditions.
price_area = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

# Нажатие на кнопку "Book":
book_button = browser.find_element(By.CSS_SELECTOR, "#book")
book_button.click()

# Рассчет формулы:
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
print(y)

input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
input1.send_keys(y)

# Нажатие на кнопку "Submit":
button_submit = browser.find_element(By.CSS_SELECTOR, "#solve")
button_submit.click()

time.sleep(2)
browser.quit()