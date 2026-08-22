import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_single_multi_checkbox(driver):
    driver.get("https://demoqa.com/checkbox")
    driver.find_element(By.CLASS_NAME, "rc-tree-switcher").click()
    driver.find_element(By.CSS_SELECTOR, "[aria-label='Select Desktop']").click()
    driver.find_element(By.CSS_SELECTOR, "[aria-label='Select Documents']").click()
    driver.find_element(By.CSS_SELECTOR, "[aria-label='Select Downloads']").click()
    desktop = driver.find_element(By.CSS_SELECTOR, "[aria-label='Select Desktop']")
    assert desktop.get_attribute('aria-checked') == 'true',"It needs to be checked"
    desktop.click()
    assert desktop.get_attribute('aria-checked') == 'false',"It needs to be checked"

def test_dropdown(driver):
    driver.get("https://demoqa.com/select-menu")
    driver.find_element(By.ID, 'withOptGroup').click()
    driver.find_element(By.ID, 'react-select-2-input').send_keys('Group 1, option 1', Keys.ENTER)

def test_select_dropdown(driver):
    driver.get("https://demoqa.com/select-menu")
    select_data = Select(driver.find_element(By.ID, 'oldSelectMenu'))
    Color_list = []
    for option in select_data.options:
        Color_list.append(option.text)
    print('Color lists ->', Color_list)
    select_data.select_by_visible_text('Blue')
    select_data.select_by_index(3)  # Yellow
    select_data.select_by_value('4')  # Purple

    select_data1 = Select(driver.find_element(By.ID, 'cars'))
    select_data1.select_by_visible_text('Volvo')
    select_data1.select_by_visible_text('Audi')

    driver.find_element(By.ID, 'react-select-4-input').send_keys('Black',Keys.ENTER,'Blue',Keys.ENTER)

def test_radio(driver):
    driver.get("https://demoqa.com/radio-button")
    yes_btn = driver.find_element(By.ID, 'yesRadio')
    impressive_btn = driver.find_element(By.ID, 'impressiveRadio')
    no_btn = driver.find_element(By.ID, 'noRadio')
    yes_btn.click()

    assert yes_btn.is_enabled(),"Yes button should be enabled"
    assert yes_btn.is_selected(),"Yes button should be selected"
    assert impressive_btn.is_enabled(),"Impressive button should be enabled"
    assert not impressive_btn.is_selected(),"Impressive button should not be selected"
    assert not no_btn.is_enabled(),"No button should be disabled"

    impressive_btn.click()
    assert not yes_btn.is_selected(),"Yes button should not be selected"

def test_dynamic_properties(driver):
    driver.get("https://demoqa.com/dynamic-properties")
    enable_5_sec_btn = driver.find_element(By.ID, 'enableAfter')
    print('enableAfter expected false ->',enable_5_sec_btn.is_enabled())
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(enable_5_sec_btn))  # Explicit wait
    print('enableAfter expected true ->',enable_5_sec_btn.is_enabled())

    visible_5_sec_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'visibleAfter')))
    print('Visible status -',visible_5_sec_btn.is_displayed())

    driver.get("https://the-internet.herokuapp.com/infinite_scroll")    # paragraph count
    for _ in range(5):
        driver.execute_script('window.scrollBy(0,1000)')
        time.sleep(1)
    paragraphs = driver.find_elements(By.CLASS_NAME,'jscroll-added')
    print('Total stanzas -', len(paragraphs))

    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")  # Progress-bar 
    finish_btn = driver.find_element(By.ID, 'finish')
    print('finish btn hidden? (before load) -',finish_btn.is_displayed())
    driver.find_element(By.XPATH,"//*[text()='Start']").click()
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.ID, 'loading')))
    print('finish btn hidden? (after load) -',finish_btn.is_displayed())