from pypom import Page
from selenium.webdriver.common.by import By

class Home(Page):
    """Locators and actions related to the home page used for testing."""
    _download_firefox_cta_locator = (By.ID, 'download-firefox-primary-cta')
    _panel_button_locator = (By.ID, 'pageActionButton')
    _panel_locator = (By.ID, 'pageActionPanel')
    _take_screenshot_button_locator = (By.ID, 'pageAction-panel-screenshots')

    @property
    def loaded(self):
        page = self.find_element(*self._download_firefox_cta_locator)
        return page.is_displayed()

    @property
    def door_hanger(self):
        from pages.door_hanger import DoorHangerRegion
        return DoorHangerRegion(self)

    def open_and_switch_to_hanger(self):
        with self.selenium.context(self.selenium.CONTEXT_CHROME):
            self.find_element(*self._panel_button_locator).click()
            # self.wait_for_region_to_load()
            self.wait.until(
                lambda s: s.find_element(*self._panel_locator).is_displayed())
            return self.find_element(*self._panel_locator)



    def click_take_screenshot(self):
        """Open the door hanger."""
        self.open_and_switch_to_hanger()
        with self.selenium.context(self.selenium.CONTEXT_CHROME):
            self.find_element(*self._take_screenshot_button_locator).click()