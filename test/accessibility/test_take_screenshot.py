from selenium import webdriver
from selenium.webdriver.common.actions.pointer_actions import PointerActions
from time import sleep


def test_take_screenshot():
    driver = webdriver.Firefox()
    driver.get('https://pypi.org')
    with driver.context('chrome'):
        driver.find_element_by_css_selector('image#pageActionButton').click()
        driver.find_element_by_css_selector('#pageAction-panel-screenshots').click()
        with driver.context(driver.CONTEXT_CONTENT):
            sleep(2)
            onboarding = driver.find_element_by_id('firefox-screenshots-onboarding-iframe')
            driver.switch_to.frame(onboarding)
            driver.find_element_by_id('skip').click()
            sleep(2)
            driver.switch_to.default_content()
            sleep(1)
            el = driver.find_element_by_class_name('statistics-bar')
            action = webdriver.ActionChains(driver).move_to_element(el).click(el)
            action.perform()
            sleep(2)
            frame = driver.find_element_by_id('firefox-screenshots-selection-iframe')
            driver.switch_to.frame(frame)
            sleep(2)
            driver.find_element_by_class_name('highlight-button-save').click()
    sleep(10)
    driver.close()