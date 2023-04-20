import allure
from pytest import mark

from src.pages.player.player_component import PlayerComponent, locSmallPauseBtn

"""
Run locally: 
    pytest tests/ui/test_index_page/test_play_videobook.py
Make report:
    allure generate -c allure-results
"""


class TestPlayingVideoBook:
    @allure.title('Check process playing video book')
    @allure.severity(allure.severity_level.CRITICAL)
    @mark.smoke
    def test_play_video_book(self, desktop):
        WAIT_VIDEO = 5
        with allure.step(f"GIVEN: user at index page"):
            player = PlayerComponent(desktop.driver)
        with allure.step(f"WHEN: user playing video"):
            player.press_big_btn_play_video()
            desktop.wait_present_element(locSmallPauseBtn)
            duration_1 = player.get_time_after_start()
            desktop.wait_for_time(WAIT_VIDEO)
            duration_2 = player.get_time_after_start()
        with allure.step(f"THEN: check playing video and page duration"):
            assert duration_2 > duration_1, f'Video not played 1st {duration_1}, 2d {duration_2}'
            assert WAIT_VIDEO <= int((duration_2 - duration_1)), 'Video works with lag'

    @allure.title('Check switch page in video book')
    @allure.severity(allure.severity_level.CRITICAL)
    @mark.smoke
    def test_check_switch_page(self, desktop):
        with allure.step(f"GIVEN: user at index page"):
            player = PlayerComponent(desktop.driver)
        with allure.step(f"WHEN: change pages"):
            player.press_big_btn_play_video()
            desktop.wait_present_element(locSmallPauseBtn)
            player.press_next_page_btn()
            player.press_next_page_btn()
            page_num = player.get_page_number()
            duration = player.get_time_after_start()
        with allure.step(f"THEN: check page number and page time start"):
            assert page_num == 2, f"Incorrect page"
            assert duration == 40.0, f"Incorrect page start"

    @allure.title('Example Fail Test')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_example_fake_result(self, desktop):
        with allure.step(f"GIVEN: user at index page"):
            player = PlayerComponent(desktop.driver)
        with allure.step(f"WHEN: change pages"):
            player.press_big_btn_play_video()
            desktop.wait_present_element(locSmallPauseBtn)
            player.press_next_page_btn()
            player.press_next_page_btn()
            page_num = player.get_page_number()
            duration = player.get_time_after_start()
        with allure.step(f"THEN: check page number and page time start"):
            assert page_num == 3, f"Incorrect page"  # it's mistake
            assert duration == 40.0, f"Incorrect page start"
