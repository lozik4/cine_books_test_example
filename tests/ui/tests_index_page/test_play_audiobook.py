import allure
from pytest import mark

from src.pages.player.player_component import PlayerComponent, locSmallPauseBtn

"""
Run locally: 
    pytest tests/ui/test_index_page/test_play_audiobook.py
Make report:
    allure generate -c allure-results
"""


class TestPlayAudioBook:

    @allure.title('Check playing audio book')
    @allure.severity(allure.severity_level.CRITICAL)
    @mark.smoke
    def test_play_audio_book(self, playing_video):
        with allure.step(f"GIVEN: user at audio book mode"):
            player = PlayerComponent(playing_video.driver)
            player.switch_to_audio_book()
        with allure.step(f"WHEN: User switch to audio book and listen"):
            assert playing_video.present_element(locSmallPauseBtn), 'Audio not continue play after switch mode'
            playing_video.scroll_page_to_element(locSmallPauseBtn)
            playing_video.wait_for_time(2)
            player.press_next_page_btn()
            player.press_next_page_btn()
            page_num = player.get_page_number()
            duration = player.get_time_after_start()
        with allure.step(f"THEN: Page changed, page duration correct"):
            assert page_num == 2, f"Incorrect page"
            assert duration == 40.0, f"Incorrect page start"
