import pytest
from pages.door_hanger import DoorHangerRegion
from pages.onboarding import OnboardingPage
from pages.selection import PreSelectionRegion, SelectionRegion
from pages.home import Home

@pytest.fixture
def home_page(base_url, selenium):
    selenium.get(base_url)
    return Home(selenium, base_url).wait_for_page_to_load()

@pytest.fixture
def door_hanger(home_page):
    return DoorHangerRegion(home_page).wait_for_region_to_load()

@pytest.fixture
def onboarding(home_page):
    return OnboardingPage(home_page).wait_for_page_to_load()

@pytest.fixture
def preselection(home_page):
    return PreSelectionRegion(home_page).wait_for_region_to_load()

@pytest.fixture
def selection(home_page):
    return SelectionRegion(home_page).wait_for_region_to_load()