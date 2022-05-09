import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
s=Service ("C:/BrowserWindows/chromedriver.exe")


@pytest.fixture (scope='module')
def init_driver():
    global driver
    print("-------------setup-------")
    driver=webdriver .Chrome (service=s)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")
    yield
    print("------Teardown----")
    driver.quit()
def test_google_title(init_driver):
    assert driver.title == "Google"
def test_google_url(init_driver):
    assert driver.current_url == 'https://www.google.com/?gws_rd=ssl'