import time
from selenium.webdriver.common.keys import Keys
from generator.generator import *
from pages.base import BasePage
from locators.locator_register import LocatorRegisterPage as Locator


class RegisterPageName(BasePage):

    # EXP-001 Пользователь вводит валидные данные, где в поле «Имя» 2 символа
    def valid_register_name_2_symbol(self):
        # Генерируем: Фамилию и Почту
        person_info = next(generator_parsen())
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(generator_lower_rus(2))
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Московская обл')
        # Текст в поле имя
        text = self.element_is_visible(Locator.NAME)
        name_text = self.get_attribute(text)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст c подтверждением регестрации
        text_confirm = self.element_is_visible(Locator.TEXT_CONFIRM_EMAIL_PHONE).text
        url = self.get_relative_link()
        return name_text, text_confirm, url

    # EXP-002 Пользователь вводит валидные данные, где в поле «Имя» 30 символов
    def valid_register_name_30_symbol(self):
        # Генерируем: Фамилию и Почту
        person_info = next(generator_parsen())
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(generator_lower_rus(30))
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Республика Беларусь')
        # Текст в поле имя
        text = self.element_is_visible(Locator.NAME)
        name_text = self.get_attribute(text)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст c подтверждением регестрации
        text_confirm = self.element_is_visible(Locator.TEXT_CONFIRM_EMAIL_PHONE).text
        url = self.get_relative_link()
        return name_text, text_confirm, url

    # EXP-003 Пользователь вводит валидные данные, кроме поля «Имя», которая принимает 1 символ
    def not_valid_register_name_1_symbol(self):
        # Генерируем: Фамилию и Почту
        person_info = next(generator_parsen())
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(generator_lower_rus(1))
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        # Текст при неверном введенном поле "Имя"
        error = self.element_is_visible(Locator.TEXT_NAME_ERROR).text
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Республика Казахстан')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        # Текст в поле имя
        text = self.element_is_visible(Locator.NAME)
        name_text = self.get_attribute(text)
        return name_text, error, url

    # EXP-004 Пользователь вводит валидные данные, кроме поля «Имя», которая принимает 31 символ
    def not_valid_register_name_31_symbol(self):
        # Генерируем: Фамилию и Почту
        person_info = next(generator_parsen())
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(generator_lower_rus(31))
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        # Текст при неверном введенном поле "Имя"
        error = self.element_is_visible(Locator.TEXT_NAME_ERROR).text
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Алтай Респ')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        # Текст в поле имя
        text = self.element_is_visible(Locator.NAME)
        name_text = self.get_attribute(text)
        return name_text, error, url

    # EXP-005 Пользователь вводит валидные данные, кроме поля «Имя», которая принимает 255 символов
    def not_valid_register_name_255_symbol(self):
        # Генерируем: Фамилию и Почту
        person_info = next(generator_parsen())
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(generator_lower_rus(255))
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        # Текст при неверном введенном поле "Имя"
        error = self.element_is_visible(Locator.TEXT_NAME_ERROR).text
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Архангельская обл')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        # Текст в поле имя
        text = self.element_is_visible(Locator.NAME)
        name_text = self.get_attribute(text)
        return name_text, error, url

    # EXP-006 Пользователь вводит валидные данные, кроме поля «Имя», которая принимает 500 символов
    def not_valid_register_name_500_symbol(self):
        # Генерируем: Фамилию и Почту
        person_info = next(generator_parsen())
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(generator_lower_rus(500))
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        # Текст при неверном введенном поле "Имя"
        error = self.elements_is_present(Locator.TEXT_NAME_ERROR).text
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Архангельская обл')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        # Текст в поле имя
        text = self.element_is_visible(Locator.NAME)
        name_text = self.get_attribute(text)
        return name_text, error, url

    # EXP-007 Пользователь вводит валидные данные, кроме поля «Имя», поле остается пустым
    def not_valid_register_name_empty(self):
        # Генерируем: Фамилию и Почту
        person_info = next(generator_parsen())
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Ярославская обл')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст при неверном введенном поле "Имя"
        error = self.element_is_visible(Locator.TEXT_NAME_ERROR).text
        url = self.get_relative_link()
        # Текст в поле имя
        text = self.element_is_visible(Locator.NAME)
        name_text = self.get_attribute(text)
        return error, url, name_text

    # EXP-008 Пользователь вводит валидные данные, кроме поля «Имя», которая принимает спец. символы
    def not_valid_register_name_special_symbol(self):
        # Генерируем: Фамилию и Почту
        person_info = next(generator_parsen())
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(generator_special_symbol())
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        # Текст при неверном введенном поле "Имя"
        error = self.element_is_visible(Locator.TEXT_NAME_ERROR).text
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Байконур г')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        # Текст в поле имя
        text = self.element_is_visible(Locator.NAME)
        name_text = self.get_attribute(text)
        return name_text, error, url

    # EXP-009 Пользователь вводит валидные данные, кроме поля «Имя», которая принимает числа
    def not_valid_register_name_number(self):
        # Генерируем: Фамилию и Почту
        person_info = next(generator_parsen())
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(generator_number())
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        # Текст при неверном введенном поле "Имя"
        error = self.element_is_visible(Locator.TEXT_NAME_ERROR).text
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Калининградская обл')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        # Текст в поле имя
        text = self.element_is_visible(Locator.NAME)
        name_text = self.get_attribute(text)
        return name_text, error, url

    # EXP-010 Пользователь вводит валидные данные, кроме поля «Имя», которая принимает кирильские заглавные буквы
    def not_valid_register_name_rus_upper(self):
        # Генерируем: Фамилию и Почту
        person_info = next(generator_parsen())
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        # Генератор кирилицы с заглавными буквами
        name_rus_upper = generator_upper_rus()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name_rus_upper)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Калининградская обл')
        # Текст в поле имя
        text = self.element_is_visible(Locator.NAME)
        name_text = self.get_attribute(text)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        return name_text, name_rus_upper, url

    # EXP-011 Пользователь вводит валидные данные, кроме поля «Имя», которая принимает латинские буквы
    def not_valid_register_name_latin_characters(self):
        # Генерируем: Фамилию и Почту
        person_info = next(generator_parsen())
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Псковская обл')
        # Текст при неверном введенном поле "Имя"
        error = self.element_is_visible(Locator.TEXT_NAME_ERROR).text
        # Текст в поле имя
        text = self.element_is_visible(Locator.NAME)
        name_text = self.get_attribute(text)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        return name_text, error, url



class RegisterPageSurname(BasePage):

    # EXP-012 Пользователь вводит валидные данные, где в поле «Фамилия» 2 символа
    def valid_register_surname_2_symbol(self):
        # Генерируем: Имя и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(generator_lower_rus(2))
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Московская обл')
        # Текст в поле фамилия
        text = self.element_is_visible(Locator.SURNAME)
        surname_text = self.get_attribute(text)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст c подтверждением регестрации
        text_confirm = self.element_is_visible(Locator.TEXT_CONFIRM_EMAIL_PHONE).text
        url = self.get_relative_link()
        return surname_text, text_confirm, url

    # EXP-013 Пользователь вводит валидные данные, где в поле «Фамилия» 30 символов
    def valid_register_surname_30_symbol(self):
        # Генерируем: Имя и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(generator_lower_rus(30))
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Республика Беларусь')
        # Текст в поле фамилия
        text = self.element_is_visible(Locator.SURNAME)
        surname_text = self.get_attribute(text)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст c подтверждением регестрации
        text_confirm = self.element_is_visible(Locator.TEXT_CONFIRM_EMAIL_PHONE).text
        url = self.get_relative_link()
        return surname_text, text_confirm, url

    # EXP-014 Пользователь вводит валидные данные, кроме поля «Фамилия», которая принимает 1 символ
    def not_valid_register_surname_1_symbol(self):
        # Генерируем: Имя и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(generator_lower_rus(1))
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        # Текст при неверном введенном поле "Фамилия"
        error = self.element_is_visible(Locator.TEXT_SURNAME_ERROR).text
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Республика Казахстан')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        # Текст в поле фамилия
        text = self.element_is_visible(Locator.SURNAME)
        surname_text = self.get_attribute(text)
        return surname_text, error, url

    # EXP-015 Пользователь вводит валидные данные, кроме поля «Фамилия», которая принимает 31 символ
    def not_valid_register_surname_31_symbol(self):
        # Генерируем: Имя и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(generator_lower_rus(31))
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        # Текст при неверном введенном поле "Фамилия"
        error = self.element_is_visible(Locator.TEXT_SURNAME_ERROR).text
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Алтай Респ')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        # Текст в поле фамилия
        text = self.element_is_visible(Locator.SURNAME)
        surname_text = self.get_attribute(text)
        return surname_text, error, url

    # EXP-016 Пользователь вводит валидные данные, кроме поля «Фамилия», которая принимает 255 символов
    def not_valid_register_surname_255_symbol(self):
        # Генерируем: Имя и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(generator_lower_rus(255))
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        # Текст при неверном введенном поле "Фамилия"
        error = self.element_is_visible(Locator.TEXT_SURNAME_ERROR).text
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Архангельская обл')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        # Текст в поле фамилия
        text = self.element_is_visible(Locator.SURNAME)
        surname_text = self.get_attribute(text)
        return surname_text, error, url

    # EXP-017 Пользователь вводит валидные данные, кроме поля «Фамилия», которая принимает 500 символов
    def not_valid_register_surname_500_symbol(self):
        # Генерируем: Имя и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(generator_lower_rus(500))
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        # Текст при неверном введенном поле "Фамилия"
        error = self.elements_is_present(Locator.TEXT_SURNAME_ERROR).text
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Архангельская обл')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        # Текст в поле фамилия
        text = self.element_is_visible(Locator.SURNAME)
        surname_text = self.get_attribute(text)
        return surname_text, error, url

    # EXP-018 Пользователь вводит валидные данные, кроме поля «Фамилия», поле остается пустым
    def not_valid_register_surname_empty(self):
        # Генерируем: Имя и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Ярославская обл')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст при неверном введенном поле "Фамилия"
        error = self.element_is_visible(Locator.TEXT_SURNAME_ERROR).text
        url = self.get_relative_link()
        # Текст в поле фамилия
        text = self.element_is_visible(Locator.SURNAME)
        surname_text = self.get_attribute(text)
        return error, url, surname_text

    # EXP-019 Пользователь вводит валидные данные, кроме поля «Фамилия», которая принимает спец. символы
    def not_valid_register_surname_special_symbol(self):
        # Генерируем: Имя и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(generator_special_symbol())
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        # Текст при неверном введенном поле "Фамилия"
        error = self.element_is_visible(Locator.TEXT_SURNAME_ERROR).text
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Байконур г')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        # Текст в поле фамилия
        text = self.element_is_visible(Locator.SURNAME)
        surname_text = self.get_attribute(text)
        return surname_text, error, url

    # EXP-020 Пользователь вводит валидные данные, кроме поля «Фамилия», которая принимает числа
    def not_valid_register_surname_number(self):
        # Генерируем: Имя и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(generator_number())
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        # Текст при неверном введенном поле "Фамилия"
        error = self.element_is_visible(Locator.TEXT_SURNAME_ERROR).text
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Калининградская обл')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        # Текст в поле фамилия
        text = self.element_is_visible(Locator.SURNAME)
        surname_text = self.get_attribute(text)
        return surname_text, error, url

    # EXP-021 Пользователь вводит валидные данные, кроме поля «Фамилия», которая принимает кирильские заглавные буквы
    def not_valid_register_surname_rus_upper(self):
        # Генерируем: Имя и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        # Генератор кирилицы с заглавными буквами
        name_rus_upper = generator_upper_rus()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(name_rus_upper)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Калининградская обл')
        # Текст в поле фамилия
        text = self.element_is_visible(Locator.SURNAME)
        surname_text = self.get_attribute(text)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        return surname_text, name_rus_upper, url

    # EXP-022 Пользователь вводит валидные данные, кроме поля «Фамилия», которая принимает латинские буквы
    def not_valid_register_surname_latin_characters(self):
        # Генерируем: Имя и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(generator_lowers_eng())
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Псковская обл')
        # Текст при неверном введенном поле "Фамилия"
        error = self.element_is_visible(Locator.TEXT_SURNAME_ERROR).text
        # Текст в поле фамилия
        text = self.element_is_visible(Locator.SURNAME)
        surname_text = self.get_attribute(text)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        return surname_text, error, url

class RegisterPageEmail(BasePage):

    # EXP-023 Пользователь вводит валидные данные, кроме поля «Email», которая принимает 255 символов
    def not_valid_register_email_255_symbol(self):
        # Генерируем: Имя и Фамилию
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(generator_lower_rus(255))
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Архангельская обл')
        # Текст при неверном введенном поле "Email"
        error = self.element_is_visible(Locator.TEXT_EMAIL_PHONE_ERROR).text
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        # Текст в поле Email
        text = self.element_is_visible(Locator.EMAIL_PHONE)
        email_text = self.get_attribute(text)
        return email_text, error, url

    # EXP-024 Пользователь вводит валидные данные, кроме поля «Email», которая принимает 500 символов
    def not_valid_register_email_500_symbol(self):
        # Генерируем: Имя и Фамилию
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(generator_lower_rus(500))
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Архангельская обл')
        # Текст при неверном введенном поле "Email"
        error = self.element_is_visible(Locator.TEXT_EMAIL_PHONE_ERROR).text
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        # Текст в поле Email
        text = self.element_is_visible(Locator.EMAIL_PHONE)
        email_text = self.get_attribute(text)
        return email_text, error, url

    # EXP-025 Пользователь вводит валидные данные, кроме поля «Email», поле остается пустым
    def not_valid_register_email_empty(self):
        # Генерируем: Имя и Фамилию
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Ярославская обл')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст при неверном введенном поле "Email"
        error = self.element_is_visible(Locator.TEXT_EMAIL_PHONE_ERROR).text
        url = self.get_relative_link()
        # Текст в поле Email
        text = self.element_is_visible(Locator.EMAIL_PHONE)
        email_text = self.get_attribute(text)
        return error, url, email_text

    # EXP-026 Пользователь вводит валидные данные, кроме поля «Email», которая принимает спец. символы
    def register_email_special_symbol(self):
        # Генерируем: Имя и Фамилию
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        # Генератор спец. символов
        email_input = generator_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email_input)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Байконур г')
        # Текст при неверном введенном поле "Email"
        error = self.element_is_visible(Locator.TEXT_EMAIL_PHONE_ERROR).text
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        # Текст в поле Email
        text = self.element_is_visible(Locator.EMAIL_PHONE)
        email_text = self.get_attribute(text)
        return email_input, email_text, error, url

    # EXP-027 Пользователь вводит валидные данные, кроме поля «Email», которая принимает числа
    def not_valid_register_email_number(self):
        # Генерируем: Имя и Фамилию
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        # Генератор чисел
        email_number = generator_number()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email_number)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Калининградская обл')
        # Текст при неверном введенном поле "Email"
        error = self.element_is_visible(Locator.TEXT_EMAIL_PHONE_ERROR).text
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        # Текст в поле Email
        text = self.element_is_visible(Locator.EMAIL_PHONE)
        email_text = self.get_attribute(text)
        return email_text, email_number, error, url

    # EXP-028 Пользователь вводит валидные данные, кроме поля «Email», которая принимает кирильские и китайские символы
    def not_valid_register_email_rus_chaine_symbol(self):
        # Генерируем: Имя и Фамилию
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        # Генератор кирильских и китайских символов
        email_rus_chaine = generator_lowers_rus_chaine()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email_rus_chaine)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Калининградская обл')
        # Текст в поле Email
        text = self.element_is_visible(Locator.EMAIL_PHONE)
        email_text = self.get_attribute(text)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        return email_text, email_rus_chaine, url

    # EXP-029 Пользователь вводит валидные данные, кроме поля «Email», в которой нет символа @
    def not_valid_register_email_dog(self):
        # Генерируем: Имя, Фамилию, Email
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        email = person_info.email
        # Удаляем символ @ из Email
        email = email.replace('@', '')
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Псковская обл')
        # Текст при неверном введенном поле "Email"
        error = self.element_is_visible(Locator.TEXT_EMAIL_PHONE_ERROR).text
        # Текст в поле Email
        text = self.element_is_visible(Locator.EMAIL_PHONE)
        email_text = self.get_attribute(text)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        return email_text, email, error, url

class RegisterPageRegion(BasePage):

    # EXP-030 Пользователь вводит валидные данные, кроме поле «Ренион», поле «Ренион» пустое
    def not_valid_register_region_empty(self):
        # Генерируем: Имя, Фамилию, Email
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        # Текст в поле "Регион"
        text = self.element_is_visible(Locator.REGION)
        region_text = self.get_attribute(text)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        return region_text, url

    # EXP-031 Пользователь вводит валидные данные, кроме поля «Ренион», в котором находятся не существующие данные
    def not_valid_register_region_non_existing_data(self):
        # Генерируем: Имя, Фамилию, Email
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys(name)
        # Текст в поле Email
        text = self.element_is_visible(Locator.EMAIL_PHONE)
        email_text = self.get_attribute(text)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        return email_text, name, url

class RegisterPagePhone(BasePage):

    # EXP-032 Пользователь вводит валидные данные, кроме поле «Телефон», где введены данные в формате +7ХХХХХХХХХХ
    def valid_register_phone_number_seven(self):
        # Генерируем: Имя, Фамилию
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        # Генератор телефлна
        phone = generator_phone_number_7("+7")
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(phone)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Московская обл')
        # Текст в поле телефон
        text = self.element_is_visible(Locator.EMAIL_PHONE)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст c подтверждением регестрации
        text_confirm = self.element_is_visible(Locator.TEXT_CONFIRM_EMAIL_PHONE).text
        url = self.get_relative_link()
        return phone_text, phone, text_confirm, url

    # EXP-033 Пользователь вводит валидные данные, кроме поле «Телефон», где введены данные в формате +375XXXXXXXXX
    def valid_register_phone_number_three(self):
        # Генерируем: Имя, Фамилию
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        # Генератор телефлна
        phone = generator_phone_number_7('+375')
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(phone)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Ивановская обл')
        # Текст в поле телефон
        text = self.element_is_visible(Locator.EMAIL_PHONE)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст c подтверждением регестрации
        text_confirm = self.element_is_visible(Locator.TEXT_CONFIRM_EMAIL_PHONE).text
        url = self.get_relative_link()
        return phone_text, phone, text_confirm, url

    # EXP-034 Пользователь вводит валидные данные, кроме поле «Телефон», где введены данные в формате 7ХХХХХХХХХХ
    def not_valid_register_phone_number_seven_not_plus(self):
        # Генерируем: Имя, Фамилию
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        # Генератор телефлна
        phone = generator_phone_number_7('7')
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(phone)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Оренбургская обл')
        # Текст в поле телефон
        text = self.element_is_visible(Locator.EMAIL_PHONE)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        phone_text = phone_text.replace('+', '')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст c подтверждением регестрации
        text_confirm = self.element_is_visible(Locator.TEXT_CONFIRM_EMAIL_PHONE).text
        url = self.get_relative_link()
        return phone_text, phone, text_confirm, url

    # EXP-035 Пользователь вводит валидные данные, кроме поле «Телефон», где введены данные в формате 375XXXXXXXXX
    def not_valid_register_phone_number_three_not_plus(self):
        # Генерируем: Имя, Фамилию
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        # Генератор телефона
        phone = generator_phone_number_7("375")
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(phone)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Чукотский АО')
        # Текст в поле телефон
        text = self.element_is_visible(Locator.EMAIL_PHONE)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        phone_text = phone_text.replace('+', '')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст c подтверждением регестрации
        text_confirm = self.element_is_visible(Locator.TEXT_CONFIRM_EMAIL_PHONE).text
        url = self.get_relative_link()
        return phone_text, phone, text_confirm, url

    # EXP-036 Пользователь вводит валидные данные, кроме поля «Телефон», где первое число невалидное. Формат для
    # ввода: '+7ХХХХХХХХХХ',
    def not_valid_register_phone_number_one_int_changed(self):
        # Генерируем: Имя, Фамилию
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        # Генератор телефлна
        phone = generator_phone_number_7('+')
        phone = phone + '24'
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(phone)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Калужская обл')
        # Текст в поле телефон
        text = self.element_is_visible(Locator.EMAIL_PHONE)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст c подтверждением регестрации
        text_confirm = self.element_is_visible(Locator.TEXT_CONFIRM_EMAIL_PHONE).text
        url = self.get_relative_link()
        return phone_text, phone, text_confirm, url

    # EXP-037 Пользователь вводит валидные данные, кроме поля «Телефон», где первое число 8. Формат для ввода:
    # '+7ХХХХХХХХХХ',
    def not_valid_register_phone_number_one_int_eight(self):
        # Генерируем: Имя, Фамилию
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        # Генератор телефлна
        phone = generator_phone_number_7('8')
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(phone)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Калужская обл')
        # Текст в поле телефон
        text = self.element_is_visible(Locator.EMAIL_PHONE)
        phone_text = self.get_attribute(text)
        phone_text = phone_text.replace(' ', '')
        phone_text = phone_text.replace('-', '')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст c подтверждением регестрации
        text_confirm = self.element_is_visible(Locator.TEXT_CONFIRM_EMAIL_PHONE).text
        url = self.get_relative_link()
        return phone_text, phone, text_confirm, url

class RegisterPagePassword(BasePage):

    # EXP-038 Пользователь вводит валидные данные, где в полях «Пароль/Подтвердить пароль» нет спец. символов
    def valid_register_password_not_special_symbol(self):
        # Генерируем: Имя, Фамилию и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Московская обл')
        # Текст в поле "Пароль"
        text = self.element_is_visible(Locator.PASSWORD)
        text_pass = self.get_attribute(text)
        # Текст в поле "Подтвердить пароль"
        text_confirm_pass = self.element_is_visible(Locator.CONFIRM_PASSWORD)
        text_pass_confirm = self.get_attribute(text_confirm_pass)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст c подтверждением регестрации
        text_confirm_email = self.element_is_visible(Locator.TEXT_CONFIRM_EMAIL_PHONE).text
        url = self.get_relative_link()
        return text_pass, text_pass_confirm, text_confirm_email, url

    # EXP-039 Пользователь вводит валидные данные, где в полях «Пароль/Подтвердить пароль» нет цифр
    def valid_register_password_not_number(self):
        # Генерируем: Имя, Фамилию и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_not_number()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Башкортостан Респ')
        # Текст в поле "Пароль"
        text = self.element_is_visible(Locator.PASSWORD)
        text_pass = self.get_attribute(text)
        # Текст в поле "Подтвердить пароль"
        text_confirm_pass = self.element_is_visible(Locator.CONFIRM_PASSWORD)
        text_pass_confirm = self.get_attribute(text_confirm_pass)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст c подтверждением регестрации
        text_confirm_email = self.element_is_visible(Locator.TEXT_CONFIRM_EMAIL_PHONE).text
        url = self.get_relative_link()
        return text_pass, text_pass_confirm, text_confirm_email, url

    # EXP-040 Пользователь вводит валидные данные, где в полях «Пароль/Подтвердить пароль» более 8 символов
    def valid_register_password_more_8_symbol(self):
        # Генерируем: Имя, Фамилию и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_number_simbol(9)
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Калмыкия Респ')
        # Текст в поле "Пароль"
        text = self.element_is_visible(Locator.PASSWORD)
        text_pass = self.get_attribute(text)
        # Текст в поле "Подтвердить пароль"
        text_confirm_pass = self.element_is_visible(Locator.CONFIRM_PASSWORD)
        text_pass_confirm = self.get_attribute(text_confirm_pass)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст c подтверждением регестрации
        text_confirm_email = self.element_is_visible(Locator.TEXT_CONFIRM_EMAIL_PHONE).text
        url = self.get_relative_link()
        return text_pass, text_pass_confirm, text_confirm_email, url

    # EXP-041 Пользователь вводит валидные данные, где в полях «Пароль/Подтвердить пароль» 8 символов
    def valid_register_password_8_symbol(self):
        # Генерируем: Имя, Фамилию и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_number_simbol(8)
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Томская обл')
        # Текст в поле "Пароль"
        text = self.element_is_visible(Locator.PASSWORD)
        text_pass = self.get_attribute(text)
        # Текст в поле "Подтвердить пароль"
        text_confirm_pass = self.element_is_visible(Locator.CONFIRM_PASSWORD)
        text_pass_confirm = self.get_attribute(text_confirm_pass)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст c подтверждением регестрации
        text_confirm_email = self.element_is_visible(Locator.TEXT_CONFIRM_EMAIL_PHONE).text
        url = self.get_relative_link()
        return text_pass, text_pass_confirm, text_confirm_email, url

    # EXP-042 Пользователь вводит валидные данные, где в полях «Пароль/Подтвердить пароль» менее 8 символов
    def not_valid_register_password_less_8_symbol(self):
        # Генерируем: Имя, Фамилию и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_number_simbol(7)
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Коми Респ')
        # Текст в поле "Пароль"
        text = self.element_is_visible(Locator.PASSWORD)
        text_pass = self.get_attribute(text)
        # Текст в поле "Подтвердить пароль"
        text_confirm_pass = self.element_is_visible(Locator.CONFIRM_PASSWORD)
        text_pass_confirm = self.get_attribute(text_confirm_pass)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст при неверном введенном поле "Пароль"
        error_password = self.element_is_visible(Locator.TEXT_PASSWORD_ERROR).text
        # Текст при неверном введенном поле "Пароль"
        error_password_confirm = self.element_is_visible(Locator.TEXT_PASSWORD_CONFIRM_ERROR).text
        url = self.get_relative_link()
        return text_pass, text_pass_confirm, error_password, error_password_confirm, url

    # EXP-043 Пользователь вводит валидные данные, где в полях «Пароль/Подтвердить пароль» все буквы заглавные
    def not_valid_register_password_upper_symbol(self):
        # Генерируем: Имя, Фамилию и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_number_simbol(10)
        password = password.upper()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Ростовская обл')
        # Текст в поле "Пароль"
        text = self.element_is_visible(Locator.PASSWORD)
        text_pass = self.get_attribute(text)
        # Текст в поле "Подтвердить пароль"
        text_confirm_pass = self.element_is_visible(Locator.CONFIRM_PASSWORD)
        text_pass_confirm = self.get_attribute(text_confirm_pass)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст при неверном введенном поле "Пароль"
        error_password = self.element_is_visible(Locator.TEXT_PASSWORD_ERROR).text
        # Текст при неверном введенном поле "Подтвердить пароль"
        error_confirm_password = self.element_is_visible(Locator.TEXT_PASSWORD_CONFIRM_ERROR).text
        url = self.get_relative_link()
        return text_pass, text_pass_confirm, error_password, error_confirm_password, url

    # EXP-044 Пользователь вводит валидные данные, где в полях «Пароль/Подтвердить пароль» все буквы строчные
    def not_valid_register_password_lower_symbol(self):
        # Генерируем: Имя, Фамилию и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_number_simbol(15)
        password = password.lower()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Российская Федерация, Бурятия Респ.')
        # Текст в поле "Пароль"
        text = self.element_is_visible(Locator.PASSWORD)
        text_pass = self.get_attribute(text)
        # Текст в поле "Подтвердить пароль"
        text_confirm_pass = self.element_is_visible(Locator.CONFIRM_PASSWORD)
        text_pass_confirm = self.get_attribute(text_confirm_pass)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст при неверном введенном поле "Пароль"
        error_password = self.element_is_visible(Locator.TEXT_PASSWORD_ERROR).text
        # Текст при неверном введенном поле "Подтвердить пароль"
        error_confirm_password = self.element_is_visible(Locator.TEXT_PASSWORD_CONFIRM_ERROR).text
        url = self.get_relative_link()
        return text_pass, text_pass_confirm, error_password, error_confirm_password, url

    # EXP-045 Пользователь вводит валидные данные, где в полях «Пароль/Подтвердить пароль» все буквы кириллицы
    def not_valid_register_password_rus_symbol(self):
        # Генерируем: Имя, Фамилию и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_rus()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Северная Осетия - Алания Респ')
        # Текст в поле "Пароль"
        text = self.element_is_visible(Locator.PASSWORD)
        text_pass = self.get_attribute(text)
        # Текст в поле "Подтвердить пароль"
        text_confirm_pass = self.element_is_visible(Locator.CONFIRM_PASSWORD)
        text_pass_confirm = self.get_attribute(text_confirm_pass)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст при неверном введенном поле "Пароль"
        error_password = self.element_is_visible(Locator.TEXT_PASSWORD_ERROR).text
        # Текст при неверном введенном поле "Подтвердить пароль"
        error_confirm_password = self.element_is_visible(Locator.TEXT_PASSWORD_CONFIRM_ERROR).text
        url = self.get_relative_link()
        return text_pass, text_pass_confirm, error_password, error_confirm_password, url

    # EXP-046 Пользователь вводит валидные данные, где в полях «Пароль/Подтвердить пароль» введены разные данные
    def not_valid_register_password_different_data(self):
        # Генерируем: Имя, Фамилию и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_number_simbol(9)
        # Подтверждение пароля отличается на один символ
        password_confirm = password[1:9]
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password_confirm)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Амурская обл')
        # Текст в поле "Пароль"
        text = self.element_is_visible(Locator.PASSWORD)
        text_pass = self.get_attribute(text)
        # Текст в поле "Подтвердить пароль"
        text_confirm_pass = self.element_is_visible(Locator.CONFIRM_PASSWORD)
        text_pass_confirm = self.get_attribute(text_confirm_pass)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст при неверном введенном поле "Пароль"
        error = self.element_is_visible(Locator.TEXT_PASSWORD_CONFIRM_ERROR).text
        url = self.get_relative_link()
        return text_pass, text_pass_confirm, error, url

    # EXP-047 Пользователь вводит валидные данные, где в полях «Пароль/Подтвердить пароль» введены 255 символов
    def not_valid_register_password_255_symbol(self):
        # Генерируем: Имя, Фамилию и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_lower_rus(255)
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Татарстан Респ')
        # Текст в поле "Пароль"
        text = self.element_is_visible(Locator.PASSWORD)
        text_pass = self.get_attribute(text)
        # Текст в поле "Подтвердить пароль"
        text_confirm_pass = self.element_is_visible(Locator.CONFIRM_PASSWORD)
        text_pass_confirm = self.get_attribute(text_confirm_pass)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        return text_pass, text_pass_confirm, url

    # EXP-048 Пользователь вводит валидные данные, где в полях «Пароль/Подтвердить пароль» введены 500 символов
    def not_valid_register_password_500_symbol(self):
        # Генерируем: Имя, Фамилию и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_lower_rus(500)
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Омская обл')
        # Текст в поле "Пароль"
        text = self.element_is_visible(Locator.PASSWORD)
        text_pass = self.get_attribute(text)
        # Текст в поле "Подтвердить пароль"
        text_confirm_pass = self.element_is_visible(Locator.CONFIRM_PASSWORD)
        text_pass_confirm = self.get_attribute(text_confirm_pass)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        return text_pass, text_pass_confirm, url

    # EXP-049 Пользователь вводит валидные данные, где в полях «Пароль/Подтвердить пароль» нет данных
    def not_valid_register_password_not_data(self):
        # Генерируем: Имя, Фамилию и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        email = person_info.email
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Саха /Якутия/ Респ')
        # Текст в поле "Пароль"
        text = self.element_is_visible(Locator.PASSWORD)
        text_pass = self.get_attribute(text)
        # Текст в поле "Подтвердить пароль"
        text_confirm_pass = self.element_is_visible(Locator.CONFIRM_PASSWORD)
        text_pass_confirm = self.get_attribute(text_confirm_pass)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст под полем Пароль
        error = self.element_is_visible(Locator.TEXT_PASSWORD_ERROR).text
        # Текст под полем Подтвердить пароль
        error_confirm = self.element_is_visible(Locator.TEXT_PASSWORD_CONFIRM_ERROR).text
        url = self.get_relative_link()
        return text_pass, text_pass_confirm, error, error_confirm, url

    # EXP-050 Пользователь вводит валидные данные, где в поле «Пароль» нет данных
    def not_valid_register_password_not_data_password(self):
        # Генерируем: Имя, Фамилию и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_number_simbol(8)
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Смоленская обл')
        # Текст в поле "Пароль"
        text = self.element_is_visible(Locator.PASSWORD)
        text_pass = self.get_attribute(text)
        # Текст в поле "Подтвердить пароль"
        text_confirm_pass = self.element_is_visible(Locator.CONFIRM_PASSWORD)
        text_pass_confirm = self.get_attribute(text_confirm_pass)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст под полем Пароль
        error = self.element_is_visible(Locator.TEXT_PASSWORD_ERROR).text
        url = self.get_relative_link()
        return password, text_pass, text_pass_confirm, error, url

    # EXP-051 Пользователь вводит валидные данные, где в поле «Подтвердить пароль» нет данных
    def not_valid_register_password_not_data_password_confirm(self):
        # Генерируем: Имя, Фамилию и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        email = person_info.email
        # Генерируем пароль
        password = generator_password_number_simbol(8)
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Российская Федерация, Дагестан Респ.')
        # Текст в поле "Пароль"
        text = self.element_is_visible(Locator.PASSWORD)
        text_pass = self.get_attribute(text)
        # Текст в поле "Подтвердить пароль"
        text_confirm_pass = self.element_is_visible(Locator.CONFIRM_PASSWORD)
        text_pass_confirm = self.get_attribute(text_confirm_pass)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Текст под полем Подтвердить пароль
        error = self.element_is_visible(Locator.TEXT_PASSWORD_CONFIRM_ERROR).text
        url = self.get_relative_link()
        return password, text_pass, text_pass_confirm, error, url

    # EXP-052 Пользователь вводит валидные данные, где в полях «Пароль/Подтвердить пароль» только числа
    def not_valid_register_password_number(self):
        # Генерируем: Имя, Фамилию и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        email = person_info.email
        # Генератор чисел
        password = generator_number()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Ростовская обл')
        # Текст в поле "Пароль"
        text = self.element_is_visible(Locator.PASSWORD)
        text_pass = self.get_attribute(text)
        # Текст в поле "Подтвердить пароль"
        text_confirm_pass = self.element_is_visible(Locator.CONFIRM_PASSWORD)
        text_pass_confirm = self.get_attribute(text_confirm_pass)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        return password, text_pass, text_pass_confirm, url

    # EXP-053 Пользователь вводит валидные данные, где в полях «Пароль/Подтвердить пароль» только спец. символы
    def not_valid_register_password_special_symbol(self):
        # Генерируем: Имя, Фамилию и Почту
        person_info = next(generator_parsen())
        name = person_info.name
        surname = person_info.surname
        email = person_info.email
        # Генератор чисел
        password = generator_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(name)
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys(email)
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Челябинская обл')
        # Текст в поле "Пароль"
        text = self.element_is_visible(Locator.PASSWORD)
        text_pass = self.get_attribute(text)
        # Текст в поле "Подтвердить пароль"
        text_confirm_pass = self.element_is_visible(Locator.CONFIRM_PASSWORD)
        text_pass_confirm = self.get_attribute(text_confirm_pass)
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        url = self.get_relative_link()
        return password, text_pass, text_pass_confirm, url

class RegisterPage(BasePage):

    # EXP-054 Пользователь нажимает на кнопку в поле "Регион"
    def button_region_click(self):
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        region_button = self.element_is_visible(Locator.BUTTON_REGION)
        # Если кнопка видима и активна, а так же он видим пользователю
        if region_button.is_enabled() and region_button.is_displayed():
            print("Кнопка в поле 'Регион' доступен для нажатия")
        else:
            print("Кнопка в поле 'Регион' недоступен для нажатия")
        region_button.click()
        region_button.click()

    # EXP-055 Пользователь нажимает на кнопку 'Пользовательские соглашения' под кнопкой 'Зарегистрироваться'
    def button_user_agreements(self):
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        user_agreements = self.element_is_visible(Locator.BUTTON_USER_AGREEMENTS)
        # Если кнопка видима и активна, а так же он видим пользователю
        if user_agreements.is_enabled() and user_agreements.is_displayed():
            print("Кнопка 'Пользовательские соглашения' доступен для нажатия")
        else:
            print("Кнопка 'Пользовательские соглашения' недоступен для нажатия")
        text_user_agreements = user_agreements.text
        user_agreements.click()
        self.new_window()
        url = self.get_relative_link_http()
        return text_user_agreements, url

    # EXP-056 Пользователь нажимает на кнопку в поле 'Пароль'
    def button_password_click(self):
        # Генератор пароля
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        password_button = self.element_is_visible(Locator.BUTTON_PASSWORD)
        # Если кнопка видима и активна, а так же он видим пользователю
        if password_button.is_enabled() and password_button.is_displayed():
            print("Кнопка в поле 'Пароль' доступен для нажатия")
        else:
            print("Кнопка в поле 'Пароль' недоступен для нажатия")
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        password_button.click()
        password_button.click()

    # EXP-057 Пользователь нажимает на кнопку в поле 'Подтвердить пароль'
    def button_password_confirm_click(self):
        # Генератор пароля
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        password_confirm_button = self.element_is_visible(Locator.BUTTON_PASSWORD)
        # Если кнопка видима и активна, а так же он видим пользователю
        if password_confirm_button.is_enabled() and password_confirm_button.is_displayed():
            print("Кнопка в поле 'Подтвердить пароль' доступен для нажатия")
        else:
            print("Кнопка в поле 'Подтвердить пароль' недоступен для нажатия")
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        password_confirm_button.click()
        password_confirm_button.click()

    # EXP-058 Пользователь нажимает на кнопку 'Cookies' в footer
    def button_cookie_footer(self):
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.COOKIE).click()
        cookie_text = self.element_is_visible(Locator.COOKIE_TEXT).text
        return cookie_text

    # EXP-059 В отобразившемся шаблоне 'Cookies' нажать на кнопку 'крестик'
    def button_cookie_close_footer(self):
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.COOKIE).click()
        cookie_text_close = self.element_is_visible(Locator.COOKIE_TEXT_CLOSE)
        # Если кнопка видима и активна, а так же он видим пользователю
        if cookie_text_close.is_enabled() and cookie_text_close.is_displayed():
            print("Кнопка 'крестик' доступен для нажатия в отобразившемся шаблоне 'Cookies'")
        else:
            print("Кнопка 'крестик' недоступен для нажатия в отобразившемся шаблоне 'Cookies'")

    # EXP-060 Пользователь нажимает на кнопку 'Политикой конфиденциальности' в footer
    def button_privacy_policy_footer(self):
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        privacy_policy = self.element_is_visible(Locator.PRIVACY_POLICY).text
        self.element_is_visible(Locator.PRIVACY_POLICY).click()
        self.new_window()
        url = self.get_relative_link_http()
        return privacy_policy, url

    # EXP-061 Пользователь нажимает на кнопку 'Пользовательские соглашения' в footer
    def button_user_agreements_footer(self):
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        text_user_agreements = self.element_is_visible(Locator.USER_AGREEMENTS_FOOTER).text
        self.element_is_visible(Locator.USER_AGREEMENTS_FOOTER).click()
        self.new_window()
        url = self.get_relative_link_http()
        return text_user_agreements, url

class RegisterPageExistingAccount(BasePage):

    # EXP-062 Пользователь вводит существующие данные, где в сплывающем окне нажимает кнопку "Войти"
    def valid_register_existing_account_enter(self):
        # Генерируем: Фамилию
        person_info = next(generator_parsen())
        surname = person_info.surname
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(generator_lower_rus(2))
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys('shebarshov2015@mail.ru')
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Московская обл')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Кнопки Войти
        enter = self.element_is_visible(Locator.ENTER_RECOVERY).text
        self.element_is_visible(Locator.ENTER_RECOVERY).click()
        url = self.get_relative_link()
        return enter, url

    # EXP-063 Пользователь вводит существующие данные, где в сплывающем окне нажимает кнопку "Восстановить пароль"
    def valid_register_existing_account_restore_password(self):
        # Генерируем: Фамилию
        person_info = next(generator_parsen())
        surname = person_info.surname
        # Генерируем пароль
        password = generator_password_not_special_symbol()
        self.element_is_visible(Locator.REGISTER_AUTH).click()
        self.element_is_visible(Locator.NAME).send_keys(generator_lower_rus(2))
        self.element_is_visible(Locator.SURNAME).send_keys(surname)
        self.element_is_visible(Locator.EMAIL_PHONE).send_keys('shebarshov2015@mail.ru')
        self.element_is_visible(Locator.PASSWORD).send_keys(password)
        self.element_is_visible(Locator.CONFIRM_PASSWORD).send_keys(password)
        self.elements_is_present(Locator.REGION).send_keys("\b\b\b\b\b\b\b\b")
        self.elements_is_present(Locator.REGION).send_keys('Московская обл')
        self.element_is_visible(Locator.REGION).send_keys(Keys.ENTER)
        # Кнопки Восстановить пароль
        restore_password = self.element_is_visible(Locator.RESTORE_PASSWORD).text
        self.element_is_visible(Locator.RESTORE_PASSWORD).click()
        url = self.get_relative_link()
        return restore_password, url