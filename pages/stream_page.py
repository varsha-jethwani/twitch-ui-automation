import time
from pages.base_page import BasePage


class StreamPage(BasePage):

    STREAMERS = "//a[contains(@href,'/')]"

    def scroll_twice(self):
        self.scroll()
        time.sleep(2)
        self.scroll()

    def select_streamer(self):
        streams = self.elements(self.STREAMERS)
        streams[4].click()

    def capture_stream(self):
        time.sleep(5)
        self.screenshot("stream.png")