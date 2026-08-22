import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_upload_download(driver):
    driver.get("https://demoqa.com/upload-download")
    file_path = os.path.abspath("Files/DownUpload/UploadFile.jpeg")

    upload = driver.find_element(By.ID, "uploadFile")
    upload.send_keys(file_path)
    # driver.find_element(By.ID, "uploadFile").send_keys(f"{path1}\n{path2}")  # multi upload

    driver.find_element(By.ID, "downloadButton").click()  # download

def test_frames(driver):
    driver.get("https://demoqa.com/frames")
    frame = driver.find_element(By.ID, "frame1")    # frame by id
    driver.switch_to.frame(frame)
    print('text value-->', driver.find_element(By.ID, "sampleHeading").text)

    driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_default")
    driver.switch_to.frame("iframeResult")  # frame by name
    print('Text value w3-->', driver.find_element(By.TAG_NAME, "h1").text) 

    driver.get("https://the-internet.herokuapp.com/nested_frames")
    frames = driver.find_elements(By.TAG_NAME, "frame")
    print('Total frames->', len(frames))
    for frame in frames:
        print('name of herokuapp frame->', frame.get_attribute("name"))
        print('url of herokuapp frame->', frame.get_attribute("src"))
    driver.switch_to.frame('frame-top')
    child_frames = driver.find_elements(By.TAG_NAME, "frame")
    for child_frame in child_frames:
        frame_name = child_frame.get_attribute("name")
        driver.switch_to.frame(child_frame)
        print("Inside->", frame_name)
        driver.switch_to.parent_frame()

def test_JSExecutor(driver):
    driver.get("https://demoqa.com/text-box")
    print('Page title', driver.execute_script("return document.title"))
    print('Page url', driver.execute_script("return window.location.href"))
    print('Page width', driver.execute_script("return window.innerWidth"))

    driver.execute_script("window.scrollBy(0,100)")  # Scroll down using mouse
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Scroll to bottom
    driver.execute_script("window.scrollTo(0,0)")  # Scroll to top
    submit = driver.find_element(By.ID, "submit")  # scroll until locator found
    driver.execute_script("arguments[0].scrollIntoView(true);", submit)

    username = driver.find_element(By.ID, "userName")
    driver.execute_script("arguments[0].value='Rohit';",username)  # Enter value
    print("Retrieved value->",driver.execute_script("return document.querySelector('#userName').value"))
    driver.execute_script("arguments[0].click();", submit)  # Click submit button