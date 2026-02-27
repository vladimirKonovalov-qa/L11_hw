import pytest
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from utils import attach


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

selenoid_login = os.getenv("SELENOID_LOGIN")
selenoid_pass = os.getenv("SELENOID_PASS")
selenoid_url = os.getenv("SELENOID_URL")

@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "selenoid:options": {
            "enableVNC": False,
            "enableVideo": False
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()