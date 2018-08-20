"""Locators and actions for door hanger interactions."""

from pypom import Region
from selenium.webdriver.common.by import By

class DoorHangerRegion(Region):
    """Locators and actions related to the door hanger."""

    _panel_button_locator = (By.ID, 'pageActionButton')
    _panel_locator = (By.ID, 'pageActionPanel')
    _take_screenshot_button_locator = (By.ID, 'pageAction-panel-screenshots')

    @property
    def loaded(self):
        """Opens the door hanger and returns true when loaded."""
        with self.selenium.context(self.selenium.CONTEXT_CHROME):
            self.find_element(*self._panel_button_locator).click()
            panel = self.find_element(*self._panel_locator)
            return panel.is_displayed()

    def click_take_screenshot(self):
        """Click take screenshot button."""
        with self.selenium.context(self.selenium.CONTEXT_CHROME):
            self.find_element(*self._take_screenshot_button_locator).click()