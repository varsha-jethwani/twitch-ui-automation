from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(By.XPATH, locator).click()

    def type(self, locator, text):
        self.driver.find_element(By.XPATH, locator).send_keys(text)

    def elements(self, locator):
        return self.driver.find_elements(By.XPATH, locator)

    def scroll(self):
        self.driver.execute_script("window.scrollBy(0,1000)")

    def screenshot(self, name):
        self.driver.save_screenshot(name)