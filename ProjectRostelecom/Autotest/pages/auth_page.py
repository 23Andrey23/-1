from pages.base import BasePage
from locators.locator_auth import LocatorAuthPage as Locator
from generator.generator import *





class AuthButtonType(BasePage):

    # EXP-138 Функция выбора типа ввода на странице 'Авторизации', автоматически выбрана 'Номер'
    def auto_auth_selection(self):
        self.element_is_visible(Locator.INPUT_USERNAME).click()
        # Название кнопки выбора формы восстановления пароля
        phone = self.element_is_visible(Locator.PHONE).text
        # Название поле для ввода 'Мобильный телефон'
        name_field = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        # Ссылка страницы на которой находимся(без домена)
        url = self.get_relative_link()
        return phone, name_field, url

    # EXP-139 Функционал кнопки 'Номер'
    def button_phone(self):
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.PHONE).click()
        self.element_is_visible(Locator.INPUT_USERNAME).click()
        # Название поле для ввода 'Мобильный телефон'
        name_field = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return name_field

    # EXP-140 Функционирование кнопки "Почта"
    def button_email(self):
        email = self.element_is_visible(Locator.EMAIL)
        email.click()
        # Название кнопки выбора формы восстановления пароля
        email_text = email.text
        # Название поле для ввода 'Электронная почта'
        name_field = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return email_text, name_field

    # EXP-141 Функционирование кнопки "Логин"
    def button_login(self):
        login = self.element_is_visible(Locator.LOGIN)
        login.click()
        # Название кнопки выбора формы восстановления пароля
        login_text = login.text
        # Название поле для ввода 'Логин'
        name_field = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return login_text, name_field

    # EXP-142 Функционирование кнопки "Лицевой счёт"
    def button_personal_account(self):
        personal_account = self.element_is_visible(Locator.PERSONAL_ACCOUNT)
        personal_account.click()
        # Название кнопки выбора формы восстановления пароля
        personal_account_text = personal_account.text
        # Название поле для ввода 'Лицевой счёт'
        name_field = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return personal_account_text, name_field


class AuthInputPhone(BasePage):

    # EXP-143 Валидность принятых данных, в поле для ввода 'Номер', введены данные в формате +7ХХХХХХХХХХ
    def input_phone_number_seven(self):
        # Генератор телефона
        phone_input = generator_phone_number_7("+7")
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input)
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        return phone_input, phone_text

    # EXP-144 Валидность принятых данных, в поле для ввода 'Номер', введены данные в формате +375XXXXXXXXX
    def input_phone_number_three(self):
        # Генератор телефона
        phone_input = generator_phone_number_7('+375')
        phone_input = phone_input[:13]
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input)
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        return phone_input, phone_text

    # EXP-145 Валидность принятых данных, в поле для ввода 'Номер', введены данные в формате 7ХХХХХХХХХХ
    def input_phone_number_seven_not_plus(self):
        # Генератор телефона
        phone_input = generator_phone_number_7('7')
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input)
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        return phone_text

    # EXP-146 Валидность принятых данных, в поле для ввода 'Номер', введены данные в формате 8ХХХХХХХХХХ
    def input_phone_number_eight_not_plus(self):
        # Генератор телефона
        phone_input = generator_phone_number_7('8')
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input)
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        return phone_text

    # EXP-147 Валидность принятых данных, в поле для ввода 'Номер', введены данные в формате 375XXXXXXXXX
    def input_phone_number_three_not_plus(self):
        # Генератор телефона
        phone_input = generator_phone_number_7('375')
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input)
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        return phone_text

    # EXP-148 Валидность принятых данных, в поле для ввода 'Номер', введены данные в формате +375XXXXXXXXX
    def input_phone_number_three_more_values(self):
        num = generator_number()
        # Генератор телефона
        phone_input = generator_phone_number_7('+375')
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input + str(num))
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        return phone_text

    # EXP-149 Валидность принятых данных, в поле для ввода 'Номер', введены данные в формате +7ХХХХХХХХХХ
    def input_phone_number_seven_more_values(self):
        num = generator_number()
        # Генератор телефона
        phone_input = generator_phone_number_7('+7')
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input + str(num))
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        return phone_text

    # EXP-150 Валидность принятых данных, в поле для ввода 'Номер', когда первая цифра не валидна
    def input_phone_first_digit_not_valid(self):
        # Генератор телефона
        phone_input = generator_phone_number_7('1')
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input)
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        return phone_text

    # EXP-151 Валидность принятых данных, в поле для ввода 'Номер', когда в середине строки поставлен пробел
    def input_phone_space_middle(self):
        # Генератор телефона
        phone_input = generator_phone_number_7('+7')
        # Добавляем пробел в середину текста
        phone_input = phone_input[:7] + " " + phone_input[7:]
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input)
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace('-', '')
        return phone_text

    # EXP-152 Валидность принятых данных, в поле для ввода 'Номер', когда в конце строки поставлен пробел
    def input_phone_space_end(self):
        # Генератор телефона
        phone_input = generator_phone_number_7('+7')
        # Добавляем пробел в конец текста
        phone_input = phone_input[:12] + " "
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input)
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace('-', '')
        return phone_text

    # EXP-153 Ввод кириллицы в поле для ввода 'Мобильный телефон
    def input_phone_rus_eng(self):
        # Генератор кириллицы и латиницы
        phone_input = generator_lower_rus(5)
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone_input)
        # Текст в поле 'Мобильный телефон'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        phone_text = self.get_attribute(text)
        return phone_text


class AuthInputEmail(BasePage):

    # EXP-154 Ввод латиницы в поле для ввода 'Электронная почта'
    def valid_input_email_eng(self):
        # Генератор латиницы
        email_input = generator_lowers_eng()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email_input)
        # Текст в поле 'Электронная почта'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        email_text = self.get_attribute(text)
        return email_input, email_text

    # EXP-155 Ввод спец. символов в поле для ввода 'Электронная почта'
    def valid_input_email_special_symbol(self):
        # Генератор латиницы
        email_input = generator_special_symbol()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email_input)
        # Текст в поле 'Электронная почта'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        email_text = self.get_attribute(text)
        return email_input, email_text

    # EXP-156 Ввод числа в поле для ввода 'Электронная почта'
    def valid_input_email_num(self):
        # Генератор латиницы
        email_input = generator_number()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email_input)
        # Текст в поле 'Электронная почта'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        email_text = self.get_attribute(text)
        return email_input, email_text

    # EXP-157 Ввод прописных букв в поле для ввода 'Электронная почта'
    def valid_input_email_eng_upper(self):
        # Генератор латиницы
        email_input = generator_eng_upper()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email_input)
        # Текст в поле 'Электронная почта'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        email_text = self.get_attribute(text)
        return email_input, email_text

    # EXP-158 Ввод 255 символов в поле для ввода 'Электронная почта'
    def valid_input_email_255_symbol(self):
        # Генератор латиницы
        email_input = generator_eng_lowers_col(255)
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email_input)
        # Текст в поле 'Электронная почта'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        email_text = self.get_attribute(text)
        return email_input, email_text

    # EXP-159 Ввод 500 символов в поле для ввода 'Электронная почта'
    def valid_input_email_500_symbol(self):
        # Генератор латиницы
        email_input = generator_eng_lowers_col(500)
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email_input)
        # Текст в поле 'Электронная почта'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        email_text = self.get_attribute(text)
        return email_input, email_text

    # EXP-160 Ввод кирилльских и китайских символов в поле ввода 'Электронная почта'
    def valid_input_email_rus_chaine(self):
        # Генератор латиницы
        email_input = generator_lowers_rus_chaine()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email_input)
        # Текст в поле 'Электронная почта'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        email_text = self.get_attribute(text)
        return email_text

    # EXP-161 Ввод валидных данных в поле ввода 'Электронная почта' с пробелом в середине текста
    def valid_input_email_space_middle(self):
        # Генератор латиницы
        email_input = generator_lowers_eng()
        # Добавляем пробел в середину текста
        email_input = email_input[:5] + " " + email_input[5:]
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email_input)
        # Убираем пробел для проверки
        email_input = email_input.replace(' ', '')
        # Текст в поле 'Электронная почта'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        email_text = self.get_attribute(text)
        return email_input, email_text


class AuthInputLogin(BasePage):

    # EXP-162 Ввод латиницы в поле для ввода 'Логин'
    def valid_input_login_eng(self):
        # Генератор латиницы
        login_input = generator_lowers_eng()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login_input)
        # Текст в поле 'Логин'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        login_text = self.get_attribute(text)
        return login_input, login_text

    # EXP-163 Ввод спец. символов в поле для ввода 'Логин'
    def valid_input_login_special_symbol(self):
        # Генератор латиницы
        login_input = generator_special_symbol()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login_input)
        # Текст в поле 'Логин'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        login_text = self.get_attribute(text)
        return login_input, login_text

    # EXP-164 Ввод числа в поле для ввода 'Логин'
    def valid_input_login_num(self):
        # Генератор латиницы
        login_input = generator_number()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login_input)
        # Текст в поле 'Логин'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        login_text = self.get_attribute(text)
        return login_input, login_text

    # EXP-165 Ввод прописных букв в поле для ввода 'Логин'
    def valid_input_login_eng_upper(self):
        # Генератор латиницы
        login_input = generator_eng_upper()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login_input)
        # Текст в поле 'Логин'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        login_text = self.get_attribute(text)
        return login_input, login_text

    # EXP-166 Ввод 255 символов в поле для ввода 'Логин'
    def input_login_255_symbol(self):
        # Генератор латиницы
        login_input = generator_eng_lowers_col(255)
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login_input)
        # Текст в поле 'Логин'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        login_text = self.get_attribute(text)
        return login_input, login_text

    # EXP-167 Ввод 500 символов в поле для ввода 'Логин'
    def input_login_500_symbol(self):
        # Генератор латиницы
        login_input = generator_eng_lowers_col(500)
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login_input)
        # Текст в поле 'Логин'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        login_text = self.get_attribute(text)
        return login_input, login_text

    # EXP-168 Ввод кирилльских и китайских символов в поле ввода 'Логин'
    def input_login_rus_chaine(self):
        # Генератор латиницы
        login_input = generator_lowers_rus_chaine()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login_input)
        # Текст в поле 'Логин'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        login_text = self.get_attribute(text)
        return login_text

    # EXP-169 Ввод валидных данных в поле ввода 'Логин' с пробелом в середине текста
    def input_login_space_middle(self):
        # Генератор латиницы
        login_input = generator_lowers_eng()
        # Добавляем пробел в середину текста
        login_input = login_input[:5] + " " + login_input[5:]
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login_input)
        # Убираем пробел для проверки
        login_input = login_input.replace(' ', '')
        # Текст в поле 'Логин'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        login_text = self.get_attribute(text)
        return login_input, login_text


class AuthInputPersonalAccount(BasePage):

    # EXP-170 Валидный ввод 12 чисел в поле ввода 'Лицевой счет'
    def valid_input_personal_account_12_num(self):
        # Генератор лицевого счета
        personal_account_input = generator_phone_number_7('14')
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(personal_account_input)
        # Текст в поле 'Лицевой счет'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        personal_account_text = self.get_attribute(text)
        return personal_account_text

    # EXP-171 Ввод данных в поле ввода 'Лицевой счет' с пробелом в середине
    def input_personal_account_space_middle(self):
        # Генератор лицевого счета
        personal_account_input = generator_phone_number_7('54')
        # Добавляем пробел в середину текста
        personal_account_input = personal_account_input[:6] + " " + personal_account_input[6:]
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(personal_account_input)
        # Текст в поле 'Лицевой счет'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        personal_account_text = self.get_attribute(text)
        # Убираем пробел для проверки
        personal_account_input = personal_account_input.replace(' ', '')
        return personal_account_input, personal_account_text

    # EXP-172 Ввод данных в поле ввода 'Лицевой счет' с пробелом в конце
    def input_personal_account_space_end(self):
        # Генератор лицевого счета
        personal_account_input = generator_phone_number_7('54')
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(personal_account_input + ' ')
        # Текст в поле 'Лицевой счет'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        personal_account_text = self.get_attribute(text)
        # Убираем пробел для проверки
        personal_account_input = personal_account_input.replace(' ', '')
        return personal_account_input, personal_account_text

    # EXP-173 Ввод кирилльских и латинских символов в поле ввода 'Лицевой счет'
    def input_personal_account_rus_eng(self):
        # Генератор кирилльских и латинских символов
        personal_account_input = generator_lowers_rus_eng()
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(personal_account_input)
        # Текст в поле 'Лицевой счет'
        text = self.element_is_visible(Locator.INPUT_USERNAME)
        personal_account_text = self.get_attribute(text)
        return personal_account_text


class AuthPassword(BasePage):

    # EXP-174 Ввод латиницы в поле «Пароль»
    def valid_password_eng(self):
        # Генератор латиницы
        pass_input = generator_lowers_eng()
        self.element_is_visible(Locator.INPUT_PASSWORD).send_keys(pass_input)
        # Текст в поле 'Пароль'
        text = self.element_is_visible(Locator.INPUT_PASSWORD)
        pass_text = self.get_attribute(text)
        return pass_text, pass_input

    # EXP-175 Ввод заглавных букв в поле «Пароль»
    def valid_password_upper_symbol(self):
        # Генератор заглавных букв
        pass_input = generator_eng_upper()
        self.element_is_visible(Locator.INPUT_PASSWORD).send_keys(pass_input)
        # Текст в поле 'Пароль'
        text = self.element_is_visible(Locator.INPUT_PASSWORD)
        pass_text = self.get_attribute(text)
        return pass_text, pass_input

    # EXP-176 Ввод чисел в поле «Пароль»
    def valid_password_number(self):
        # Генератор чисел
        pass_input = generator_number()
        self.element_is_visible(Locator.INPUT_PASSWORD).send_keys(pass_input)
        # Текст в поле 'Пароль'
        text = self.element_is_visible(Locator.INPUT_PASSWORD)
        pass_text = self.get_attribute(text)
        return pass_text, str(pass_input)

    # EXP-177 Ввод спец. символов в поле «Пароль»
    def valid_password_special_symbol(self):
        # Генератор спец. символов
        pass_input = generator_special_symbol()
        self.element_is_visible(Locator.INPUT_PASSWORD).send_keys(pass_input)
        # Текст в поле 'Пароль'
        text = self.element_is_visible(Locator.INPUT_PASSWORD)
        pass_text = self.get_attribute(text)
        return pass_text, pass_input

    # EXP-178 Ввод кирилльских и китайских символов в поле «Пароль»
    def not_valid_password_rus_chaine(self):
        # Генератор кирилльских и китайских символов
        pass_input = generator_lowers_rus_chaine()
        self.element_is_visible(Locator.INPUT_PASSWORD).send_keys(pass_input)
        # Текст в поле 'Пароль'
        text = self.element_is_visible(Locator.INPUT_PASSWORD)
        pass_text = self.get_attribute(text)
        return pass_text, pass_input

    # EXP-179 Ввод данных с пробелом в тексте в поле «Пароль»
    def not_valid_password_spece(self):
        # Генератор пароля
        pass_input = generator_password_number_simbol(10)
        # Добавляем пробел в середину текста
        pass_input = pass_input[:5] + " " + pass_input[5:]
        self.element_is_visible(Locator.INPUT_PASSWORD).send_keys(pass_input)
        # Текст в поле 'Пароль'
        text = self.element_is_visible(Locator.INPUT_PASSWORD)
        pass_text = self.get_attribute(text)
        # Убираем пробел для проверки
        pass_input = pass_input.replace(' ', '')
        return pass_text, pass_input

    # EXP-180 Ввод 255 символов в поле «Пароль»
    def not_valid_password_255_symbol(self):
        # Генератор пароля
        pass_input = generator_eng_lowers_col(255)
        self.element_is_visible(Locator.INPUT_PASSWORD).send_keys(pass_input)
        # Текст в поле 'Пароль'
        text = self.element_is_visible(Locator.INPUT_PASSWORD)
        pass_text = self.get_attribute(text)
        return pass_text

    # EXP-181 Ввод 255 символов в поле «Пароль»
    def not_valid_password_500_symbol(self):
        # Генератор пароля
        pass_input = generator_eng_lowers_col(500)
        self.element_is_visible(Locator.INPUT_PASSWORD).send_keys(pass_input)
        # Текст в поле 'Пароль'
        text = self.element_is_visible(Locator.INPUT_PASSWORD)
        pass_text = self.get_attribute(text)
        return pass_text


class AuthPage(BasePage):

    # EXP-182 Валидность заголовка на странице 'Авторизации'
    def main_title(self):
        # Текст в заголовка
        text = self.element_is_visible(Locator.MAIN_TITLE_AUTH).text
        return text

    # EXP-183 Валидность кнопки в поле пароль
    def button_password(self):
        # Генератор пароля
        password = generator_password_not_special_symbol()
        password_button = self.element_is_visible(Locator.BUTTON_PASSWORD)
        # Если кнопка видима и активна, а так же он видим пользователю
        if password_button.is_enabled() and password_button.is_displayed():
            test = "Прошел"
        else:
            test = "Не прошел"
        self.element_is_visible(Locator.INPUT_PASSWORD).send_keys(password)
        password_button.click()
        password_button.click()
        return test

    # EXP-184 Валидность кнопки 'Запомнить меня' на странице 'Авторизации'
    def button_forgot_password(self):
        button = self.element_is_visible(Locator.BUTTON_REMEMBER)
        # Если кнопка видима и активна, а так же он видим пользователю
        if button.is_enabled() and button.is_displayed():
            test = "Прошел"
        else:
            test = "Не прошел"
        button.click()
        button.click()
        return test

    # EXP-185 Валидность текстовой кнопки 'Запомнить меня' на странице 'Авторизации'
    def button_text_forgot_password(self):
        button = self.element_is_visible(Locator.BUTTON_TEXT_REMEMBER)
        # Если кнопка видима и активна, а так же он видим пользователю
        if button.is_enabled() and button.is_displayed():
            print("Текстовая кнопка 'Запомнить меня' доступен для нажатия")
        else:
            print("Текстовая кнопка 'Запомнить меня' недоступен для нажатия")
        button.click()
        button.click()
        text_button = button.text
        return text_button

    # EXP-186 Валидность кнопки 'Забыл пароль' на странице 'Авторизации'
    def button_recovery_password(self):
        # Кнопка 'Забыл пароль'
        button = self.element_is_visible(Locator.BUTTON_FORGOT)
        text_button = button.text
        button.click()
        # Ссылка страницы (без домена)
        url = self.get_relative_link()
        return text_button, url

    # EXP-187 Пользователь нажимает на кнопку 'Пользовательские соглашения' под кнопкой 'Войти', на странице 'Авторизации'
    def button_user_agreements(self):
        user_agreements = self.element_is_visible(Locator.USER_AGREEMENTS)
        text_user_agreements = user_agreements.text
        user_agreements.click()
        self.new_window()
        url = self.get_relative_link_http()
        return text_user_agreements, url

    # EXP-188 Валидность кнопки 'Зарегистрироваться' на странице 'Авторизации'
    def button_register(self):
        # Кнопка 'Зарегистрироваться'
        button = self.element_is_visible(Locator.REGISTER_AUTH)
        text_button = button.text
        button.click()
        # Ссылка страницы (без домена)
        url = self.get_relative_link()
        return text_button, url

    # EXP-189 Валидность текса продуктового слогана, на странице 'Авторизации'
    def product_slogan(self):
        # Слоган
        text = self.element_is_visible(Locator.TEXT_PERSONAL_OFFICE).text
        return text


class SocialNetworks(BasePage):

    # EXP-190 Функционал иконки VK
    def iconka_vk(self):
        self.element_is_visible(Locator.BUTTON_VK).click()
        # Ссылка страницы (без домена)
        url = self.get_relative_not_id()
        return url

    # EXP-191 Функционал иконки OK
    def iconka_ok(self):
        self.element_is_visible(Locator.BUTTON_OK).click()
        # Ссылка страницы (без домена)
        url = self.get_relative_not_id()
        return url

    # EXP-192 Функционал иконки Mail
    def iconka_mail(self):
        self.element_is_visible(Locator.BUTTON_MAIL).click()
        # Ссылка страницы (без домена)
        url = self.get_relative_not_id()
        return url

    # EXP-193 Функционал иконки Yandex
    def iconka_ya(self):
        self.element_is_visible(Locator.BUTTON_YANDEX).click()
        # Ссылка страницы (без домена)
        url = self.get_relative_not_id()
        return url


class AuthFooter(BasePage):

    # EXP-194 Пользователь нажимает на кнопку 'Cookies' в footer
    def button_cookie_footer(self):
        self.element_is_visible(Locator.COOKIE).click()
        cookie_text = self.element_is_visible(Locator.COOKIE_TEXT).text
        return cookie_text

    # EXP-195 отобразившемся шаблоне 'Cookies' нажать на кнопку 'крестик'
    def button_cookie_close_footer(self):
        self.element_is_visible(Locator.COOKIE).click()
        cookie_text_close = self.element_is_visible(Locator.COOKIE_TEXT_CLOSE)
        # Если кнопка видима и активна, а так же он видим пользователю
        if cookie_text_close.is_enabled() and cookie_text_close.is_displayed():
            test = "Прошел"
        else:
            test = "Не прошел"
        return test

    # EXP-196 Пользователь нажимает на кнопку 'Политикой конфиденциальности' в footer
    def button_privacy_policy_footer(self):
        privacy_policy = self.element_is_visible(Locator.PRIVACY_POLICY).text
        self.element_is_visible(Locator.PRIVACY_POLICY).click()
        self.new_window()
        url = self.get_relative_link_http()
        return privacy_policy, url

    # EXP-197 Пользователь нажимает на кнопку 'Пользовательские соглашения' в footer
    def button_user_agreements_footer(self):
        text_user_agreements = self.element_is_visible(Locator.USER_AGREEMENTS_FOOTER).text
        self.element_is_visible(Locator.USER_AGREEMENTS_FOOTER).click()
        self.new_window()
        url = self.get_relative_link_http()
        return text_user_agreements, url


class AuthLogicTypeInput(BasePage):

    # EXP-198 Логика типа ввода контактных данных телефона, когда в поле ввода 'Мобильный телефон' не полный номер
    def incomplete_number_phone(self):
        # Генерируем телефон
        person_info = next(generator_parsen())
        phone = person_info.phone
        phone = phone[:6]
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone)
        self.element_is_visible(Locator.INPUT_PASSWORD).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR_TYPE_INPUT).text
        return error

    # EXP-199 Логика типа ввода контактных данных телефона, когда в поле ввода 'Мобильный телефон' латинские буквы
    def input_eng_phone(self):
        # Генерируем латинские символы
        phone = generator_lowers_eng()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone)
        self.element_is_visible(Locator.INPUT_PASSWORD).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-200 Логика типа ввода контактных данных телефона, когда в поле ввода 'Мобильный телефон' спец. символы
    def input_special_symbol_phone(self):
        # Генерируем спец. символы
        phone = generator_special_symbol()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(phone)
        self.element_is_visible(Locator.INPUT_PASSWORD).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-201 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' номер телефона
    def input_number_phone_field_email(self):
        # Генерируем номер телефона
        person_info = next(generator_parsen())
        email = person_info.phone
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email)
        self.element_is_visible(Locator.INPUT_PASSWORD).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-202 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' числа
    def input_number_field_email(self):
        # Генератор чисел
        email = generator_number()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email)
        self.element_is_visible(Locator.INPUT_PASSWORD).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-203 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' латинские буквы
    def input_eng_email(self):
        # Генератор латинских букв
        email = generator_lowers_eng()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email)
        self.element_is_visible(Locator.INPUT_PASSWORD).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-204 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' спец. символы
    def input_special_symbol_email(self):
        # Генератор спец. символов
        email = generator_special_symbol()
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email)
        self.element_is_visible(Locator.INPUT_PASSWORD).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-205 Логика типа ввода контактных данных почта, когда в поле ввода 'Электронная почта' 12 цифр
    def input_12_number_email(self):
        # Генератор 12 цифр
        email = generator_phone_number_7('12')
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(email)
        self.element_is_visible(Locator.INPUT_PASSWORD).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-206 Логика типа ввода контактных данных логин, когда в поле ввода 'Логин' номер телефона
    def input_number_phone_field_login(self):
        # Генерируем номер телефона
        person_info = next(generator_parsen())
        login = person_info.phone
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login)
        self.element_is_visible(Locator.INPUT_PASSWORD).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-207 Логика типа ввода контактных данных логин, когда в поле ввода 'Логин' 12 цифр
    def input_12_number_login(self):
        # Генерируем 12 цифр
        login = generator_phone_number_7('41')
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login)
        self.element_is_visible(Locator.INPUT_PASSWORD).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-208 Логика типа ввода контактных данных логин, когда в поле ввода 'Логин' латинские буквы
    def input_eng_login(self):
        # Генератор латинских букв
        login = generator_lowers_eng()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login)
        self.element_is_visible(Locator.INPUT_PASSWORD).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-209 Логика типа ввода контактных данных логин, когда в поле ввода 'Логин' спец. символы
    def input_special_symbol_login(self):
        # Генератор спец. символов
        login = generator_special_symbol()
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(login)
        self.element_is_visible(Locator.INPUT_PASSWORD).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-210 Логика типа ввода контактных данных лицевой счёт, когда в поле ввода 'Лицевой счёт' номер телефона
    def input_number_phone_field_person_account(self):
        # Генерируем номер телефона
        person_account = generator_phone_number_7('89')
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(person_account)
        self.element_is_visible(Locator.INPUT_PASSWORD).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data

    # EXP-211 Логика типа ввода контактных данных лицевой счёт, когда в поле ввода 'Лицевой счёт' не полный лицевой счет
    def input_incomplete_person_account(self):
        # Генерируем не полный лицевой счет
        person_account = generator_phone_number_7('@')
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(person_account)
        self.element_is_visible(Locator.INPUT_PASSWORD).click()
        # Тип ввода
        type_data = self.element_is_visible(Locator.TEXT_INPUT_USERNAME).text
        return type_data


class AuthLogicButtonEnter(BasePage):

    # EXP-212 Логика кнопки 'Войти', когда валидны данные только в поле 'Мобильный телефон'
    def valid_phone_not_valid_pass(self):
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys('+79193242824')
        self.element_is_visible(Locator.INPUT_PASSWORD).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.BUTTON_ENTER).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR_TYPE_AND_PASS).text
        # Название кнопки 'Войти'
        text_button = self.element_is_visible(Locator.BUTTON_ENTER).text
        url = self.get_relative_not_id()
        return text_button, error, url

    # EXP-213 Логика кнопки 'Войти', когда в полях введены невалидны данные
    def not_valid_phone_not_valid_pass(self):
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.INPUT_PASSWORD).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.BUTTON_ENTER).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR_TYPE_AND_PASS).text
        url = self.get_relative_not_id()
        return error, url

    # EXP-214 Логика кнопки 'Войти', когда валидны данные только в поле 'Мобильный телефон', поле 'Пароль' пустое
    def valid_phone_empty_pass(self):
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys('+79193242824')
        self.element_is_visible(Locator.BUTTON_ENTER).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR_TYPE_AND_PASS).text
        url = self.get_relative_not_id()
        return error, url

    # EXP-215 Логика кнопки 'Войти' по почте, когда введены валидны данные
    def valid_email_valid_pass(self):
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys('shebarshov2015@mail.ru')
        self.element_is_visible(Locator.INPUT_PASSWORD).send_keys('Shebarshov2015')
        self.element_is_visible(Locator.BUTTON_ENTER).click()
        url = self.get_relative_not_id()
        return url

    # EXP-216 Логика кнопки 'Войти' по почте, когда валидны данные только в поле 'Электронная почта'
    def valid_email_not_valid_pass(self):
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys('shebarshov2015@mail.ru')
        self.element_is_visible(Locator.INPUT_PASSWORD).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.BUTTON_ENTER).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR_TYPE_AND_PASS).text
        url = self.get_relative_not_id()
        return error, url

    # EXP-217 Логика кнопки 'Войти' по почте, когда в полях введены невалидны данные
    def not_valid_email_not_valid_pass(self):
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.INPUT_PASSWORD).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.BUTTON_ENTER).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR_TYPE_AND_PASS).text
        url = self.get_relative_not_id()
        return error, url

    # EXP-218 Логика кнопки 'Войти' по почте, когда данные 'Электронная почта' валидна, поле 'Пароль' пустое
    def valid_email_empty_pass(self):
        self.element_is_visible(Locator.EMAIL).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys('shebarshov2015@mail.ru')
        self.element_is_visible(Locator.BUTTON_ENTER).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR_TYPE_AND_PASS).text
        url = self.get_relative_not_id()
        return error, url

    # EXP-219 Логика кнопки 'Войти' по логину, когда валидны данные только в поле 'Логин'
    def valid_login_not_valid_pass(self):
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys('lk_46106848')
        self.element_is_visible(Locator.INPUT_PASSWORD).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.BUTTON_ENTER).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR_TYPE_AND_PASS).text
        url = self.get_relative_not_id()
        return error, url

    # EXP-220 Логика кнопки 'Войти' по логину, когда в полях введены невалидны данные
    def not_valid_login_not_valid_pass(self):
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.INPUT_PASSWORD).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.BUTTON_ENTER).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR_TYPE_AND_PASS).text
        url = self.get_relative_not_id()
        return error, url

    # EXP-221 Логика кнопки 'Войти', когда данные 'Логин' валиден, поле 'Пароль' пустое
    def valid_login_empty_pass(self):
        self.element_is_visible(Locator.LOGIN).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys('lk_46106848')
        self.element_is_visible(Locator.BUTTON_ENTER).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR_TYPE_AND_PASS).text
        url = self.get_relative_not_id()
        return error, url

    # EXP-222 Логика кнопки 'Войти' по лицевому счету, когда валидны данные только в поле 'Лицевой счет'
    def valid_person_account_not_valid_pass(self):
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys('850014328079')
        self.element_is_visible(Locator.INPUT_PASSWORD).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.BUTTON_ENTER).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR_TYPE_AND_PASS).text
        url = self.get_relative_not_id()
        return error, url

    # EXP-223 Логика кнопки 'Войти' по лицевому счету, когда поле 'ЛС' пустое; в поле 'Пароль' невалидные данные
    def empty_person_account_not_valid_pass(self):
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_PASSWORD).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.BUTTON_ENTER).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR_TYPE_INPUT).text
        url = self.get_relative_not_id()
        return error, url

    # EXP-224 Логика кнопки 'Войти' по лицевому счету, когда данные 'ЛС' валидны, поле 'Пароль' пустое
    def valid_person_account_empty_pass(self):
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys('850014328079')
        self.element_is_visible(Locator.BUTTON_ENTER).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR_TYPE_AND_PASS).text
        url = self.get_relative_not_id()
        return error, url

    # EXP-225 Логика кнопки 'Войти' по лицевому счету, когда данные 'ЛС' невалидны, поле 'Пароль' пустое
    def not_valid_person_account_empty_pass(self):
        self.element_is_visible(Locator.PERSONAL_ACCOUNT).click()
        self.element_is_visible(Locator.INPUT_USERNAME).send_keys('8500143')
        self.element_is_visible(Locator.BUTTON_ENTER).click()
        # Текст ошибки
        error = self.element_is_visible(Locator.ERROR_TYPE_INPUT).text
        url = self.get_relative_not_id()
        return error, url


class AuthCookie(BasePage):

    # EXP-226 При отключении cookie всплывает окно
    def cookie_title_text(self):
        are_cookies_disabled = self.cookie_disabled()
        if are_cookies_disabled:
            cookie = "Cookie отключены"
        else:
            cookie = "Cookie включены"
        return cookie