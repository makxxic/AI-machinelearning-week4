# test_login_ai.py
# Automated login testing using Selenium WebDriver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome WebDriver (ensure chromedriver is in PATH)
driver = webdriver.Chrome()

# Base URL
driver.get("https://example-login-page.com")  # Replace with actual URL
driver.maximize_window()

def login_test(username, password, expected):
    # Locate username and password fields
    user_field = driver.find_element(By.ID, "username")
    pass_field = driver.find_element(By.ID, "password")

    # Clear old text and input new credentials
    user_field.clear()
    pass_field.clear()
    user_field.send_keys(username)
    pass_field.send_keys(password)
    pass_field.send_keys(Keys.RETURN)
    time.sleep(2)

    # Capture result (AI plugin can automatically detect dynamic messages)
    if expected in driver.page_source:
        print(f"✅ Test Passed for: {username}")
    else:
        print(f"❌ Test Failed for: {username}")

# Run tests
login_test("valid_user", "correct_pass", "Welcome")
login_test("invalid_user", "wrong_pass", "Invalid credentials")

driver.quit()
