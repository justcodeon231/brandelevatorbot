# 🚀 Twitter Engagement Bot v1.1

## Overview

**Twitter Engagement Bot v1.1** is a Python-powered tool designed to help users fetch, filter, and analyze tweets based on engagement metrics like likes, replies, and total engagements. Whether you're a social media manager, content creator, or researcher, this bot will streamline your Twitter data-gathering process and help you extract valuable insights. 

## ✨ Features

- **🔍 Search-Based Tweet Fetching**: Fetch tweets using specific keywords or hashtags, filtered by engagement metrics (likes, replies, and engagements).
- **👤 Profile-Based Tweet Fetching**: Retrieve tweets from specific Twitter profiles, filtered by engagement metrics.
- **📅 Date Range Support**: Filter tweets within a specific date range (API permitting).
- **⏳ Rate Limit Handling**: Automatically handle API rate limits with timed pauses to avoid disruptions.
- **💾 Save to File**: Export fetched tweets to text files, organized by query or profile name.
- **📊 Scalable**: Process and handle large volumes of tweet data while staying within Twitter API limits.

## 🎯 Functions

- **Filter by Engagement**: Define the minimum number of likes, replies, or engagements a tweet should have to be included in the results.
- **Save Results**: Automatically save fetched tweets to a file for easy reference and further analysis.
- **Rate Limit Management**: Automatically pauses the bot when rate limits are reached, preventing failures and extending usage.

## 🔧 Problems It Solves

- **Time-Consuming Data Collection**: No need to manually sift through tweets for high-engagement content. The bot does it for you.
- **Effortless Analysis**: Instantly gather high-engagement tweets to analyze trends, content strategies, or user behavior.
- **Data Organization**: Automatically saves results to a file, neatly organized by search terms or profile names.

## 📋 Requirements

- Python 3.x
- Tweepy module (`pip install tweepy`)
- Twitter Developer Account with API keys and access tokens (basic level)
  
## ⚙️ Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/twitter-engagement-bot.git
   cd twitter-engagement-bot
   ```

2. **Install Dependencies**:

   Ensure Python is installed. Then install the required packages:

   ```bash
   pip install tweepy
   ```

3. **Set Up Twitter API Credentials**:

   - Sign up for a Twitter Developer account at [Twitter Developer Portal](https://developer.twitter.com/).
   - Create a new application and generate your API keys (API key, API secret key, Access token, and Access token secret).
   - Add your credentials to the script by replacing the placeholders:

   ```python
   consumer_key = 'your_consumer_key'
   consumer_secret = 'your_consumer_secret'
   access_token = 'your_access_token'
   access_token_secret = 'your_access_token_secret'
   ```

4. **Create a Folder for Saved Tweets**:

   The bot saves tweets into a `tweets` folder automatically. If you prefer to manually create this folder, you can do so with:

   ```bash
   mkdir tweets
   ```

## 💡 Usage

1. **Choose Your Source Type**:

   In the `twitter_bot.py` script, choose the source type:
   - Set `source_type` to `"search"` for searching by keyword/hashtag.
   - Set `source_type` to `"profile"` for fetching tweets from a specific user.

2. **Customize Your Criteria**:

   You can customize your search or profile retrieval by modifying the following parameters:

   - `query`: Keyword or hashtag for search-based retrieval.
   - `username`: Twitter handle for profile-based retrieval.
   - `min_likes`: Minimum number of likes a tweet should have to be fetched.
   - `min_replies`: Minimum number of replies a tweet should have to be fetched.
   - `min_engagements`: Minimum total engagements (likes + replies) for a tweet.
   - `max_tweets`: The maximum number of tweets to retrieve in a single run.

3. **Run the Bot**:

   Once you've set up your criteria, execute the script:

   ```bash
   python twitter_bot.py
   ```

4. **Check the Output**:

   The fetched tweets will be saved in the `tweets` folder. The file name will be based on the query term or the profile username, making it easy to locate your results.

### Example Usage

Fetching tweets with a minimum of 10 likes and 5 replies from the keyword "AI":

```python
source_type = "search"
query = "AI"
min_likes = 10
min_replies = 5
max_tweets = 50
```

Fetching tweets from Elon Musk’s timeline with a minimum of 20 total engagements:

```python
source_type = "profile"
username = "elonmusk"
min_engagements = 20
max_tweets = 100
```

### ⚠️ Rate Limiting

To manage Twitter API rate limits, the bot includes basic rate-limit handling using timers. If you exceed the rate limit, the bot will pause and resume after the necessary cooldown period. This helps prevent errors and extends the bot's ability to fetch data continuously.

## 📜 Preferred License

This project is open-source under the [MIT License](LICENSE). Feel free to use, modify, and distribute this code for both personal and commercial projects.

## 🤝 Collaboration & Contributions

This bot is a work in progress, and I welcome collaboration from developers, data enthusiasts, and anyone with ideas for improvement! 

- **Fork the Repo**: Make your changes and submit a pull request.
- **Report Issues**: If you encounter bugs or have feature suggestions, feel free to open an issue.
- **Add New Features**: If you’ve implemented new features or optimizations, share them with the community through a pull request.

Together, we can enhance this tool and empower more people to efficiently manage their Twitter data.

## 📬 Contact Info

For questions, suggestions, or collaboration requests, please reach out to me at:

- **Author**: Leo
- **Email**: ntlukaleo@gmail.com
- **Twitter**: [@YourTwitterHandle](https://twitter.com/GrowthWithLeo)

Happy Tweeting! 🎉
