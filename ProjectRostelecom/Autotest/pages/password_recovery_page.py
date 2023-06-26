import time
from generator.generator import *
from pages.base import BasePage
from locators.locator_password_recovery import LocatorPasswordRecovery as Locator



class PasswordRecoveryButtonType(BasePage):

    # EXP-064 Функция выбора по восстановлению пароля, автоматически выбран "Номер"
    def auto_pass_recovery_selection(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_USERNAME).click()
        # Название кнопки выбора формы восстановления пароля
        phone = self.element_is_visible(Locator.PHONE).text
        # Название поле для ввода 'Мобильный телефон'
        name_field = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return phone, name_field, url

    # EXP-065 Функционирование кнопки "Почта"
    def button_email(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        email = self.element_is_visible(Locator.EMAIL)
        email.click()
        # Название кнопки выбора формы восстановления пароля
        email_text = email.text
        # Название поле для ввода 'Электронная почта'
        name_field = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return email_text, name_field, url

    # EXP-066 Функционирование кнопки "Логин"
    def button_login(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        login = self.element_is_visible(Locator.LOGIN)
        login.click()
        # Название кнопки выбора формы восстановления пароля
        login_text = login.text
        # Название поле для ввода 'Логин'
        name_field = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return login_text, name_field, url

    # EXP-067 Функционирование кнопки "Лицевой счёт"
    def button_personal_account(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        personal_account = self.element_is_visible(Locator.PERSONAL_ACCOUNT)
        personal_account.click()
        # Название кнопки выбора формы восстановления пароля
        personal_account_text = personal_account.text
        # Название поле для ввода 'Лицевой счёт'
        name_field = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return personal_account_text, name_field, url

class PasswordRecoveryInputPhone(BasePage):

    # EXP-068 Валидность принятых данных, в поле для ввода 'Номер', введены данные в формате +7ХХХХХХХХХХ
    def input_phone_number_seven(self):
        # Генератор телефона
        phone_input = generator_phone_number_7("+7")
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input)
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return phone_input, phone_text, url

    # EXP-069 Валидность принятых данных, в поле для ввода 'Номер', введены данные в формате +375XXXXXXXXX
    def input_phone_number_three(self):
        # Генератор телефона
        phone_input = generator_phone_number_7('+375')
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input)
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return phone_input, phone_text, url

    # EXP-070 Валидность принятых данных, в поле для ввода 'Номер', введены данные в формате 7ХХХХХХХХХХ
    def input_phone_number_seven_not_plus(self):
        # Генератор телефона
        phone_input = generator_phone_number_7('7')
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input)
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return phone_text, url

    # EXP-071 Валидность принятых данных, в поле для ввода 'Номер', введены данные в формате 8ХХХХХХХХХХ
    def input_phone_number_eight_not_plus(self):
        # Генератор телефона
        phone_input = generator_phone_number_7('8')
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input)
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return phone_text, url

    # EXP-072 Валидность принятых данных, в поле для ввода 'Номер', введены данные в формате 375XXXXXXXXX
    def input_phone_number_three_not_plus(self):
        # Генератор телефона
        phone_input = generator_phone_number_7('375')
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input)
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return phone_text, url

    # EXP-073 Валидность принятых данных, в поле для ввода 'Номер', введены данные в формате +375XXXXXXXXX
    def input_phone_number_three_more_values(self):
        num = generator_number()
        # Генератор телефона
        phone_input = generator_phone_number_7('+375')
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input + str(num))
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return phone_text, url

    # EXP-074 Валидность принятых данных, в поле для ввода 'Номер', введены данные в формате +7ХХХХХХХХХХ
    def input_phone_number_seven_more_values(self):
        num = generator_number()
        # Генератор телефона
        phone_input = generator_phone_number_7('+7')
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input + str(num))
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return phone_text, url

    # EXP-075 Валидность принятых данных, в поле для ввода 'Номер', когда первая цифра не валидна
    def input_phone_first_digit_not_valid(self):
        # Генератор телефона
        phone_input = generator_phone_number_7('1')
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input)
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return phone_text, url

    # EXP-076 Валидность принятых данных, в поле для ввода 'Номер', когда в середине строки поставлен пробел
    def input_phone_space_middle(self):
        # Генератор телефона
        phone_input = generator_phone_number_7('+7')
        # Добавляем пробел в середину текста
        phone_input = phone_input[:7] + " " + phone_input[7:]
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input)
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace('-', '')
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return phone_text, url

    # EXP-077 Валидность принятых данных, в поле для ввода 'Номер', когда в конце строки поставлен пробел
    def input_phone_space_end(self):
        # Генератор телефона
        phone_input = generator_phone_number_7('+7')
        # Добавляем пробел в конец текста
        phone_input = phone_input[:12] + " "
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input)
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace('-', '')
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return phone_text, url

    # EXP-078 Ввод кириллицы в поле для ввода 'Мобильный телефон
    def input_phone_rus_eng(self):
        # Генератор кириллицы и латиницы
        phone_input = generator_lower_rus(5)
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input)
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return phone_text, url


class PasswordRecoveryInputEmail(BasePage):

    # EXP-079 Ввод латиницы в поле для ввода 'Электронная почта'
    def valid_input_email_eng(self):
        # Генератор латиницы
        email_input = generator_lowers_eng()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email_input)
        # Текст в поле 'Электронная почта'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        email_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return email_input, email_text, url

    # EXP-080 Ввод спец. символов в поле для ввода 'Электронная почта'
    def valid_input_email_special_symbol(self):
        # Генератор латиницы
        email_input = generator_special_symbol()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email_input)
        # Текст в поле 'Электронная почта'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        email_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return email_input, email_text, url

    # EXP-081 Ввод числа в поле для ввода 'Электронная почта'
    def valid_input_email_num(self):
        # Генератор латиницы
        email_input = generator_number()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email_input)
        # Текст в поле 'Электронная почта'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        email_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return email_input, email_text, url

    # EXP-082 Ввод прописных букв в поле для ввода 'Электронная почта'
    def valid_input_email_eng_upper(self):
        # Генератор латиницы
        email_input = generator_eng_upper()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email_input)
        # Текст в поле 'Электронная почта'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        email_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return email_input, email_text, url

    # EXP-083 Ввод 255 символов в поле для ввода 'Электронная почта'
    def valid_input_email_255_symbol(self):
        # Генератор латиницы
        email_input = generator_eng_lowers_col(255)
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email_input)
        # Текст в поле 'Электронная почта'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        email_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return email_input, email_text, url

    # EXP-084 Ввод 500 символов в поле для ввода 'Электронная почта'
    def valid_input_email_500_symbol(self):
        # Генератор латиницы
        email_input = generator_eng_lowers_col(500)
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email_input)
        # Текст в поле 'Электронная почта'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        email_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return email_input, email_text, url

    # EXP-085 Ввод кирилльских и китайских символов в поле ввода 'Электронная почта'
    def valid_input_email_rus_chaine(self):
        # Генератор латиницы
        email_input = generator_lowers_rus_chaine()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email_input)
        # Текст в поле 'Электронная почта'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        email_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return email_text, url

    # EXP-086 Ввод валидных данных в поле ввода 'Электронная почта' с пробелом в середине текста
    def valid_input_email_space_middle(self):
        # Генератор латиницы
        email_input = generator_lowers_eng()
        # Добавляем пробел в середину текста
        email_input = email_input[:5] + " " + email_input[5:]
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email_input)
        # Убираем пробел для проверки
        email_input = email_input.replace(' ', '')
        # Текст в поле 'Электронная почта'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        email_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return email_input, email_text, url


class PasswordRecoveryInputLogin(BasePage):

    # EXP-087 Ввод латиницы в поле для ввода 'Логин'
    def valid_input_login_eng(self):
        # Генератор латиницы
        login_input = generator_lowers_eng()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login_input)
        # Текст в поле 'Логин'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        login_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return login_input, login_text, url

    # EXP-088 Ввод спец. символов в поле для ввода 'Логин'
    def valid_input_login_special_symbol(self):
        # Генератор латиницы
        login_input = generator_special_symbol()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login_input)
        # Текст в поле 'Логин'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        login_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return login_input, login_text, url

    # EXP-089 Ввод числа в поле для ввода 'Логин'
    def valid_input_login_num(self):
        # Генератор латиницы
        login_input = generator_number()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login_input)
        # Текст в поле 'Логин'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        login_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return login_input, login_text, url

    # EXP-090 Ввод прописных букв в поле для ввода 'Логин'
    def valid_input_login_eng_upper(self):
        # Генератор латиницы
        login_input = generator_eng_upper()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login_input)
        # Текст в поле 'Логин'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        login_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return login_input, login_text, url

    # EXP-091 Ввод 255 символов в поле для ввода 'Логин'
    def input_login_255_symbol(self):
        # Генератор латиницы
        login_input = generator_eng_lowers_col(255)
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login_input)
        # Текст в поле 'Логин'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        login_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return login_input, login_text, url

    # EXP-092 Ввод 500 символов в поле для ввода 'Логин'
    def input_login_500_symbol(self):
        # Генератор латиницы
        login_input = generator_eng_lowers_col(500)
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login_input)
        # Текст в поле 'Логин'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        login_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return login_input, login_text, url

    # EXP-093 Ввод кирилльских и китайских символов в поле ввода 'Логин'
    def input_login_rus_chaine(self):
        # Генератор латиницы
        login_input = generator_lowers_rus_chaine()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login_input)
        # Текст в поле 'Логин'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        login_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return login_text, url

    # EXP-094 Ввод валидных данных в поле ввода 'Логин' с пробелом в середине текста
    def input_login_space_middle(self):
        # Генератор латиницы
        login_input = generator_lowers_eng()
        # Добавляем пробел в середину текста
        login_input = login_input[:5] + " " + login_input[5:]
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login_input)
        # Убираем пробел для проверки
        login_input = login_input.replace(' ', '')
        # Текст в поле 'Логин'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        login_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return login_input, login_text, url


class PasswordRecoveryInputPersonalAccount(BasePage):

    # EXP-095 Валидный ввод 12 чисел в поле ввода 'Лицевой счет'
    def valid_input_personal_account_12_num(self):
        # Генератор лицевого счета
        personal_account_input = generator_phone_number_7('14')
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(personal_account_input)
        # Текст в поле 'Лицевой счет'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        personal_account_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return personal_account_text, url

    # EXP-096 Ввод данных в поле ввода 'Лицевой счет' с пробелом в середине
    def input_personal_account_space_middle(self):
        # Генератор лицевого счета
        personal_account_input = generator_phone_number_7('54')
        # Добавляем пробел в середину текста
        personal_account_input = personal_account_input[:6] + " " + personal_account_input[6:]
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(personal_account_input)
        # Текст в поле 'Лицевой счет'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        personal_account_text = self.get_attribute(text)
        # Убираем пробел для проверки
        personal_account_input = personal_account_input.replace(' ', '')
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return personal_account_input, personal_account_text, url

    # EXP-097 Ввод данных в поле ввода 'Лицевой счет' с пробелом в конце
    def input_personal_account_space_end(self):
        # Генератор лицевого счета
        personal_account_input = generator_phone_number_7('54')
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(personal_account_input + ' ')
        # Текст в поле 'Лицевой счет'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        personal_account_text = self.get_attribute(text)
        # Убираем пробел для проверки
        personal_account_input = personal_account_input.replace(' ', '')
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return personal_account_input, personal_account_text, url

    # EXP-098 Ввод кирилльских и латинских символов в поле ввода 'Лицевой счет'
    def input_personal_account_rus_eng(self):
        # Генератор кирилльских и латинских символов
        personal_account_input = generator_lowers_rus_eng()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(personal_account_input)
        # Текст в поле 'Лицевой счет'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        personal_account_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return personal_account_text, url


class PasswordRecoveryInputSymbol(BasePage):

    # EXP-099 Ввод латинских символов в поле ввода 'Символы'
    def valid_input_personal_account_symbol(self):
        # Генератор латинских букв
        symbol_input = generator_lowers_eng()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_CAPTCHA).send_keys(symbol_input)
        # Текст в поле 'Символы'
        text = self.element_is_visible(Locator.INPUT_CAPTCHA)
        symbol_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return symbol_input, symbol_text, url

    # EXP-100 Ввод чисел в поле ввода 'Символы'
    def valid_input_personal_account_num(self):
        # Генератор чисел
        symbol_input = str(generator_number())
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_CAPTCHA).send_keys(symbol_input)
        # Текст в поле 'Символы'
        text = self.element_is_visible(Locator.INPUT_CAPTCHA)
        symbol_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return symbol_input, symbol_text, url

    # EXP-101 Ввод прописных букв в поле ввода 'Символы'
    def valid_input_personal_account_upper(self):
        # Генератор прописных букв
        symbol_input = generator_eng_upper()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_CAPTCHA).send_keys(symbol_input)
        # Текст в поле 'Символы'
        text = self.element_is_visible(Locator.INPUT_CAPTCHA)
        symbol_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return symbol_input, symbol_text, url

    # EXP-102 Ввод кирилльских и китайских символов в поле ввода 'Символы'
    def input_personal_account_rus_chaine(self):
        # Генератор кирилльских и китайских символов
        symbol_input = generator_lowers_rus_chaine()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_CAPTCHA).send_keys(symbol_input)
        # Текст в поле 'Символы'
        text = self.element_is_visible(Locator.INPUT_CAPTCHA)
        symbol_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return symbol_text, url

    # EXP-103 Ввод 255 символов в поле ввода 'Символы'
    def input_personal_account_255_symbol(self):
        # Генератор 255 символов
        symbol_input = generator_eng_lowers_col(255)
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_CAPTCHA).send_keys(symbol_input)
        # Текст в поле 'Символы'
        text = self.element_is_visible(Locator.INPUT_CAPTCHA)
        symbol_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return symbol_text, url

    # EXP-104 Ввод 500 символов в поле ввода 'Символы'
    def input_personal_account_500_symbol(self):
        # Генератор 500 символов
        symbol_input = generator_eng_lowers_col(500)
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_CAPTCHA).send_keys(symbol_input)
        # Текст в поле 'Символы'
        text = self.element_is_visible(Locator.INPUT_CAPTCHA)
        symbol_text = self.get_attribute(text)
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return symbol_text, url


class PasswordRecovery(BasePage):

    # EXP-105 Валидность заголовка на странице 'Восстановление пароля'
    def main_title(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        text = self.element_is_visible(Locator.MAIN_TITLE).text
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return text, url

    # EXP-106 Валидность текста над выбором типа ввода контактных данных
    def text_above_type(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        text = self.element_is_visible(Locator.TEXT_ABOVE_TYPE).text
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return text, url

    # EXP-107 Функциональность кнопки 'Вернутся назад'
    def button_back(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        text = self.element_is_visible(Locator.BUTTON_GO_BACK).text
        self.element_is_visible(Locator.BUTTON_GO_BACK).click()
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return text, url

class PasswordRecoveryFooter(BasePage):

    # EXP-108 Пользователь нажимает на кнопку 'Cookies' в footer
    def button_cookie_footer(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.COOKIE).click()
        cookie_text = self.element_is_visible(Locator.COOKIE_TEXT).text
        return cookie_text

    # EXP-109 В отобразившемся шаблоне 'Cookies' нажать на кнопку 'крестик'
    def button_cookie_close_footer(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.COOKIE).click()
        cookie_text_close = self.element_is_visible(Locator.COOKIE_TEXT_CLOSE)
        # Если кнопка видима и активна, а так же он видим пользователю
        if cookie_text_close.is_enabled() and cookie_text_close.is_displayed():
            print("Кнопка 'крестик' доступен для нажатия в отобразившемся шаблоне 'Cookies'")
        else:
            print("Кнопка 'крестик' недоступен для нажатия в отобразившемся шаблоне 'Cookies'")

    # EXP-110 Пользователь нажимает на кнопку 'Политикой конфиденциальности' в footer
    def button_privacy_policy_footer(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        privacy_policy = self.element_is_visible(Locator.PRIVACY_POLICY).text
        self.element_is_visible(Locator.PRIVACY_POLICY).click()
        self.new_window()
        url = self.get_relative_link_http()
        return privacy_policy, url

    # EXP-111 Пользователь нажимает на кнопку 'Пользовательские соглашения' в footer
    def button_user_agreements_footer(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        text_user_agreements = self.element_is_visible(Locator.USER_AGREEMENTS_FOOTER).text
        self.element_is_visible(Locator.USER_AGREEMENTS_FOOTER).click()
        self.new_window()
        url = self.get_relative_link_http()
        return text_user_agreements, url


class PasswordRecoveryContinue(BasePage):

    # EXP-112 Логика восстановление пароля, когда валидны данные только в поле 'восстановления пароля по телефону'
    def valid_phone_not_valid_symbol(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys('+79193242824')
        self.element_is_visible(Locator.INPUT_CAPTCHA).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.BUTTON_CONTINUE).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR).text
        # Название кнопки 'Далее'
        text_button = self.element_is_visible(Locator.BUTTON_CONTINUE).text
        url = self.get_relative_link()
        return text_button, error, url

    # EXP-113 Логика кнопки 'Далее' в форме 'восстановления пароля по телефону', когда в полях введены невалидны данные
    def not_valid_phone_not_valid_symbol(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.INPUT_CAPTCHA).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.BUTTON_CONTINUE).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR).text
        url = self.get_relative_link()
        return error, url

    # EXP-114 Логика кнопки 'Далее', когда данные 'восстановления пароля по телефону' валидны, поле 'Символы' пустое
    def valid_phone_empty_symbol(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys('+79193242824')
        self.element_is_visible(Locator.BUTTON_CONTINUE).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR).text
        url = self.get_relative_link()
        return error, url

    # EXP-115 Логика восстановление пароля, когда валидны данные только в поле 'восстановления пароля по почте'
    def valid_email_not_valid_symbol(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys('shebarshov2015@mail.ru')
        self.element_is_visible(Locator.INPUT_CAPTCHA).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.BUTTON_CONTINUE).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR).text
        url = self.get_relative_link()
        return error, url

    # EXP-116 Логика кнопки 'Далее' в форме 'восстановления пароля по почте', когда в полях введены невалидны данные
    def not_valid_email_not_valid_symbol(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.INPUT_CAPTCHA).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.BUTTON_CONTINUE).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR).text
        url = self.get_relative_link()
        return error, url

    # EXP-117 Логика кнопки 'Далее', когда данные 'восстановления пароля по почте' валидны, поле 'Символы' пустое
    def valid_email_empty_symbol(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys('shebarshov2015@mail.ru')
        self.element_is_visible(Locator.BUTTON_CONTINUE).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR).text
        url = self.get_relative_link()
        return error, url

    # EXP-118 Логика восстановление пароля, когда валидны данные только в поле 'восстановления пароля по логину'
    def valid_login_not_valid_symbol(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys('lk_46106848')
        self.element_is_visible(Locator.INPUT_CAPTCHA).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.BUTTON_CONTINUE).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR).text
        url = self.get_relative_link()
        return error, url

    # EXP-119 Логика кнопки 'Далее' в форме 'восстановления пароля по логину', когда в полях введены невалидны данные
    def not_valid_login_not_valid_symbol(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.INPUT_CAPTCHA).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.BUTTON_CONTINUE).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR).text
        url = self.get_relative_link()
        return error, url

    # EXP-120 Логика кнопки 'Далее', когда данные 'восстановления пароля по логину' валидны, поле 'Символы' пустое
    def valid_login_empty_symbol(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys('lk_46106848')
        self.element_is_visible(Locator.BUTTON_CONTINUE).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR).text
        url = self.get_relative_link()
        return error, url

    # EXP-121 Логика восстановление пароля, когда валидны данные только в поле 'восстановления пароля по ЛС'
    def valid_person_account_not_valid_symbol(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys('850014328079')
        self.element_is_visible(Locator.INPUT_CAPTCHA).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.BUTTON_CONTINUE).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR).text
        url = self.get_relative_link()
        return error, url

    # EXP-122 Логика кнопки 'Далее', когда в поле 'ЛС' пустое; в поле 'Символ' невалидные данные
    def empty_person_account_not_valid_symbol(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_CAPTCHA).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.BUTTON_CONTINUE).click()
        time.sleep(1)
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR_UNDER_INPUT).text
        url = self.get_relative_link()
        return error, url

    # EXP-123 Логика кнопки 'Далее', когда данные 'восстановления пароля по ЛС' валидны, поле 'Символы' пустое
    def valid_person_account_empty_symbol(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys('850014328079')
        self.element_is_visible(Locator.BUTTON_CONTINUE).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR).text
        url = self.get_relative_link()
        return error, url

    # EXP-124 Логика кнопки 'Далее', когда данные 'восстановления пароля по ЛС' невалидны, поле 'Символы' пустое
    def not_valid_person_account_empty_symbol(self):
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys('8500143')
        self.element_is_visible(Locator.BUTTON_CONTINUE).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR_UNDER_INPUT).text
        url = self.get_relative_link()
        return error, url


class PasswordRecoveryLogicTypeInput(BasePage):

    # EXP-125 Логика типа ввода контактных данных телефона, когда в поле ввода 'Мобильный телефон' не полный номер
    def incomplete_number_phone(self):
        # Генерируем телефон
        person_info = next(generator_parsen())
        phone = person_info.phone
        phone = phone[:6]
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone)
        self.element_is_visible(Locator.INPUT_CAPTCHA).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR_UNDER_INPUT).text
        return error

    # EXP-126 Логика типа ввода контактных данных телефона, когда в поле ввода 'Мобильный телефон' латинские буквы
    def input_eng_phone(self):
        # Генерируем латинские символы
        phone = generator_lowers_eng()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone)
        self.element_is_visible(Locator.INPUT_CAPTCHA).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-127 Логика типа ввода контактных данных телефона, когда в поле ввода 'Мобильный телефон' спец. символы
    def input_special_symbol_phone(self):
        # Генерируем спец. символы
        phone = generator_special_symbol()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone)
        self.element_is_visible(Locator.INPUT_CAPTCHA).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-128 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' номер телефона
    def input_number_phone_field_email(self):
        # Генерируем номер телефона
        person_info = next(generator_parsen())
        email = person_info.phone
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email)
        self.element_is_visible(Locator.INPUT_CAPTCHA).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-129 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' числа
    def input_number_field_email(self):
        # Генератор чисел
        email = generator_number()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email)
        self.element_is_visible(Locator.INPUT_CAPTCHA).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-130 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' латинские буквы
    def input_eng_email(self):
        # Генератор латинских букв
        email = generator_lowers_eng()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email)
        self.element_is_visible(Locator.INPUT_CAPTCHA).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-131 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' спец. символы
    def input_special_symbol_email(self):
        # Генератор спец. символов
        email = generator_special_symbol()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email)
        self.element_is_visible(Locator.INPUT_CAPTCHA).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-132 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' 12 цифр
    def input_12_number_email(self):
        # Генератор 12 цифр
        email = generator_phone_number_7('12')
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email)
        self.element_is_visible(Locator.INPUT_CAPTCHA).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-133 Логика типа ввода контактных данных логин, когда в поле ввода 'Логин' номер телефона
    def input_number_phone_field_login(self):
        # Генерируем номер телефона
        person_info = next(generator_parsen())
        login = person_info.phone
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login)
        self.element_is_visible(Locator.INPUT_CAPTCHA).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-134 Логика типа ввода контактных данных логин, когда в поле ввода 'Логин' 12 цифр
    def input_12_number_login(self):
        # Генерируем 12 цифр
        login = generator_phone_number_7('41')
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login)
        self.element_is_visible(Locator.INPUT_CAPTCHA).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-135 Логика типа ввода контактных данных логин, когда в поле ввода 'Логин' латинские буквы
    def input_eng_login(self):
        # Генератор латинских букв
        login = generator_lowers_eng()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login)
        self.element_is_visible(Locator.INPUT_CAPTCHA).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-136 Логика типа ввода контактных данных логин, когда в поле ввода 'Логин' спец. символы
    def input_special_symbol_login(self):
        # Генератор спец. символов
        login = generator_special_symbol()
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login)
        self.element_is_visible(Locator.INPUT_CAPTCHA).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-137 Логика типа ввода контактных данных лицевой счёт, когда в поле ввода 'Лицевой счёт' номер телефона
    def input_number_phone_field_person_account(self):
        # Генерируем номер телефона
        person_account = generator_phone_number_7('89')
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(person_account)
        self.element_is_visible(Locator.INPUT_CAPTCHA).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-138 Логика типа ввода контактных данных лицевой счёт, когда в поле ввода 'Лицевой счёт' не полный лицевой счет
    def input_incomplete_person_account(self):
        # Генерируем не полный лицевой счет
        person_account = generator_phone_number_7('@')
        self.element_is_visible(Locator.BUTTON_FORGOT_PASSWORD).click()
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(person_account)
        self.element_is_visible(Locator.INPUT_CAPTCHA).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data