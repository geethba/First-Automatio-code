from selenium import webdriver

from selenium.webdriver.chrome.service import Service
s=Service("C:/BrowserWindows/chromedriver.exe")
import pytest


#driver=None

def setup_module():
    global driver
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")
def teardown_module():
    driver.quit()


def test_google_title():
    assert driver.title=="Google"
def test_google_url():
    assert driver.current_url =='https://www.google.com/?gws_rd=ssl'