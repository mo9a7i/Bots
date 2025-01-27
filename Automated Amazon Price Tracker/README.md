# Amazon Price Tracker

A GUI-based automation tool that tracks Amazon product prices and alerts users when prices drop below specified thresholds.

## Features

- GUI interface for easy product tracking
- Price history tracking
- Price change percentage calculation
- Automated price checking
- Historical price data storage

## Requirements

- Selenium WebDriver
- Chrome browser
- Python Tkinter for GUI

## Usage

```python
python main.py
# GUI will launch automatically
```

## How It Works

1. Enter Amazon product URL
2. Set desired price threshold
3. System will:
   - Fetch current price
   - Compare with threshold
   - Calculate price change percentage
   - Store price history
   - Show price alerts

## Data Storage

- Prices stored in `data.json`
- Format:
```json
{
  "product_url": price_value
}
```

## Limitations

- Amazon's anti-bot measures may affect reliability
- Requires active Chrome session
- Price format changes may need updates
- Region-specific pricing may vary

## Error Handling

- Invalid URL detection
- Price format validation
- Connection error recovery
- Session management

## Best Practices

- Don't overuse to avoid IP blocking
- Verify product URLs before tracking
- Regular checks of stored data
- Keep Chrome WebDriver updated 