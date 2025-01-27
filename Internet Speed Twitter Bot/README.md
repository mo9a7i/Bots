# Internet Speed Twitter Bot

An automated tool that tests your internet speed and tweets at your ISP when speeds are below promised levels.

## Features

- Automated speed testing using speedtest.net
- Twitter integration for automated complaints
- GUI interface for credentials
- Measures:
  - Download speed (Mbps)
  - Upload speed (Mbps)
  - Ping (ms)

## Requirements

- Selenium WebDriver
- Chrome browser
- Twitter account
- Python Tkinter for GUI

## Configuration

```python
# Run from command line
python main.py
# GUI will launch for credentials
```

## How It Works

1. Enter Twitter credentials in GUI
2. Bot automatically:
    - Runs speed test
    - Captures results
    - Formats tweet
    - Posts to Twitter

## Speed Test Process

- Connects to speedtest.net
- Initiates speed test
- Waits 60 seconds for completion
- Extracts results:
  ```python
  self.upload_speed = float(upload.text)
  self.download_speed = float(download.text)
  self.ping = int(ping.text)
  ```

## Limitations

- Requires stable internet connection
- Twitter API rate limits
- Speed test duration (~1 minute)
- Browser automation dependencies

## Security Notes

- Store credentials securely
- Use environment variables when possible
- Never commit credentials to version control

## Error Handling

- Connection failure recovery
- Twitter login validation
- Speed test timeout handling
- GUI input validation 