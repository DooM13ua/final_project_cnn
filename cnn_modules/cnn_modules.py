class Cnn:
    def __init__(self, page):
        self.page = page

    def cnn_goto(self):
        """Go to http://www.cnn.com."""
        url = "https://www.cnn.com/"
        self.page.goto(url)

    def assert_logo(self):
        """Check if page header 'CNN logo' present."""
        assert self.page.locator("#pageheader").get_by_role("link", name="CNN logo")

    def log_in_page(self):
        """Go to 'Log in' page"""
        self.page.locator("#pageHeader").get_by_role("link", name="User Account Log In Button").click()

    def log_in_mail(self, log_in):
        """Enter log in data into 'Email address' field."""
        self.page.get_by_placeholder("Email address").click()
        self.page.get_by_placeholder("Email address").fill(log_in)

    def log_in_password(self, password):
        """Enter log in data into 'Password' field."""
        self.page.get_by_placeholder("Password").click()
        self.page.get_by_placeholder("Password").fill(password)

    def log_in_sign_in(self):
        """Press 'Sign in' button."""
        self.page.get_by_role("button", name="Sign in").click()

    def header_world(self):
        """Click on 'World' section."""
        self.page.locator("#pageHeader").get_by_role("link", name="World").click()

    def header_menu(self):
        """Click on 'Menu' section."""
        self.page.get_by_label("Open Menu Icon").click()

    def news_europe(self):
        """Click on 'Europe' section."""
        self.page.goto("https://www.cnn.com/world/europe")

    def russ_invasion(self):
        """Click on 'Russian invasion of Ukraine' article."""
        self.page.get_by_role("link", name="Russian invasion of Ukraine:").click()

    def cnn_logo(self):
        """Click on 'CNN logo' button."""
        self.page.locator("#pageHeader").get_by_role("link", name="CNN logo").click()

    def cnn_logo_listen(self):
        """Click on 'CNN' button."""
        self.page.get_by_role("link", name="CNN", exact=True).click()

    def cnn_logo_watch(self):
        """Click on 'CNN' button."""
        self.page.locator("#header-nav-container").get_by_label("CNN", exact=True).click()

    def cnn_listen(self):
        """Go to CNN 'Listen'."""
        self.page.locator("#pageHeader").get_by_role("link", name="Listen").click()

    def cnn_watch(self):
        """Go to CNN 'Watch'."""
        self.page.locator("#pageHeader").get_by_role("link", name="Watch").click()

    def cnn_listen_play(self):
        """Click on play button at CNN 'Listen'."""
        self.page.locator("audio-player-wc #playpause").click()

    def cnn_watch_play(self):
        """Click on play button at CNN 'Watch'."""
        self.page.get_by_role("button", name="Play").click()

    def cnn_search_button(self):
        """Go to 'Search'."""
        self. page.get_by_label("Search Icon").click()

    def cnn_account_button(self):
        """Click on 'account' button."""
        self.page.locator("#pageHeader").get_by_role("button", name="User Account Nav Button").click()

    def log_in(self, log_in, password):
        """Full log in process for end-to-end testing."""
        self.log_in_page()
        self.log_in_mail(log_in)
        self.log_in_password(password)

    def read_russ_invasion(self):
        """Go to 'Russian Invasion' article."""
        self.header_world()
        self.header_menu()
        self.news_europe()
        self.russ_invasion()

    def listen(self):
        """Play audio."""
        self.cnn_listen()
        self.cnn_listen_play()

    def watch(self):
        """Play video."""
        self.cnn_watch()
        self.cnn_watch_play()

    def cnn_search_ukraine(self):
        """Search for 'Ukraine' news."""
        self.page.get_by_label("Search Icon").click()
        self.page.locator("#pageHeader").get_by_placeholder("Search CNN...").click()
        self.page.locator("#pageHeader").get_by_placeholder("Search CNN...").fill("Ukraine")
        self.page.locator("#pageHeader").get_by_placeholder("Search CNN...").press("Enter")

    def cnn_log_out(self):
        """Log out form cnn.com."""
        self.cnn_account_button()
        self.page.get_by_role("link", name="Log Out").click()

    def account_settings(self):
        """Click account/settings button."""
        self.cnn_account_button()
        self.page.get_by_role("link", name="Settings", exact=True).click()

    def edit_new_name(self, new_name):
        """Edit username"""
        self.page.get_by_placeholder("Display name", exact=True).click()
        self.page.get_by_placeholder("Display name", exact=True).fill(new_name)
        self.page.get_by_placeholder("Display name", exact=True).press("Enter")
        self.page.get_by_role("button", name="Request display name").click()
        self.page.get_by_role("button", name="Go to settings").click()

    def edit_new_location(self, new_location):
        self.page.get_by_role("main").locator("section").filter(has_text="Location Manage your location").get_by_role("button").click()
        self.page.get_by_placeholder("optional").click()
        self.page.get_by_placeholder("optional").fill(new_location)
        self.page.get_by_placeholder("optional").press("Enter")
        self.page.get_by_role("button", name="Save").click()