from selenium.webdriver.common.by import By

class LocatorAuthPage:

    # Главный заголовок страницы "Авторизация"
    MAIN_TITLE_AUTH = (By.CLASS_NAME, 'card-container__title')


    # Меню способа авторизации
    PHONE = (By.ID, 't-btn-tab-phone')
    EMAIL = (By.ID, 't-btn-tab-mail')
    LOGIN = (By.ID, 't-btn-tab-login')
    PERSONAL_ACCOUNT = (By.ID, 't-btn-tab-ls')


    # Поле ввода способа авторизации
    INPUT_USERNAME = (By.ID, 'username')
    # Название поля вода
    TEXT_INPUT_USERNAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    # Поле ввода пароль способа авторизации
    INPUT_PASSWORD = (By.ID, 'password')
    # Кнопка для видимости пароля
    BUTTON_PASSWORD = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div[2]')


    # Кнопка "Запомнить меня"
    BUTTON_REMEMBER = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/span[1]')
    # Текст "Запомнить меня"
    BUTTON_TEXT_REMEMBER = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/span[2]/span[1]')


    # Кнопка "Забыл пароль"
    BUTTON_FORGOT = (By.ID, 'forgot_password')


    # Кнопка "Войти"
    BUTTON_ENTER = (By.ID, 'kc-login')


    # Пользовательские соглашения в кнопкой "Войти"
    USER_AGREEMENTS = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/a')


    # Кнопки войдите с помощью соц. сетей
    BUTTON_VK = (By.ID, 'oidc_vk')
    BUTTON_OK = (By.ID, 'oidc_ok')
    BUTTON_MAIL = (By.ID, 'oidc_mail')
    BUTTON_YANDEX = (By.ID, 'oidc_ya')


    # Кнопка зарегестрироваться
    REGISTER_AUTH = (By.ID, 'kc-register')


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


    # Текст "Личный кабинет"
    TEXT_PERSONAL_OFFICE = (By.CLASS_NAME, 'what-is__title')


    # Ошибка при неверном вводе тип данных, под полем тип ввода
    ERROR_TYPE_INPUT = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    # Ошибка при неверном вводе тип данных и пароля
    ERROR_TYPE_AND_PASS = (By.ID, 'form-error-message')