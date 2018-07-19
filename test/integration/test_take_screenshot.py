"""Tests for taking and saving a screenshot."""
import pytest
from time import sleep
from regions.onboarding import Onboarding

@pytest.mark.nondestructive
def test_click_take_screenshot(door_hanger):
    door_hanger.click_take_screenshot()
    onboarding = Onboarding(door_hanger.selenium)
    assert onboarding.loaded

