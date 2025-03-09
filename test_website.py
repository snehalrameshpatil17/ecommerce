from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import matplotlib.pyplot as plt
import time

# Set up WebDriver using Service class
service = Service(r"C:\Users\91886\Documents\ecommerce\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Tracking test results
test_results = {
    "Test Case 1": {"description": "Homepage title verification", "status": None},
    "Test Case 2": {"description": "Check products section visibility", "status": None},
    "Test Case 3": {"description": "Verify product details", "status": None},
    "Test Case 4": {"description": "Navigate to login page", "status": None},
    "Test Case 5": {"description": "Fill and submit login form", "status": None},
    "Test Case 6": {"description": "Navigate to signup page", "status": None},
    "Test Case 7": {"description": "Fill and submit signup form", "status": None},
}

try:
    # Test Case 1: Open the homepage and verify title
    driver.get("file:///C:/Users/91886/Documents/ecommerce/index.html")
    assert "Online Shopping Website" in driver.title
    print("Homepage title verified successfully!")
    test_results["Test Case 1"]["status"] = "Pass"

    # Test Case 2: Check product section is displayed
    products_section = driver.find_element(By.CLASS_NAME, "products")
    assert products_section.is_displayed()
    print("Products section is visible!")
    test_results["Test Case 2"]["status"] = "Pass"

    # Test Case 3: Verify product details
    product_elements = driver.find_elements(By.CLASS_NAME, "product")
    assert len(product_elements) > 0, "No products found!"

    for product in product_elements:
        product_name = product.find_element(By.TAG_NAME, "h3").text
        product_price = product.find_element(By.TAG_NAME, "p").text
        print(f"Product Found: {product_name} - {product_price}")
    test_results["Test Case 3"]["status"] = "Pass"

    # Test Case 4: Navigate to login page
    login_link = driver.find_element(By.LINK_TEXT, "Login")
    login_link.click()
    time.sleep(8)
    assert "Login - Your Shop Hub" in driver.title
    print("Login page title verified successfully!")
    test_results["Test Case 4"]["status"] = "Pass"

    # Test Case 5: Fill login form
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.TAG_NAME, "button")

    username_input.send_keys("testuser")
    password_input.send_keys("testpassword")
    print("Login form filled successfully!")

    login_button.click()
    print("Login form submitted!")
    time.sleep(8)
    test_results["Test Case 5"]["status"] = "Pass"

    # Test Case 6: Navigate to signup page
    signup_link = driver.find_element(By.LINK_TEXT, "Signup")
    signup_link.click()
    time.sleep(8)
    assert "Signup - Your Shop Hub" in driver.title
    print("Signup page title verified successfully!")
    test_results["Test Case 6"]["status"] = "Pass"

    # Test Case 7: Fill signup form
    username_input = driver.find_element(By.ID, "username")
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    signup_button = driver.find_element(By.TAG_NAME, "button")

    username_input.send_keys("newuser")
    email_input.send_keys("newuser@example.com")
    password_input.send_keys("securepassword")
    print("Signup form filled successfully!")

    signup_button.click()
    print("Signup form submitted!")
    time.sleep(5)
    test_results["Test Case 7"]["status"] = "Pass"

except AssertionError as e:
    print(f"Assertion Error: {e}")
    # Mark failed test case
    for test_case, result in test_results.items():
        if result["status"] is None:
            result["status"] = "Fail"
finally:
    # Close the browser
    driver.quit()
    print("Test Completed and Browser Closed.")

# Visualization
# Prepare data for visualization
test_case_names = list(test_results.keys())
test_case_statuses = [1 if result["status"] == "Pass" else 0 for result in test_results.values()]
passed_count = sum(test_case_statuses)
failed_count = len(test_case_statuses) - passed_count

# Bar Graph: Test Results
plt.figure(figsize=(10, 6))
plt.bar(test_case_names, test_case_statuses, color=["green" if status == 1 else "red" for status in test_case_statuses])
plt.title("Test Case Results")
plt.ylabel("Status (1=Pass, 0=Fail)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Pie Chart: Pass/Fail Distribution
plt.figure(figsize=(8, 8))
plt.pie([passed_count, failed_count], labels=["Passed", "Failed"], autopct='%1.1f%%', colors=["green", "red"])
plt.title("Pass/Fail Distribution")
plt.show()

# Line Chart: Test Case Execution
plt.figure(figsize=(10, 6))
plt.plot(test_case_names, test_case_statuses, marker="o", color="blue", label="Test Execution")
plt.title("Test Case Execution Timeline")
plt.ylabel("Status (1=Pass, 0=Fail)")
plt.xticks(rotation=45, ha="right")
plt.legend()
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Update test results with detailed failure status (manually or programmatically captured).
test_results = {
    "Test Case 1": {"description": "Homepage title verification", "status": "Pass"},
    "Test Case 2": {"description": "Check products section visibility", "status": "Pass"},
    "Test Case 3": {"description": "Verify product details", "status": "Pass"},
    "Test Case 4": {"description": "Navigate to login page", "status": "Pass"},
    "Test Case 5": {"description": "Fill and submit login form", "status": "Pass"},
    "Test Case 6": {"description": "Navigate to signup page", "status": "Fail", "reason": "Page title mismatch"},
    "Test Case 7": {"description": "Fill and submit signup form", "status": "Pass"},
}

# Prepare data for visualization
test_case_names = list(test_results.keys())
test_case_statuses = [1 if result["status"] == "Pass" else 0 for result in test_results.values()]
failure_reasons = [result.get("reason", "") if result["status"] == "Fail" else None for result in test_results.values()]

# Passed and Failed Counts
passed_count = test_case_statuses.count(1)
failed_count = test_case_statuses.count(0)

# Bar Graph: Test Results
plt.figure(figsize=(12, 6))
colors = ["green" if status == 1 else "red" for status in test_case_statuses]
plt.bar(test_case_names, test_case_statuses, color=colors)
plt.title("Test Case Results (Bar Graph)")
plt.ylabel("Status (1=Pass, 0=Fail)")
plt.xticks(rotation=45, ha="right")

# Annotate failed test cases
for i, reason in enumerate(failure_reasons):
    if reason:
        plt.text(i, 0.1, f"Fail: {reason}", ha="center", color="black", fontsize=8)

plt.tight_layout()
plt.show()

# Pie Chart: Pass/Fail Distribution
plt.figure(figsize=(8, 8))
plt.pie([passed_count, failed_count], labels=["Passed", "Failed"], autopct='%1.1f%%', colors=["green", "red"])
plt.title("Pass/Fail Distribution")
plt.show()

# Line Chart: Test Case Execution
plt.figure(figsize=(12, 6))
plt.plot(test_case_names, test_case_statuses, marker="o", color="blue", label="Test Execution")
plt.title("Test Case Execution Timeline (Line Chart)")
plt.ylabel("Status (1=Pass, 0=Fail)")
plt.xticks(rotation=45, ha="right")

# Highlight failures in the timeline
for i, reason in enumerate(failure_reasons):
    if reason:
        plt.annotate(f"Fail: {reason}", (i, 0), textcoords="offset points", xytext=(-15, -25), ha="center", color="red")

plt.legend()
plt.tight_layout()
plt.show()

