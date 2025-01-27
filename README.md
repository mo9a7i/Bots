# Python Automation Tools Collection

A collection of Python automation scripts for various web services and applications using Selenium and API integrations.

## Overview

This repository contains several automation tools:

- GitHub Bot (3 versions)
- Stock Trading News Alert System
- Amazon Price Tracker
- Internet Speed Twitter Bot
- Tinder Bot
- Cookie Clicker Bot
- Lab Report Signup Bot

## Requirements

- Python 3.7+
- Chrome WebDriver
- Required Python packages:
  ```bash
  pip install selenium beautifulsoup4 requests python-dotenv
  ```

## Project Structure

```
.
├── Github Bot 3.0/               # GitHub API-based follower bot
├── github_bot_personal/         # Selenium-based GitHub bot
├── Github Follow-Unfollow Bot/  # Basic GitHub follow/unfollow bot
├── Stock Trading News Alert/    # Stock price monitoring system
├── Automated Amazon Price Tracker/ # Amazon price monitoring
├── Internet Speed Twitter Bot/  # Internet speed test tweeting bot
├── Tinder Like-Reject Bot/      # Tinder automation
├── Cookie Clicker/             # Cookie Clicker game bot
└── London App Brewery Lab Report/ # Lab report signup automation
```

## Environment Variables

Create a `.env` file with:

```bash
# GitHub Bots
GITHUB_TOKEN=your_github_token
GITHUB_EMAIL=your_email
GITHUB_PASSWORD=your_password

# Stock Trading
ALPHA_VANTAGE_KEY=your_key
NEWS_API_KEY=your_key

# Twitter Bot
TWITTER_USERNAME=your_username
TWITTER_PASSWORD=your_password

# Email Settings (for alerts)
SMTP_EMAIL=your_email
SMTP_PASSWORD=your_app_password
```

## Security Notice

⚠️ Never commit sensitive credentials to version control
- Use environment variables for all sensitive data
- Store credentials securely
- Follow API rate limits and terms of service

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Open a Pull Request

## License

MIT License - See LICENSE file for details 