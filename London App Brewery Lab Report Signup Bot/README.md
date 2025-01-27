# Lab Report Signup Bot

A simple automation tool for signing up to the London App Brewery Lab Report system.

## Features

- Automated form filling
- Single-click signup
- Chrome browser automation
- Form validation handling

## Requirements

- Selenium WebDriver
- Chrome browser
- Python 3.7+

## Usage

First edit credentials in main.py:
```python
name = "Your Name"
surname = "Your Surname"
email = "your.email@example.com"
```

```python
# Edit credentials in main.py first
python main.py
```

## How It Works

1. Launches signup page
2. Locates form elements:
   ```python
   name_entry = self.chrome.find_element(By.NAME, "fName")
   surname_entry = self.chrome.find_element(By.NAME, "lName")
   email_entry = self.chrome.find_element(By.NAME, "email")
   ```
3. Fills in provided information
4. Submits form automatically

## Limitations

- Single-use signup only
- No error handling
- Fixed form structure dependency
- No verification step

## Best Practices

- Verify form submission
- Keep credentials secure
- Update WebDriver regularly
- Check for site changes 