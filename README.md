# CSE 270 Smoke Tests

This repository contains automated smoke tests for the Teton Idaho Chamber of Commerce website (v1.6).

## Test Coverage

The smoke test suite covers the following functionality:

1. **Home Page Verification**
   - Site logo display
   - Website heading "Teton Idaho Chamber of Commerce"
   - Browser tab title "Teton Idaho CoC"

2. **Navigation and UI Elements**
   - Full navigation menu visibility
   - Two spotlights presence
   - Join Us link functionality

3. **Directory Page**
   - Grid view functionality
   - List view functionality
   - Business data display (specifically "Teton Turf and Tree")

4. **Join Page**
   - Form input validation
   - Multi-step form navigation

5. **Admin Page**
   - Login form presence
   - Error handling for invalid credentials

## Prerequisites

- Python 3.8 or higher
- Chrome browser installed
- Chrome WebDriver (will be automatically managed by Selenium)

## Installation

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Ensure the Teton v1.6 website files are in the `teton/1.6/` directory.

## Running Tests

### Local Development

1. Start a local web server on port 5500:
   - Use VS Code Live Server extension
   - Or use Python's built-in server: `python -m http.server 5500`

2. Run the smoke tests:
   ```bash
   cd tests
   pytest test_smoke.py -v
   ```

### CI/CD Pipeline

The tests are configured to run automatically in the GitHub Actions pipeline on port 5500.

## Test Structure

- **test_home_page_logo_and_heading**: Verifies basic page elements and title
- **test_home_page_navigation_and_spotlights**: Tests navigation and dynamic content
- **test_directory_page_grid_and_list_views**: Tests directory view switching
- **test_join_page_form**: Tests form functionality and navigation
- **test_admin_page_login_error**: Tests error handling

## Configuration

- Tests run in headless mode for CI/CD compatibility
- Window size is set to 1200x800 to ensure full navigation menu visibility
- All tests use explicit waits for dynamic content loading

## Troubleshooting

- Ensure Chrome browser is installed
- Verify the web server is running on port 5500
- Check that all website files are present in the teton/1.6/ directory

## Files

- `tests/test_smoke.py` - Main test suite
- `requirements.txt` - Python dependencies
- `pytest.ini` - Pytest configuration
- `.github/workflows/main.yml` - CI/CD pipeline configuration
