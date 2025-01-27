# GitHub Bot 3.0

An advanced GitHub automation bot using the GitHub API for following/unfollowing users and data collection.

## Features

- Automated following/unfollowing based on configurable rules
- Data collection on user profiles
- Blacklist management
- Special users list
- Rate limit handling
- Follow/unfollow timing controls

## Configuration

Required environment variables:
```bash
token=your_github_token
```

## Usage

First set GitHub token in environment:
```bash
export GITHUB_TOKEN="your_github_token"
```

```python
# Run from command line
python main.py
```

## Key Methods

- `find_followers()`: Gets current followers
- `find_following()`: Gets accounts you follow
- `follow_one_account()`: Follows a single account
- `unfollow_one_account()`: Unfollows a single account
- `gather_account_data()`: Collects user profile data

## Data Collection

The bot collects:
- Account creation date
- Follower/following counts
- Repository count
- Profile completeness
- Follow/unfollow response data

## Limitations

- GitHub API rate limits (5000 requests/hour)
- Maximum 500 follows per day
- Requires GitHub API token

## Error Handling

- Automatic retry on API failures
- Rate limit pause/resume
- Data validation 