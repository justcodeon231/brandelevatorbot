import tweepy
import os

# Set up your Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate to the Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Function to fetch tweets based on criteria
def fetch_tweets(source_type,
                 query=None,
                 username=None,
                 min_likes=0,
                 min_replies=0,
                 min_engagements=0,
                 max_tweets=100):
    tweets = []

    if source_type == "search":
        for tweet in tweepy.Cursor(api.search_tweets,
                                   q=query,
                                   lang="en",
                                   tweet_mode='extended').items(max_tweets):
            likes = tweet.favorite_count
            replies = tweet.reply_count
            engagements = likes + replies + tweet.retweet_count

            if likes >= min_likes and replies >= min_replies and engagements >= min_engagements:
                tweets.append({
                    'text': tweet.full_text,
                    'likes': likes,
                    'replies': replies,
                    'engagements': engagements,
                    'created_at': tweet.created_at,
                    'username': tweet.user.screen_name
                })

    elif source_type == "profile":
        for tweet in tweepy.Cursor(api.user_timeline,
                                   screen_name=username,
                                   tweet_mode='extended').items(max_tweets):
            likes = tweet.favorite_count
            replies = tweet.reply_count
            engagements = likes + replies + tweet.retweet_count

            if likes >= min_likes and replies >= min_replies and engagements >= min_engagements:
                tweets.append({
                    'text': tweet.full_text,
                    'likes': likes,
                    'replies': replies,
                    'engagements': engagements,
                    'created_at': tweet.created_at,
                    'username': tweet.user.screen_name
                })

    return tweets

# Function to save tweets to a text file
def save_tweets_to_file(tweets, source_name, folder_path='tweets'):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filename = f"{source_name}.txt"
    file_path = os.path.join(folder_path, filename)

    with open(file_path, 'w', encoding='utf-8') as file:
        for tweet in tweets:
            file.write(f"Username: {tweet['username']}\n")
            file.write(f"Created at: {tweet['created_at']}\n")
            file.write(f"Text: {tweet['text']}\n")
            file.write(f"Likes: {tweet['likes']}\n")
            file.write(f"Replies: {tweet['replies']}\n")
            file.write(f"Engagements: {tweet['engagements']}\n")
            file.write("-" * 50 + "\n")

    print(f"Tweets saved to {file_path}")

# Example usage
if __name__ == "__main__":
    source_type = "search"  # Choose between "search" or "profile"
    
    if source_type == "search":
        query = "AI"  # search keyword or hashtag
        username = None  # Not needed for search
        source_name = query.replace(" ", "_")  # Use query as file name
    elif source_type == "profile":
        query = None  # Not needed for profile
        username = "elonmusk"  # Replace with the desired Twitter username
        source_name = username  # Use username as file name

    min_likes = 10
    min_replies = 5
    min_engagements = 20
    max_tweets = 50

    tweets = fetch_tweets(source_type,
                          query,
                          username,
                          min_likes,
                          min_replies,
                          min_engagements,
                          max_tweets)
    
    save_tweets_to_file(tweets, source_name)
