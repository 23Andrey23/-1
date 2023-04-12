from settings import valid_password, valid_email
from api_19_7_2 import ApiPets
import os

pet = ApiPets()

def test_get_api_key(email=valid_email, password=valid_password):
    """ Проверяем, что запрос ключа API возвращает статус 200 и в результате содержит ключ слова"""
    status, result = pet.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_list_pets(filter='my_pets'):
    """ Проверяем, что запрос всех питомцев возвращает не пустой список"""

    _, auth_key = pet.get_api_key(valid_email, valid_password)
    status, result = pet.get_list_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0

def test_post_api_create_pet_simple_valid(name='Баф', animal_type='Собака', age='5'):
    """Проверяем, что этот запоос добавляет инфориацию о новом питомце"""

    _, auth_key = pet.get_api_key(valid_email, valid_password)
    status, result = pet.post_api_create_pet_simple(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name

def test_post_api_pets_set_photo_pet_id_valid(pet_photo='images/Dog.jpeg'):
    """Проверяем, что можем добавить фотографию домашнего животного"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pet.get_api_key(valid_email, valid_password)
    _, my_pets = pet.get_list_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pet.post_api_pets_set_photo_pet_id(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200
    else:
        raise Exception("Список пуст")

def test_get_api_key_not_valid_email(email="email", password=valid_password):
    """Проверяем, что пользователь не сможет войти в аккаунт с не валидной почтой"""
    status, result = pet.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result

def test_get_api_key_not_valid_password(email=valid_email, password="password"):
    """Проверяем, что пользователь не сможет войти в аккаунт с не валидным поролем"""
    status, result = pet.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result

def test_get_api_key_not_valid_password_and_email(email="email", password="password"):
    """Проверяем, что пользователь не сможет войти в аккаунт с не валидным поролем и почтой"""
    status, result = pet.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result

def test_post_api_create_pet_simple_not_valid_name(name="Баф", animal_type='Собака', age='5'):
    """Проверяем, что пользователь не может добавляет инфориацию о новом питомце без имени питомца"""

    _, auth_key = pet.get_api_key(valid_email, valid_password)
    status, result = pet.post_api_create_pet_simple(auth_key, name, animal_type, age)

    assert status == 400

def test_post_api_create_pet_simple_not_valid_age(name="Баф", animal_type='Собака', age=''):
    """Проверяем, что пользователь не может добавляет инфориацию о новом питомце без возроста питомца"""

    _, auth_key = pet.get_api_key(valid_email, valid_password)
    status, result = pet.post_api_create_pet_simple(auth_key, name, animal_type, age)

    assert status == 400

def test_post_api_pets_set_not_valid_photo():
    """Проверяем, пользователь не может отправить запрос на добавление фотографии
     домашнего животного без самой фотографии"""

    _, auth_key = pet.get_api_key(valid_email, valid_password)
    _, my_pets = pet.get_list_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pet.post_api_pets_set_photo_pet_id_not_valid_photo(auth_key, my_pets['pets'][0]['id'])
        assert status == 400
    else:
        raise Exception("Список пуст")

def test_post_api_pets_not_valid_animal_type(name='Персик', animal_type='', age="2", pet_photo='images/Unknown.jpeg'):
    """Проверяем, что пользователь не можно добавить питомца без типа животного"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pet.get_api_key(valid_email, valid_password)
    status, result = pet.post_api_pets(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert result['name'] == name
    # Баг

def test_post_api_pets_not_valid_name(name='', animal_type='Кот', age="2", pet_photo='images/Unknown.jpeg'):
    """Проверяем, что пользователь не можно добавить питомца без имени животного"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pet.get_api_key(valid_email, valid_password)
    status, result = pet.post_api_pets(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert result['name'] == name
    # Баг

def test_post_api_pets_not_valid_age(name='Персик', animal_type='Кот', age='', pet_photo='images/Unknown.jpeg'):
    """Проверяем, что пользователь не можно добавить питомца без возроста животного"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pet.get_api_key(valid_email, valid_password)
    status, result = pet.post_api_pets(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert result['name'] == name
    # Баг