from .base_page import BasePage
from .settings.locators import FrontendLoginLocators as Locator
from .settings.config import FrontendConfig as Config

class FrontendLogin(BasePage):

    def open(self, error):        
        try:
            super().open_url(Config.URL_LOGIN)
        except:
            assert 1 != 1, f"{error} {Config.URL_LOGIN}"

    def should_be_find_login_and_password(self, error1, error2, wait = 10):
        result = self.is_element_present_with_wait(*Locator.INPUT_LOGIN, wait)
        assert result, error1
        result = self.is_element_present_with_wait(*Locator.INPUT_PASSWORD, wait)
        assert result, error2
    
    def set_login_and_password(self, login, password):
        self.browser.find_element(*Locator.INPUT_LOGIN).send_keys(login)
        self.browser.find_element(*Locator.INPUT_PASSWORD).send_keys(password)

    def should_be_find_button_enter(self, error, wait = 10):
        result = self.is_element_present_with_wait(*Locator.BUTTON_ENTER, wait)
        assert result, error

    def click_button_enter(self, error, wait = 10):
        result = self.is_element_clickable_with_wait(*Locator.BUTTON_ENTER, wait)
        if result:
            self.browser.find_element(*Locator.BUTTON_ENTER).click()
        assert result, error
            
    def check_authorized(self, error, wait = 10):
        assert self.is_not_element_present(*Locator.MESSAGE_ERROR, wait), error
