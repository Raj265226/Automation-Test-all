import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(scope='module')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=['--start-maximized']
        )
        yield browser
        browser.close()

def test_single_multi_checkbox(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/checkbox")
    page.locator('.rc-tree-switcher').click()
    page.get_by_role('checkbox', name='Select Desktop').check()
    page.get_by_role('checkbox', name='Select Documents').click()
    page.get_by_role('checkbox', name='Select Downloads').click()
    checkbox = page.get_by_role('checkbox', name='Select Desktop')
    assert checkbox.is_checked(), 'It needs to be checked'
    expect(checkbox).to_be_checked()
    page.get_by_role('checkbox', name='Select Desktop').uncheck()
    assert not checkbox.is_checked(), 'It needs to be unchecked'
    expect(checkbox).not_to_be_checked()
    context.close()

def test_dropdown(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/select-menu")
    page.locator('#withOptGroup').click()  # Select Value
    page.locator('#react-select-2-input').fill('Group 1, option 1')
    page.keyboard.press('Enter')
    context.close()

def test_select_dropdown(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/select-menu")
    select_option = page.locator('#oldSelectMenu')  # Old Style Select Menu
    select_option.select_option(value='1')
    select_option.select_option('2')
    select_option.select_option('Yellow')
    select_option1 = page.locator('#cars')  # Standard multi select
    select_option1.select_option(['Volvo', 'Audi'])
    locator_multi_dd = page.locator('#react-select-4-input')  # Multiselect drop down
    locator_multi_dd.fill('Black')
    locator_multi_dd.press('Enter')
    locator_multi_dd.fill('Blue')
    locator_multi_dd.press('Enter')
    context.close()

def test_radio(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/radio-button")
    yes_btn = page.locator('#yesRadio')
    impressive_btn = page.locator('#impressiveRadio')
    no_btn = page.locator('#noRadio')
    yes_btn.click()
    expect(yes_btn).to_be_enabled()
    expect(yes_btn).to_be_checked()
    expect(impressive_btn).to_be_enabled()
    expect(impressive_btn).not_to_be_checked()
    expect(no_btn).to_be_disabled()
    impressive_btn.click()
    expect(yes_btn).not_to_be_checked()
    expect(impressive_btn).to_be_enabled()
    expect(impressive_btn).to_be_checked()
    context.close()


def test_dynamic_properties(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/dynamic-properties")
    enable_5_sec_btn = page.locator('#enableAfter')
    expect(enable_5_sec_btn).to_be_visible()
    print('Visible status 1 -', enable_5_sec_btn.is_visible())
    visible_5_sec_btn = page.locator('#visibleAfter')
    visible_5_sec_btn.wait_for(state='visible')
    print('Visible status after wait -',visible_5_sec_btn.is_visible())

    # visible_5_sec_btn.wait_for(state='attached')  # for remember purpose
    # visible_5_sec_btn.wait_for(state='detached')

    page.goto("https://the-internet.herokuapp.com/infinite_scroll")
    for _ in range(5):
        page.mouse.wheel(0, 1000)
        page.wait_for_timeout(500)

    paragraphs = page.locator('.jscroll-added')
    print('Total stanzas -', paragraphs.count())

    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    finish_btn = page.locator('#finish')
    print('finish btn Hidden? (before load) -',finish_btn.is_hidden())
    page.locator('#start button').click()
    page.locator('#loading').wait_for(state='hidden')
    print('finish btn hidden? (after load) -',finish_btn.is_hidden())
    context.close()