import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_element_action(driver):
    driver.get("https://demoqa.com/buttons")

    double_click_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "doubleClickBtn")))  # Double click
    time.sleep(2)
    ActionChains(driver).double_click(double_click_btn).perform()

    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "doubleClickMessage")))

    assert message.text == "You have done a double click", "Not matching"
    assert "double click" in message.text, "Not matching"

    right_click_btn = driver.find_element(By.ID, "rightClickBtn")  # Right click
    ActionChains(driver).context_click(right_click_btn).perform()
    message = driver.find_element(By.ID, "rightClickMessage")

    assert message.text == "You have done a right click", "Not matching"
    assert "right click" in message.text, "Not matching"

    driver.find_element(By.XPATH,                               # dynamic id + click
        "//*[@id='rightClickBtn']/parent::div/following-sibling::div/button").click()  
    message = driver.find_element(By.ID, "dynamicClickMessage")

    assert message.text == "You have done a dynamic click", "Not matching"


    driver.get("https://demoqa.com/text-box")
    username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "userName"))
    )

    print("username field visible?", username.is_displayed())  # visible / display
    print("username field enabled?", username.is_enabled())  # enable
    username.send_keys("Roh")
    print("Input value -", username.get_attribute("value"))

    username.send_keys(Keys.CONTROL, "A")  # Keyboard combination
    username.send_keys(Keys.DELETE)
    username.clear()
    username.send_keys("Rohit")
    submit_btn = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].click();", submit_btn)

    assert driver.find_element(By.ID, "name").text == "Name:Rohit"


    driver.get("https://demoqa.com/menu")
    time.sleep(4)
    actions = ActionChains(driver)
    main_item_2 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Main Item 2")))
    actions.move_to_element(main_item_2).perform()
    sub_sub_list = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "SUB SUB LIST »")))
    actions.move_to_element(sub_sub_list).perform()
    sub_sub_item_2 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Sub Sub Item 2")))
    actions.move_to_element(sub_sub_item_2).perform()

    driver.get("https://demoqa.com/droppable")
    time.sleep(3)
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_elements(By.ID, "droppable")[0]
    ActionChains(driver).drag_and_drop(source, target).perform()

def test_Exception(driver):

    try:
        driver.get("https://demoqa.com/text-box")
        driver.find_element(By.ID, "wrongid")  # NoSuchElementException
    except Exception as e:
        if type(e).__name__ == "NoSuchElementException":
            print("NoSuchElementException NSE")

    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "wrongid")))  # TimeoutException
    except Exception as e:
        if type(e).__name__ == "TimeoutException":
            print("TimeoutException TE")

    try:
        assert driver.title == "wrong url"  # AssertionError
    except Exception as e:
        if type(e).__name__ == "AssertionError":
            print("AssertionError AE")

    try:
        username = driver.find_element(
            By.ID, "userName")  # StaleElementReferenceException
        driver.refresh()
        username.send_keys("Rohit")
    except Exception as e:
        if type(e).__name__ == "StaleElementReferenceException":
            print("StaleElementReferenceException SERE")

    try:
        driver.switch_to.alert.accept()  # NoAlertPresentException
    except Exception as e:
        if type(e).__name__ == "NoAlertPresentException":
            print("NoAlertPresentException NAPE")

    try:
        driver.switch_to.frame("wrongFrame")  # NoSuchFrameException
    except Exception as e:
        if type(e).__name__ == "NoSuchFrameException":
            print("NoSuchFrameException NSFE")

    try:
        driver.execute_script("XYZ")  # JavascriptException
    except Exception as e:
        if type(e).__name__ == "JavascriptException":
            print("JavascriptException JSEE")

    try:
        driver.close()
        driver.switch_to.window("wrongwindow")  # NoSuchWindowException
    except Exception as e:
        if type(e).__name__ == "NoSuchWindowException":
            print("NoSuchWindowException NSWE")