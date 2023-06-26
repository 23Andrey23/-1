import pytest
from pages.auth_page import *



class TestAuthButtonType:

    """EXP-138 Функция выбора типа ввода на странице 'Авторизации', автоматически выбрана 'Номер'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-033"')
    def test_auto_auth_selection(self, driver):
        register_page = AuthButtonType(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone, name_field, url = register_page.auto_auth_selection()
        # Проверяем, что название кнопки соответствует требованиям
        assert phone == 'Номер'
        # Проверяем, что выбор типа ввода по восстановлению пароля, автоматически выбрана 'Номер'
        assert name_field == 'Мобильный телефон'
        # Проверяем что мы находимся на странице 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/authenticate'

    """EXP-139 Функционал кнопки 'Номер' на странице 'Авторизация'"""
    def test_button_phone(self, driver):
        register_page = AuthButtonType(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        name_field = register_page.button_phone()
        # Проверяем, что кнопка 'Номер' валидна при нажатии на нее
        assert name_field == 'Мобильный телефон'

    """EXP-140 Функционирование кнопки 'Почта' на странице 'Авторизация'"""
    def test_button_email(self, driver):
        register_page = AuthButtonType(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email, name_field = register_page.button_email()
        # Проверяем, что название кнопки соответствует требованиям
        assert email == 'Почта'
        # Проверяем, что кнопка 'Почта' валидна при нажатии на нее
        assert name_field == 'Электронная почта'

    """EXP-141 Функционирование кнопки 'Логин' на странице 'Авторизация'"""
    def test_button_login(self, driver):
        register_page = AuthButtonType(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        login, name_field = register_page.button_login()
        # Проверяем, что название кнопки соответствует требованиям
        assert login == 'Логин'
        # Проверяем, что кнопка 'Логин' валидна при нажатии на нее
        assert name_field == 'Логин'

    """EXP-142 Функционирование кнопки 'Лицевой счёт' на странице 'Авторизация'"""
    def test_button_personal_account(self, driver):
        register_page = AuthButtonType(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        personal_account, name_field = register_page.button_personal_account()
        # Проверяем, что название кнопки соответствует требованиям
        assert personal_account == 'Лицевой счёт'
        # Проверяем, что кнопка 'Лицевой счёт' валидна при нажатии на нее
        assert name_field == 'Лицевой счёт'


"""Валидность принятых данных, в поле для ввода 'Мобильный телефон' на странице 'Авторизация'"""
class TestAuthInputPhone:

    """EXP-143 Валидность принятых данных, в поле ввода 'Мобильный телефон', введены данные в формате +7ХХХХХХХХХХ"""
    def test_input_phone_number_seven(self, driver):
        register_page = AuthInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_input, phone_text = register_page.input_phone_number_seven()
        # Проверяем что поле "Мобильный телефон" содержит введенные пользователем значения
        assert phone_text == phone_input

    """EXP-144 Валидность принятых данных, в поле ввода 'Мобильный телефон', введены данные в формате +375XXXXXXXXX"""
    def test_input_phone_number_three(self, driver):
        register_page = AuthInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_input, phone_text = register_page.input_phone_number_three()
        # Проверяем что поле "Мобильный телефон" содержит введенные пользователем значения
        assert phone_text == phone_input

    """EXP-145 Валидность принятых данных, в поле ввода 'Мобильный телефон', введены данные в формате 7ХХХХХХХХХХ"""
    def test_input_phone_number_seven_not_plus(self, driver):
        register_page = AuthInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text = register_page.input_phone_number_seven_not_plus()
        # Проверяем что поле "Мобильный телефон" автоматически вставляет первый символ '+'
        assert phone_text[0] == '+'

    """EXP-146 Валидность принятых данных, в поле ввода 'Мобильный телефон', введены данные в формате 8ХХХХХХХХХХ"""
    def test_input_phone_number_eight_not_plus(self, driver):
        register_page = AuthInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text = register_page.input_phone_number_eight_not_plus()
        # Проверяем что в поле "Мобильный телефон", цифра "8" переобразовалось в символы "+7"
        assert phone_text[0] == '+'

    """EXP-147 Валидность принятых данных, в поле ввода 'Мобильный телефон', введены данные в формате 375XXXXXXXXX"""
    def test_input_phone_number_three_not_plus(self, driver):
        register_page = AuthInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text = register_page.input_phone_number_three_not_plus()
        # Проверяем что поле "Мобильный телефон" автоматически вставляет первый символ '+'
        assert phone_text[0] == '+'

    """EXP-148 Валидность принятых данных, в поле ввода 'Мобильный телефон', когда значений больше формата +375XXXXXXXXX"""
    def test_input_phone_number_three_more_values(self, driver):
        register_page = AuthInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text = register_page.input_phone_number_three_more_values()
        # Проверяем что поле "Мобильный телефон" принимает не более 13 символов в формате +375XXXXXXXXX
        assert len(phone_text) == 13

    """EXP-149 Валидность принятых данных, в поле ввода 'Мобильный телефон', когда значений больше формата +7ХХХХХХХХХХ"""
    def test_input_phone_number_seven_more_values(self, driver):
        register_page = AuthInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text = register_page.input_phone_number_seven_more_values()
        # Проверяем что поле "Мобильный телефон" принимает не более 12 символов в формате +7ХХХХХХХХХХ
        assert len(phone_text) == 12

    """EXP-150 Валидность принятых данных, в поле ввода 'Мобильный телефон', когда первая цифра не валидна"""
    def test_input_phone_number_first_digit_not_valid(self, driver):
        register_page = AuthInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text = register_page.input_phone_first_digit_not_valid()
        # Проверяем что поле "Мобильный телефон" при вводе не валидной цифры (например '1'), она ставится после символов '+7'
        assert phone_text[2] == '1'

    """EXP-151 Валидность принятых данных, в поле ввода 'Мобильный телефон', когда в середине строки поставлен пробел"""
    def test_input_phone_number_space_middle(self, driver):
        register_page = AuthInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text = register_page.input_phone_space_middle()
        # Проверяем что поле "Мобильный телефон" не отображает пробел в середине строки
        assert phone_text[7] != ' '

    """EXP-152 Валидность принятых данных, в поле ввода 'Мобильный телефон', когда в конце строки поставлен пробел"""
    def test_input_phone_number_space_end(self, driver):
        register_page = AuthInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text = register_page.input_phone_space_end()
        # Проверяем что поле "Мобильный телефон" не отображает пробел в конце строки
        assert phone_text[-1] != ' '

    """EXP-153 Ввод кириллицы в поле ввода 'Мобильный телефон' на странице 'Авторизация'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-034')
    def test_input_phone_rus_eng(self, driver):
        register_page = AuthInputPhone(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        phone_text = register_page.input_phone_rus_eng()
        # Проверяем что поле "Мобильный телефон" не отображает кириллицу
        assert phone_text == ' '


"""Валидность принятых данных, в поле для ввода 'Электронная почта' на странице 'Авторизация'"""
class TestAuthInputEmail:

    """EXP-154 Ввод латиницы в поле ввода 'Электронная почта' на странице 'Авторизация'"""
    def test_valid_input_email_eng(self, driver):
        register_page = AuthInputEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email_input, email_text = register_page.valid_input_email_eng()
        # Проверяем что поле "Электронная почта" отображает вводимые латинские значения
        assert email_text == email_input

    """EXP-155 Ввод спец. символов в поле ввода 'Электронная почта' на странице 'Авторизация'"""
    def test_valid_input_email_special_symbol(self, driver):
        register_page = AuthInputEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email_input, email_text = register_page.valid_input_email_special_symbol()
        # Проверяем что поле "Электронная почта" отображает спец. символы
        assert email_text == email_input

    """EXP-156 Ввод чисел в поле ввода 'Электронная почта' на странице 'Авторизация'"""
    def test_valid_input_email_num(self, driver):
        register_page = AuthInputEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email_input, email_text = register_page.valid_input_email_num()
        # Проверяем что поле "Электронная почта" отображает числа
        assert int(email_text) == email_input

    """EXP-157 Ввод прописных букв в поле ввода 'Электронная почта' на странице 'Авторизация'"""
    def test_valid_input_email_eng_upper(self, driver):
        register_page = AuthInputEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email_input, email_text = register_page.valid_input_email_eng_upper()
        # Проверяем что поле "Электронная почта" отображает прописные буквы
        assert email_text != email_input

    """EXP-158 Ввод 255 символов в поле ввода 'Электронная почта' на странице 'Авторизация'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-035')
    def test_valid_input_email_255_symbol(self, driver):
        register_page = AuthInputEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email_input, email_text = register_page.valid_input_email_255_symbol()
        # Проверяем что поле "Электронная почта" не отображает все 255 символов
        assert len(email_text) != 255

    """EXP-159 Ввод 500 символов в поле ввода 'Электронная почта' на странице 'Авторизация'"""
    @pytest.mark.skip(reason='Баг в продукте - странице "Bugs: FB-036"')
    def test_valid_input_email_500_symbol(self, driver):
        register_page = AuthInputEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email_input, email_text = register_page.valid_input_email_500_symbol()
        # Проверяем что поле "Электронная почта" не отображает все 500 символов
        assert len(email_text) != 500

    """EXP-160 Ввод кирилльских и китайских символов в поле ввода 'Электронная почта' на странице 'Авторизация'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-037"')
    def test_valid_input_email_rus_chaine(self, driver):
        register_page = AuthInputEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email_text = register_page.valid_input_email_rus_chaine()
        # Проверяем что поле "Электронная почта" не отображает все кирилльские и китайские символы
        assert email_text == ''

    """EXP-161 Ввод валидных данных в поле ввода 'Электронная почта' с пробелом в середине текста на странице 'Авторизация'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-038')
    def test_valid_input_email_space_middle(self, driver):
        register_page = AuthInputEmail(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        email_input, email_text = register_page.valid_input_email_space_middle()
        # Проверяем что поле "Электронная почта" не отображает пробел в середине текста
        assert email_text == email_input


"""Валидность принятых данных, в поле для ввода 'Логин' на странице 'Авторизация'"""
class TestAuthInputLogin:

    """EXP-162 Ввод латиницы в поле ввода 'Логин' на странице 'Авторизация'"""
    def test_valid_input_login_eng(self, driver):
        register_page = AuthInputLogin(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        login_input, login_text = register_page.valid_input_login_eng()
        # Проверяем что поле "Логин" отображает вводимые латинские значения
        assert login_text == login_input

    """EXP-163 Ввод спец. символов в поле ввода 'Логин' на странице 'Авторизация'"""
    def test_valid_input_login_special_symbol(self, driver):
        register_page = AuthInputLogin(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        login_input, login_text = register_page.valid_input_login_special_symbol()
        # Проверяем что поле "Логин" отображает спец. символы
        assert login_text == login_input

    """EXP-164 Ввод чисел в поле ввода 'Логин' на странице 'Авторизация'"""
    def test_valid_input_login_num(self, driver):
        register_page = AuthInputLogin(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        login_input, login_text = register_page.valid_input_login_num()
        # Проверяем что поле "Логин" отображает числа
        assert int(login_text) == login_input

    """EXP-165 Ввод прописных букв в поле ввода 'Логин' на странице 'Авторизация'"""
    def test_valid_input_login_eng_upper(self, driver):
        register_page = AuthInputLogin(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        login_input, login_text = register_page.valid_input_login_eng_upper()
        # Проверяем что поле "Логин" отображает прописные буквы
        assert login_text != login_input

    """EXP-166 Ввод 255 символов в поле ввода 'Логин' на странице 'Авторизация'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-039')
    def test_input_login_255_symbol(self, driver):
        register_page = AuthInputLogin(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        login_input, login_text = register_page.input_login_255_symbol()
        # Проверяем что поле "Логин" не отображает все 255 символов
        assert len(login_text) != 255

    """EXP-167 Ввод 500 символов в поле ввода 'Логин' на странице 'Авторизация'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-040')
    def test_input_login_500_symbol(self, driver):
        register_page = AuthInputLogin(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        login_input, login_text = register_page.input_login_500_symbol()
        # Проверяем что поле "Логин" не отображает все 500 символов
        assert len(login_text) != 500

    """EXP-168 Ввод кирилльских и китайских символов в поле ввода 'Логин' на странице 'Авторизация'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-041')
    def test_input_login_rus_chaine(self, driver):
        register_page = AuthInputLogin(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        login_text = register_page.input_login_rus_chaine()
        # Проверяем что поле "Логин" не отображает все кирилльские и китайские символы
        assert login_text == ''

    """EXP-169 Ввод валидных данных в поле ввода 'Логин' с пробелом в середине текста на странице 'Авторизация'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-042')
    def test_input_login_space_middle(self, driver):
        register_page = AuthInputLogin(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        login_input, login_text = register_page.input_login_space_middle()
        # Проверяем что поле "Логин" не отображает пробел в середине текста
        assert login_text == login_input


"""Валидность принятых данных, в поле для ввода 'Лицевой счет'"""
class TestAuthInputPersonalAccount:

    """EXP-170 Валидный ввод 12 чисел в поле ввода 'Лицевой счет' на странице 'Авторизация'"""
    def test_valid_input_personal_account_12_num(self, driver):
        register_page = AuthInputPersonalAccount(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        personal_account_text = register_page.valid_input_personal_account_12_num()
        # Проверяем что поле "Лицевой счет" отображает валидное значение
        assert len(personal_account_text) == 12

    """EXP-171 Ввод данных в поле ввода 'Лицевой счет' с пробелом в середине на странице 'Авторизация'"""
    def test_input_personal_account_space_middle(self, driver):
        register_page = AuthInputPersonalAccount(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        personal_account_input, personal_account_text = register_page.input_personal_account_space_middle()
        # Проверяем поле "Лицевой счет" не принимает пробелов
        assert personal_account_text == personal_account_input

    """EXP-172 Ввод данных в поле ввода 'Лицевой счет' с пробелом в конце на странице 'Авторизация'"""
    def test_input_personal_account_space_end(self, driver):
        register_page = AuthInputPersonalAccount(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        personal_account_input, personal_account_text = register_page.input_personal_account_space_end()
        # Проверяем поле "Лицевой счет" не принимает пробелов
        assert personal_account_text == personal_account_input

    """EXP-173 Ввод кирилльских и латинских символов в поле ввода 'Лицевой счет' на странице 'Авторизация'"""
    def test_input_personal_account_rus_eng(self, driver):
        register_page = AuthInputPersonalAccount(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        personal_account_text = register_page.input_personal_account_rus_eng()
        # Проверяем поле "Лицевой счет" не принимает кирилльские и латинские символы
        assert personal_account_text == ''


"""Валидность принятых данных, в поле для ввода 'Пароль' на странице 'Авторизация'"""
class TestAuthPassword:

    # Тестируем с использованием валидных данных
    """EXP-174 Ввод латиницы в поле «Пароль» на странице 'Авторизация'"""
    def test_valid_password_eng(self, driver):
        register_page = AuthPassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass, input_pass = register_page.valid_password_eng()
        # Проверяем что поле "Пароль", принимает вводимые значения
        assert text_pass == input_pass

    """EXP-175 Ввод заглавных букв в поле «Пароль» на странице 'Авторизация'"""
    def test_valid_password_upper_symbol(self, driver):
        register_page = AuthPassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass, input_pass = register_page.valid_password_upper_symbol()
        # Проверяем что поле "Пароль", принимает вводимые значения
        assert text_pass == input_pass

    """EXP-176 Ввод чисел в поле «Пароль» на странице 'Авторизация'"""
    def test_valid_password_number(self, driver):
        register_page = AuthPassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass, input_pass = register_page.valid_password_number()
        # Проверяем что поле "Пароль", принимает вводимые значения
        assert text_pass == input_pass

    """EXP-177 Ввод спец. символов в поле «Пароль» на странице 'Авторизация'"""
    def test_valid_password_special_symbol(self, driver):
        register_page = AuthPassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass, input_pass = register_page.valid_password_special_symbol()
        # Проверяем что поле "Пароль", принимает вводимые значения
        assert text_pass == input_pass

    # Тестируем невалидных данных
    """EXP-178 Ввод кирилльских и китайских символов в поле «Пароль» на странице 'Авторизация'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-043"')
    def test_not_valid_password_rus_chaine(self, driver):
        register_page = AuthPassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass, input_pass = register_page.not_valid_password_rus_chaine()
        # Проверяем что поле "Пароль", не принимает вводимые значения
        assert text_pass != input_pass

    """EXP-179 Ввод данных с пробелом в тексте в поле «Пароль» на странице 'Авторизация'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-044"')
    def test_not_valid_password_spece(self, driver):
        register_page = AuthPassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass, input_pass = register_page.not_valid_password_spece()
        # Проверяем что поле "Пароль", не принимает пробелом в тексте
        assert text_pass == input_pass

    """EXP-180 Ввод 255 символов в поле «Пароль» на странице 'Авторизация'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-045"')
    def test_not_valid_password_255_symbol(self, driver):
        register_page = AuthPassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass = register_page.not_valid_password_255_symbol()
        # Проверяем что данные в поле "Пароль" не принимают 255 символов
        assert len(text_pass) != 255

    """EXP-181 Ввод 500 символов в поле «Пароль» на странице 'Авторизация'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-046"')
    def test_not_valid_password_500_symbol(self, driver):
        register_page = AuthPassword(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_pass = register_page.not_valid_password_500_symbol()
        # Проверяем что данные в поле "Пароль" не принимают 500 символов
        assert len(text_pass) != 500


class TestAuthPage:

    """EXP-182 Валидность заголовка на странице 'Авторизации'"""
    def test_main_title(self, driver):
        register_page = AuthPage(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_title = register_page.main_title()
        # Проверяем, что главный заголовок страницы валидный
        assert text_title == 'Авторизация'

    """EXP-183 Валидность кнопки в поле пароль на странице 'Авторизация'"""
    def test_button_password(self, driver):
        register_page = AuthPage(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        test = register_page.button_password()
        assert test == "Прошел"

    """EXP-184 Валидность кнопки 'Запомнить меня' на странице 'Авторизации'"""
    def test_button_forgot_password(self, driver):
        register_page = AuthPage(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        test = register_page.button_forgot_password()
        return test == "Прошел"

    """EXP-185 Валидность текстовой кнопки 'Запомнить меня' на странице 'Авторизации'"""
    def test_button_text_forgot_password(self, driver):
        register_page = AuthPage(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_button = register_page.button_text_forgot_password()
        # Проверяем, что название текстовой кнопки валидно
        assert text_button == 'Запомнить меня'

    """EXP-186 Валидность кнопки 'Забыл пароль' на странице 'Авторизации'"""
    def test_button_recovery_password(self, driver):
        register_page = AuthPage(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_button, url = register_page.button_recovery_password()
        # Проверяем, что название текстовой кнопки валидно
        assert text_button == 'Забыл пароль'
        # Проверяем что при нажатии на кнопку, пользователь переходет на страницу 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/reset-credentials'

    """EXP-187 Пользователь нажимает на кнопку 'Пользовательские соглашения' под кнопкой 'Войти', на странице 'Авторизации'"""
    def test_button_user_agreements(self, driver):
        register_page = AuthPage(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_user_agreements, url = register_page.button_user_agreements()
        # Проверяем что кнопка отображает валидное значение
        assert text_user_agreements == 'пользовательского соглашения'
        # Проверяем что мы перешли на страницу Пользовательского соглашения
        assert url == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

    """EXP-188 Валидность кнопки 'Зарегистрироваться' на странице 'Авторизации'"""
    def test_button_register(self, driver):
        register_page = AuthPage(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_button, url = register_page.button_register()
        # Проверяем, что название текстовой кнопки валидно
        assert text_button == 'Зарегистрироваться'
        # Проверяем что при нажатии на кнопку, пользователь переходет на страницу 'Восстановления пароля'
        assert url == '/auth/realms/b2c/login-actions/registration'

    """EXP-189 Валидность текса продуктового слогана, на странице 'Авторизации'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-047"')
    def test_product_slogan(self, driver):
        register_page = AuthPage(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text = register_page.product_slogan()
        # Проверяем, что название валидно
        assert text == 'Ростелеком ID'


"""Валидность иконок социальных сетей"""
class TestSocialNetworks:

    """EXP-190 Функционал иконки VK"""
    def test_iconka_vk(self, driver):
        register_page = SocialNetworks(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        url = register_page.iconka_vk()
        # Проверяем что при нажатии на кнопку, пользователь переходит на сайт 'VK'
        assert url == 'https://id.vk.com/auth'

    """EXP-191 Функционал иконки OK"""
    def test_iconka_ok(self, driver):
        register_page = SocialNetworks(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        url = register_page.iconka_ok()
        # Проверяем что при нажатии на кнопку, пользователь переходит на сайт 'OK'
        assert url == 'https://connect.ok.ru/dk'

    """EXP-192 Функционал иконки Mail"""
    def test_iconka_mail(self, driver):
        register_page = SocialNetworks(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        url = register_page.iconka_mail()
        # Проверяем что при нажатии на кнопку, пользователь переходит на сайт 'MAIL'
        assert url == 'https://connect.mail.ru/oauth/authorize'

    """EXP-193 Функционал иконки Yandex"""
    @pytest.mark.skipif(reason='???ХЗ???')
    def test_iconka_ya(self, driver):
        register_page = SocialNetworks(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        url = register_page.iconka_ya()
        # Проверяем что при нажатии на кнопку, пользователь переходит на сайт 'YA'
        assert url == 'https://passport.yandex.ru/auth'


"""Проверка footer на функционал"""
class TestAuthFooter:

    """EXP-194 Пользователь нажимает на кнопку 'Cookies' в footer на странице 'Авторизации'"""
    def test_button_cookie_footer(self, driver):
        register_page = AuthFooter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        cookie_text = register_page.button_cookie_footer()
        # Проверяем что при нажатии на кнопку 'Cookies' отображается шаблон с текстом
        assert cookie_text == 'Мы используем Cookie'

    """EXP-195 В отобразившемся шаблоне 'Cookies' нажать на кнопку 'крестик' на странице 'Авторизации'"""
    def test_button_cookie_close_footer(self, driver):
        register_page = AuthFooter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        test = register_page.button_cookie_close_footer()
        return test == "Прошел"

    """EXP-196 Пользователь нажимает на кнопку 'Политикой конфиденциальности' в footer на странице 'Авторизации'"""
    def test_button_privacy_policy_footer(self, driver):
        register_page = AuthFooter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_privacy_policy, url = register_page.button_privacy_policy_footer()
        # Проверяем что кнопка отображает валидное значение
        assert text_privacy_policy == 'Политикой конфиденциальности'
        # Проверяем что мы перешли на страницу Политикой конфиденциальности
        assert url == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

    """EXP-197 Пользователь нажимает на кнопку 'Пользовательские соглашения' в footer на странице 'Авторизации'"""
    def test_button_user_agreements_footer(self, driver):
        register_page = AuthFooter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        text_user_agreements, url = register_page.button_user_agreements_footer()
        # Проверяем что кнопка отображает валидное значение
        assert text_user_agreements == 'Пользовательским соглашением'
        # Проверяем что мы перешли на страницу Пользовательского соглашения
        assert url == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'


"""Логика типа ввода контактных данных"""
class TestAuthLogicTypeInput:

    """EXP-198 Логика типа ввода контактных данных телефона, когда в поле ввода 'Мобильный телефон' не полный номер
    на странице 'Авторизация'"""
    def test_incomplete_number_phone(self, driver):
        register_page = AuthLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error = register_page.incomplete_number_phone()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный формат телефона'

    """EXP-199 Логика типа ввода контактных данных телефона, когда в поле ввода 'Мобильный телефон' латинские буквы 
    на странице 'Авторизация'"""
    def test_input_eng_phone(self, driver):
        register_page = AuthLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_eng_phone()
        # Проверяем что при вводе латинских букв, тип ввода контактных данных меняется на 'Логин'
        assert type_data == 'Логин'

    """EXP-200 Логика типа ввода контактных данных телефона, когда в поле ввода 'Мобильный телефон' спец. символы на 
    странице 'Авторизация'"""
    def test_input_special_symbol_phone(self, driver):
        register_page = AuthLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_special_symbol_phone()
        # Проверяем что при вводе спец. символов, тип ввода контактных данных меняется на 'Логин'
        assert type_data == 'Логин'

    """EXP-201 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' номер телефона на 
    странице 'Авторизация'"""
    def test_input_number_phone_field_email(self, driver):
        register_page = AuthLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_number_phone_field_email()
        # Проверяем что при вводе номера телефона, тип ввода контактных данных меняется на 'Номер'
        assert type_data == 'Мобильный телефон'

    """EXP-202 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' числа на странице 
    'Авторизация'"""
    def test_input_number_field_email(self, driver):
        register_page = AuthLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_number_field_email()
        # Проверяем что при вводе чисел, тип ввода контактных данных меняется на 'Логин'
        assert type_data == 'Логин'

    """EXP-203 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' латинские буквы на 
    странице 'Авторизация'"""
    def test_input_eng_email(self, driver):
        register_page = AuthLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_eng_email()
        # Проверяем что при вводе латинских букв, тип ввода контактных данных меняется на 'Логин'
        assert type_data == 'Логин'

    """EXP-204 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' спец. символы на 
    странице 'Авторизация'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-048')
    def test_input_special_symbol_email(self, driver):
        register_page = AuthLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_special_symbol_email()
        # Проверяем что при вводе спец. символы, тип ввода контактных данных не меняется
        assert type_data == 'Электронная почта'

    """EXP-205 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' 12 цифр на странице 
    'Авторизация'"""
    def test_input_12_number_email(self, driver):
        register_page = AuthLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_12_number_email()
        # Проверяем что при вводе 12 цифр, тип ввода контактных данных меняется на 'Лицевой счёт'
        assert type_data == 'Лицевой счёт'

    """EXP-206 Логика типа ввода контактных данных логин, когда в поле ввода 'Логин' номер телефона на странице 
    'Авторизация'"""
    @pytest.mark.skip(reason='Баг в продукте - "Bugs: FB-049')
    def test_input_number_phone_field_login(self, driver):
        register_page = AuthLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_number_phone_field_login()
        # Проверяем что при вводе номера телефона, тип ввода контактных данных не меняется
        assert type_data == 'Логин'

    """EXP-207 Логика типа ввода контактных данных логин, когда в поле ввода 'Логин' 12 цифр на странице 
    'Авторизация'"""
    def test_input_12_number_login(self, driver):
        register_page = AuthLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_12_number_login()
        # Проверяем что при вводе 12 цифр, тип ввода контактных данных меняется на 'Лицевой счёт'
        assert type_data == 'Лицевой счёт'

    """EXP-208 Логика типа ввода контактных данных логин, когда в поле ввода 'Логин' латинские буквы на странице 
    'Авторизация'"""
    def test_input_eng_login(self, driver):
        register_page = AuthLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_eng_login()
        # Проверяем что при вводе латинских букв, тип ввода контактных данных остается 'Логин'
        assert type_data == 'Логин'

    """EXP-209 Логика типа ввода контактных данных логин, когда в поле ввода 'Логин' спец. символы на странице 
    'Авторизация'"""
    def test_input_special_symbol_login(self, driver):
        register_page = AuthLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_special_symbol_login()
        # Проверяем что при вводе спец. символов, тип ввода контактных данных остается 'Логин'
        assert type_data == 'Логин'

    """EXP-210 Логика типа ввода контактных данных лицевой счёт, когда в поле ввода 'Лицевой счёт' номер телефона на 
    странице 'Авторизация'"""
    def test_input_number_phone_field_person_account(self, driver):
        register_page = AuthLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_number_phone_field_person_account()
        # Проверяем что при вводе номера телефона, тип ввода контактных данных остается 'Лицевой счёт'
        assert type_data == 'Лицевой счёт'

    """EXP-211 Логика типа ввода контактных данных лицевой счёт, когда в поле ввода 'Лицевой счёт' не полный лицевой 
    счет на странице 'Авторизация'"""
    def test_input_incomplete_person_account(self, driver):
        register_page = AuthLogicTypeInput(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        type_data = register_page.input_incomplete_person_account()
        # Проверяем что при вводе не полный лицевой счет, тип ввода контактных данных остается 'Лицевой счёт'
        assert type_data == 'Лицевой счёт'


"""Логика кнопки войти с использованием валидных и невалидных данных"""
@pytest.mark.skip(reason='Тесты не валидны из-за капчи')
class TestAuthLogicButtonEnter:

    """EXP-212 Логика кнопки 'Войти', когда валидны данные только в поле 'Мобильный телефон'"""
    def test_valid_phone_not_valid_pass(self, driver):
        register_page = AuthLogicButtonEnter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        button_enter, error, url = register_page.valid_phone_not_valid_pass()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или пароль'
        # Проверяем валидность названия кнопки 'Войти'
        assert button_enter == 'Войти'
        # Проверяем что пользователь остался на странице 'Авторизация'
        assert url == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate'

    """EXP-213 Логика кнопки 'Войти', когда в полях введены невалидны данные"""
    def test_not_valid_phone_not_valid_pass(self, driver):
        register_page = AuthLogicButtonEnter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.not_valid_phone_not_valid_pass()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или пароль'
        # Проверяем что пользователь остался на странице 'Авторизация'
        assert url == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate'

    """EXP-214 Логика кнопки 'Войти', когда валидны данные только в поле 'Мобильный телефон', поле 'Пароль' пустое"""
    def test_valid_phone_empty_pass(self, driver):
        register_page = AuthLogicButtonEnter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.valid_phone_empty_pass()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или пароль'
        # Проверяем что пользователь остался на странице 'Авторизация'
        assert url == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate'

    """EXP-215 Логика кнопки 'Войти' по почте, когда введены валидны данные"""
    def test_valid_email_valid_pass(self, driver):
        register_page = AuthLogicButtonEnter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        url = register_page.valid_email_valid_pass()
        # Проверяем что пользователь вошел в свой аккаунт
        assert url == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate'

    """EXP-216 Логика кнопки 'Войти' по почте, когда валидны данные только в поле 'Электронная почта'"""
    def test_valid_email_not_valid_pass(self, driver):
        register_page = AuthLogicButtonEnter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.valid_email_not_valid_pass()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или пароль'
        # Проверяем что пользователь остался на странице 'Авторизация'
        assert url == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate'

    """EXP-217 Логика кнопки 'Войти' по почте, когда в полях введены невалидны данные"""
    def test_not_valid_email_not_valid_pass(self, driver):
        register_page = AuthLogicButtonEnter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.not_valid_email_not_valid_pass()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или пароль'
        # Проверяем что пользователь остался на странице 'Авторизация'
        assert url == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate'

    """EXP-218 Логика кнопки 'Войти' по почте, когда данные 'Электронная почта' валидна, поле 'Пароль' пустое"""
    def test_valid_email_empty_pass(self, driver):
        register_page = AuthLogicButtonEnter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.valid_email_empty_pass()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или пароль'
        # Проверяем что пользователь остался на странице 'Авторизация'
        assert url == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate'

    """EXP-219 Логика кнопки 'Войти' по логину, когда валидны данные только в поле 'Логин'"""
    def test_valid_login_not_valid_pass(self, driver):
        register_page = AuthLogicButtonEnter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.valid_login_not_valid_pass()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или пароль'
        # Проверяем что пользователь остался на странице 'Авторизация'
        assert url == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate'

    """EXP-220 Логика кнопки 'Войти' по логину, когда в полях введены невалидны данные"""
    def test_not_valid_login_not_valid_pass(self, driver):
        register_page = AuthLogicButtonEnter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.not_valid_login_not_valid_pass()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или пароль'
        # Проверяем что пользователь остался на странице 'Авторизация'
        assert url == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate'

    """EXP-221 Логика кнопки 'Войти', когда данные 'Логин' валиден, поле 'Пароль' пустое"""
    def test_valid_login_empty_pass(self, driver):
        register_page = AuthLogicButtonEnter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.valid_login_empty_pass()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или пароль'
        # Проверяем что пользователь остался на странице 'Авторизация'
        assert url == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate'

    """EXP-222 Логика кнопки 'Войти' по лицевому счету, когда валидны данные только в поле 'Лицевой счет'"""
    def test_valid_person_account_not_valid_pass(self, driver):
        register_page = AuthLogicButtonEnter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.valid_person_account_not_valid_pass()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или пароль'
        # Проверяем что пользователь остался на странице 'Авторизация'
        assert url == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate'

    """EXP-223 Логика кнопки 'Войти' по лицевому счету, когда поле 'ЛС' пустое; в поле 'Пароль' невалидные данные"""
    def test_empty_person_account_not_valid_pass(self, driver):
        register_page = AuthLogicButtonEnter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.empty_person_account_not_valid_pass()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Введите номер вашего лицевого счета'
        # Проверяем что пользователь остался на странице 'Авторизация'
        assert url == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate'

    """EXP-224 Логика кнопки 'Войти' по лицевому счету, когда данные 'ЛС' валидны, поле 'Пароль' пустое"""
    def test_valid_person_account_empty_pass(self, driver):
        register_page = AuthLogicButtonEnter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.valid_person_account_empty_pass()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Неверный логин или пароль'
        # Проверяем что пользователь остался на странице 'Авторизация'
        assert url == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate'

    """EXP-225 Логика кнопки 'Войти' по лицевому счету, когда данные 'ЛС' невалидны, поле 'Пароль' пустое"""
    def test_not_valid_person_account_empty_pass(self, driver):
        register_page = AuthLogicButtonEnter(driver, url='https://b2c.passport.rt.ru')
        register_page.open()
        error, url = register_page.not_valid_person_account_empty_pass()
        # Проверяем что при не верном вводе данных, отображается текст с ошибкой
        assert error == 'Проверьте, пожалуйста, номер лицевого счета'
        # Проверяем что пользователь остался на странице 'Авторизация'
        assert url == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate'


"""Форма авторизации с настройкой (Блокировать/Отключить файлы cookie)"""
class TestAuthCookie:

    """EXP-226 При отключении cookie всплывает окно"""
    @pytest.mark.skipif(reason="Cookie не отключаются")
    def test_cookie_title_text(self, cookie):
        register_page = AuthCookie(cookie, url='https://b2c.passport.rt.ru')
        register_page.open()
        cookie = register_page.cookie_title_text()
        assert cookie == "Cookie отключены"