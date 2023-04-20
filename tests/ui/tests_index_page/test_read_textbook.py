import allure
from pytest import mark

from data.text_content.text_data import Subtitles
from src.pages.player.player_component import PlayerComponent

"""
Run locally: 
    pytest tests/ui/test_index_page/test_read_textbook.py
Make report:
    allure generate -c allure-results
"""


class TestReadTextBook:
    @allure.title('Test Switch page in text book')
    @allure.severity(allure.severity_level.CRITICAL)
    @mark.smoke
    def test_switch_page_read_book(self, playing_video):
        with allure.step(f"GIVEN: user at index page"):
            player = PlayerComponent(playing_video.driver)
        with allure.step(f"WHEN: User switch to text book and read book"):
            player.switch_to_text_book()
            zero_frame_src = player.get_image_src()
            player.pres_block_next_frame()
            current_page, all_pages = player.get_current_page_num_and_all_pages()
            frame_img_src = player.get_image_src()
            frame_text = player.get_text_from_frame()
        with allure.step(f"THEN: Frame changed, image changed, text changed check"):
            assert current_page == 1, 'Frame not changed'
            assert all_pages == 78, 'All pages incorrect value'
            assert frame_img_src != zero_frame_src, 'Image not changes'
            assert frame_text == Subtitles.first_frame_text_demo, 'Incorrect text on slide'
