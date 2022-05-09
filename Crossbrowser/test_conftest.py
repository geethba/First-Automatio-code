import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver .firefox .service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def tc_setup(browser,driver):
    if browser=="chrome":
        s=Service(ChromeDriverManager().install())
        driver=webdriver .Chrome (service= s)
    elif browser=="firefox":
        s=Service (GeckoDriverManager().install())
        driver=webdriver .Firefox (service= s)
    else:
        print("provide valid browser")
    driver.get("https://www.yatra.com/")
    time.sleep(10)
    yield
    driver.close()
def pytest_addoption(parser):
    parser.addoption("--browser--")
@pytest.fixture(scope="class",autouse=True)
def browser(request):
    return request.config.getoption("--browser")