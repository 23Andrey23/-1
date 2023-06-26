import pytest
from pages.password_recovery_page import *

"""Функционал кнопок выбора типа ввода на странице 'Восстановление пароля'"""
class TestPasswordRecoveryButtonType:

    """EXP-064 Функция выбора типа ввода по восстановлению пароля, автоматически выбрана 'Номер'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-016"')
    def test_auto_pass_recovery_selection(self, driver):
        register_page = PasswordRecoveryButtonType(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone, name_field, url = register_page.auto_pass_recovery_selection()
        # Проверяем, что название кнопки соответствует требованиям
        assert phone == 'Номер'
        # Проверяем, что выбор типа ввода по восстановлению пароля, автоматически выбрана 'Номер'
        assert name_field == 'Мобильный телефон'
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-065 Функционирование кнопки 'Почта'"""
    def test_button_email(self, driver):
        register_page = PasswordRecoveryButtonType(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email, name_field, url = register_page.button_email()
        # Проверяем, что название кнопки соответствует требованиям
        assert email == 'Почта'
        # Проверяем, что кнопка 'Почта' валидна при нажатии на нее
        assert name_field == 'Электронная почта'
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-066 Функционирование кнопки 'Логин'"""
    def test_button_login(self, driver):
        register_page = PasswordRecoveryButtonType(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        login, name_field, url = register_page.button_login()
        # Проверяем, что название кнопки соответствует требованиям
        assert login == 'Логин'
        # Проверяем, что кнопка 'Логин' валидна при нажатии на нее
        assert name_field == 'Логин'
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-067 Функционирование кнопки 'Лицевой счёт'"""
    def test_button_personal_account(self, driver):
        register_page = PasswordRecoveryButtonType(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        personal_account, name_field, url = register_page.button_personal_account()
        # Проверяем, что название кнопки соответствует требованиям
        assert personal_account == 'Лицевой счёт'
        # Проверяем, что кнопка 'Лицевой счёт' валидна при нажатии на нее
        assert name_field == 'Лицевой счёт'
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'


"""Валидность принятых данных, в поле для ввода 'Мобильный телефон'"""
class TestPasswordRecoveryInputPhone:

    """EXP-068 Валидность принятых данных, в поле ввода 'Мобильный телефон', введены данные в формате +7ХХХХХХХХХХ"""
    def test_input_phone_number_seven(self, driver):
        register_page = PasswordRecoveryInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_input, phone_text, url = register_page.input_phone_number_seven()
        # Проверяем что поле "Мобильный телефон" содержит введенные пользователем значения
        assert phone_text == phone_input
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-069 Валидность принятых данных, в поле ввода 'Мобильный телефон', введены данные в формате +375XXXXXXXXX"""
    def test_input_phone_number_three(self, driver):
        register_page = PasswordRecoveryInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_input, phone_text, url = register_page.input_phone_number_three()
        # Проверяем что поле "Мобильный телефон" содержит введенные пользователем значения
        assert phone_text == phone_input
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-070 Валидность принятых данных, в поле ввода 'Мобильный телефон', введены данные в формате 7ХХХХХХХХХХ"""
    def test_input_phone_number_seven_not_plus(self, driver):
        register_page = PasswordRecoveryInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text, url = register_page.input_phone_number_seven_not_plus()
        # Проверяем что поле "Мобильный телефон" автоматически вставляет первый символ '+'
        assert phone_text[0] == '+'
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-071 Валидность принятых данных, в поле ввода 'Мобильный телефон', введены данные в формате 8ХХХХХХХХХХ"""
    def test_input_phone_number_eight_not_plus(self, driver):
        register_page = PasswordRecoveryInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text, url = register_page.input_phone_number_eight_not_plus()
        # Проверяем что в поле "Мобильный телефон", цифра "8" переобразовалось в символы "+7"
        assert phone_text[0] == '+'
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-072 Валидность принятых данных, в поле ввода 'Мобильный телефон', введены данные в формате 375XXXXXXXXX"""
    def test_input_phone_number_three_not_plus(self, driver):
        register_page = PasswordRecoveryInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text, url = register_page.input_phone_number_three_not_plus()
        # Проверяем что поле "Мобильный телефон" автоматически вставляет первый символ '+'
        assert phone_text[0] == '+'
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-073 Валидность принятых данных, в поле ввода 'Мобильный телефон', когда значений больше формата +375XXXXXXXXX"""
    def test_input_phone_number_three_more_values(self, driver):
        register_page = PasswordRecoveryInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text, url = register_page.input_phone_number_three_more_values()
        # Проверяем что поле "Мобильный телефон" принимает не более 13 символов в формате +375XXXXXXXXX
        assert len(phone_text) == 13
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-074 Валидность принятых данных, в поле ввода 'Мобильный телефон', когда значений больше формата +7ХХХХХХХХХХ"""
    def test_input_phone_number_seven_more_values(self, driver):
        register_page = PasswordRecoveryInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text, url = register_page.input_phone_number_seven_more_values()
        # Проверяем что поле "Мобильный телефон" принимает не более 12 символов в формате +7ХХХХХХХХХХ
        assert len(phone_text) == 12
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-075 Валидность принятых данных, в поле ввода 'Мобильный телефон', когда первая цифра не валидна"""
    def test_input_phone_number_first_digit_not_valid(self, driver):
        register_page = PasswordRecoveryInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text, url = register_page.input_phone_first_digit_not_valid()
        # Проверяем что поле "Мобильный телефон" при вводе не валидной цифры (например '1'), она ставится после символов '+7'
        assert phone_text[2] == '1'
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-076 Валидность принятых данных, в поле ввода 'Мобильный телефон', когда в середине строки поставлен пробел"""
    def test_input_phone_number_space_middle(self, driver):
        register_page = PasswordRecoveryInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text, url = register_page.input_phone_space_middle()
        # Проверяем что поле "Мобильный телефон" не отображает пробел в середине строки
        assert phone_text[7] != ' '
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-077 Валидность принятых данных, в поле ввода 'Мобильный телефон', когда в конце строки поставлен пробел"""
    def test_input_phone_number_space_end(self, driver):
        register_page = PasswordRecoveryInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text, url = register_page.input_phone_space_end()
        # Проверяем что поле "Мобильный телефон" не отображает пробел в конце строки
        assert phone_text[-1] != ' '
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-078 Ввод кириллицы в поле ввода 'Мобильный телефон'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-017')
    def test_input_phone_rus_eng(self, driver):
        register_page = PasswordRecoveryInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text, url = register_page.input_phone_rus_eng()
        # Проверяем что поле "Мобильный телефон" не отображает кириллицу
        assert phone_text == ' '
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'


"""Валидность принятых данных, в поле для ввода 'Электронная почта'"""
class TestPasswordRecoveryInputEmail:

    """EXP-079 Ввод латиницы в поле ввода 'Электронная почта'"""
    def test_valid_input_email_eng(self, driver):
        register_page = PasswordRecoveryInputEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email_input, email_text, url = register_page.valid_input_email_eng()
        # Проверяем что поле "Электронная почта" отображает вводимые латинские значения
        assert email_text == email_input
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-080 Ввод спец. символов в поле ввода 'Электронная почта'"""
    def test_valid_input_email_special_symbol(self, driver):
        register_page = PasswordRecoveryInputEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email_input, email_text, url = register_page.valid_input_email_special_symbol()
        # Проверяем что поле "Электронная почта" отображает спец. символы
        assert email_text == email_input
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-081 Ввод чисел в поле ввода 'Электронная почта'"""
    def test_valid_input_email_num(self, driver):
        register_page = PasswordRecoveryInputEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email_input, email_text, url = register_page.valid_input_email_num()
        # Проверяем что поле "Электронная почта" отображает числа
        assert int(email_text) == email_input
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-082 Ввод прописных букв в поле ввода 'Электронная почта'"""
    def test_valid_input_email_eng_upper(self, driver):
        register_page = PasswordRecoveryInputEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email_input, email_text, url = register_page.valid_input_email_eng_upper()
        # Проверяем что поле "Электронная почта" отображает прописные буквы
        assert email_text != email_input
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-083 Ввод 255 символов в поле ввода 'Электронная почта'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-018')
    def test_valid_input_email_255_symbol(self, driver):
        register_page = PasswordRecoveryInputEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email_input, email_text, url = register_page.valid_input_email_255_symbol()
        # Проверяем что поле "Электронная почта" не отображает все 255 символов
        assert len(email_text) != 255
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-084 Ввод 500 символов в поле ввода 'Электронная почта'"""
    @pytest.mark.skip(reason='Баг в продукте - странице "Bugs: FB-019"')
    def test_valid_input_email_500_symbol(self, driver):
        register_page = PasswordRecoveryInputEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email_input, email_text, url = register_page.valid_input_email_500_symbol()
        # Проверяем что поле "Электронная почта" не отображает все 500 символов
        assert len(email_text) != 500
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-085 Ввод кирилльских и китайских символов в поле ввода 'Электронная почта'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-020"')
    def test_valid_input_email_rus_chaine(self, driver):
        register_page = PasswordRecoveryInputEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email_text, url = register_page.valid_input_email_rus_chaine()
        # Проверяем что поле "Электронная почта" не отображает все кирилльские и китайские символы
        assert email_text == ''
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-086 Ввод валидных данных в поле ввода 'Электронная почта' с пробелом в середине текста"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-021')
    def test_valid_input_email_space_middle(self, driver):
        register_page = PasswordRecoveryInputEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email_input, email_text, url = register_page.valid_input_email_space_middle()
        # Проверяем что поле "Электронная почта" не отображает пробел в середине текста
        assert email_text == email_input
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'


"""Валидность принятых данных, в поле для ввода 'Логин'"""
class TestPasswordRecoveryInputLogin:

    """EXP-087 Ввод латиницы в поле ввода 'Логин'"""
    def test_valid_input_login_eng(self, driver):
        register_page = PasswordRecoveryInputLogin(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        login_input, login_text, url = register_page.valid_input_login_eng()
        # Проверяем что поле "Логин" отображает вводимые латинские значения
        assert login_text == login_input
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-088 Ввод спец. символов в поле ввода 'Логин'"""
    def test_valid_input_login_special_symbol(self, driver):
        register_page = PasswordRecoveryInputLogin(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        login_input, login_text, url = register_page.valid_input_login_special_symbol()
        # Проверяем что поле "Логин" отображает спец. символы
        assert login_text == login_input
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-089 Ввод чисел в поле ввода 'Логин'"""
    def test_valid_input_login_num(self, driver):
        register_page = PasswordRecoveryInputLogin(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        login_input, login_text, url = register_page.valid_input_login_num()
        # Проверяем что поле "Логин" отображает числа
        assert int(login_text) == login_input
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-090 Ввод прописных букв в поле ввода 'Логин'"""
    def test_valid_input_login_eng_upper(self, driver):
        register_page = PasswordRecoveryInputLogin(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        login_input, login_text, url = register_page.valid_input_login_eng_upper()
        # Проверяем что поле "Логин" отображает прописные буквы
        assert login_text != login_input
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-091 Ввод 255 символов в поле ввода 'Логин'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-022')
    def test_input_login_255_symbol(self, driver):
        register_page = PasswordRecoveryInputLogin(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        login_input, login_text, url = register_page.input_login_255_symbol()
        # Проверяем что поле "Логин" не отображает все 255 символов
        assert len(login_text) != 255
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-092 Ввод 500 символов в поле ввода 'Логин'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-023')
    def test_input_login_500_symbol(self, driver):
        register_page = PasswordRecoveryInputLogin(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        login_input, login_text, url = register_page.input_login_500_symbol()
        # Проверяем что поле "Логин" не отображает все 500 символов
        assert len(login_text) != 500
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-093 Ввод кирилльских и китайских символов в поле ввода 'Логин'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-024')
    def test_input_login_rus_chaine(self, driver):
        register_page = PasswordRecoveryInputLogin(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        login_text, url = register_page.input_login_rus_chaine()
        # Проверяем что поле "Логин" не отображает все кирилльские и китайские символы
        assert login_text == ''
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-094 Ввод валидных данных в поле ввода 'Логин' с пробелом в середине текста"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-025')
    def test_input_login_space_middle(self, driver):
        register_page = PasswordRecoveryInputLogin(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        login_input, login_text, url = register_page.input_login_space_middle()
        # Проверяем что поле "Логин" не отображает пробел в середине текста
        assert login_text == login_input
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'


"""Валидность принятых данных, в поле для ввода 'Лицевой счет'"""
class TestPasswordRecoveryInputPersonalAccount:

    """EXP-095 Валидный ввод 12 чисел в поле ввода 'Лицевой счет'"""
    def test_valid_input_personal_account_12_num(self, driver):
        register_page = PasswordRecoveryInputPersonalAccount(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        personal_account_text, url = register_page.valid_input_personal_account_12_num()
        # Проверяем что поле "Лицевой счет" отображает валидное значение
        assert len(personal_account_text) == 12
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-096 Ввод данных в поле ввода 'Лицевой счет' с пробелом в середине"""
    def test_input_personal_account_space_middle(self, driver):
        register_page = PasswordRecoveryInputPersonalAccount(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        personal_account_input, personal_account_text, url = register_page.input_personal_account_space_middle()
        # Проверяем поле "Лицевой счет" не принимает пробелов
        assert personal_account_text == personal_account_input
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-097 Ввод данных в поле ввода 'Лицевой счет' с пробелом в конце"""
    def test_input_personal_account_space_end(self, driver):
        register_page = PasswordRecoveryInputPersonalAccount(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        personal_account_input, personal_account_text, url = register_page.input_personal_account_space_end()
        # Проверяем поле "Лицевой счет" не принимает пробелов
        assert personal_account_text == personal_account_input
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-098 Ввод кирилльских и латинских символов в поле ввода 'Лицевой счет'"""
    def test_input_personal_account_rus_eng(self, driver):
        register_page = PasswordRecoveryInputPersonalAccount(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        personal_account_text, url = register_page.input_personal_account_rus_eng()
        # Проверяем поле "Лицевой счет" не принимает кирилльские и латинские символы
        assert personal_account_text == ''
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

"""Валидность принятых данных, в поле для ввода 'Символы'"""
class TestPasswordRecoveryInputSymbol:

    """EXP-099 Ввод латинских символов в поле ввода 'Символы'"""
    def test_valid_input_personal_account_rus_eng(self, driver):
        register_page = PasswordRecoveryInputSymbol(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        symbol_input, symbol_text, url = register_page.valid_input_personal_account_symbol()
        # Проверяем поле "Символы" принимает латинские символы
        assert symbol_text == symbol_input
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-100 Ввод чисел в поле ввода 'Символы'"""
    def test_valid_input_personal_account_num(self, driver):
        register_page = PasswordRecoveryInputSymbol(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        symbol_input, symbol_text, url = register_page.valid_input_personal_account_num()
        # Проверяем поле "Символы" принимает числа
        assert symbol_text == symbol_input
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-101 Ввод прописных букв в поле ввода 'Символы'"""
    def test_valid_input_personal_account_upper(self, driver):
        register_page = PasswordRecoveryInputSymbol(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        symbol_input, symbol_text, url = register_page.valid_input_personal_account_upper()
        # Проверяем поле "Символы" принимает прописные буквы
        assert symbol_text == symbol_input
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-102 Ввод кирилльских и китайских символов в поле ввода 'Символы'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-026')
    def test_input_personal_account_rus_chaine(self, driver):
        register_page = PasswordRecoveryInputSymbol(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        symbol_text, url = register_page.input_personal_account_rus_chaine()
        # Проверяем поле "Символы" не принимает кирилльские и китайские символовы
        assert symbol_text == ''
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-103 Ввод 255 символов в поле ввода 'Символы'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-027')
    def test_input_personal_account_255_symbol(self, driver):
        register_page = PasswordRecoveryInputSymbol(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        symbol_text, url = register_page.input_personal_account_255_symbol()
        # Проверяем поле "Символы" не принимает 255 символов
        assert len(symbol_text) != 255
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-104 Ввод 500 символов в поле ввода 'Символы'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-028')
    def test_input_personal_account_500_symbol(self, driver):
        register_page = PasswordRecoveryInputSymbol(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        symbol_text, url = register_page.input_personal_account_500_symbol()
        # Проверяем поле "Символы" не принимает 500 символов
        assert len(symbol_text) != 500
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'


class TestPasswordRecovery:

    """EXP-105 Валидность заголовка на странице 'Восстановление пароля'"""
    def test_main_title(self, driver):
        register_page = PasswordRecovery(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text, url = register_page.main_title()
        # Проверяем на валидность заголовка
        assert text == 'Восстановление пароля'
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-106 Валидность текста над выбором типа ввода контактных данных"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-029')
    def test_text_above_type(self, driver):
        register_page = PasswordRecovery(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text, url = register_page.text_above_type()
        # Проверяем на валидность заголовка
        assert text == 'Введите данные и нажмите «Далее»'
        # Проверяем что мы находимся на странице 'Восстановление пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-107 Функционирование кнопки 'Вернуться назад' """
    def test_button_back(self, driver):
        register_page = PasswordRecovery(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text, url = register_page.button_back()
        # Проверяем на валидность заголовка
        assert text == 'Вернуться назад'
        # Проверяем что мы находимся на странице "Авторицации"
        assert url == '/auth/realms/b2c/login-actions/authenticate'

class TestPasswordRecoveryFooter:

    """EXP-108 Пользователь нажимает на кнопку 'Cookies' в footer"""
    def test_button_cookie_footer(self, driver):
        register_page = PasswordRecoveryFooter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        cookie_text = register_page.button_cookie_footer()
        # Проверяем что при нажатии на кнопку 'Cookies' отображается шаблон с текстом
        assert cookie_text == 'Мы используем Cookie'

    """EXP-109 В отобразившемся шаблоне 'Cookies' нажать на кнопку 'крестик'"""
    def test_button_cookie_close_footer(self, driver):
        register_page = PasswordRecoveryFooter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        register_page.button_cookie_close_footer()

    """EXP-110 Пользователь нажимает на кнопку 'Политикой конфиденциальности' в footer"""
    def test_button_privacy_policy_footer(self, driver):
        register_page = PasswordRecoveryFooter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_privacy_policy, url = register_page.button_privacy_policy_footer()
        # Проверяем что кнопка отображает валидное значение
        assert text_privacy_policy == 'Политикой конфиденциальности'
        # Проверяем что мы перешли на страницу Политикой конфиденциальности
        assert url == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

    """EXP-111 Пользователь нажимает на кнопку 'Пользовательские соглашения' в footer"""
    def test_button_user_agreements_footer(self, driver):
        register_page = PasswordRecoveryFooter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_user_agreements, url = register_page.button_user_agreements_footer()
        # Проверяем что кнопка отображает валидное значение
        assert text_user_agreements == 'Пользовательским соглашением'
        # Проверяем что мы перешли на страницу Пользовательского соглашения
        assert url == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'


"""Логика кнопки 'Далее'"""
class TestPasswordRecoveryContinue:

    """EXP-112 Логика кнопки 'Далее', когда валидны данные только в поле 'восстановления пароля по телефону'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-030')
    def test_valid_phone_not_valid_symbol(self, driver):
        register_page = PasswordRecoveryContinue(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        button_further, error, url = register_page.valid_phone_not_valid_symbol()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или текст с картинки'
        # Проверяем валидность названия кнопки 'Далее'
        assert button_further == 'Далее'
        # Проверяем что пользователь остался на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-113 Логика кнопки 'Далее' в форме 'восстановления пароля по телефону', когда в полях введены невалидны данные"""
    def test_not_valid_phone_not_valid_symbol(self, driver):
        register_page = PasswordRecoveryContinue(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.not_valid_phone_not_valid_symbol()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или текст с картинки'
        # Проверяем что пользователь остался на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-114 Логика кнопки 'Далее', когда данные 'восстановления пароля по телефону' валидны, поле 'Символы' пустое"""
    def test_valid_phone_empty_symbol(self, driver):
        register_page = PasswordRecoveryContinue(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.valid_phone_empty_symbol()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или текст с картинки'
        # Проверяем что пользователь остался на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-115 Логика кнопки 'Далее', когда валидны данные только в поле 'восстановления пароля по почте'"""
    def test_valid_email_not_valid_symbol(self, driver):
        register_page = PasswordRecoveryContinue(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.valid_email_not_valid_symbol()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или текст с картинки'
        # Проверяем что пользователь остался на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-116 Логика кнопки 'Далее' в форме 'восстановления пароля по почте', когда в полях введены невалидны данные"""
    def test_not_valid_email_not_valid_symbol(self, driver):
        register_page = PasswordRecoveryContinue(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.not_valid_email_not_valid_symbol()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или текст с картинки'
        # Проверяем что пользователь остался на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-117 Логика кнопки 'Далее', когда данные 'восстановления пароля по почте' валидны, поле 'Символы' пустое"""
    def test_valid_email_empty_symbol(self, driver):
        register_page = PasswordRecoveryContinue(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.valid_email_empty_symbol()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или текст с картинки'
        # Проверяем что пользователь остался на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-118 Логика кнопки 'Далее', когда валидны данные только в поле 'восстановления пароля по логину'"""
    def test_valid_login_not_valid_symbol(self, driver):
        register_page = PasswordRecoveryContinue(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.valid_login_not_valid_symbol()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или текст с картинки'
        # Проверяем что пользователь остался на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-119 Логика кнопки 'Далее' в форме 'восстановления пароля по логину', когда в полях введены невалидны данные"""
    def test_not_valid_login_not_valid_symbol(self, driver):
        register_page = PasswordRecoveryContinue(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.not_valid_login_not_valid_symbol()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или текст с картинки'
        # Проверяем что пользователь остался на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-120 Логика кнопки 'Далее', когда данные 'восстановления пароля по логину' валидны, поле 'Символы' пустое"""
    def test_valid_login_empty_symbol(self, driver):
        register_page = PasswordRecoveryContinue(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.valid_login_empty_symbol()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или текст с картинки'
        # Проверяем что пользователь остался на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-121 Логика кнопки 'Далее', когда валидны данные только в поле 'восстановления пароля по ЛС'"""
    def test_valid_person_account_not_valid_symbol(self, driver):
        register_page = PasswordRecoveryContinue(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.valid_person_account_not_valid_symbol()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или текст с картинки'
        # Проверяем что пользователь остался на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-122 Логика кнопки 'Далее', когда в поле 'ЛС' пустое; в поле 'Символ' невалидные данные"""
    def test_empty_person_account_not_valid_symbol(self, driver):
        register_page = PasswordRecoveryContinue(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.empty_person_account_not_valid_symbol()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Введите номер вашего лицевого счета'
        # Проверяем что пользователь остался на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-123 Логика кнопки 'Далее', когда данные 'восстановления пароля по ЛС' валидны, поле 'Символы' пустое"""
    def test_valid_person_account_empty_symbol(self, driver):
        register_page = PasswordRecoveryContinue(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.valid_person_account_empty_symbol()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или текст с картинки'
        # Проверяем что пользователь остался на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-124 Логика кнопки 'Далее', когда данные 'восстановления пароля по ЛС' невалидны, поле 'Символы' пустое"""
    def test_not_valid_person_account_empty_symbol(self, driver):
        register_page = PasswordRecoveryContinue(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.not_valid_person_account_empty_symbol()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Проверьте, пожалуйста, номер лицевого счета'
        # Проверяем что пользователь остался на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'


"""Логика типа ввода контактных данных"""
class TestPasswordRecoveryLogicTypeInput:

    """EXP-125 Логика типа ввода контактных данных телефона, когда в поле ввода 'Мобильный телефон' не полный номер"""
    def test_incomplete_number_phone(self, driver):
        register_page = PasswordRecoveryLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error = register_page.incomplete_number_phone()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный формат телефона'

    """EXP-126 Логика типа ввода контактных данных телефона, когда в поле ввода 'Мобильный телефон' латинские буквы"""
    def test_input_eng_phone(self, driver):
        register_page = PasswordRecoveryLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_eng_phone()
        # Проверяем что при вводе латинских букв, тип ввода контактных данных меняется на 'Логин'
        assert type_data == 'Логин'

    """EXP-127 Логика типа ввода контактных данных телефона, когда в поле ввода 'Мобильный телефон' спец. символы"""
    def test_input_special_symbol_phone(self, driver):
        register_page = PasswordRecoveryLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_special_symbol_phone()
        # Проверяем что при вводе спец. символов, тип ввода контактных данных меняется на 'Логин'
        assert type_data == 'Логин'

    """EXP-128 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' номер телефона"""
    def test_input_number_phone_field_email(self, driver):
        register_page = PasswordRecoveryLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_number_phone_field_email()
        # Проверяем что при вводе номера телефона, тип ввода контактных данных меняется на 'Номер'
        assert type_data == 'Мобильный телефон'

    """EXP-129 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' числа"""
    def test_input_number_field_email(self, driver):
        register_page = PasswordRecoveryLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_number_field_email()
        # Проверяем что при вводе чисел, тип ввода контактных данных меняется на 'Логин'
        assert type_data == 'Логин'

    """EXP-130 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' латинские буквы"""
    def test_input_eng_email(self, driver):
        register_page = PasswordRecoveryLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_eng_email()
        # Проверяем что при вводе латинских букв, тип ввода контактных данных меняется на 'Логин'
        assert type_data == 'Логин'

    """EXP-131 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' спец. символы"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-031')
    def test_input_special_symbol_email(self, driver):
        register_page = PasswordRecoveryLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_special_symbol_email()
        # Проверяем что при вводе спец. символы, тип ввода контактных данных не меняется
        assert type_data == 'Электронная почта'

    """EXP-132 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' 12 цифр"""
    def test_input_12_number_email(self, driver):
        register_page = PasswordRecoveryLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_12_number_email()
        # Проверяем что при вводе 12 цифр, тип ввода контактных данных меняется на 'Лицевой счёт'
        assert type_data == 'Лицевой счёт'

    """EXP-133 Логика типа ввода контактных данных логин, когда в поле ввода 'Логин' номер телефона"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-032')
    def test_input_number_phone_field_login(self, driver):
        register_page = PasswordRecoveryLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_number_phone_field_login()
        # Проверяем что при вводе номера телефона, тип ввода контактных данных не меняется
        assert type_data == 'Логин'

    """EXP-134 Логика типа ввода контактных данных логин, когда в поле ввода 'Логин' 12 цифр"""
    def test_input_12_number_login(self, driver):
        register_page = PasswordRecoveryLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_12_number_login()
        # Проверяем что при вводе 12 цифр, тип ввода контактных данных меняется на 'Лицевой счёт'
        assert type_data == 'Лицевой счёт'

    """EXP-135 Логика типа ввода контактных данных логин, когда в поле ввода 'Логин' латинские буквы"""
    def test_input_eng_login(self, driver):
        register_page = PasswordRecoveryLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_eng_login()
        # Проверяем что при вводе латинских букв, тип ввода контактных данных остается 'Логин'
        assert type_data == 'Логин'

    """EXP-136 Логика типа ввода контактных данных логин, когда в поле ввода 'Логин' спец. символы"""
    def test_input_special_symbol_login(self, driver):
        register_page = PasswordRecoveryLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_special_symbol_login()
        # Проверяем что при вводе спец. символов, тип ввода контактных данных остается 'Логин'
        assert type_data == 'Логин'

    """EXP-137 Логика типа ввода контактных данных лицевой счёт, когда в поле ввода 'Лицевой счёт' номер телефона"""
    def test_input_number_phone_field_person_account(self, driver):
        register_page = PasswordRecoveryLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_number_phone_field_person_account()
        # Проверяем что при вводе номера телефона, тип ввода контактных данных остается 'Лицевой счёт'
        assert type_data == 'Лицевой счёт'

    """EXP-138 Логика типа ввода контактных данных лицевой счёт, когда в поле ввода 'Лицевой счёт' не полный лицевой счет"""
    def test_input_incomplete_person_account(self, driver):
        register_page = PasswordRecoveryLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_incomplete_person_account()
        # Проверяем что при вводе не полный лицевой счет, тип ввода контактных данных остается 'Лицевой счёт'
        assert type_data == 'Лицевой счёт'