# Stock Trading News Alert System

An automated system that monitors stock prices and sends email alerts with relevant news when significant price changes occur.

## Features

- Real-time stock price monitoring
- News article aggregation for monitored stocks
- Email alerts for price movements
- Industry/category-based stock tracking
- Customizable price change thresholds

## Configuration

Required environment variables:
```bash
STOCK_API_KEY=your_alphavantage_key
NEWS_API_KEY=your_newsapi_key
EMAIL_PASSWORD=your_app_password
```

## Usage

First set required environment variables:
```bash
export STOCK_API_KEY="your_alphavantage_key"
export NEWS_API_KEY="your_newsapi_key"
export EMAIL_PASSWORD="your_app_password"
```

```python
# Run from command line
python main.py

# Available commands in interactive mode:
# - show_categories() : Display all stock categories
# - check_industry("Tech") : Check specific industry
# - check_all() : Monitor all stocks
```

## Email Setup

1. Create an app password in Google Account settings
2. Use the 16-character password in environment variables
3. Configure sender and recipient emails in the code

## Supported Features

- Multiple industry tracking
- Customizable alert thresholds
- Relevant news article filtering
- Price change percentage calculation
- Historical price comparison

## Limitations

- API rate limits apply
- Limited to publicly available stock data
- News API article count restrictions
- Email provider restrictions

## Error Handling

- API failure recovery
- Invalid stock symbol handling
- Email sending retry mechanism
- Data validation checks 