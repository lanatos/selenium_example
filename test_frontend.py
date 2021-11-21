import pytest
import allure
from pages.frontend_login import FrontendLogin 
from pages.settings.config import FrontendConfig as Config

@pytest.mark.regress
class TestFrontend():

    @allure.feature("Авторизация")
    @allure.story("Проверка авторизации")
    @allure.title("Проверка авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('login, password', [ (Config.USER_LOGIN, Config.USER_PASSWORD) ])
    def test_frontend_login_fail(self, browser, login, password):
        DL = FrontendLogin(browser, 5)
        with allure.step("1. Открыть страницу https://demo.rtmis.ru/"):
            DL.open("Ошибка открытия ссылки")
        with allure.step("2. Найти поля ввода «Логин» и «Пароль»"):
            DL.should_be_find_login_and_password("Поле «Логин» не найдено", 
                                                "Поле «Пароль» не найдено")
        with allure.step("3. Ввести логин и пароль"):
            DL.set_login_and_password(login, password)
        with allure.step("4. Найти кнопку «Войти»"):
            DL.should_be_find_button_enter("Кнопка «Войти» не найдена")
        with allure.step("5. Нажать кнопку «Войти»"):
            DL.click_button_enter("Кнопка «Войти» не кликабельна")
        with allure.step(f"6. Проверить авторизацию"):
            DL.check_authorized("Найдено сообщение об ошибке авторизации", 30)


