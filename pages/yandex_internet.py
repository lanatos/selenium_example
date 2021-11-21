from .base_page import BasePage
from .settings.locators import YandexInternetLocators as Locator
from .settings.config import YandexConfig as Config

class YandexInternet(BasePage):
    
    def open(self, error):
        try:
            super().open_url(Config.URL_INTERNET)
        except:
            assert 1 != 1, f"{error} {Config.URL_INTERNET}"

    def should_be_find_button_measure(self, error):
        result = self.is_element_present(*Locator.BUTTON_MEASURE)
        assert result, error
    
    def click_button_measure(self):
        self.browser.find_element(*Locator.BUTTON_MEASURE).click()
            
    def should_be_find_button_measure_again(self, error, wait = 120):
        assert self.is_element_present_with_wait(*Locator.BUTTON_MEASURE_AGAIN, wait), error

    def get_incoming_value(self, error):
        self.incoming_value = 0
        txts_mb = self.browser.find_element(*Locator.INCOMING).text.split(" Мбит/с")
        if len(txts_mb) > 1:
            txts_kb = txts_mb[0].split("Кбит/с")
            if len(txts_kb) > 1:
                self.incoming_value = float(txts_kb[0]) / 1024        # Кбит/с в Мбит/с
            else:
                self.incoming_value = float(txts_mb[0])               # в Мбит/с
        assert self.incoming_value > 0, error

    def check_incoming_value(self, val, error):
        assert self.incoming_value >= val, f"error ({self.incoming_value})"