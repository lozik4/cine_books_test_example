import allure
from pytest import mark
from src.pages.player.player_component import PlayerComponent

first_frame_text: str = 'True! Nervous – very, very dreadfully nervous I had been and am. But why will you say that I am mad?'


class TestReadTextBook:
    @allure.title('Test Switch page in text book')
    @allure.severity(allure.severity_level.CRITICAL)
    @mark.smoke
    def test_switch_page_read_book(self, desktop_with_playing_video):
        player = PlayerComponent(desktop_with_playing_video.driver)
        player.switch_to_text_book()
        zero_frame_src = player.get_image_src()
        player.pres_block_next_frame()
        current_page, all_pages = player.get_current_page_num_and_all_pages()
        frame_img_src = player.get_image_src()
        frame_text = player.get_text_from_frame()
        assert current_page == 1, 'Frame not changed'
        assert all_pages == 78, 'All pages incorrect value'
        assert frame_img_src != zero_frame_src, 'Image not changes'
        assert frame_text == first_frame_text, 'Incorrect text on slide'
