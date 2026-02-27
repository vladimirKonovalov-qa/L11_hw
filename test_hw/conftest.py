import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser

from utils import attach


@pytest.fixture(scope="function", autouse=True)
def browser_setup():

    options = Options()

    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": False
    })

    browser.config.driver_remote_url = "https://user1:1234@selenoid.autotests.cloud/wd/hub"
    browser.config.driver_options = options

    yield

    browser.quit()

# @pytest.fixture(scope='function', autouse=True)
# def setup_browser(request):
#     options = Options()
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": "145.0.7632.117",
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": False
#         }
#     }
#     options.capabilities.update(selenoid_capabilities)
#     driver = webdriver.Remote(
#         command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
#         options=options
#     )
#
#     browser.config.driver = driver
#
#     yield browser
#
#     attach.add_screenshot(browser)
#     attach.add_html(browser)
#     attach.add_logs(browser)
#
#     browser.quit()