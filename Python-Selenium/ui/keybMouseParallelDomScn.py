import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_keyboard_mouse_screenshot_context(driver, request):
    os.makedirs("Files/DownUpload", exist_ok=True)
    driver.get("https://demoqa.com/text-box")
    textbox = driver.find_element(By.ID, "userName")
    textbox.click()
    textbox.send_keys("Rohit")
    submit_btn = driver.find_element(By.ID, "submit")
    test_name = request.node.name
    submit_btn.screenshot(f"Files/DownUpload/{test_name}.jpeg")
    actions = ActionChains(driver)
    actions.move_to_element(submit_btn).click().perform()

    try:
        assert driver.title == "wrong title"
    except AssertionError:
        driver.save_screenshot("Files/DownUpload/failure.jpeg")

def test_dom_context_2(driver):
    driver.get("https://practice.expandtesting.com/shadowdom")

    btn1 = driver.find_elements(By.CSS_SELECTOR, "#my-btn")[0]
    print("Text of dom first btn ->", btn1.text)

    shadow_host = driver.find_element(By.CSS_SELECTOR, "#shadow-host")
    shadow_root = shadow_host.shadow_root
    btn2 = shadow_root.find_element(By.CSS_SELECTOR, "#my-btn")
    print("Text of dom second btn ->", btn2.text)


# For parallel execution: -> pytest <path> -n 2 -v