import time

#webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс Ву, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# #Инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()
#
#
#Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://suninjuly.github.io/text_input_task.html")
time.sleep(2) #команда time.sleep() устанавливает паузу чтобы успеть посмотреть что происходит в браузере
#
# # Метод find_element позволяет найти нужный элемент на сайте, указав нужный путь к нему
# # Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать.
#
# # ищем поле для ввода текста
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
time.sleep(2)
#
# # напишем текст в найденном поле
textarea.send_keys('get()')
time.sleep(2)
#
# # найдем кнопку, которая отправяет введенное решение
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
#
# # скажем драйверу нажать на кнопку. После этого ответа мы увидим сообщение о правильном ответе
submit_button.click()
time.sleep(5)
driver.quit()