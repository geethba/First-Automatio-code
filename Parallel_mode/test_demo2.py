from calendar import error

from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from webdriver_manager.chrome import ChromeDriverManaager
s=Service  ("C:/BrowserWindows/chromedriver.exe")


def test_google():
    driver = webdriver.Chrome(service=s)

    driver.implicitly_wait(10)
    driver.get("http://www.google.com")
    assert driver.title == "Google"
    driver.quit()

def test_facebook():
        driver = webdriver.Chrome(service=s)

        driver.implicitly_wait(10)
        driver.get("http://www.facebook.com")
        assert driver.title == "Facebook – log in or sign up"
        driver.quit()
def test_gmail():
    driver=webdriver .Chrome (service= s)
    driver.implicitly_wait(10)
    driver.get("http://www.gmail.com")
    assert driver.title=="Gmail"
    driver.quit()

