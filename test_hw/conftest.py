import pytest
from selene import browser, have

@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    # browser.config.window_width = 1000
    # browser.config.window_height = 1080
    browser.config.driver_name = 'chrome'
    # browser.config.wait_for_no_overlap_found_by_js = True
    # browser.open('https://demoqa.com/')
    # browser.all('[class="card mt-4 top-card"]').element_by(
    #     have.exact_text('Alerts, Frame & Windows')).click()
    # browser.all('[class="header-text"]').element_by(have.exact_text('Forms')).click()
    # browser.all('[class="element-list accordion-collapse collapse show"]').element_by(have.exact_text('Practice Form')).click()


    yield

    browser.quit()