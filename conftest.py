import allure
from allure_commons.types import AttachmentType
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--show', action='store', default='0',
                     help="Choose show = 1, if need no see browser")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    browser_show = request.config.getoption("show")
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name.lower() == "chrome":
        print("\nstart chrome browser for test..")
        options = ChromeOptions()
        if browser_show == '0':
            options.add_argument('--no-sandbox')
            options.add_argument('--headless')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument("--start-maximized")

        browser = webdriver.Chrome(options=options)
        browser.set_window_size(1280,1024)

    elif browser_name.lower() == "firefox":
        print("\nstart firefox browser for test...")
        options = FirefoxOptions()
        if browser_show == '0':
            options.headless = True
        
        browser = webdriver.Firefox(options=options)
        browser.maximize_window()
        browser.set_window_size(1280,1024)

    yield browser
    
    print("\nquit browser...")
    browser.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        try:
            if 'browser' in item.fixturenames:
                web_driver = item.funcargs['browser']
            else:
                print('Fail to take screen-shot')
                return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name = 'screenshot',
                attachment_type = AttachmentType.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))