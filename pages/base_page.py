from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, TimeoutException 

class BasePage():

    def __init__(self, browser, url=None, timeout=10):
        self.browser = browser
        self.url = url or ''
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def open_url(self, url):
        self.browser.get(url)

    def is_title_contains_with_wait(self, substring, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until( EC.title_contains(substring) )
        except TimeoutException:
            return False
        return True
    
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_present_with_wait(self, how, what, timeout=4):
        return not self.is_not_element_present(how, what, timeout)

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_element_clickable_with_wait(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until( EC.element_to_be_clickable((how, what)) )
        except TimeoutException:
            return False
        return True
