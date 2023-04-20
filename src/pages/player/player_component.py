from allure import step

from modules.Utils import convert_str_to_seconds
from src.elements import AllElements
from src.pages.base_page import BasePage

locPlayer: str = "//div[contains(@class, 'play-block-center')]"
locTimeAfterStart: str = "//div[@class = 'time current-duration']//time"
locCurrentPageNumber: str = "//div[@class = 'control frame-number'][1]"
locAllPagesInBook: str = "//div[@class = 'control frame-number'][2]"
locFrameCounter: str = "//div[@class='control frame-counter']"
locTextOnFrame: str = "//div[@class='cnb-text-player__text']//span"
locImageBackground: str = "//div[contains(@class,'image-frame no-background')]/img"


class PlayerComponent:

    def __init__(self, driver):
        self.page = BasePage(driver)
        self.el = AllElements(driver)

    @step('Press big btn Play Video')
    def press_big_btn_play_video(self):
        self.page.scroll_page_to_element(locPlayer)
        self.page.wait_for_time(1)  # need to finish scroll animation
        self.el.button.press_btn('play-block-center')

    @step('Get time after start')
    def get_time_after_start(self) -> float:
        """
        :return: ex. 2.0 seconds after start
        """
        self.page.move_to_element(locTimeAfterStart)
        duration = self.page.get_text(locTimeAfterStart)
        return convert_str_to_seconds(duration)

    @step('Switch to audio book')
    def switch_to_audio_book(self):
        self.page.move_to_element(locTimeAfterStart)
        self.el.button.press_btn('webviewer-icon-listen-mode')

    @step('Switch to text book')
    def switch_to_text_book(self):
        self.page.move_to_element(locTimeAfterStart)
        self.el.button.press_btn('webviewer-icon-reading-mode')

    @step('Press next page button')
    def press_next_page_btn(self):
        self.page.move_to_element(locAllPagesInBook)
        self.el.button.press_btn('webviewer-icon-next')

    @step('Press previous button')
    def press_previous_btn(self):
        self.page.move_to_element(locTimeAfterStart)
        self.el.button.press_btn('webviewer-icon-previous')

    @step('Get page number')
    def get_page_number(self) -> int:
        self.page.move_to_element(locTimeAfterStart)
        return int(self.page.get_text(locCurrentPageNumber))

    @step('Get all pages number')
    def get_all_pages_number(self) -> int:
        self.page.move_to_element(locTimeAfterStart)
        return int(self.page.get_text(locAllPagesInBook))

    @step('Get number page and all page in text pook')
    def get_current_page_num_and_all_pages(self) -> (int, int):
        self.page.wait_present_element(locFrameCounter)
        frame_info = self.page.get_text(locFrameCounter)
        return list(map(int, frame_info.replace(' ', '').split('/')))

    @step('Get text from frame in text book')
    def get_text_from_frame(self) -> str:
        self.page.wait_app_loadings()
        return self.page.get_text(locTextOnFrame)

    @step('Press block next frame')
    def pres_block_next_frame(self):
        self.page.wait_app_loadings()
        self.page.click_element("//div[@class='canvas-container__prev-frame']")

    @step('Press block previous frame')
    def press_btn_previous_frame(self):
        self.page.wait_app_loadings()
        self.page.click_element("//div[@class='canvas-container__next-frame']")

    @step('Get image src on text book frame')
    def get_image_src(self) -> str:
        self.page.wait_app_loadings()
        return self.page.get_element_attribute(locImageBackground, 'src')
