"""Locators and actions for door hanger interactions."""

from pypom import Region
from selenium.webdriver.common.by import By

class DoorHanger(Region):
    """Locators and actions related to the door hanger."""

    _panel_button_locator = (By.ID, 'pageActionButton')
    _panel_locator = (By.ID, 'pageActionPanel')
    _take_screenshot_button_locator = (By.ID, 'pageAction-panel-screenshots')

    @property
    def loaded(self):
        panel = self.find_element(*self._panel_locator)
        return panel.is_displayed()

    def _open_and_switch_to_hanger(self):
        with self.selenium.context(self.selenium.CONTEXT_CHROME):
            self.find_element(*self._panel_locator).click()
            self.wait_for_region_to_load()

    def click_take_screenshot(self):
        """Open the door hanger."""
        self._open_and_switch_to_hanger()
        self.find_element(*self._take_screenshot_button_locator).click()