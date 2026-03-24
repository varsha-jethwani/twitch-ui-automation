import time
from core.driver_manager import create_driver
from pages.home_page import HomePage
from pages.stream_page import StreamPage


def test_twitch_search_streamer():

    driver = create_driver()

    driver.get("https://m.twitch.tv/")

    home = HomePage(driver)

    home.open_search()
    home.search("StarCraft II")

    time.sleep(3)

    stream = StreamPage(driver)

    stream.scroll_twice()
    stream.select_streamer()

    stream.capture_stream()

    driver.quit()