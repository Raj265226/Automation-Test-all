import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximized"]
        )
        yield browser
        browser.close()

def test_wait(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/dynamic-properties")
    # page.wait_for_function("()=>document.querySelector('#enableAfter').disabled === false")

    enable_btn = page.locator("#enableAfter")       # enable button
    expect(enable_btn).to_be_enabled(timeout=8000)
    print("Enable button text - ", enable_btn.inner_text())

    visible_btn = page.locator("#visibleAfter")     # visible button
    visible_btn.wait_for(state="visible")
    print("Visible button text - ", visible_btn.inner_text())

    page.goto("https://demoqa.com/")
    page.wait_for_load_state()       # load
    page.wait_for_timeout(3000)      # timeout
    context.close()

def test_WebTable_sort(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/webtables")
    rows = page.locator(".table tbody tr")
    print("Total rows -> ", rows.count())
    print("Total columns -> ",page.locator(".table thead tr th").count())

    for i in range(rows.count()):
        row = rows.nth(i)
        if "Alden" in row.text_content():       # Find particular row
            cols = row.locator("td").all_text_contents()
            cols.pop()
            print(" | ".join(cols))
            break

    names = page.locator(".table tbody tr td:nth-child(1)").all_text_contents()  # sorting
    assert names == sorted(names)
    print("Names :", names)
    print("Sorted Names :", sorted(names))
    context.close()

def test_WebTable_search(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/webtables")
    page.locator("#searchBox").fill("ierra")
    rows = page.locator("tbody tr")
    for i in range(rows.count()):
        row = rows.nth(i)
        print(" | ".join(row.locator("td").all_text_contents()))
    context.close()

def test_pagination_name_search(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practice.expandtesting.com/dynamic-pagination-table")

    search_name = "Raj Roy"       # Ethan Thomas
    found = False

    while True:
        rows = page.locator("#example tbody tr")
        for i in range(rows.count()):
            row = rows.nth(i)
            if search_name in row.locator("td").all_text_contents():
                found = True
                print(
                    "Found->",
                    " | ".join(row.locator("td").all_text_contents())
                )
                break

        if found:
            break

        next_btn = page.locator("#example_next")

        if "disabled" in next_btn.get_attribute("class"):
            break

        next_btn.click()
        page.wait_for_timeout(1000)

    try:
        assert found
    except Exception as e:
        if type(e).__name__ == "AssertionError":
            print(f"{search_name} not found")

    context.close()

def test_windows_tabs(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/browser-windows")
    with context.expect_page() as Tab:       # individual tab details
        page.locator("#tabButton").click()
    new_tab = Tab.value
    print("Tab url", new_tab.url)
    print("Tab title", new_tab.title())

    with context.expect_page():
        page.locator("#windowButton").click()

    with context.expect_page():
        page.locator("#messageWindowButton").click()

    for i in context.pages:                  # All tabs/windows details
        print("Url ->", i.url)
        print("Title ->", i.title())

    context.close()

def test_switch_by_url(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/browser-windows")
    with context.expect_page():
        page.locator("#tabButton").click()

    with context.expect_page():
        page.locator("#windowButton").click()

    with context.expect_page():
        page.locator("#messageWindowButton").click()

    for i in context.pages:                  # switch by url
        if "sample" in i.url:
            break

    # for i in context.pages:              # switch by title
    #     if i.title() == "demosite":
    #         print("found ->", i.title())
    #         break

    context.close()


def test_child_close_parent(browser):
    context = browser.new_context()
    parent = context.new_page()
    parent.goto("https://demoqa.com/browser-windows")

    with context.expect_page():
        parent.locator("#tabButton").click()

    with context.expect_page():
        parent.locator("#windowButton").click()

    with context.expect_page():
        parent.locator("#messageWindowButton").click()

    print("Before closing child tabs ->", len(context.pages))

    for i in context.pages:
        if i != parent:
            i.close()

    parent.bring_to_front()
    print("After closing child tabs ->", len(context.pages))
    context.close()