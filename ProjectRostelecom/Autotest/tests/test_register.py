import pytest
from pages.register_page import *



"""Логика регистрации при введении в поле 'Имя' валидных и невалидных данных"""
class TestRegisterName:

    # Тестируем логику регестрации с использованием валидных данных
    """EXP-001 Регестрация пользователя, когда в поле «Имя» 2 символа"""
    def test_valid_register_name_2_symbol(self, driver):
        register_page = RegisterPageName(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        name, text_confirm, url = register_page.valid_register_name_2_symbol()
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что мы находимся на странице "подтверждения email"
        assert text_confirm == 'Подтверждение email'
        # Проверяем что имя принимает 2 символова
        assert len(name) == 2

    """EXP-002 Регестрация пользователя, когда в поле «Имя» 30 символов"""
    def test_valid_register_name_30_symbol(self, driver):
        register_page = RegisterPageName(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        name, text_confirm, url = register_page.valid_register_name_30_symbol()
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что мы находимся на странице "подтверждения email"
        assert text_confirm == 'Подтверждение email'
        # Проверяем что имя принимает все 30 символов
        assert len(name) == 30

    # Тестируем логику регестрации с использованием не валидных данных в поле «Имя»
    """EXP-003 Регестрация пользователя, когда в поле «Имя» 1 символ"""
    def test_not_valid_register_name_1_symbol(self, driver):
        register_page = RegisterPageName(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        name, error, url = register_page.not_valid_register_name_1_symbol()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под именем отобразился при неудачном вводе имени
        assert error == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        # Проверяем что имя принимает 1 символов
        assert len(name) == 1

    """EXP-004 Регестрация пользователя, когда в поле «Имя» 31 символа"""
    def test_not_valid_register_name_31_symbol(self, driver):
        register_page = RegisterPageName(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        name, error, url = register_page.not_valid_register_name_31_symbol()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под именем отобразился при неудачном вводе имени
        assert error == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        # Проверяем что имя принимает все 31 символовы
        assert len(name) == 31

    """EXP-005 Регестрация пользователя, когда в поле «Имя» 255 символа"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-001"')
    def test_not_valid_register_name_255_symbol(self, driver):
        register_page = RegisterPageName(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        name, error, url = register_page.not_valid_register_name_255_symbol()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под именем отобразился при неудачном вводе имени
        assert error == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        # Проверяем что поле "Имя" не принимает все 255 символов
        assert len(name) != 255

    """EXP-006 Регестрация пользователя, когда в поле «Имя» 500 символа"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-002"')
    def test_not_valid_register_name_500_symbol(self, driver):
        register_page = RegisterPageName(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        name, error, url = register_page.not_valid_register_name_500_symbol()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под именем отобразился при неудачном вводе имени
        assert error == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        # Проверяем что "Имя" не принимает все 500 символов
        assert len(name) != 500

    """EXP-007 Регестрация пользователя, когда поле «Имя» пустое """
    def test_not_valid_register_name_empty(self, driver):
        register_page = RegisterPageName(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url, name = register_page.not_valid_register_name_empty()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под именем отобразился при неудачном вводе имени
        assert error == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        # Проверяем что поле имя пустое
        assert name == ''

    """EXP-008 Регестрация пользователя, когда в поле «Имя» спец. символы """
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-003"')
    def test_not_valid_register_name_special_symbol(self, driver):
        register_page = RegisterPageName(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        name, error, url = register_page.not_valid_register_name_special_symbol()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под именем отобразился при неудачном вводе имени
        assert error == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        # Проверяем что поле "Имя" не отображает спец. символы
        assert name == ''

    """EXP-009 Регестрация пользователя, когда в поле «Имя» числа"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-004"')
    def test_not_valid_register_name_number(self, driver):
        register_page = RegisterPageName(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        name, error, url = register_page.not_valid_register_name_number()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под именем отобразился при неудачном вводе имени
        assert error == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        # Проверяем что поле "Имя" не отображает числа
        assert name == ''

    """EXP-010 Регестрация пользователя, когда в поле «Имя» кирильские заглавные буквы"""
    def test_not_valid_register_name_rus_upper(self, driver):
        register_page = RegisterPageName(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        name, name_rus_upper, url = register_page.not_valid_register_name_rus_upper()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что поле имя не отображает заглавные буквы
        assert name != name_rus_upper

    """EXP-011 Регестрация пользователя, когда в поле «Имя» латинские символы"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-005"')
    def test_not_valid_register_name_latin_characters(self, driver):
        register_page = RegisterPageName(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        name, error, url = register_page.not_valid_register_name_latin_characters()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под именем отобразился при неудачном вводе имени
        assert error == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        # Проверяем что поле имя не отображает заглавные буквы
        assert name == ''

"""Логика регистрации при введении в поле 'Фамилия' валидные и невалидные данные"""
class TestRegisterSurname:

    # Тестируем логику регестрации с использованием валидных данных
    """EXP-012 Регестрация пользователя, когда в поле «Фамилия» 2 символа"""
    def test_valid_register_surname_2_symbol(self, driver):
        register_page = RegisterPageSurname(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        surname, text_confirm, url = register_page.valid_register_surname_2_symbol()
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что мы находимся на странице "подтверждения email"
        assert text_confirm == 'Подтверждение email'
        # Проверяем что Фамилия принимает 2 символова
        assert len(surname) == 2

    """EXP-013 Регестрация пользователя, когда в поле «Фамилия» 30 символов"""
    def test_valid_register_surname_30_symbol(self, driver):
        register_page = RegisterPageSurname(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        surname, text_confirm, url = register_page.valid_register_surname_30_symbol()
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что мы находимся на странице "подтверждения email"
        assert text_confirm == 'Подтверждение email'
        # Проверяем что Фамилия принимает все 30 символов
        assert len(surname) == 30

    # Тестируем логику регестрации с использованием невалидных данных в поле «Фамилия»
    """EXP-014 Регестрация пользователя, когда в поле «Фамилия» 1 символ"""
    def test_not_valid_register_surname_1_symbol(self, driver):
        register_page = RegisterPageSurname(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        surname, error, url = register_page.not_valid_register_surname_1_symbol()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под Фамилией отобразился при неудачном вводе Фамилии
        assert error == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        # Проверяем что Фамилия принимает 1 символов
        assert len(surname) == 1

    """EXP-015 Регестрация пользователя, когда в поле «Фамилия» 31 символа"""
    def test_not_valid_register_surname_31_symbol(self, driver):
        register_page = RegisterPageSurname(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        surname, error, url = register_page.not_valid_register_surname_31_symbol()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под Фамилией отобразился при неудачном вводе Фамилии
        assert error == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        # Проверяем что Фамилия принимает все 31 символовы
        assert len(surname) == 31

    """EXP-016 Регестрация пользователя, когда в поле «Фамилия» 255 символа"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-006"')
    def test_not_valid_register_surname_255_symbol(self, driver):
        register_page = RegisterPageSurname(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        surname, error, url = register_page.not_valid_register_surname_255_symbol()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под Фамилией отобразился при неудачном вводе Фамилии
        assert error == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        # Проверяем что поле "Фамилия" не принимает все 255 символов
        assert len(surname) != 255

    """EXP-017 Регестрация пользователя, когда в поле «Фамилия» 500 символа"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-007"')
    def test_not_valid_register_surname_500_symbol(self, driver):
        register_page = RegisterPageSurname(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        surname, error, url = register_page.not_valid_register_surname_500_symbol()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под Фамилией отобразился при неудачном вводе Фамилии
        assert error == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        # Проверяем что "Фамилия" не принимает все 500 символов
        assert len(surname) != 500

    """EXP-018 Регестрация пользователя, когда поле «Фамилия» пустое """
    def test_not_valid_register_surname_empty(self, driver):
        register_page = RegisterPageSurname(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url, surname = register_page.not_valid_register_surname_empty()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под Фамилией отобразился при неудачном вводе Фамилии
        assert error == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        # Проверяем что поле Фамилия пустое
        assert surname == ''

    """EXP-019 Регестрация пользователя, когда в поле «Фамилия» спец. символы """
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-008"')
    def test_not_valid_register_surname_special_symbol(self, driver):
        register_page = RegisterPageSurname(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        surname, error, url = register_page.not_valid_register_surname_special_symbol()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под Фамилией отобразился при неудачном вводе Фамилии
        assert error == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        # Проверяем что поле "Фамилия" не отображает спец. символы
        assert surname == ''

    """EXP-020 Регестрация пользователя, когда в поле «Фамилия» числа"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-009"')
    def test_not_valid_register_surname_number(self, driver):
        register_page = RegisterPageSurname(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        surname, error, url = register_page.not_valid_register_surname_number()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под Фамилией отобразился при неудачном вводе Фамилии
        assert error == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        # Проверяем что поле "Фамилия" не отображает числа
        assert surname == ''

    """EXP-021 Регестрация пользователя, когда в поле «Фамилия» кирильские заглавные буквы"""
    def test_not_valid_register_surname_rus_upper(self, driver):
        register_page = RegisterPageSurname(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        surname, surname_rus_upper, url = register_page.not_valid_register_surname_rus_upper()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что поле "Фамилия" не отображает заглавные буквы
        assert surname != surname_rus_upper

    """EXP-022 Регестрация пользователя, когда в поле «Фамилия» латинские символы"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-010"')
    def test_not_valid_register_surname_latin_characters(self, driver):
        register_page = RegisterPageSurname(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        surname, error, url = register_page.not_valid_register_surname_latin_characters()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под Фамилией отобразился при неудачном вводе Фамилии
        assert error == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        # Проверяем что поле Фамилия не отображает заглавные буквы
        assert surname == ''

"""Логика регистрации при введении в поле 'Email' невалидные данные"""
class TestRegisterEmail:

    """EXP-023 Регистрация пользователя, когда в поле «Email» 255 символа"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-011"')
    def test_not_valid_register_email_255_symbol(self, driver):
        register_page = RegisterPageEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email, error, url = register_page.not_valid_register_email_255_symbol()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под Email, отобразился при неудачном вводе Email
        assert error == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
        # Проверяем что поле "Email" не принимает все 255 символов
        assert len(email) != 255

    """EXP-024 Регистрация пользователя, когда в поле «Email» 500 символа"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-012"')
    def test_not_valid_register_email_500_symbol(self, driver):
        register_page = RegisterPageEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email, error, url = register_page.not_valid_register_email_500_symbol()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под Email отобразился при неудачном вводе Email
        assert error == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
        # Проверяем что "Email" не принимает все 500 символов
        assert len(email) != 500

    """EXP-025 Регистрация пользователя, когда поле «Email» пустое """
    def test_not_valid_register_email_empty(self, driver):
        register_page = RegisterPageEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url, email = register_page.not_valid_register_email_empty()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под Email отобразился при неудачном вводе Email
        assert error == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
        # Проверяем что поле Email пустое
        assert email == ''

    """EXP-026 Регистрация пользователя, когда в поле «Email» спец. символы """
    def test_register_email_special_symbol(self, driver):
        register_page = RegisterPageEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email_input, email, error, url = register_page.register_email_special_symbol()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под Email отобразился при неудачном вводе Email
        assert error == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
        # Проверяем что поле "Email" отображает спец. символы
        assert email == email_input

    """EXP-027 Регистрация пользователя, когда в поле «Email» числа"""
    def test_not_valid_register_surname_number(self, driver):
        register_page = RegisterPageEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email, email_text, error, url = register_page.not_valid_register_email_number()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под Email отобразился при неудачном вводе Email
        assert error == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
        # Проверяем что поле "Email" отображает числа
        assert int(email) == email_text

    """EXP-028 Регистрация пользователя, когда в поле «Email» кирильские и китайские символы"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-013"')
    def test_not_valid_register_email_rus_chaine_symbol(self, driver):
        register_page = RegisterPageEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email, email_text, url = register_page.not_valid_register_email_rus_chaine_symbol()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что поле "Email" не отображает кирильские и китайские символы
        assert email != email_text

    """EXP-029 Регистрация пользователя, когда в поле «Email» нет символа @"""
    def test_not_valid_register_email_dog(self, driver):
        register_page = RegisterPageEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email, email_text, error, url = register_page.not_valid_register_email_dog()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под Email отобразился при неудачном вводе Email
        assert error == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
        # Проверяем что поле Фамилия не отображает заглавные буквы
        assert email == email_text

"""Логика регистрации при введении в поле 'Регион' невалидные данные"""
class TestRegisterRegion:

    """EXP-030 Регистрация пользователя, когда поле «Регион» пустая строка"""
    def test_not_valid_register_region_empty(self, driver):
        register_page = RegisterPageRegion(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        region, url = register_page.not_valid_register_region_empty()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что поле "Ренион" не пустое
        assert region != ""

    """EXP-031 Регистрация пользователя, когда в поле «Регион» не существующие данные"""
    def test_not_valid_register_region_non_existing_data(self, driver):
        register_page = RegisterPageRegion(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        region, region_text, url = register_page.not_valid_register_region_non_existing_data()
        # Проверяем что мы находимся на странице регестрации
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что поле "Регион" не содержит не существующие значения
        assert region != region_text

"""Логика регистрации при введении в поле 'Телефон' валидные и невалидные данные"""
class TestRegisterPhone:

    # Тестируем логику регестрации с использованием валидных данных, где в поле "E-mail или мобильный телефон" напечатан номер телефона"
    """EXP-032 Регистрация пользователя, когда в поле «Телефон» введены данные в формате +7ХХХХХХХХХХ"""
    def test_valid_register_phone_number_seven(self, driver):
        register_page = RegisterPagePhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text, phone, text_confirm, url = register_page.valid_register_phone_number_seven()
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что мы находимся на странице "подтверждения email"
        assert text_confirm == 'Подтверждение телефона'
        # Проверяем что поле Телефон содержит валидные значения
        assert phone_text == phone

    """EXP-033 Регистрация пользователя, когда в поле «Телефон» введены данные в формате +375XXXXXXXXX"""
    def test_valid_register_phone_number_three(self, driver):
        register_page = RegisterPagePhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text, phone, text_confirm, url = register_page.valid_register_phone_number_three()
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что мы находимся на странице "подтверждения email"
        assert text_confirm == 'Подтверждение телефона'
        # Проверяем что поле Телефон содержит валидные значения
        assert phone_text == phone

    # Тестируем логику регестрации с использованием невалидных данных в поле «E-mail или мобильный телефон" напечатан телефон»
    """EXP-034 Регистрация пользователя, когда в поле «Телефон» введены данные в формате 7ХХХХХХХХХХ"""
    def test_valid_register_phone_number_seven_not_plus(self, driver):
        register_page = RegisterPagePhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text, phone, text_confirm, url = register_page.not_valid_register_phone_number_seven_not_plus()
        # Проверяем что мы находимся на странице "подтверждения email"
        assert text_confirm == 'Подтверждение телефона'
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что поле Телефон содержит валидные значения
        assert phone_text == phone

    """EXP-035 Регистрация пользователя, когда в поле «Телефон» введены данные в формате 375XXXXXXXXX"""
    def test_valid_register_phone_number_three_not_plus(self, driver):
        register_page = RegisterPagePhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text, phone, text_confirm, url = register_page.not_valid_register_phone_number_three_not_plus()
        # Проверяем что мы находимся на странице "подтверждения email"
        assert text_confirm == 'Подтверждение телефона'
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что поле Телефон содержит валидные значения
        assert phone_text == phone

    """EXP-036 Регистрация пользователя, когда в поле «Телефон» первая цифра невалидна, введены данные в формате 7ХХХХХХХХХХ"""
    def test_not_valid_register_phone_number_one_int_changed(self, driver):
        register_page = RegisterPagePhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text, phone, text_confirm, url = register_page.not_valid_register_phone_number_one_int_changed()
        # Проверяем что мы находимся на странице "подтверждения email"
        assert text_confirm == 'Регистрация'
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что поле Телефон содержит валидные значения
        assert phone_text == phone

    """EXP-037 Регистрация пользователя, когда в поле «Телефон» первая цифра '8', введены данные в формате 7ХХХХХХХХХХ"""
    def test_not_valid_register_phone_number_one_int_eight(self, driver):
        register_page = RegisterPagePhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text, phone, text_confirm, url = register_page.not_valid_register_phone_number_one_int_eight()
        # Проверяем что мы находимся на странице "подтверждения email"
        assert text_confirm == 'Подтверждение телефона'
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что в поле Телефон, цифра "8" переобразовалось в символы "+7"
        assert phone_text[1] == '7'

"""Логика регистрации при введении в полях 'Пароль/Подтвердить пароль' валидные и невалидные данные"""
class TestRegisterPassword:

    # Тестируем логику регестрации с использованием валидных данных
    """EXP-038 Регистрация пользователя, где в полях «Пароль/Подтвердить пароль» нет спец. символов"""
    def test_valid_register_password_not_special_symbol(self, driver):
        register_page = RegisterPagePassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass, text_pass_confirm, text_confirm_email, url = register_page.valid_register_password_not_special_symbol()
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что в поле "Пароль", содержит одинаковое значение, что и поле "Подтвердить пароль"
        assert text_pass == text_pass_confirm
        # Проверяем что мы находимся на странице "подтверждения email"
        assert text_confirm_email == 'Подтверждение email'

    """EXP-039 Регистрация пользователя, где в полях «Пароль/Подтвердить пароль» нет цифр"""
    def test_valid_register_password_not_number(self, driver):
        register_page = RegisterPagePassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass, text_pass_confirm, text_confirm_email, url = register_page.valid_register_password_not_number()
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что в поле "Пароль", содержит одинаковое значение, что и поле "Подтвердить пароль"
        assert text_pass == text_pass_confirm
        # Проверяем что мы находимся на странице "подтверждения email"
        assert text_confirm_email == 'Подтверждение email'

    """EXP-040 Регистрация пользователя, где в полях «Пароль/Подтвердить пароль» более 8 символов"""
    def test_valid_register_password_more_8_symbol(self, driver):
        register_page = RegisterPagePassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass, text_pass_confirm, text_confirm_email, url = register_page.valid_register_password_more_8_symbol()
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что в поле "Пароль", содержит одинаковое значение, что и поле "Подтвердить пароль"
        assert text_pass == text_pass_confirm
        # Проверяем что мы находимся на странице "подтверждения email"
        assert text_confirm_email == 'Подтверждение email'

    """EXP-041 Регистрация пользователя, где в полях «Пароль/Подтвердить пароль» 8 символов"""
    def test_valid_register_password_8_symbol(self, driver):
        register_page = RegisterPagePassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass, text_pass_confirm, text_confirm_email, url = register_page.valid_register_password_8_symbol()
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что в поле "Пароль", содержит одинаковое значение, что и поле "Подтвердить пароль"
        assert text_pass == text_pass_confirm
        # Проверяем что мы находимся на странице "подтверждения email"
        assert text_confirm_email == 'Подтверждение email'

    # Тестируем логику регистрации с использованием невалидных данных
    """EXP-042 Регистрация пользователя, где в полях «Пароль/Подтвердить пароль» менее 8 символов"""
    def test_not_valid_register_password_less_8_symbol(self, driver):
        register_page = RegisterPagePassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass, text_pass_confirm, error_password, error_confirm_pass, url = register_page.not_valid_register_password_less_8_symbol()
        # Проверяем что в поле "Пароль", содержит одинаковое значение, что и поле "Подтвердить пароль"
        assert text_pass == text_pass_confirm
        # Проверяем что текст под Паролем отобразился при неудачном вводе пароля
        assert error_password == 'Длина пароля должна быть не менее 8 символов'
        # Проверяем что текст под полем Подтвердить пароль отобразился при неудачном вводе пароля
        assert error_password == 'Длина пароля должна быть не менее 8 символов'
        # Проверяем что мы остались на той же странице
        assert url == '/auth/realms/b2c/login-actions/registration'

    """EXP-043 Регистрация пользователя, где в полях «Пароль/Подтвердить пароль» все буквы заглавные"""
    def test_not_valid_register_password_upper_symbol(self, driver):
        register_page = RegisterPagePassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass, text_pass_confirm, error_password, error_confirm_pass, url = register_page.not_valid_register_password_upper_symbol()
        # Проверяем что в поле "Пароль", содержит одинаковое значение, что и поле "Подтвердить пароль"
        assert text_pass == text_pass_confirm
        # Проверяем что текст под Паролем отобразился при неудачном вводе пароля
        assert error_password == 'Пароль должен содержать хотя бы одну строчную букву'
        # Проверяем что текст под полем Подтвердить пароль отобразился при неудачном вводе пароля
        assert error_confirm_pass == 'Пароль должен содержать хотя бы одну строчную букву'
        # Проверяем что мы остались на той же странице
        assert url == '/auth/realms/b2c/login-actions/registration'

    """EXP-044 Регистрация пользователя, где в полях «Пароль/Подтвердить пароль» все буквы строчные"""
    def test_not_valid_register_password_lower_symbol(self, driver):
        register_page = RegisterPagePassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass, text_pass_confirm, error_password, error_confirm_pass, url = register_page.not_valid_register_password_lower_symbol()
        # Проверяем что в поле "Пароль", содержит одинаковое значение, что и поле "Подтвердить пароль"
        assert text_pass == text_pass_confirm
        # Проверяем что текст под Паролем отобразился при неудачном вводе пароля
        assert error_password == 'Пароль должен содержать хотя бы одну заглавную букву'
        # Проверяем что текст под полем Подтвердить пароль отобразился при неудачном вводе пароля
        assert error_confirm_pass == 'Пароль должен содержать хотя бы одну заглавную букву'
        # Проверяем что мы остались на той же странице
        assert url == '/auth/realms/b2c/login-actions/registration'

    """EXP-045 Регистрация пользователя, где в полях «Пароль/Подтвердить пароль» все буквы кириллицы"""
    def test_not_valid_register_password_rus_symbol(self, driver):
        register_page = RegisterPagePassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass, text_pass_confirm, error_password, error_confirm_pass, url = register_page.not_valid_register_password_rus_symbol()
        # Проверяем что в поле "Пароль", содержит одинаковое значение, что и поле "Подтвердить пароль"
        assert text_pass == text_pass_confirm
        # Проверяем что текст под Паролем отобразился при неудачном вводе пароля
        assert error_password == 'Пароль должен содержать только латинские буквы'
        # Проверяем что текст под полем Подтвердить пароль отобразился при неудачном вводе пароля
        assert error_confirm_pass == 'Пароль должен содержать только латинские буквы'
        # Проверяем что мы остались на той же странице
        assert url == '/auth/realms/b2c/login-actions/registration'

    """EXP-046 Регистрация пользователя, где в полях «Пароль/Подтвердить пароль» введены разные данные"""
    def test_not_valid_register_password_different_data(self, driver):
        register_page = RegisterPagePassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass, text_pass_confirm, error, url = register_page.not_valid_register_password_different_data()
        # Проверяем что данные в поле "Пароль" и поле "Подтвердить пароль" разные
        assert text_pass != text_pass_confirm
        # Проверяем что текст под Паролем отобразился при неудачном вводе пароля
        assert error == 'Пароли не совпадают'
        # Проверяем что мы остались на той же странице
        assert url == '/auth/realms/b2c/login-actions/registration'

    """EXP-047 Регистрация пользователя, где в полях «Пароль/Подтвердить пароль» введены 255 символов"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-014"')
    def test_not_valid_register_password_255_symbol(self, driver):
        register_page = RegisterPagePassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass, text_pass_confirm, url = register_page.not_valid_register_password_255_symbol()
        # Проверяем что данные в поле "Пароль" не принимают 255 символов
        assert len(text_pass) != 255
        # Проверяем что данные в поле "Подтвердить пароль" не принимают 255 символов
        assert len(text_pass_confirm) != 255
        # Проверяем что мы остались на той же странице
        assert url == '/auth/realms/b2c/login-actions/registration'

    """EXP-048 Регистрация пользователя, где в полях «Пароль/Подтвердить пароль» введены 500 символов"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-015"')
    def test_not_valid_register_password_500_symbol(self, driver):
        register_page = RegisterPagePassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass, text_pass_confirm, url = register_page.not_valid_register_password_500_symbol()
        # Проверяем что данные в поле "Пароль" не принимают 500 символов
        assert len(text_pass) != 500
        # Проверяем что данные в поле "Подтвердить пароль" не принимают 500 символов
        assert len(text_pass_confirm) != 500
        # Проверяем что мы остались на той же странице
        assert url == '/auth/realms/b2c/login-actions/registration'

    """EXP-049 Регистрация пользователя, где в полях «Пароль/Подтвердить пароль» нет данных"""
    def test_not_valid_register_password_not_data(self, driver):
        register_page = RegisterPagePassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass, text_pass_confirm, error_password, error_confirm_password, url = register_page.not_valid_register_password_not_data()
        # Проверяем что нет данные в поле "Пароль"
        assert text_pass == ""
        # Проверяем что нет данных в поле "Подтвердить пароль"
        assert text_pass_confirm == ""
        # Проверяем что мы остались на той же странице
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под Паролем отобразился при неудачном вводе пароля
        assert error_password == 'Длина пароля должна быть не менее 8 символов'
        # Проверяем что текст под полем Подтвердить пароль отобразился при неудачном вводе подтверждения
        assert error_confirm_password == 'Длина пароля должна быть не менее 8 символов'

    """EXP-050 Регистрация пользователя, где в поле «Пароль» нет данных"""
    def test_not_valid_register_password_not_data_password(self, driver):
        register_page = RegisterPagePassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        password, text_pass, text_pass_confirm, error_password, url = register_page.not_valid_register_password_not_data_password()
        # Проверяем что нет данных в поле "Пароль"
        assert text_pass == ""
        # Проверяем что в поле "Подтвердить пароль" отобразились данные
        assert text_pass_confirm == password
        # Проверяем что мы остались на той же странице
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под Паролем отобразился при неудачном вводе пароля
        assert error_password == 'Длина пароля должна быть не менее 8 символов'

    """EXP-051 Регистрация пользователя, где в поле «Подтвердить пароль» нет данных"""
    def test_not_valid_register_password_not_data_password_confirm(self, driver):
        register_page = RegisterPagePassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        password, text_pass, text_pass_confirm, error_password_confirm, url = register_page.not_valid_register_password_not_data_password_confirm()
        # Проверяем что в поле "Пароль" отобразились данные
        assert text_pass == password
        # Проверяем что в поле "Подтвердить пароль" нет данных
        assert text_pass_confirm == ""
        # Проверяем что мы остались на той же странице
        assert url == '/auth/realms/b2c/login-actions/registration'
        # Проверяем что текст под Паролем отобразился при неудачном вводе пароля
        assert error_password_confirm == 'Длина пароля должна быть не менее 8 символов'

    """EXP-052 Регистрация пользователя, где в полях «Пароль/Подтвердить пароль» только числа"""
    def test_not_valid_register_password_number(self, driver):
        register_page = RegisterPagePassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        password, text_pass, text_pass_confirm, url = register_page.not_valid_register_password_number()
        # Проверяем что в поле "Пароль" отобразились вводимые данные
        assert int(text_pass) == password
        # Проверяем что в поле "Подтвердить пароль" отобразились вводимые данные
        assert int(text_pass_confirm) == password
        # Проверяем что мы остались на той же странице
        assert url == '/auth/realms/b2c/login-actions/registration'

    """EXP-053 Регистрация пользователя, где в полях «Пароль/Подтвердить пароль» только спец. символы"""
    def test_not_valid_register_password_special_symbol(self, driver):
        register_page = RegisterPagePassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        password, text_pass, text_pass_confirm, url = register_page.not_valid_register_password_special_symbol()
        # Проверяем что в поле "Пароль" отобразились вводимые данные
        assert text_pass == password
        # Проверяем что в поле "Подтвердить пароль" отобразились вводимые данные
        assert text_pass_confirm == password
        # Проверяем что мы остались на той же странице
        assert url == '/auth/realms/b2c/login-actions/registration'

class TestRegister:

    """EXP-054 Пользователь нажимает на кнопку в поле 'Регион'"""
    def test_button_region_click(self, driver):
        register_page = RegisterPage(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        register_page.button_region_click()

    """EXP-055 Пользователь нажимает на кнопку 'Пользовательские соглашения' под кнопкой 'Зарегистрироваться'"""
    def test_button_user_agreements(self, driver):
        register_page = RegisterPage(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_user_agreements, url = register_page.button_user_agreements()
        # Проверяем что кнопка отображает валидное значение
        assert text_user_agreements == 'пользовательского соглашения'
        # Проверяем что мы перешли на страницу Пользовательского соглашения
        assert url == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

    """EXP-056 Пользователь нажимает на кнопку в поле 'Пароль'"""
    def test_button_password_click(self, driver):
        register_page = RegisterPage(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        register_page.button_password_click()

    """EXP-057 Пользователь нажимает на кнопку в поле 'Подтвердить пароль'"""
    def test_button_password_confirm_click(self, driver):
        register_page = RegisterPage(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        register_page.button_password_confirm_click()

    """EXP-058 Пользователь нажимает на кнопку 'Cookies' в footer"""
    def test_button_cookie_footer(self, driver):
        register_page = RegisterPage(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        cookie_text = register_page.button_cookie_footer()
        # Проверяем что при нажатии на кнопку 'Cookies' отображается шаблон с текстом
        assert cookie_text == 'Мы используем Cookie'

    """EXP-059 В отобразившемся шаблоне 'Cookies' нажать на кнопку 'крестик'"""
    def test_button_cookie_close_footer(self, driver):
        register_page = RegisterPage(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        register_page.button_cookie_close_footer()

    """EXP-060 Пользователь нажимает на кнопку 'Политикой конфиденциальности' в footer"""
    def test_button_privacy_policy_footer(self, driver):
        register_page = RegisterPage(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_privacy_policy, url = register_page.button_privacy_policy_footer()
        # Проверяем что кнопка отображает валидное значение
        assert text_privacy_policy == 'Политикой конфиденциальности'
        # Проверяем что мы перешли на страницу Политикой конфиденциальности
        assert url == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

    """EXP-061 Пользователь нажимает на кнопку 'Пользовательские соглашения' в footer"""
    def test_button_user_agreements_footer(self, driver):
        register_page = RegisterPage(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_user_agreements, url = register_page.button_user_agreements_footer()
        # Проверяем что кнопка отображает валидное значение
        assert text_user_agreements == 'Пользовательским соглашением'
        # Проверяем что мы перешли на страницу Пользовательского соглашения
        assert url == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

"""Логика введения существующего E-mail или мобильный телефон"""
class TestRegisterPageExistingAccount:

    """EXP-062 Функционал кнопки 'Войти', при введении существующего E-mail или мобильный телефон"""
    def test_valid_register_existing_account_enter(self, driver):
        register_page = RegisterPageExistingAccount(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        enter, url = register_page.valid_register_existing_account_enter()
        assert url == '/auth/realms/b2c/login-actions/authenticate'
        # Проверяем что кнопка 'Войти' отображена верно
        assert enter == 'Войти'

    """EXP-063 Функционал кнопки 'Восстановить пароль', при введении существующего E-mail или мобильный телефон"""
    def test_valid_register_existing_account_restore_password(self, driver):
        register_page = RegisterPageExistingAccount(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        restore_password, url = register_page.valid_register_existing_account_restore_password()
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'
        # Проверяем что кнопка 'Восстановить пароль' отображена верно
        assert restore_password == 'Восстановить пароль'