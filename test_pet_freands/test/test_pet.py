import pytest
from settings import valid_password, valid_email
from api_19_7_2 import ApiPets

pet = ApiPets()

def generator(n):
    return 'x' * n
def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'
def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'
# def is_age_valid(age):
#    # Проверяем, что возраст - это число от 1 до 49 и целое
#    return age.isdigit() \
#           and 0 < int(age) < 50 \
#           and float(age) == int(age)

@pytest.fixture(autouse=True)
def ket_api_pets():
    status, pytest.key = pet.get_api_key(valid_email, valid_password)

    assert status == 200
    assert 'key' in pytest.key
    yield
    assert pytest.status == 200

@pytest.mark.parametrize("filter", ['', 'my_pets'], ids=['empty string', 'only my pets'])
def test_get_all_pets_with_valid_key(filter):
    pytest.status, result = pet.get_list_pets(pytest.key, filter)

    assert len(result['pets']) > 0


@pytest.mark.parametrize("name"
    , [generator(255), generator(1001), russian_chars(), russian_chars().upper(), chinese_chars(), special_chars(),
       '123']
    , ids=['255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
@pytest.mark.parametrize("animal_type"
    , [generator(255), generator(1001), russian_chars(), russian_chars().upper(), chinese_chars(), special_chars(),
       '123']
    , ids=['255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
@pytest.mark.parametrize("age", ['1'], ids=['min'])
def test_add_new_pet_simple_valid(name, animal_type, age):
    pytest.status, result = pet.post_api_create_pet_simple(pytest.key, name, animal_type, age)

    assert pytest.status == 200
    assert result['name'] == name
    assert result['age'] == age
    assert result['animal_type'] == animal_type


@pytest.mark.parametrize("name", [''], ids=['empty'])
@pytest.mark.parametrize("animal_type", [''], ids=['empty'])
@pytest.mark.parametrize("age", ['', '-1', '0', '100', '1.5', '2147483647', '2147483648', special_chars(), russian_chars(),
                         russian_chars().upper(), chinese_chars()]
   , ids=['empty', 'negative', 'zero', 'greater than max', 'float', 'int_max', 'int_max + 1', 'specials',
          'russian', 'RUSSIAN', 'chinese'])
def test_add_new_pet_simple_negativ(name, animal_type, age):
    pytest.status, result = pet.post_api_create_pet_simple(pytest.key, name, animal_type, age)

    assert pytest.status == 400