from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):

    SEARCH_ICON = "//button[@aria-label='Search']"
    SEARCH_INPUT = "//input[@type='search']"
    ACCEPT_COOKIES = "//button[contains(text(),'Accept')]"

    def handle_cookies(self):

        try:
            wait = WebDriverWait(self.driver, 5)

            cookie_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, self.ACCEPT_COOKIES))
            )

            cookie_btn.click()

        except:
            pass

    def open_search(self):

        self.handle_cookies()

        wait = WebDriverWait(self.driver, 20)

        search_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.SEARCH_ICON))
        )

        search_btn.click()

    def search(self, text):

        wait = WebDriverWait(self.driver, 20)

        search_box = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.SEARCH_INPUT))
        )

        search_box.send_keys(text)