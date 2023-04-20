from allure import step
from src.pages.base_page import BasePage


class ButtonElement:
    def __init__(self, driver):
        self.page = BasePage(driver)

    @step('Press button')
    def press_btn(self, btn_class, end_path=''):
        loc = f"//button[contains(@class, '{btn_class}')]{end_path}|//div[contains(@class, '{btn_class}')]{end_path}"
        self.page.click_element(loc)
