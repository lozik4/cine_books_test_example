import logging
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

import config_file as cfg

# Turn off webdriver-manager logs
logging.getLogger('WDM').setLevel(logging.NOTSET)
os.environ['WDM_LOG'] = "false"


class Driver:
    def __init__(self):
        self.WINDOW_SIZE = (str(cfg.SCREEN_WIDTH), str(cfg.SCREEN_HEIGHT))

    def get_driver(self, browser_name, version, headless, hub, lang: str = 'en'):

        if browser_name == "chrome":
            driver = self._get_chrome_driver(version=version, headless=headless, hub=hub, lang=lang)

        else:
            raise KeyError(f'Oops! Wrong browser: "{browser_name}"')
        return driver

    def _get_chrome_driver(self, version, headless, hub, lang: str = 'en'):
        options = webdriver.ChromeOptions()
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "intl.accept_languages": lang
        }
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        if headless:
            options.add_argument('--headless')
        if hub:
            options.set_capability("browserVersion", version)
            driver = webdriver.Remote(command_executor=f'{cfg.HUB}/wd/hub', options=options)
        else:
            service = ChromeService(
                executable_path=ChromeDriverManager(version=version, path=cfg.BASE_DIR + "/drivers").install())
            driver = webdriver.Chrome(service=service, options=options)
        driver.set_window_size(*self.WINDOW_SIZE)

        return driver
