import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximize"]
        )
        yield browser
        browser.close()

def test_upload_download(browser):
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("https://demoqa.com/upload-download")
    page.locator("#uploadFile").set_input_files(["Files/DownUpload/UploadFile.jpeg"])  # Upload

    # page.locator("#uploadFile").set_input_files(["path1", "path2"])  # Multi upload

    with page.expect_download() as download_info:  # Download
        page.locator("#downloadButton").click()

    download_file = download_info.value
    file_name = download_file.suggested_filename
    file_path = download_file.path()
    download_file.save_as(f"Files/DownUpload/{file_name}")
    assert file_path is not None  # Verify download
    context.close()

def test_frames(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/frames")
    frame = page.frame_locator("#frame1")  # frame by id
    print("text value--->",frame.locator("#sampleHeading").inner_text())

    page.goto("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_default")
    print("Text value w3--->",page.frame(name="iframeResult").locator("h1").inner_text())  # frame by name

    page.goto("https://the-internet.herokuapp.com/nested_frames")
    print("Total frames-->", len(page.frames))
    for frame in page.frames:
        print("name of herokupp frame-->", frame.name)
        print("url of herokupp frame-->", frame.url)

    parent = page.frame(name="frame-top")

    for child_frame in parent.child_frames:  # parent > child
        print("parent to child -->", child_frame)

    print("Index switch -->", parent.child_frames[0].url)

    child = page.frame(name="frame-middle")  # child > parent
    print("Child to parent -->", child.parent_frame)
    context.close()

def test_JSExecutor(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/text-box")
    print("Page title", page.evaluate("() => document.title"))
    print("Page url", page.evaluate("() => window.location.href"))
    print("Page width", page.evaluate("() => window.innerWidth"))
    print("Page handle", page.evaluate_handle("() => document.body"))

    page.mouse.wheel(0, 100)  # Scroll down using mouse
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")  # Scroll to bottom
    page.evaluate("window.scrollTo(0, 0)")  # Scroll to top
    page.locator("#submit").scroll_into_view_if_needed()  # Scroll until locator found
    username = page.locator("#userName")
    username.evaluate("(element) => element.value = 'Rohit'")  # Enter value
    print("Retrieved value-->",page.evaluate("() => document.querySelector('#userName').value"))
    submit = page.locator("#submit")
    submit.evaluate("(element) => element.click()")  # Click submit button
    context.close()