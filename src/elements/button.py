from allure import step
from src.pages.base_page import BasePage


class ButtonElement:
    def __init__(self, driver):
        self.page = BasePage(driver)

    @step('Press button')
    def press_btn(self, btn_class):
        loc = f"//button[contains(@class, '{btn_class}')]|//div[contains(@class, '{btn_class}')]"
        self.page.click_element(loc)
