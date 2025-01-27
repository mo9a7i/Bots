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

First, set up your config files:
```bash
# Create config directory
mkdir -p config

# Copy example files
cp config/following.json.example config/following.json
cp config/blacklist.json.example config/blacklist.json
cp config/scanned_targets.json.example config/scanned_targets.json
cp config/special_users.json.example config/special_users.json
cp config/target_users.json.example config/target_users.json
cp .env.example .env
```

Required environment variables:

Create a `.env` file in the Github Bot 3.0 directory:

```bash
# Github Bot 3.0/.env
token=ghp_xxxxxxxxxxxxxxxxxxxx    # Your GitHub personal access token
my_username=yourusername         # Your GitHub username
```

To get your GitHub token:
1. Go to GitHub Settings → Developer Settings → Personal Access Tokens → Tokens (classic)
2. Generate new token (classic)
3. Select scopes:
   - `read:user`
   - `user:follow`
4. Copy token and paste in `.env` file

## Usage

1. Set up configuration files:

- Create `config/special_users.json` with users you never want to unfollow
- Create `config/target_users.json` with users whose followers you want to target

2. Create required files:
```bash
touch blacklist.json    # Users that won't be followed again
touch following.json    # Tracks who you follow and their status
touch results.json      # Stores data about unfollowed users
```

3. Run the bot:
```python
# Run from command line
python main.py
```

## Troubleshooting

If you get a "Bad credentials" error:
1. Check your `.env` file has correct variables:
   ```bash
   token=ghp_xxxxxxxxxxxxxxxxxxxx  # Your GitHub Personal Access Token
   my_username=yourusername        # Your GitHub username
   ```
2. Verify your token has required permissions:
   - `read:user`
   - `user:follow`
3. Make sure token hasn't expired

Common status codes:
- 401: Bad credentials or expired token
- 403: Rate limit exceeded
- 404: User not found

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

## Data Files

- `following.json`: Tracks followed users with dates and status
- `blacklist.json`: Users that won't be followed again
- `results.json`: Data about unfollowed users
- `config/special_users.json`: Users to never unfollow
- `config/target_users.json`: Users whose followers to target 