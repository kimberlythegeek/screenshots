from pypom import Page
from selenium.webdriver.common.by import By

class ScreenshotPage(Page):
    """Locators and actions for an individual screenshot page."""
    _screenshot_image_locator = (By.ID, 'clipImage')

    @property
    def loaded(self):
        screenshot = self.find_element(*self._screenshot_image_locator)
        return screenshot.is_displayed*()

    