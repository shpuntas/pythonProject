from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os
from selenium.webdriver.support.wait import WebDriverWait


# получить текст между открывающим и закрывающим тэгом
# x_element = browser.find_element_by_id("input_value")
# x = x_element.text

# ПОЛУЧИТЬ ЗНАЧЕНИЕ АТРИБУТА
# x = browser.find_element_by_id("treasure").get_attribute("valuex")

# ВЫБРАТЬ ИЗ ДРОПДАУНА
# select = Select(browser.find_element_by_id("dropdown"))
# select.select_by_value(f)

# МЕТОД
# def calc(x):
#          ln(abs(12*sin(x)))
#    return str(math.log(abs(12 * math.sin(int(x)))))
#
# потом в тесте его использовать так:
#     a = int(browser.find_element_by_id("input_value").text)
#     z = calc(a)

# ЯВАСКРИПТ
# input_field = browser.find_element_by_id("answer")
# browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)

# АТТАЧИ
#     current_dir = os.path.abspath(os.path.dirname("/Users/shpuntas/Downloads/"))
#     file_path = os.path.join(current_dir, "Untitled.txt")
#     attach_btn = browser.find_element_by_css_selector("[type=file]")
#     attach_btn.send_keys(file_path)

# АЛЕРТЫ
# апрувить:
# alert = browser.switch_to.alert
# alert.accept()
#
# получить текст:
# alert = browser.switch_to.alert
# alert_text = alert.text
#
# окна типа confirm (если есть выбор, согласиться или отказаться):
# confirm = browser.switch_to.alert
# confirm.accept()/confirm.dismiss()
#
# окна типа prompt (надо ввести какие-то данные):
# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()

# ВКЛАДКИ
# browser.switch_to.window(window_name)
#
# узнать имя вкладки:
# new_window = browser.window_handles[1] - новой
# first_window = browser.window_handles[0] - изначальной

# ОЖИДАНИЯ
# говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
#
# говорим Selenium waitUntil
# button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
#
# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
# button = WebDriverWait(browser, 5).until_not(EC.element_to_be_clickable((By.ID, "verify")))
#
# WebDriverWait(browser, 12).until(
#         EC.text_to_be_present_in_element((By.ID, "price"), "$100")
#     )


link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    browser = webdriver.Chrome(executable_path="../driver/chromedriver")
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element_by_id("book").click()
    a = int(browser.find_element_by_id("input_value").text)
    z = calc(a)
    browser.find_element_by_id("answer").send_keys(z)
    browser.find_element_by_id("solve").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
