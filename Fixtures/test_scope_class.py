
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='class')
def init_chrome_driver(request):
    s = Service("C:/BrowserWindows/chromedriver.exe")

    ch_driver=webdriver .Chrome (service=s)
    request.cls.driver=ch_driver

    ch_driver .get("http://www.google.com")
    yield
    print("------Teardown----")
    ch_driver .quit()

@pytest.fixture(scope='class')
def init_ff_driver(request):
    s1 = Service("C:/BrowserWindows/geckodriver.exe")

    ff_driver=webdriver.Firefox (service=s1)
    request .cls.driver=ff_driver

    ff_driver .get("http://www.google.com")
    yield
    print("------Teardown----")
    ff_driver .quit()

@pytest.mark.usefixtures ("init_chrome_driver")
class base_chrome_test:
    pass
class Test_google_chrome(base_chrome_test ):

    def test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"

@pytest.mark.usefixtures ("init_ff_driver")
class base_ff_test:
    pass
class Test_google_firefox(base_ff_test ):

    def test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"

