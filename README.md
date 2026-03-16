# QA Automation Tools

Python scripts for automated UI testing and web quality assurance.

---

## Scripts

### Form_test.py — Login Form Validation
Tests a login form end-to-end by simulating a real user interaction.

**What it does:**
- Opens a login page in Chrome automatically
- Fills in username and password fields
- Clicks the submit button
- Validates that the correct error message appears for invalid credentials

---

### Health_check.py — UI Health Audit
Automated audit tool that checks the general health of any webpage.

**What it does:**
- Measures page load time
- Detects the page title
- Searches for specific text on the page
- Counts key HTML elements
- Generates a full status report

---

### LoginCheck_AutoReport.py — Login Test with Auto Excel Report
Advanced login form validator that tests each UI element individually
and generates a formatted Excel report automatically.

**What it does:**
- Validates each login element separately (username, password, button)
- Exports results to a color-coded Excel file (green = PASSED, red = FAILED)
- Handles 3 result states: PASSED, FAILED, and CRITICAL
- Appends new results to the same report on each run (historical log)
## Tech Stack

| Python | 
| Selenium WebDriver |
| webdriver-manager |

---

## Installation
pip install selenium webdriver-manager
pip install pandas openpyxl

## Author

**Oscar Santos** — QA Tester & Python Developer  
[LinkedIn](https://linkedin.com/in/oscar-santos-9a9a64389) · [Fiverr](https://www.fiverr.com/exsauscripts)
