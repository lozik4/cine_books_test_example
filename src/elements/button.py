from allure import step
from src.pages.base_page import BasePage


class ButtonElement:
    def __init__(self, driver):
        self.page = BasePage(driver)

    @step('Press button')
    def press_btn(self, btn_class: str, end_path: str = '', root_loc: str = ''):
        loc = f"{root_loc}//button[contains(@class, '{btn_class}')]{end_path}|{root_loc}//div[contains(@class, '{btn_class}')]{end_path}"
        self.page.click_element(loc)
