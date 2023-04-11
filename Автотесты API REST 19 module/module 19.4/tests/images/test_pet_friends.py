from settings import valid_password, valid_email
from api import ApiPet
import os

pet = ApiPet()

def test_get_api_key(email=valid_email, password=valid_password):
    """ Проверяем, что запрос ключа API возвращает статус 200 и в результате содержит ключ слова"""
    status, result = pet.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_list_pets(filter='my_pets'):
    """ Проверяем, что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем ключ API и сохраняем его в переменной auth_key. Далее, используя этот ключ
    запрашиваем список всех питомцев и проверяем, что список не пуст."""

    _, auth_key = pet.get_api_key(valid_email, valid_password)
    status, result = pet.get_list_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0

def test_post_api_pets(name='Персик', animal_type='Кот', age="2", pet_photo='images/Unknown.jpeg'):
    """Проверяем, что можно добавить питомца с корректными данными"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pet.get_api_key(valid_email, valid_password)
    status, result = pet.post_api_pets(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name

def test_put_api_pets(name='Персик', animal_type='Шатланский кот', age='2'):
    """Проверяем возможность обновления информации о питомце"""

    _, auth_key = pet.get_api_key(valid_email, valid_password)
    _, my_pets = pet.get_list_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pet.put_api_pets(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['animal_type'] == animal_type
    else:
        raise Exception("Список пуст")

def test_delete_api_pets():
    """Проверяем возможность удаления питомца"""

    _, auth_key = pet.get_api_key(valid_email, valid_password)
    _, my_pets = pet.get_list_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']

    if len(my_pets['pets']) == 0:
        status, result = pet.delete_api_pets(auth_key, my_pets['pets'][0]['id'])
        assert status == 200
        assert pet_id not in my_pets.values()