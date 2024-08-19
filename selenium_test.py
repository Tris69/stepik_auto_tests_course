from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация браузера Chrome
driver = webdriver.Chrome()

try:
    # Открываем веб-страницу
    driver.get("https://www.google.com")

    # Явное ожидание для поиска элемента
    wait = WebDriverWait(driver, 10)

    # Найти элемент поиска по имени
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))

    # Ввести текст в поле поиска
    search_box.send_keys("OpenAI GPT-4")

    # Отправить форму поиска
    search_box.submit()

    # Явное ожидание загрузки результатов поиска
    wait.until(EC.presence_of_element_located((By.ID, "search")))

    # Выводим на экран заголовок страницы после выполнения поиска
    print("Page title after search:", driver.title)

    # Задержка для демонстрации, чтобы браузер не закрывался сразу
    import time
    time.sleep(5)
    
finally:
    # Закрываем браузер
    driver.quit()
