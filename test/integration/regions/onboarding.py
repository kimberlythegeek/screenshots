"""Locators and actions for onboarding iframe interactions."""

from pypom import Region
from selenium.webdriver.common.by import By

class Onboarding(Region):
    """Locators and actions related to the onboarding iframe."""
    _onboarding_iframe_locator = (By.ID,
                                    'firefox-screenshots-onboarding-iframe')
    _onboarding_skip_button_locator = (By.ID, 'skip')

    @property
    def loaded(self):
        onboarding = self.find_element(*self._onboarding_iframe_locator)
        return onboarding.is_displayed()

    def _switch_to_onboarding_iframe(self):
        with self.selenium.context(self.selenium.CONTEXT_CONTENT):
            self.wait_for_region_to_load()
            onboarding = self.find_element(*self._onboarding_iframe_locator)
            self.selenium.switch_to.frame(onboarding)

    def _skip_screenshots_onboarding(self):
        self._switch_to_onboarding_iframe()
        skip = self.find_element(*self._onboarding_skip_button_locator)
        skip.click()