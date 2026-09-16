import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage

STANDARD_USER = ("standard_user", "secret_sauce")
LOCKED_OUT_USER = ("locked_out_user", "secret_sauce")
PROBLEM_USER = ("problem_user", "secret_sauce")


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,900")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    yield drv
    drv.quit()


@pytest.fixture
def logged_in_driver(driver):
    """Driver already authenticated as the standard user, left on the inventory page."""
    login_page = LoginPage(driver).open()
    login_page.login(*STANDARD_USER)
    return driver
