# 🖥️ Login Automation Testing with Selenium (Python)

## 📌 Project Description  
This project demonstrates a **beginner-friendly automation testing framework** using **Selenium WebDriver with Python**.  
It focuses on **data-driven testing** of a login page using multiple combinations of usernames and passwords.  

The script automatically:  
- Opens a browser  
- Navigates to the login page  
- Enters usernames and passwords from a test dataset  
- Verifies whether login is successful or fails  
- Prints test results (✅ Pass / ❌ Fail) for each test case  
- Closes the browser after execution  

This project is a great starting point for anyone learning **manual-to-automation testing migration** and **Selenium basics**.

---

## 🎯 Features  
✅ Automates login testing for multiple data sets  
✅ Data-driven testing using Python list/dictionaries (easy to expand)  
✅ Verifies both valid and invalid login scenarios  
✅ Simple console output for test results  
✅ Beginner-friendly, easy to customize  

---

## 🛠️ Tech Stack  
- **Language:** Python  
- **Automation Tool:** Selenium WebDriver  
- **Browser:** Chrome (can be modified for Firefox/Edge)  

---

## 📂 Project Structure  
📁 selenium-login-automation
- ┣ 📜 login_test.py # Main script with data-driven test cases
- ┣ 📜 requirements.txt # Project dependencies (selenium)
- ┗ 📄 README.md # Project documentation (this file)


---

## 🚀 Getting Started  

### 1️⃣ Install Dependencies  
```bash
pip install selenium
```

2️⃣ Run the Script
```bash
python testing.py
```

## 🧪 Sample Output
- ✅ Test Passed for student | Expected: PASS
- ✅ Test Passed for student | Expected: FAIL
- ✅ Test Passed for wronguser | Expected: FAIL
- ✅ Test Passed for  | Expected: FAIL
- ✅ Test Passed for student | Expected: FAIL
