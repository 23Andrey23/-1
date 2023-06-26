from selenium.webdriver.common.by import By

class LocatorRegisterPage:

    # Поля ввода "Личные данные"
    NAME = (By.NAME, 'firstName')
    SURNAME = (By.NAME, 'lastName')
    REGION = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div[1]/div/input')


    # Поля ввода "Данные для входа"
    EMAIL_PHONE = (By.CSS_SELECTOR, 'input[id="address"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[id="password"]')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, 'input[id="password-confirm"]')


    # Кнопка "Зарегестрироваться" на странице регестрации
    REGISTER_ACC = (By.CSS_SELECTOR, 'button[type="submit"]')
    # Кнопка "Зарегестрироваться" на странице аунтификации
    REGISTER_AUTH = (By.ID, 'kc-register')


    # Кнопка "Пользовательское соглашение"
    DOCUMENT = (By.CLASS_NAME, 'rt-link')


    # Текст под именем при неверно введенных данных
    TEXT_NAME_ERROR = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span')
    # Текст под фамилией при неверно введенных данных
    TEXT_SURNAME_ERROR = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    # Текст под почты/телефона при неверно введенных данных
    TEXT_EMAIL_PHONE_ERROR = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/span')
    # Текст под паролем при неверно введенных данных
    TEXT_PASSWORD_ERROR = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    # Текст под полем подтвердить пароль при неверно введенных данных
    TEXT_PASSWORD_CONFIRM_ERROR = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')


    # Текст подтверждения на странице подтверждения телефона/email
    TEXT_CONFIRM_EMAIL_PHONE = (By.CLASS_NAME, 'card-container__title')


    # Кнопка в поле "Регион"
    BUTTON_REGION = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/div[2]')
    # Кнопка 'Пользовательские соглашения' под кнопкой 'Зарегистрироваться'
    BUTTON_USER_AGREEMENTS = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[5]/a')
    # Кнопка в поле "Пароль"
    BUTTON_PASSWORD = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/div/div[2]')
    # Кнопка в поле "Подтвердить пароль"
    BUTTON_PASSWORD_CONFIRM = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/div/div[2]')


    # Кнопка "Cookies" в footer
    COOKIE = (By.ID, 'cookies-tip-open')
    # Текст после нажатия на кнопку "Cookies"
    COOKIE_TEXT = (By.CLASS_NAME, 'rt-tooltip__title')
    # Кнопка закрытия текста в высвечиваемом "Cookies"
    COOKIE_TEXT_CLOSE = (By.CLASS_NAME, 'rt-tooltip__close')


    # Кнопка 'Политикой конфиденциальности' в footer
    PRIVACY_POLICY = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[1]')
    # Кнопка 'Пользовательские соглашения' в footer
    USER_AGREEMENTS_FOOTER = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[2]')


    # Кнопка "Войти" в сплывающем окне, при введении существующей E-mail или мобильный телефон
    ENTER_RECOVERY = (By.NAME, 'gotoLogin')
    # Кнопка "Восстановить пароль" в сплывающем окне, при введении существующей E-mail или мобильный телефон
    RESTORE_PASSWORD = (By.ID, 'reg-err-reset-pass')