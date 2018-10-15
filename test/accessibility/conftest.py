import pytest
from pytest_axe.pytest_axe import PytestAxe as Axe
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://screenshots.stage.mozaws.net/"

_panel_button_locator = "pageActionButton"
_take_screenshot_button_locator = (By.ID, "pageAction-panel-screenshots")
_onboarding_iframe_locator = (By.ID, "firefox-screenshots-onboarding-iframe")
_test_image_locator = "banner-image-front"
_preselection_iframe_locator = (By.ID, "firefox-screenshots-preselection-iframe")
_selection_iframe_locator = (By.ID, "firefox-screenshots-selection-iframe")
_save_screenshots_button_locator = "highlight-button-save"
_screenshot_page_locator = (By.ID, "react-body-container")


def wait_for_element_to_load(driver, selector):
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located(selector))
    return element


@pytest.fixture(scope="class")
def home_page():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("security.csp.enable", False)
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get(base_url)
    axe = Axe(driver)
    axe.inject()
    yield axe
    driver.close()


@pytest.fixture(scope="class")
def onboarding_frame(home_page):
    driver = home_page.selenium
    with driver.context("chrome"):
        btn = driver.find_element_by_id(_panel_button_locator)
        btn.click()
        wait_for_element_to_load(driver, _take_screenshot_button_locator).click()
    onboarding = wait_for_element_to_load(driver, _onboarding_iframe_locator)
    driver.switch_to.frame(onboarding)
    axe = Axe(driver)
    axe.inject()
    yield axe


@pytest.fixture(scope="class")
def preselection_frame(onboarding_frame):
    driver = onboarding_frame.selenium
    driver.find_element_by_id("skip").click()
    driver.switch_to.default_content()
    preselection = wait_for_element_to_load(driver, _preselection_iframe_locator)
    driver.switch_to.frame(preselection)
    axe = Axe(driver)
    axe.inject()
    yield axe


@pytest.fixture(scope="class")
def selection_frame(preselection_frame):
    driver = preselection_frame.selenium
    driver.switch_to.default_content()
    el = driver.find_element_by_class_name(_test_image_locator)
    action = webdriver.ActionChains(driver).move_to_element(el).click(el)
    action.perform()
    selection = wait_for_element_to_load(driver, _selection_iframe_locator)
    driver.switch_to.frame(selection)
    axe = Axe(driver)
    axe.inject()
    yield axe


@pytest.fixture(scope="class")
def screenshot_page(selection_frame):
    driver = selection_frame.selenium
    driver.find_element_by_class_name(_save_screenshots_button_locator).click()
    driver.switch_to.default_content()
    wait_for_element_to_load(driver, _screenshot_page_locator)
    axe = Axe(driver)
    axe.inject()
    yield axe
