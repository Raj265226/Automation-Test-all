import pytest
from selenium import webdriver

def get_driver(browser_name):
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser -> {browser_name}")

    driver.maximize_window()
    return driver

@pytest.mark.parametrize("my_browser", ["chrome", "edge"])
def test_cross_browser(my_browser):
    driver = get_driver(my_browser)

    try:
        driver.get("https://demoqa.com/")
        print(f"Browser -> {my_browser}")
        print("Title ->", driver.title)

        assert "DEMOSITE" in driver.title.upper()

    finally:
        driver.quit()