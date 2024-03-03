import pytest
from playwright.sync_api import sync_playwright
from finalProject.cnn_modules.cnn_modules import Cnn


@pytest.fixture(scope="module")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()


def test_end_to_end_cnn(page):
    # 1.Go to "http://www.cnn.com"
    cnn = Cnn(page)
    cnn.cnn_goto()
    page.wait_for_load_state("load")
    assert page.url == "https://www.cnn.com/"
    cnn.assert_logo()

    # 2. Click "Log in" button
    # 3. Enter valid data into "Email address" field
    # 4. Enter valid data into "Password" field
    # 5. Press "Sign In" button
    cnn.log_in("cnntestmail@gmail.com", "cnntestmail1?")
    page.wait_for_timeout(5000)
    assert page.url == "https://www.cnn.com/account/log-in"
    cnn.log_in_sign_in()
    page.wait_for_timeout(2000)
    assert page.url == "https://www.cnn.com/"
    cnn.assert_logo()

    # 6. Click "World" button
    # 7. Click "Menu" button
    # 8. Click "Europe" button
    # 9. Click on "Russian invasion of Ukraine: Latest news, analysis and videos"
    # 10. Go back to main page by clicking on CNN icon
    cnn.read_russ_invasion()
    page.wait_for_selector('h1:has-text("Russian invasion of Ukraine")')
    headline_locator = page.locator('h1:has-text("Russian invasion of Ukraine")')
    assert headline_locator.is_visible()
    cnn.cnn_logo()

    # 11. Click on "Listen" button
    # 12. Click on play button near "CNN 5 Things"
    # 13. Wait to audio been played
    # 14. Go back to main page by clicking on CNN icon
    cnn.listen()
    page.wait_for_timeout(5000)
    assert "audio" in page.url
    cnn.cnn_logo_listen()
    assert page.url == "https://www.cnn.com/"

    # 15. Click "Watch" button
    # 16. Click "Play button" on first video
    # 17. Wait to video been played
    # 18. Go back to main page by clicking on CNN icon
    cnn.watch()
    page.wait_for_timeout(8000)
    assert "videos" in page.url
    cnn.cnn_logo_watch()
    assert page.url == "https://www.cnn.com/"

    # 19. Click on "Search" field
    # 20. Enter "Ukraine" in search field
    # 21. Press "Enter"
    # 22. Go back to main page by clicking on CNN icon
    cnn.cnn_search_ukraine()
    page.wait_for_load_state("load")
    assert page.url == "https://www.cnn.com/search?q=Ukraine"
    cnn.cnn_logo()
    assert page.url == "https://www.cnn.com/"
    page.wait_for_timeout(2000)

    # 23. Click on "Account" icon
    # 24. Click on "Log out" button
    cnn.cnn_log_out()
    page.wait_for_timeout(5000)