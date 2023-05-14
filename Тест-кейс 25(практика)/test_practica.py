from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import math

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome("/Users/andreyshebarshov/Desktop/pythonProject/chromdriver/chromedriver")
    pytest.driver.get("https://petfriends.skillfactory.ru/login")

    yield

    pytest.driver.quit()

def test_show_my_pets():
    """Вводим почту"""
    pytest.driver.find_element(By.ID, "email").send_keys("shebarshov2015@mail.ru")
    """Вводим пароль"""
    pytest.driver.find_element(By.ID, "pass").send_keys("05451242")
    """Нажимаем на кнопку входа"""
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    """Проверяем, что мы оказались на главной странице пользователя """
    assert pytest.driver.find_element(By.PARTIAL_LINK_TEXT, 'PetFriends').text == "PetFriends"


    """Нажать на кнопку Мои питомцы"""
    pytest.driver.find_element(By.PARTIAL_LINK_TEXT, 'Мои питомцы').click()
    """Имена моих питомцев"""
    name = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
    """Порода моих питомцев"""
    breed = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[2]')
    """Возвраст моих питомцев"""
    age = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]')
    """Фото моих питомцев"""
    photo = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/th/img')
    """Статистика пользователя"""
    user_statistics = pytest.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]')
    """Кол-во питомцев"""
    num_pets = int(user_statistics.text[22:24])

    """Тес-кейсы страницы Мои питомцы"""

    """Валидность данных кол-во питомцев в статистики пользователя"""
    if len(name) != "":
        assert len(name) == num_pets
    """У половины или больше половины Моих питомцев есть фото"""
    # Мои питомцы с фото
    num_photo = 0
    for i in range(len(name)):
        if photo[i].get_attribute('src') != '':
            num_photo += 1
    polovina = num_pets / 2
    polovina = math.floor(polovina)
    assert polovina <= num_photo
    """У всех питомцев есть имя, возраст и пород"""
    counter = {}
    for i in range(len(name)):
        assert name[i].text != ''
        assert breed[i].text != ''
        assert age[i].text != ''
        """У всех питомцев разные имена"""
        parts_name = name[i].text.split(" ")
        for elem in parts_name:
            counter[elem] = counter.get(elem, 0) + 1
        povtor = {elem: counter for elem, counter in counter.items() if counter > 1}
        assert povtor == {}
    """В списке нет повторяющихся питомцев"""
    pets_list = []
    for i in range(len(name)):
        # Добавляем информацию о питомце в список
        pet_info = (name[i].text, breed[i].text, age[i].text)
        pets_list.append(pet_info)
    assert len(set(pets_list)) == len(pets_list)

    """Тест-кейсы с явными ожиданиями элементов"""

    """Ожидаем присутствия элемента в структуре документа для шапки таблицы Мои питомцы"""
    photo_elem = WebDriverWait(pytest.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/thead/tr/th[1]')))
    name_elem = WebDriverWait(pytest.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/thead/tr/th[2]')))
    breed_elem = WebDriverWait(pytest.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/thead/tr/th[3]')))
    age_elem = WebDriverWait(pytest.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/thead/tr/th[4]')))
    """Видет ли пользователь изображение питомца"""
    photo_sheredor = WebDriverWait(pytest.driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr[3]/th/img')))
    photo_sim = WebDriverWait(pytest.driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr[4]/th/img')))
    photo_rg = WebDriverWait(pytest.driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr[5]/th/img')))
    """Валидность текста в шапке таблице Мои питомцы"""
    photo_text = WebDriverWait(pytest.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/thead/tr/th[1]')))
    name_text = WebDriverWait(pytest.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/thead/tr/th[2]')))
    breed_text = WebDriverWait(pytest.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/thead/tr/th[3]')))
    age_text = WebDriverWait(pytest.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/thead/tr/th[4]')))
    """На месте для изображения питомца у которого нет фото, ожидается невидимость элемента"""
    photo_fd = WebDriverWait(pytest.driver, 3).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr[1]/th/img')))
    photo_pers = WebDriverWait(pytest.driver, 3).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr[2]/th/img')))

    """Тест-кейсы страницы Все питомцы с неявными ожиданиями элементов"""

    # Активируем неявные ожидания
    pytest.driver.implicitly_wait(2)
    pytest.driver.get("https://petfriends.skillfactory.ru/all_pets")

    # Фото питомцев
    images = pytest.driver.find_elements(By.CSS_SELECTOR, ".card-deck .card-img-top")
    # Имена питомцев
    name = pytest.driver.find_elements(By.CSS_SELECTOR, ".card-deck .card-title")
    # Пророда и возраст питомцев
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, ".card-deck .card-text")
    for i in range(len(name)):
        """Фото есть у всех питомцев"""
        assert images[i].get_attribute('src') != ''
        """Имя есть у всех питомцев"""
        assert name[i].text != ''
        """Пророда и возраст есть у всех питомцев"""
        assert descriptions[i].text != ''
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
    """Проверяем, что мы оказались на главной странице пользователя """
    assert pytest.driver.find_element(By.PARTIAL_LINK_TEXT, 'PetFriends').text == "PetFriends"