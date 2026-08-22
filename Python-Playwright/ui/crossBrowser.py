import pytest
from playwright.sync_api import sync_playwright, expect


def get_browser(p, browser_name):
    if browser_name == 'chromium':
        return p.chromium.launch(
            headless=False
        )
    elif browser_name == "webkit":
        return p.webkit.launch(
            headless=False
        )
    else:
        raise ValueError(f'Unsupported browser -> {browser_name}')

@pytest.mark.parametrize('my_browser', ['chromium', 'webkit'])
def test_browser_parameterize(my_browser):
    with sync_playwright() as p:
        browser = get_browser(p, my_browser)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://demoqa.com/")
        print("browser_name ->", my_browser)
        print("title ->", page.title())

        context.close()
        browser.close()