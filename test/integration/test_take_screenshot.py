"""Tests for taking and saving a screenshot."""
import pytest
from pages.onboarding import OnboardingPage
from pages.selection import PreSelectionRegion, SelectionRegion
from pages.screenshot import ScreenshotPage

@pytest.mark.nondestructive
def test_click_take_screenshot(home_page):
    home_page.door_hanger.click_take_screenshot()
    onboarding_page = OnboardingPage(home_page.door_hanger.selenium).wait_for_page_to_load()
    onboarding_page.skip_screenshots_onboarding()
    preselection_region = PreSelectionRegion(home_page).wait_for_region_to_load()
    preselection_region.click_desired_screenshot_area()
    selection_region = SelectionRegion(home_page).wait_for_region_to_load()
    selection_region.click_save_screenshot()
    screenshot_page = ScreenshotPage(selection_region.selenium).wait_for_page_to_load()
    assert screenshot_page.loaded

