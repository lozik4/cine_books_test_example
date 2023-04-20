from src.elements import AllElements
from src.pages.base_page import BasePage

locPlayer: str = "//div[contains(@class, 'play-block-center')]"
locTimeAfterStart: str = "//div[@class = 'time current-duration']//time"


class IndexPage:

    def __init__(self, driver):
        self.page = BasePage(driver)
        self.el = AllElements(driver)

    def click_scroll_to_block(self):
        self.el.button.press_btn('arrow-wrapper')
