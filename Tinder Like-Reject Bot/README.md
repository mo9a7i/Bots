# Tinder Like-Reject Bot

An automated Selenium-based bot that handles Tinder profile interactions within daily limits.

## Features

- Automated profile liking
- Respects Tinder's daily limit (50 likes)
- Browser automation
- Session management

## Requirements

- Selenium WebDriver
- Chrome browser
- Valid Tinder account
- Python 3.7+

## Usage

```python
# Run from command line
python main.py
```

## How It Works

1. Launches automated Chrome session
2. Logs into Tinder account
3. Processes profiles within limits:
   - Finds like button
   - Performs like action
   - Handles popups/notifications
   - Tracks interaction count

## Limitations

- 50 likes per day (Tinder limit)
- Requires manual login first time
- May break with Tinder UI updates
- No profile analysis/filtering

## Safety Features

- Built-in daily limit enforcement
- Session timeout handling
- Error recovery
- Rate limiting

## Best Practices

- Use responsibly within Tinder's terms
- Don't exceed daily limits
- Monitor bot behavior
- Keep WebDriver updated

## Warning

⚠️ Use of automation tools may violate Tinder's terms of service.
Use at your own risk and be aware of potential account restrictions. 