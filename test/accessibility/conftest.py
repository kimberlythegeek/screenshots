import pytest
from pytest_axe.pytest_axe import PytestAxe as Axe
from selenium import webdriver

base_url = "https://screenshots.stage.mozaws.net/"


@pytest.fixture(scope="session", autouse=True)
def home_page():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("security.csp.enable", False)
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get(base_url)

    axe = Axe(driver)
    axe.inject()

    yield axe
    driver.close()


def pytest_configure(config):
    """
        Included rule ID of tests that are expected to fail as a key, with the
        github issue number as a value (or any other desired info as
        reason for failure), and pass to pytestconfig to generate the tests.

        Example:
            config.xfail_rules = {
                "meta-viewport": "Reason: GitHub issue #245",
    """
    config.xfail_rules = {
        "color-contrast": "Reason: GitHub issue #5014 https://github.com/mozilla-services/screenshots/issues/5014",
        "html-has-lang": "Reason: GitHub issue #5015 https://github.com/mozilla-services/screenshots/issues/5015",
        "landmark-one-main": "Reason: GitHub issue #5016 https://github.com/mozilla-services/screenshots/issues/5016",
        "link-name": "Reason: GitHub issue #5017 https://github.com/mozilla-services/screenshots/issues/5017",
        "meta-viewport": "Reason: GitHub issue #5018 https://github.com/mozilla-services/screenshots/issues/5018",
        "region": "Reason: GitHub issue #5016 https://github.com/mozilla-services/screenshots/issues/5016",
    }
