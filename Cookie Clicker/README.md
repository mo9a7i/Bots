# Cookie Clicker Bot

An automated bot for the Cookie Clicker browser game that optimizes cookie production and upgrades.

## Features

- Automated cookie clicking
- Product purchase optimization
- Dynamic scrolling for new items
- Configurable time intervals
- Cookie count tracking

## Requirements

- Selenium WebDriver
- Chrome browser
- Python 3.7+

## Usage

The default clicking interval is 5 seconds.
You can modify the interval in main.py:
```python
time_interval = 5  # Recommended: 45 seconds
```

```python
# Run from command line
python main.py
```

## How It Works

1. Launches Cookie Clicker game
2. Continuously clicks cookie
3. Monitors available products:
   ```python
   cookie_button = self.google_driver.find_element(By.ID, "bigCookie")
   products = self.google_driver.find_elements(By.CLASS_NAME, "price")
   ```
4. Handles new product discovery
5. Manages scrolling for visibility

## Configuration

- Default interval: 5 seconds
- Recommended interval: 45 seconds
- Adjustable through `play()` parameter

## Features

- Automatic cookie clicking
- Price conversion handling
- Dynamic product discovery
- Scroll management
- Cookie count tracking

## Limitations

- Browser resource usage
- Game updates may break functionality
- No strategy optimization
- Single-session only

## Best Practices

- Monitor system resources
- Adjust intervals as needed
- Regular cookie count checks
- Keep WebDriver updated 