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

def test_element_action(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/buttons")
    page.locator('#doubleClickBtn').dblclick()  # Double click
    message = page.locator('#doubleClickMessage')

    expect(message).to_have_text('You have done a double click')  # Expect assert
    expect(message).to_contain_text('double click')  # Contain assert
    assert message.text_content() == 'You have done a double click'  # Text assert

    page.locator('#rightClickBtn').click(button='right')  # Right click
    expect(page.locator('#rightClickMessage')).to_contain_text('right click')

    page.get_by_text('Click Me').last.click()  # dynamic id + click
    expect(page.locator('#dynamicClickMessage')).to_contain_text('dynamic click')

    page.goto("https://demoqa.com/text-box")
    username = page.locator('#userName')
    print('username field visible? ', username.is_visible())
    print('username field editable? ', username.is_editable())
    print('username field enable? ', username.is_enabled())
    print('username field attribute value-', username.get_attribute('placeholder'))
    username.fill('R')
    username.type('oh')
    print('Input value - ', username.input_value())
    username.press('Control+A')
    username.press('Delete')
    username.press_sequentially('Raj', delay=1000)
    username.clear()
    username.fill('Rohit')
    page.locator('#submit').click()
    assert page.locator('#name').inner_text() == 'Name:Rohit'

    page.goto("https://demoqa.com/menu")
    page.wait_for_timeout(1000)
    page.get_by_text('Main Item 2').hover()
    page.get_by_text('SUB SUB LIST »').hover()
    page.get_by_text('Sub Sub Item 2').hover()

    page.goto("https://demoqa.com/droppable")
    page.wait_for_timeout(1000)
    source = page.locator('#draggable')
    target = page.locator('#droppable').first
    source.drag_to(target)

    context.close()

def test_Exception(browser):
    context = browser.new_context()
    page1 = context.new_page()
    page2 = context.new_page()
    page3 = context.new_page()
    page1.goto("https://demoqa.com/")
    page2.goto("https://demoqa.com/")

    try:
        page1.locator('#wrongid').click()  # TimeoutError
    except Exception as e:
        print('Timeout --->', type(e).__name__)
        if type(e).__name__ == 'TimeoutError':
            print("It's a TimeoutError")

    try:
        page1.locator('a').click()  # Strict mode Error / Error
    except Exception as e:
        if 'strict mode violation' in str(e):
            print('Strict Mode violation')
        if type(e).__name__ == 'Error':
            print("It's an Error")

    try:
        assert page1.title() == 'Wrong Title'  # AssertionError
    except Exception as e:
        print('AssertionError ->>', type(e).__name__)
        if type(e).__name__ == 'AssertionError':
            print("It's a AssertionError")

    page3.on(
        'requestfailed',
        lambda req: print(
            "Url ->", req.url,
            "Failure->", req.failure
        )
    )

    try:
        page3.goto('https://wrong-demoqa-url.com')  # NetworkError / Error
    except Exception as e:
        print('Error --->>', type(e).__name__)
        if type(e).__name__ == 'Error':
            print("It's showing error")
        if 'net::ERR_NAME_NOT_RESOLVED' in str(e):
            print('Network Error')

    page2.close()

    try:
        page2.locator('#wrongid').click()  # TargetClosedError
    except Exception as e:
        print('TargetClose --->>', type(e).__name__)

        if type(e).__name__ == 'TargetClosedError':
            print("It's a TargetClosedError")

    context.close()