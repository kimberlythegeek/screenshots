import pytest
from regions.screenshot_interface import ScreenshotInterface
from regions.door_hanger import DoorHanger
from regions.onboarding import Onboarding
from regions.selection import PreSelection, Selection

@pytest.fixture
def screenshot_interface(base_url, selenium):
    selenium.get(base_url)
    return ScreenshotInterface(selenium).wait_for_page_to_load()

@pytest.fixture
def door_hanger(screenshot_interface):
    return DoorHanger(screenshot_interface).wait_for_region_to_load()

@pytest.fixture
def onboarding(screenshot_interface):
    return Onboarding(screenshot_interface)

@pytest.fixture
def preselection(screenshot_interface):
    return PreSelection(screenshot_interface)

@pytest.fixture
def selection(screenshot_interface):
    return Selection(screenshot_interface)