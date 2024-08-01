"""
Author: liicodex
Date: 30 July 2024
Reason: BrandElevator's bot v1.0 PENDING SAAS
"""

# REQUIRED PACKAGES
import tweepy
import os

# INITIALIZING THE PROGRAM
def startAuth():
    # Authenticate to Twitter (replace with your credentials)
    try:
        auth = tweepy.OAuthHandler("API_KEY", "API_SECRET_KEY")
        auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
        api = tweepy.API(auth)
        api.verify_credentials(auth)
        print("Authentication OK")
    except:
        print("Error during authentication!")
    return api

# THE LOGIC FUNCTIONS
def getPosts(username, numberOfPosts,api):
    try:
        """ CREATING A NEW FOLDER TO SAVE EACH CLIENT'S FILE
        # Creating a new folder
        folderName = f"{username}"
        if not os.path.exists(folderName):
            os.makedirs(folderName)
        """
        # Getting user tweets
        tweets = tweepy.Cursor(api.user_timeline, screen_name=username).items(numberOfPosts)

        # Creating a text file with username
        with open(f"{username}.txt", "w") as file:
            for tweet in tweets:
                # Writing each tweet and its date into the file
                file.write(f"{tweet.text} -- {tweet.created_at}\n")

        print(f"{numberOfPosts} saved to {username}.txt")
    except tweepy.TweepyException as tperr:
        print("Something went terribly wrong!")

# Function for searching tweets 
def searchCompetitorPosts(api):
    searchKeyword = keyword 
    maxTweets = numberOfPosts
    with open(f"{username}'s Competition.txt", "w") as cFile:
        # Writing to a competitors text file
        for tweet in tweepy.Cursor(api.search_tweets, q=searchKeyword, lang="en").items(maxTweets):
            cFile.write(f"{tweet.user.name} : \n {tweet.text} -- {tweet.created_at}")

# Function for influencer Identification
def identifyInfluencers(usename, numberOfPosts,api):
    tweets = tweepy.Cursor(api.user_timeline, screen_name=username).items(numberOfPosts)
    influencers = []
    for tweet in tweets:
        if tweet.user.followers_count > 10000:
            influencers.append(tweet.user.screen_name)
    with open(f"{username}'s Influencers.txt", "w") as infl:
        for influencer in influencers:
            infl.write(f"{influencer} -- Followers: {influencer.user.followers_count} \n") # saving as GrowthWithLeo -- Followers: 30

# MAIN LOGIC
def main(username, numberOfPosts, keyword, api):
# FETCHING THE POST AND SAVING TO THE FIRST FILE!!
    try:
        """ CREATING A NEW FOLDER TO SAVE EACH CLIENT'S FILE
        # Creating a new folder
        folderName = f"{username}"
        if not os.path.exists(folderName):
            os.makedirs(folderName)
        """
        # Getting user tweets
        tweets = tweepy.Cursor(api.user_timeline, screen_name=username).items(numberOfPosts)

        # Creating a text file with username
        with open(f"{username}.txt", "w") as file:
            for tweet in tweets:
                # Writing each tweet and its date into the file
                file.write(f"{tweet.text} -- {tweet.created_at}\n")

        print(f"{numberOfPosts} saved to {username}.txt")
    except tweepy.TweepyException as tper:
        print("Something went terribly wrong in Section 1!")

# SEARCHING RELEVANT TWEETS BASED ON A KEYWORD
    try:
        searchKeyword = keyword 
        maxTweets = numberOfPosts
        with open(f"{username}'s Competition.txt", "w") as cFile:
            # Writing to a competitors text file
            for tweet in tweepy.Cursor(api.search_tweets, q=searchKeyword, lang="en").items(maxTweets):
                cFile.write(f"{tweet.user.name} : \n {tweet.text} -- {tweet.created_at}")
    except tweepy.TweepyException as tperr:
        print("Something went wrong in Section 2!")

# IDENTIFYING INFLUENCERS IN THE SPACE
    try:
        tweets = tweepy.Cursor(api.search_tweets, q=searchKeyword, lang="en").items(maxTweets)
        influencers = []
        for tweet in tweets:
            if tweet.user.followers_count > 10000:
                influencers.append(tweet.user.screen_name)
        with open(f"{username}'s Influencers.txt", "w") as infl:
            for influencer in influencers:
                infl.write(f"{influencer} -- Followers: {influencer.user.followers_count} \n") # saving as GrowthWithLeo -- Followers: 30
    except Exception as excp:
        print("Something went wrong in Section 3!")

if __name__ == '_main_':
    startAuth()
    username = None
    numberOfPosts = None
    keyword = None
    getPosts(username, numberOfPosts)