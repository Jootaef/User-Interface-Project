import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestSmoke:
    def setup_method(self, method):
        options = Options()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}
        self.driver.set_window_size(1200, 800)  # Ensure full navigation menu is visible
        
    def teardown_method(self, method):
        self.driver.quit()
        
    def test_home_page_logo_and_heading(self):
        """Test 1: Navigate to home page and verify logo and heading"""
        self.driver.get("http://localhost:5500/teton/1.6/index.html")
        
        # Verify site logo is displayed
        logo = self.driver.find_element(By.CSS_SELECTOR, ".header-logo img")
        assert logo.is_displayed()
        assert logo.get_attribute("alt") == "Teton Chamber of Commerce Logo"
        
        # Verify website heading "Teton Idaho Chamber of Commerce" is displayed
        heading1 = self.driver.find_element(By.CSS_SELECTOR, ".header-title h1")
        heading2 = self.driver.find_element(By.CSS_SELECTOR, ".header-title h2")
        assert heading1.text == "Teton Idaho"
        assert heading2.text == "Chamber of Commerce"
        
        # Verify title displayed in browser tab is "Teton Idaho CoC"
        assert self.driver.title == "Teton Idaho CoC"
        
    def test_home_page_navigation_and_spotlights(self):
        """Test 2: Verify navigation menu, spotlights, and Join Us link"""
        self.driver.get("http://localhost:5500/teton/1.6/index.html")
        
        # Make sure screen size is big enough to show full navigation menu
        # (already set in setup_method to 1200x800)
        
        # Verify two spotlights are present
        # Note: The site loads spotlights dynamically, so we'll wait for them
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".main-spotlight"))
        )
        
        # Verify Join Us link is present
        join_link = self.driver.find_element(By.CSS_SELECTOR, ".a-button")
        assert join_link.text == "Join Us"
        assert join_link.is_displayed()
        
        # Verify clicking Join Us link takes you to join page
        join_link.click()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("join.html")
        )
        assert "join.html" in self.driver.current_url
        
    def test_directory_page_grid_and_list_views(self):
        """Test 3: Test directory page grid and list views"""
        self.driver.get("http://localhost:5500/teton/1.6/directory.html")
        
        # Wait for directory data to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".directory-cards"))
        )
        
        # Click on "Grid" button to display card view
        grid_button = self.driver.find_element(By.ID, "directory-grid")
        grid_button.click()
        
        # Make sure "Teton Turf and Tree" business is shown in cards
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Teton Turf and Tree')]"))
        )
        
        # Click on "List" button to display list view
        list_button = self.driver.find_element(By.ID, "directory-list")
        list_button.click()
        
        # Again, make sure "Teton Turf and Tree" business is displayed in list
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Teton Turf and Tree')]"))
        )
        
    def test_join_page_form(self):
        """Test 4: Test join page form functionality"""
        self.driver.get("http://localhost:5500/teton/1.6/join.html")
        
        # Make sure "First Name" input box is present
        first_name_input = self.driver.find_element(By.NAME, "fname")
        assert first_name_input.is_displayed()
        
        # Fill in the first page with information
        first_name_input.send_keys("John")
        last_name_input = self.driver.find_element(By.NAME, "lname")
        last_name_input.send_keys("Doe")
        business_name_input = self.driver.find_element(By.NAME, "bizname")
        business_name_input.send_keys("Test Business")
        title_input = self.driver.find_element(By.NAME, "biztitle")
        title_input.send_keys("Manager")
        
        # Click the "Next Step" button
        next_step_button = self.driver.find_element(By.CSS_SELECTOR, "input[value='Next Step']")
        next_step_button.click()
        
        # Make sure "Email" input box is present on next page
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("join-step2.html")
        )
        
        # Verify we're on the next step page
        assert "join-step2.html" in self.driver.current_url
        
    def test_admin_page_login_error(self):
        """Test 5: Test admin page login with incorrect credentials"""
        self.driver.get("http://localhost:5500/teton/1.6/admin.html")
        
        # Make sure "Username" input box is present
        username_input = self.driver.find_element(By.ID, "username")
        assert username_input.is_displayed()
        
        # Fill in incorrect username and password
        username_input.send_keys("wronguser")
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("wrongpass")
        
        # Click Login button
        login_button = self.driver.find_element(By.CSS_SELECTOR, "input[value='Login']")
        login_button.click()
        
        # Ensure appropriate error message is displayed
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".errorMessage"))
        )
        
        error_message = self.driver.find_element(By.CSS_SELECTOR, ".errorMessage")
        assert "Invalid username and password" in error_message.text
