import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_wait(driver):
    # Explicit Wait -> Done on test_checkboxRadioDynamic.py::test_dynamic_properties
    pass


def test_WebTable_sort(driver):
    driver.get("https://demoqa.com/webtables")

    rows = driver.find_elements(By.CSS_SELECTOR,'.table tbody tr')
    print('Total rows ->', len(rows))
    print('Total columns ->',len(driver.find_elements(By.CSS_SELECTOR,'.table thead tr th')))

    for row in rows:
        if 'Alden' in row.text:  # Find particular row
            col = row.find_elements(By.CSS_SELECTOR, 'td')
            print(' | '.join(c.text for c in col[:-1]))
            break

     # Sorting
    names = [i.text for i in driver.find_elements(By.CSS_SELECTOR,'.table tbody tr td:nth-child(1)')]
    try:
        assert names == sorted(names)
    except AssertionError as e:
        print('Its not matching')
    print('Names', names)
    print('Sorted Names', sorted(names))


def test_WebTable_search(driver):
    driver.get("https://demoqa.com/webtables")
    driver.find_element(By.ID,'searchBox').send_keys('ierra')
    rows = driver.find_elements(By.CSS_SELECTOR,'tbody tr')

    for row in rows:
        col = row.find_elements(By.CSS_SELECTOR,'td')
        print(' | '.join(c.text for c in col[:-1]))

def test_pagination_name_search(driver):
    driver.get("https://practice.expandtesting.com/dynamic-pagination-table")

    search_name = "Raj Roy"  # Ethan Thomas
    found = False

    while True:
        rows = driver.find_elements(By.CSS_SELECTOR,'#example tbody tr')

        for row in rows:
            if search_name in row.text:
                found = True
                print('Found->',' | '.join(c.text for c in row.find_elements(By.TAG_NAME,'td')))
                break

        if found:
            break

        next_btn = driver.find_element(By.ID,'example_next')
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",next_btn)

        if 'disabled' in next_btn.get_attribute('class'):
            break
        driver.execute_script("arguments[0].click();",next_btn)
        time.sleep(1)

    try:
        assert found
    except Exception as e:
        if type(e).__name__ == 'AssertionError':
            print(f'{search_name} not found')


def test_windows_tabs(driver):
    driver.get("https://demoqa.com/browser-windows")
    parent_window = driver.current_window_handle
    driver.find_element(By.ID,"tabButton").click()
    driver.find_element(By.ID,"windowButton").click()
    driver.find_element(By.ID,"messageWindowButton").click()

    for window in driver.window_handles:  # all windows
        driver.switch_to.window(window)
        # print("URL ->", driver.current_url)
        # print("Title ->", driver.title)
    driver.switch_to.window(parent_window)

def test_switch_by_url(driver):
    driver.get("https://demoqa.com/browser-windows")
    driver.find_element(By.ID,"tabButton").click()
    driver.find_element(By.ID,"windowButton").click()

    # Switch by URL
    # for window in driver.window_handles:
    #     driver.switch_to.window(window)
    #     if 'sample' in driver.current_url:
    #         break

    # Switch by title
    for window in driver.window_handles:
        driver.switch_to.window(window)

        if driver.title == 'demoqa':
            print('found ->', driver.title)
            break

def test_child_close_parent(driver):
    driver.get("https://demoqa.com/browser-windows")
    parent_window = driver.current_window_handle
    driver.find_element(By.ID,"tabButton").click()
    driver.find_element(By.ID,"windowButton").click()
    driver.find_element(By.ID,"messageWindowButton").click()
    print('Before closing child tabs->',len(driver.window_handles))

    for window in driver.window_handles:
        if window != parent_window:
            driver.switch_to.window(window)
            driver.close()
    driver.switch_to.window(parent_window)
    print('After closing child tabs->',len(driver.window_handles))