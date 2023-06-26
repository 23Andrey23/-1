import random
import string
from data.data import Person
from faker import Faker


faker_ru = Faker('ru_RU')
Faker.seed()
# Генерирует: имя, фамилия, почта
def generator_parsen():
    yield Person(
        name=faker_ru.first_name(),
        surname=faker_ru.last_name(),
        email=faker_ru.email(),
        phone=faker_ru.phone_number()
    )

# Генерирует русские символовы с нижним регистром на кол-во символов
def generate_cyrillic_character():
    cyrillic_characters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    character = random.choice(cyrillic_characters)
    return character
def generator_lower_rus(num):
    output = ''.join([generate_cyrillic_character() for _ in range(num)])
    return output


# Генерирует английские символовы с нижним регистром на кол-во символов
def generate_cyrillic_character_eng_lowers_col():
    cyrillic_characters = "abcdefghijklmnopqrstuvwxyz"
    character = random.choice(cyrillic_characters)
    return character
def generator_eng_lowers_col(num):
    output = ''.join([generate_cyrillic_character_eng_lowers_col() for _ in range(num)])
    return output


# Генератор заглавных букв
def generator_cyrillic_character_upper():
    cyrillic_characters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    character = random.choice(cyrillic_characters)
    return character
def generator_upper_rus():
    num = random.randint(5, 13)
    output = ''.join([generator_cyrillic_character_upper() for _ in range(num)])
    return output



# Генератор лат. букв
def generator_cyrillic_character_eng():
    cyrillic_characters = "abcdefghijklmnopqrstuvwxyz"
    character = random.choice(cyrillic_characters)
    return character
def generator_lowers_eng():
    num = random.randint(5, 13)
    output = ''.join([generator_cyrillic_character_eng() for _ in range(num)])
    return output


# Генератор лат. заглавных букв
def generator_cyrillic_character_eng_upper():
    cyrillic_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    character = random.choice(cyrillic_characters)
    return character
def generator_eng_upper():
    num = random.randint(5, 13)
    output = ''.join([generator_cyrillic_character_eng_upper() for _ in range(num)])
    return output



# Генератор кирильских и китайских символов
def generator_cyrillic_character_rus_chaine():
    cyrillic_characters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя阿贝非给得也用热赛伊伊可罗肯卡艾了"
    character = random.choice(cyrillic_characters)
    return character
def generator_lowers_rus_chaine():
    num = random.randint(5, 13)
    output = ''.join([generator_cyrillic_character_rus_chaine() for _ in range(num)])
    return output



# Генератор кирильских и китайских символов
def generator_cyrillic_character_rus_eng():
    cyrillic_characters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz"
    character = random.choice(cyrillic_characters)
    return character
def generator_lowers_rus_eng():
    num = random.randint(5, 13)
    output = ''.join([generator_cyrillic_character_rus_eng() for _ in range(num)])
    return output





# Генератор телефона
def generator_phone_number_7(num):
    while True:
        number = num + "".join(random.choice("0123456789") for _ in range(10))
        return number





# Генератор пароля, где есть хотя бы одна заглавная буква латиницы, где есть хотя бы одна цифра,
# где есть хотя бы одна строчная буква латиницы и 8 значений
def generator_password_not_special_symbol():
    characters = string.ascii_letters + string.digits

    while True:
        password = ''.join(random.choice(characters) for i in range(8))
        password += random.choice(string.digits)
        if any(c.islower() for c in password) and any(c.isupper() for c in password):
            return password
# Генератор пароля, где есть хотя бы одна заглавная буква латиницы, где есть хотя бы один специальный символ,
# где есть хотя бы одна строчная буква латиницы и 8 значений
def generator_password_not_number():
    while True:
        password = ''.join(random.choice(string.ascii_letters + string.punctuation) for _ in range(8))
        if any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c in string.punctuation for c in password):
            return password
# Генератор пароля, где есть хотя бы одна заглавная буква латиницы, где есть хотя бы одна цифра, где есть хотя бы
# один специальный символ, где есть хотя бы одна строчная буква латиницы
def generator_password_number_simbol(num):
    while True:
        password = ''.join(random.choice(string.ascii_letters + string.punctuation + string.digits) for _ in range(num))
        if any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c in string.punctuation for c in password) and any(c in string.digits for c in password):
            return password
# Генератор пароля, где есть хотя бы одна заглавная буква кириллицы, где есть хотя бы одна цифра, где есть хотя бы
# один специальный символ, где есть хотя бы одна строчная буква кириллицы и принимает 8 значений
def generator_password_rus():
    while True:
        password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя') for _ in range(8))
        if any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password) and any(c.islower() for c in password):
            return password




# Генератор спец. символов
def generator_special_symbol():
    characters = string.punctuation

    while True:
        password = ''.join(random.choice(characters) for _ in range(8))
        if all(c in string.punctuation for c in password):
            return password



# Генератор чисел
def generator_number():
    while True:
        number = random.randint(1000, 900000)
        return number

