import pytest
from pytest_axe.pytest_axe import PytestAxe as Axe
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

base_url = "https://screenshots.stage.mozaws.net/"

_panel_button_locator = "pageActionButton"
_take_screenshot_button_locator = (By.ID, "pageAction-panel-screenshots_mozilla_org")


def wait_for_element_to_load(driver, selector):
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located(selector))
    return element


@pytest.fixture(scope="class")
def home_page():
    """Launch Screenshots home page as guest."""
    profile = webdriver.FirefoxProfile()
    # Disable CSP so aXe javascript can be injected
    profile.set_preference("security.csp.enable", False)
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get(base_url)

    # Inject accessibility API into page
    axe = Axe(driver)
    axe.inject()

    # Yield Axe instance, containing the WebDriver object as class attribute
    yield axe

    # Close WebDriver instance
    driver.close()
