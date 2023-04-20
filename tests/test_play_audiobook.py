import allure
from pytest import mark
from src.pages.player.player_component import PlayerComponent, locSmallPauseBtn


class TestPlayAudioBook:

    @allure.title('Check playing audio book')
    @allure.severity(allure.severity_level.CRITICAL)
    @mark.smoke
    def test_play_audio_book(self, desktop_with_playing_video):
        player = PlayerComponent(desktop_with_playing_video.driver)
        player.switch_to_audio_book()
        assert desktop_with_playing_video.present_element(locSmallPauseBtn), 'Audio not continue play after switch mode'
        desktop_with_playing_video.scroll_page_to_element(locSmallPauseBtn)
        desktop_with_playing_video.wait_for_time(2)
        player.press_next_page_btn()
        player.press_next_page_btn()
        page_num = player.get_page_number()
        duration = player.get_time_after_start()
        assert page_num == 2, f"Incorrect page"
        assert duration == 40.0, f"Incorrect page start"
