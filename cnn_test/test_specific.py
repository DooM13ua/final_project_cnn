import pytest
from playwright.sync_api import sync_playwright
from finalProject.cnn_modules.cnn_modules import Cnn


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()


def test_log_invalid_mail(page):
    """Attempt to log in with invalid email."""
    cnn = Cnn(page)
    # Launch the browser and navigate to "https://www.cnn.com"'.
    cnn.cnn_goto()
    page.wait_for_load_state("load")
    cnn.log_in("111", "cnntestmailsecond1?")
    cnn.log_in_sign_in()
    page.wait_for_timeout(2000)
    assert page.get_by_text("Please enter a valid email").is_visible()


def test_log_invalid_password(page):
    """Attempt to log in with invalid password."""
    cnn = Cnn(page)
    # Launch the browser and navigate to "https://www.cnn.com"'.
    cnn.cnn_goto()
    page.wait_for_load_state("load")
    # Press "log in" button
    # Enter "cnntestmail@gmail.com" in "Email address" field
    cnn.log_in("cnntestmailsecond@gmail.com", "asdf")
    cnn.log_in_sign_in()
    page.wait_for_timeout(2000)
    assert page.locator('.icon-ui-error-circle-fill').is_visible()


def test_new_user_invalid_mail(page):
    cnn = Cnn(page)
    # Launch the browser and navigate to "https://www.cnn.com"'.
    cnn.cnn_goto()
    page.wait_for_load_state("load")
    # Click on "Log in" button
    cnn.log_in_page()
    # Click on "Sign up" button
    page.get_by_role("link", name="Sign up.").click()
    page.get_by_placeholder("Email address").click()
    page.get_by_placeholder("Email address").fill("asdfgh@zfxgvbn")
    page.get_by_placeholder("Password").click()
    page.wait_for_timeout(2000)
    assert page.locator('.icon-ui-error-circle-fill').is_visible()


def test_search_invalid(page):
    cnn = Cnn(page)
    # Launch the browser and navigate to "https://www.cnn.com"'.
    cnn.cnn_goto()
    page.wait_for_load_state("load")
    # Click on "Search" button
    # Enter invalid data "!@#IU!Y%@"
    # Press "Enter"
    cnn.cnn_search("!@#IU!Y%@")
    page.wait_for_timeout(2000)
    assert page.get_by_text("0 results has been found").is_visible()
