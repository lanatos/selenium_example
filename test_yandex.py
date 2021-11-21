import pytest
import allure
from pages.yandex_internet import YandexInternet 

@pytest.mark.regress
class TestYandex():

    @allure.feature("Измерение скорости интернета")
    @allure.story("Измерение скорости интернета")
    @allure.title("Измерение скорости интернета (входящее соединение)")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_yandex_internet_incoming(self, browser):
        YI = YandexInternet(browser, "https://yandex.ru/internet", 10)
        with allure.step("1. Открыть страницу https://yandex.ru/internet"):
            YI.open("Ошибка открытия ссылки")
        with allure.step("2. Найти кнопку «Измерить»"):
            YI.should_be_find_button_measure('Кнопка "Измерить" не найдена')
        with allure.step("3. Нажать кнопку «Измерить»"):
            YI.click_button_measure()
        with allure.step("4. Дождаться выполнения замеров"):
            YI.should_be_find_button_measure_again('Кнопка "Измерить снова" не найдена', 180)
        with allure.step("5. Получить значение скорости входящего соединения"):
            YI.get_incoming_value("Скорость входящего соединения не определена")
        val = 50.66
        with allure.step(f"6. Проверить значение скорости входящего соединения (>={val})"):
            YI.check_incoming_value(val, f"Скорость входящего соединения меньше {val} Мбит/с")


