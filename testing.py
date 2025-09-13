from selenium import webdriver
from selenium.webdriver.common.by import By
import time


test_data = [
    {"username": "student", "password": "Password123", "expected": "pass"},
    {"username": "student", "password": "wrongpass", "expected": "fail"},
    {"username": "wronguser", "password": "Password123", "expected": "fail"},
    {"username": "", "password": "Password123", "expected": "fail"},
    {"username": "student", "password": "", "expected": "fail"},
]


driver = webdriver.Chrome()
driver.maximize_window()


for data in test_data:
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(1)

    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(data["username"])
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(data["password"])
    driver.find_element(By.ID, "submit").click()
    time.sleep(1)

    
    try:
        if data["expected"] == "pass":
            message = driver.find_element(By.TAG_NAME, "h1").text
            assert "Logged In Successfully" in message
            print(f"✅ Test Passed for {data['username']} | Expected: PASS")
        else:
            error_message = driver.find_element(By.ID, "error").text
            assert "Your username is invalid!" in error_message or "Your password is invalid!" in error_message
            print(f"❌✅ Test Passed for {data['username']} | Expected: FAIL")
    except:
        print(f"❌ Test Failed for {data['username']} | Expected: {data['expected'].upper()}")

driver.quit()
