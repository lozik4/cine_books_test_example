import allure
from pytest import mark
from src.pages.player.player_component import PlayerComponent


class TestPlayingVideoBook:
    @allure.title('Check process playing video book')
    @allure.severity(allure.severity_level.CRITICAL)
    @mark.smoke
    def test_play_video_book(self, desktop):
        WAIT_VIDEO = 5
        player = PlayerComponent(desktop.driver)
        player.press_big_btn_play_video()
        desktop.wait_for_time(2)
        duration_1 = player.get_time_after_start()
        desktop.wait_for_time(WAIT_VIDEO)
        duration_2 = player.get_time_after_start()
        assert duration_2 > duration_1, f'Video not played 1st {duration_1}, 2d {duration_2}'
        assert WAIT_VIDEO <= int((duration_2 - duration_1)), 'Video works with lag'

    @allure.title('Check switch page in video book')
    @allure.severity(allure.severity_level.CRITICAL)
    @mark.smoke
    def test_check_switch_page(self, desktop):
        player = PlayerComponent(desktop.driver)
        player.press_big_btn_play_video()
        desktop.wait_for_time(2)
        player.press_next_page_btn()
        player.press_next_page_btn()
        page_num = player.get_page_number()
        duration = player.get_time_after_start()
        assert page_num == 2, f"Incorrect page"
        assert duration == 40.0, f"Incorrect page start"

