import pytest
from playwright.sync_api import sync_playwright
from finalProject.cnn_modules.cnn_modules import Cnn


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


def test_new_username(page):
    """Attempt to change username."""
    cnn = Cnn(page)
    # Launch the browser and navigate to "https://www.cnn.com"'.
    cnn.cnn_goto()
    page.wait_for_load_state("load")
    # Log in
    cnn.log_in("cnntestmail@gmail.com", "cnntestmail1?")
    page.wait_for_timeout(2000)
    assert page.url == "https://www.cnn.com/account/log-in"
    cnn.log_in_sign_in()
    # Click on account/settings button
    cnn.account_settings()
    assert "settings" in page.url
    header_element = page.locator("#settings-header")
    assert header_element.inner_text() == "\n            Your account\n        "
    # Click on "Edit" button near "Display name" name field
    cnn.page.get_by_role("button", name="Edit").first.click()
    # Enter new name
    cnn.edit_new_name("Bohdan 3")
    status_element = page.locator(".user-account-settings__inline-field-status")
    assert status_element.inner_text() == "IN REVIEW"
    assert header_element.inner_text() == "\n            Your account\n        "


def test_new_location(page):
    """Attempt to change location."""
    cnn = Cnn(page)
    # Launch the browser and navigate to "https://www.cnn.com"'.
    cnn.cnn_goto()
    page.wait_for_load_state("load")
    # Log in
    cnn.log_in("cnntestmail@gmail.com", "cnntestmail1?")
    page.wait_for_timeout(2000)
    assert page.url == "https://www.cnn.com/account/log-in"
    cnn.log_in_sign_in()
    # Click on account/settings button
    cnn.account_settings()
    assert "settings" in page.url
    header_element = page.locator("#settings-header")
    assert header_element.inner_text() == "\n            Your account\n        "
    # Click on "Edit" button near "Zip Code"
    cnn.page.get_by_role("button", name="Edit").first.click()
    # Enter new location
    cnn.edit_new_location("16888")
    assert page.get_by_text("Saved!").is_visible()
    assert header_element.inner_text() == "\n            Your account\n        "


def test_log_invalid_mail(page):
    """Attempt to log in with invalid email."""
    cnn = Cnn(page)
    # Launch the browser and navigate to "https://www.cnn.com"'.
    cnn.cnn_goto()
    page.wait_for_load_state("load")
    cnn.log_in("cnntestmailnew@gmail.com", "cnntestmail1?")
    assert page.locator('p.feedback-message__text').inner_text() == "You have entered an invalid username or password"


def test_log_invalid_password(page):
    """Attempt to log in with invalid password."""
    cnn = Cnn(page)
    # Launch the browser and navigate to "https://www.cnn.com"'.
    cnn.cnn_goto()
    page.wait_for_load_state("load")
    # Press "log in" button
    # Enter "cnntestmail@gmail.com" in "Email address" field
    cnn.log_in("cnntestmailnew@gmail.com", "asdf")
    assert page.locator('p.feedback-message__text').inner_text() == "You have entered an invalid username or password"


def test_new_user(page):
    cnn = Cnn(page)
    # Launch the browser and navigate to "https://www.cnn.com"'.
    cnn.cnn_goto()
    page.wait_for_load_state("load")
    page.locator("#pageHeader").get_by_role("link", name="User Account Log In Button").click()
    page.get_by_role("link", name="Sign up.").click()
    page.get_by_placeholder("Email address").fill("kjfkjv@gmail.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("asd123321")
    page.get_by_role("button", name="Create Account").click()
    assert page.get_by_text("Your free CNN account has").is_visible()