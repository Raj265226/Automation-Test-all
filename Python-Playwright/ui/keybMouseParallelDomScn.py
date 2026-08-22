import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(scope='module')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=['--start-maximize']
        )
        yield browser
        browser.close()

def test_keyboard_mouse_screenshot_context1(browser, request):
    context = browser.new_context(record_video_dir='Files/DownUpload/video_record')  # video
    page = context.new_page()
    page.goto("https://demoqa.com/text-box")

    context.tracing.start(       # trace
        screenshots=True,
        snapshots=True,
        sources=True
    )

    textbox = page.locator('#userName')
    textbox.click()
    page.keyboard.press('R')
    page.keyboard.type('oh')
    page.keyboard.down('Shift')
    page.keyboard.up('Shift')
    page.keyboard.press('Control+A')
    page.keyboard.press('Delete')
    page.keyboard.press('R')
    submit_btn = page.locator('#submit')
    test_name = request.node.name
    submit_btn.screenshot(path=f'Files/DownUpload/{test_name}.jpeg')

    box = submit_btn.bounding_box()
    page.mouse.move(
        box['x'] + box['width'] / 2,
        box['y'] + box['height'] / 2
    )
    page.mouse.down()
    page.mouse.up()

    try:
        assert page.title() == 'wrong title'
    except AssertionError:
        page.screenshot(
            path='Files/DownUpload/failure.jpeg',
            full_page=True
        )

    context.tracing.stop(path='Files/DownUpload/tracevideo.zip')
    context.close()

def test_dom_context_2(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practice.expandtesting.com/shadowdom")
    btn1 = page.locator('#my-btn').first
    print('Text of dom first btn ', btn1.text_content())

    shadow_dom = page.locator('#shadow-host')
    btn2 = shadow_dom.locator('#my-btn')
    print('Text of dom first btn ', btn2.text_content())
    context.close()


# for parallel execution pytest <path> -n 2 -v -s