"""Locators and actions for the preselection and selection iframes."""

from pypom import Region
from selenium.webdriver.common.by import By

class PreSelectionRegion(Region):
    """Locators and actions for the selection and pre-selection iframes."""
    _preselection_iframe_locator = (By.ID,
                                    'firefox-screenshots-preselection-iframe')
    _download_firefox_cta_locator = (By.ID, 'download-firefox-primary-cta')

    @property
    def loaded(self):
        preselect = self.find_element(*self._preselection_iframe_locator)
        return preselect.is_displayed()

    def click_desired_screenshot_area(self):
        self.selenium.switch_to.default_content()
        area = self.find_element(*self._download_firefox_cta_locator)
        action = self.selenium.ActionChains(self.selenium).move_to_element(area)
        action.perform()


class SelectionRegion(Region):
    """Locators and actions for the selection iframe."""
    _selection_iframe_locator = (By.ID,
                                'firefox-screenshots-selection-iframe')
    _save_screenshot_button_locator = (By.CLASS_NAME, 'highlight-button-save')

    @property
    def loaded(self):
        select = self.find_element(*self._selection_iframe_locator)
        return select.is_displayed()

    def click_save_screenshot(self):
        self.wait_for_region_to_load()
        select = self.find_element(*self._selection_iframe_locator)
        self.selenium.switch_to.frame(select)
        save = self.find_element(*self._save_screenshot_button_locator)
        save.click()

