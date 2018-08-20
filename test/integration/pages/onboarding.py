"""Locators and actions for onboarding iframe interactions."""

from pypom import Page
from selenium.webdriver.common.by import By

class OnboardingPage(Page):
    """Locators and actions related to the onboarding iframe."""
    _onboarding_iframe_locator = (By.ID,
                                    'firefox-screenshots-onboarding-iframe')
    _onboarding_skip_button_locator = (By.ID, 'skip')

    @property
    def loaded(self):
        page = self.find_element(*self._onboarding_iframe_locator)
        return page.is_displayed()

    def _switch_to_onboarding_iframe(self):
        with self.selenium.context(self.selenium.CONTEXT_CONTENT):
            self.wait_for_page_to_load()
            frame = self.find_element(*self._onboarding_iframe_locator)
            self.selenium.switch_to.frame(frame)

    def skip_screenshots_onboarding(self):
        self._switch_to_onboarding_iframe()
        skip_button = self.find_element(*self._onboarding_skip_button_locator)
        skip_button.click()
