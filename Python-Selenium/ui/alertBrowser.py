import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='module')
def drivers():
    driver1 = webdriver.Edge()
    driver2 = webdriver.Edge()
    yield driver1, driver2
    driver1.quit()
    driver2.quit()

def test_alert_normal_click(driver):
    driver.get("https://demoqa.com/alerts")
    driver.find_element(By.ID, 'alertButton').click()
    alert = driver.switch_to.alert
    print('Alert normal type ->', alert.text)
    alert.accept()

def test_alert_wait_click(driver):
    driver.get("https://demoqa.com/alerts")
    driver.find_element(By.ID, 'timerAlertButton').click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print('Alert timer alert type ->', alert.text)
    alert.accept()

def test_alert_confirm_yes(driver):
    driver.get("https://demoqa.com/alerts")
    driver.find_element(By.ID, 'confirmButton').click()
    alert = driver.switch_to.alert
    print('Alert confirm alert type ->', alert.text)
    alert.accept()
    result = driver.find_element(By.ID, 'confirmResult').text
    print('message displayed ->', result)

def test_alert_confirm_no(driver):
    driver.get("https://demoqa.com/alerts")
    driver.find_element(By.ID, 'confirmButton').click()
    alert = driver.switch_to.alert
    print('Alert confirm alert type ->', alert.text)
    alert.dismiss()
    result = driver.find_element(By.ID, 'confirmResult').text
    print('message displayed ->', result)

def test_alert_prompt_yes(driver):
    driver.get("https://demoqa.com/alerts")
    driver.find_element(By.ID, 'promtButton').click()
    alert = driver.switch_to.alert
    print('Alert alert type ->', alert.text)
    alert.send_keys('Rohit')
    alert.accept()
    result = driver.find_element(By.ID, 'promptResult').text
    print('message displayed ->', result)
    assert 'You entered Rohit' in result, 'Not matched'

def test_browser_action(driver):
    driver.get("https://demoqa.com/alerts")
    driver.refresh()
    driver.get("https://demoqa.com/")
    driver.back()
    print('Expected url (alert) ->', driver.current_url)
    driver.forward()
    print('Expected url (main) ->', driver.current_url)

def test_separate_browser(drivers):
    driver1, driver2 = drivers
    driver1.get("https://demoqa.com/alerts")
    driver2.get("https://demoqa.com/")
    print('Expected url (alert) ->', driver1.current_url)
    print('Expected url (main) ->', driver2.current_url)

def test_window_tab(driver):
    driver.get("https://demoqa.com/alerts")
    first_tab = driver.current_window_handle
    driver.switch_to.new_window('tab')
    driver.get("https://demoqa.com/")
    print('Expected url (main) ->', driver.current_url)
    driver.switch_to.window(first_tab)
    print('Expected url (alert) ->', driver.current_url)