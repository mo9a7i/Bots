# Personal GitHub Bot

A Selenium-based GitHub automation tool for managing follows/unfollows with persistent data storage.

## Features

- Automated GitHub following/unfollowing
- JSON-based data persistence
- Follow date tracking
- Session management

## Requirements

- Selenium WebDriver
- Chrome browser
- Python 3.7+
- GitHub account

## Data Storage

Uses `following.json` to track followed accounts:
```json
{
  "username": {
    "day": 9,
    "month": 8,
    "year": 2023
  }
}
```

## Usage

```python
# Run from command line
python main.py
```

## Features

- Follow date tracking
- Automated browser control
- JSON data persistence
- Session management

## Limitations

- GitHub rate limits
- UI-dependent automation
- Single account support
- Manual login required

## Best Practices

- Regular data backups
- Monitor follow limits
- Respect GitHub TOS
- Keep WebDriver updated 