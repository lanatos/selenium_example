from selenium.webdriver.common.by import By

class YandexInternetLocators():
    BUTTON_MEASURE = (By.XPATH, "//button[contains(@class, 'measurement-management__start-button')]")
    BUTTON_MEASURE_AGAIN = (By.XPATH, "//button[contains(@class, 'measurement-management__start-again-button')]")
    INCOMING = (By.CSS_SELECTOR, ".measurement__load-box > div:nth-child(1) div.speed-progress-bar__detailed")

class FrontendLoginLocators():
    INPUT_LOGIN = (By.XPATH, '//input[@id="promed-login"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@id="promed-password"]')
    BUTTON_ENTER = (By.XPATH, '//button[@id="auth_submit"]')
    MESSAGE_ERROR = (By.XPATH, '//span[@id="login-message" and contains(text(), "Ошибка авторизации!")]')