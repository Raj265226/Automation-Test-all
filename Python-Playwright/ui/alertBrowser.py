import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='module')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=['--start-maximized']
        )
        yield browser
        browser.close()

def test_alert_normal_click(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/alerts")

    page.on('dialog', lambda dialog: (
        print('dialog type - ', dialog.type),
        print('dialog message - ', dialog.message),
        dialog.accept()
    ))

    page.locator('#alertButton').click()
    context.close()

def test_alert_wait_click(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/alerts")

    page.on('dialog', lambda dialog: (
        print('dialog type - ', dialog.type),
        print('dialog message - ', dialog.message),
        dialog.accept()
    ))

    page.locator('#timerAlertButton').click()
    context.close()

def test_alert_confirm_yes(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/alerts")

    page.on('dialog', lambda dialog: (
        print('dialog type - ', dialog.type),
        print('dialog message - ', dialog.message),
        dialog.accept()
    ))

    page.locator('#confirmButton').click()
    print('Clicked Yes - ', page.locator('#confirmResult').inner_text())
    print('Clicked Yes - ', page.locator('#confirmResult').text_content())
    context.close()

def test_alert_confirm_no(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/alerts")

    page.on('dialog', lambda dialog: (
        print('dialog type - ', dialog.type),
        print('dialog message - ', dialog.message),
        dialog.dismiss()
    ))

    page.locator('#confirmButton').click()
    print('Clicked No - ', page.locator('#confirmResult').inner_text())
    print('Clicked No - ', page.locator('#confirmResult').text_content())
    context.close()

def test_alert_prompt_yes(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/alerts")

    page.on('dialog', lambda dialog: (
        print('dialog type - ', dialog.type),
        print('dialog message - ', dialog.message),
        dialog.accept('Rohit')
    ))

    page.locator('#promtButton').click()
    print('Prompt Yes Rohit - ', page.locator('#promptResult').inner_text())
    print('Prompt Yes Rohit - ', page.locator('#promptResult').text_content())
    context.close()

def test_browser_action(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/alerts")
    page.reload()
    page.goto("https://demoqa.com/")
    page.go_back()
    print('Expected url (alert) - ', page.url)
    page.go_forward()
    print('Expected url (main) - ', page.url)
    context.close()

def test_brwser_storage_state(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/alerts")
    context.storage_state(path='Files/Testing.json')
    page.reload()
    print('Expected url (alert) - ', page.url)
    context.close()

def test_context_isolation(browser):
    context1 = browser.new_context()
    context2 = browser.new_context()
    page1 = context1.new_page()
    page2 = context2.new_page()

    page1.goto("https://demoqa.com/alerts")
    page2.goto("https://demoqa.com/")
    print('Expected url (alert) - ', page1.url)
    print('Expected url (main) - ', page2.url)
    context1.close()
    context2.close()

def test_page_tab(browser):
    context = browser.new_context()
    page1 = context.new_page()
    page2 = context.new_page()
    page1.goto("https://demoqa.com/alerts")
    page2.goto("https://demoqa.com/")
    print('Expected url (alert) - ', page1.url)
    print('Expected url (main) - ', page2.url)
    page2.close()
    context.close()