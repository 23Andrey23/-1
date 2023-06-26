from urllib.parse import urlparse
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait



class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # Открытие страницы
    def open(self):
        self.driver.get(self.url)

    # Нахождение видимого элемента
    def element_is_visible(self, locator, timeout=10):
        # Драйвер подождет 5 сек, пока этот элемент не будет виден
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    # Нахождение видимых элементов
    def elements_are_visible(self, locator, timeout=10):
        # Драйвер подождет 5 сек, пока все элементы не будет видны
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    # Найти текст элемента
    def elements_is_present(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    # Найти тексты элементов
    def elements_are_presents(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    # Нахождение не видимого элемента
    def element_is_not_visible(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    # Необходимо чтобы элемент стал кликабельным
    def element_is_clickabele(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    # Скролит страницу до нужного нам элемента
    def go_to_element(self, element):
        self.driver.execute_script("argument[0].scrollIntoView();", element)

    # Возвращает относительный путь до текущей страницы
    def get_relative_link_http(self):
        url = self.driver.current_url
        return url

    # Возвращает относительный путь до текущей страницы (без домена)
    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    # Получение текущего URL без идентификатора
    def get_relative_not_id(self):
        url = self.driver.current_url.split('?')[0]
        return url

    # Переключение на новую открытую вкладку
    def new_window(self):
        url = self.driver.switch_to.window(self.driver.window_handles[-1])
        return url

    # Проверяем что, cookie отключены
    def cookie_disabled(self):
        self.driver.execute_script('return navigator.cookieEnabled')


    def get_attribute(self, element):
        return element.get_attribute("value")