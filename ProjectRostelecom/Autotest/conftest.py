import pytest
from selenium import webdriver
# Объект который устанавливает и запускает хром драйвер
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    # Созлаем путь к драйверу
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    # Открывание браузера на все окно
    driver.maximize_window()
    yield driver
    # Выходим с драйвера
    driver.quit()

@pytest.fixture()
def cookie():
    # Опция для отключения cookie
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-cookies")
    # Создаем путь к драйверу
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service, options=options)
    # Открывание браузера на все окно
    driver.maximize_window()
    yield driver
    # Выходим с драйвера
    driver.quit()