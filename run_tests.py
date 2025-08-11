#!/usr/bin/env python3
"""
Test runner script for CSE 270 Smoke Tests
This script helps run the smoke tests locally with proper setup.
"""

import subprocess
import sys
import os
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import selenium
        import pytest
        print(f"✓ Selenium {selenium.__version__} is installed")
        print(f"✓ Pytest is available")
        return True
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def check_website_files():
    """Check if the website files are present."""
    website_path = Path("teton/1.6/index.html")
    if website_path.exists():
        print("✓ Website files found")
        return True
    else:
        print("✗ Website files not found at teton/1.6/index.html")
        print("Please ensure the Teton v1.6 website files are in the teton/1.6/ directory")
        return False

def run_tests():
    """Run the smoke tests."""
    print("\n🚀 Running Smoke Tests...")
    
    # Change to tests directory
    os.chdir("tests")
    
    try:
        # Run pytest with verbose output
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "test_smoke.py", "-v", "--tb=short"
        ], capture_output=False)
        
        if result.returncode == 0:
            print("\n✅ All tests passed!")
        else:
            print(f"\n❌ Tests failed with exit code {result.returncode}")
            
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return False
    
    return result.returncode == 0

def main():
    """Main function."""
    print("CSE 270 Smoke Test Runner")
    print("=" * 40)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check website files
    if not check_website_files():
        sys.exit(1)
    
    # Check if we're in the right directory
    if not Path("tests").exists():
        print("✗ Tests directory not found")
        print("Please run this script from the project root directory")
        sys.exit(1)
    
    print("\n📋 Prerequisites check passed!")
    print("\n⚠️  IMPORTANT: Make sure you have a web server running on port 5500")
    print("   - Use VS Code Live Server extension, or")
    print("   - Run: python -m http.server 5500")
    print()
    
    # Ask user if they want to continue
    response = input("Continue with running tests? (y/N): ").strip().lower()
    if response not in ['y', 'yes']:
        print("Tests cancelled.")
        sys.exit(0)
    
    # Run tests
    success = run_tests()
    
    if success:
        print("\n🎉 Test run completed successfully!")
        print("You can now commit your changes to trigger the CI/CD pipeline.")
    else:
        print("\n💡 Some tests failed. Check the output above for details.")
        print("Fix any issues and run the tests again.")

if __name__ == "__main__":
    main()
