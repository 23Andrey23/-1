from selenium.webdriver.common.by import By

class LocatorPasswordRecovery:

    # Кнопка "Забыл пароль"
    BUTTON_FORGOT_PASSWORD = (By.ID, 'forgot_password')


    # Кнопка "Телефон" в меню выбора типа ввода контактных данных
    PHONE = (By.ID, 't-btn-tab-phone')
    # Кнопка "Почта" в меню выбора типа ввода контактных данных
    EMAIL = (By.ID, 't-btn-tab-mail')
    # Кнопка "Логин" в меню выбора типа ввода контактных данных
    LOGIN = (By.ID, 't-btn-tab-login')
    # Кнопка "Лицевой счет" в меню выбора типа ввода контактных данных
    PERSONAL_ACCOUNT = (By.ID, 't-btn-tab-ls')


    # Поле для ввода "Телефон", "Почта", "Логин", "Лицевой счет"
    INPUT_USERNAME = (By.ID, 'username')
    # Название поля вода
    TEXT_INPUT_USERNAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')


    # Поле ввода "Капчи"
    INPUT_CAPTCHA = (By.ID, 'captcha')
    # Название поле ввода
    TEXT_CAPTCHA = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div[2]/div/span[2]')
    # Обновдение изображения "Капчи"
    BUTTON_IMAGE = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div[1]/div[2]/svg')


    # Кнопка "Продолжить"
    BUTTON_CONTINUE = (By.ID, 'reset')
    # Кнопка "Вернуться назад"
    BUTTON_GO_BACK = (By.ID, 'reset-back')


    # Ошибка при неверном вводе данных, под главным заголовком
    ERROR = (By.ID, 'form-error-message')
    # Ошибка при неверном вводе данных, под полем ввода
    ERROR_UNDER_INPUT = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')


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


    # Главный заголовок страницы "Восстановить пароль"
    MAIN_TITLE = (By.CLASS_NAME, 'card-container__title')
    # Главный текст над выбором типа ввода контактных данных
    TEXT_ABOVE_TYPE = (By.CLASS_NAME, 'card-container__desc')

