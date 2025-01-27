# GitHub Follow-Unfollow Bot

A basic GitHub automation tool for managing follow/unfollow actions using Selenium.

## Features

- Basic follow/unfollow automation
- Session management
- Browser automation
- Simple usage interface

## Requirements

- Selenium WebDriver
- Chrome browser
- Python 3.7+
- GitHub account

## Usage

```python
# Run from command line
python main.py
```

## How It Works

1. Initializes browser session
2. Logs into GitHub account
3. Performs follow/unfollow actions:
   - Finds target users
   - Executes follow/unfollow
   - Handles rate limits

## Differences from Other Versions

Compared to other versions in this repo:
- Simpler implementation than Github Bot 3.0
- No data persistence (vs github_bot_personal)
- Basic functionality only
- No API integration

## Limitations

- No data tracking
- Basic error handling
- UI-dependent
- Manual login required
- No configuration options

## Best Practices

- Monitor GitHub limits
- Use responsibly
- Keep WebDriver updated
- Regular testing

## Warning

⚠️ Follow GitHub's terms of service and rate limits
to avoid account restrictions. 