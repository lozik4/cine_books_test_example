import pytest
from modules.Driver import Driver
from src.pages.base_page import BasePage
from src.pages.player.player_component import PlayerComponent

# fixtures, plugins, list
pytest_plugins = ()


def pytest_addoption(parser):
    """ Pytest options for run tests (command line) """
    parser.addoption("--env", action="store", default="PROD")
    parser.addoption("--lang", "--locale", action="store", dest="locale_code", default="en")
    parser.addoption("--headless", action="store", default="False")
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--browser_version", action="store", default=None)
    parser.addoption("--hub", action="store", default="False")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """ This fixture make actions when test failed """

    # need register new fixture
    fixture_list = [
        'desktop'
        'desktop_with_play_video'
    ]

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    if rep.when == 'call' and rep.outcome == 'failed':
        driver = None

        item_keys = item.funcargs.keys()
        try:
            fixture_name = list(set(fixture_list) & set(item_keys))[0]
        except IndexError:
            fixture_name = None

        if fixture_name in item_keys:
            driver = item.funcargs[fixture_name].driver

        if driver:
            browser = BasePage(driver)
            browser.switch_to_window_main()  # we return to the main window, because the others are already closed
            browser.log_console_errors()
            browser.log_location()
            browser.take_full_screenshot()


@pytest.fixture(scope='function')
def desktop(request):
    # 1 - prepare webdriver instance
    headless = eval(request.config.getoption("--headless"))
    browser_name = request.config.getoption("--browser_name")
    browser_version = request.config.getoption("--browser_version")
    hub = eval(request.config.getoption("--hub"))
    app_lang = request.config.getoption("--lang")
    driver = Driver().get_driver(
        browser_name=browser_name, headless=headless, version=browser_version, hub=hub, lang=app_lang
    )
    # 2 - setup browser
    browser = BasePage(driver)
    browser.goto('')
    browser.click_element("//button[@id='gdpr-cookie-accept']")
    # 3 - make browser available
    yield browser
    # 4 - teardown browser
    browser.quit()


@pytest.fixture(scope='function')
def desktop_with_playing_video(desktop):
    PlayerComponent(desktop.driver).press_big_btn_play_video()
    desktop.wait_for_time(2)
    return desktop
