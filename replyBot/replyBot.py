import tweepy
from time import sleep

# This program serves as a BOT that checks someones twitter
# If the user posted a new tweet this BOT then replys to his tweet

# Defines the target of this BOT
USER = 'jairbolsonaro'


def main():
    print("authorizing")
    api = auth()

    while True:
        # The BOT checks for new tweets every 10 minutes
        sleep(600)
        print("starting new check")
        postId = lastPostId()

        # If there's a new tweet, reply to it
        if postedNewTweet(api, postId):
            newPostId = lastPostId()
            api.update_status(status = 'Vai se fuder @' + USER, in_reply_to_status_id = newPostId)
            print("posted reply")
        

# Checks the authorization for the API
def auth():
    # Opens a file with the API credentials
    with open('twitter-keys.txt', 'r') as keys:
        access_token = keys.readline().strip('\n')
        access_token_secret = keys.readline().strip('\n')
        consumer_key = keys.readline().strip('\n')
        consumer_secret = keys.readline().strip('\n')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    # Returns the authorized command
    return api


# Serves to check the last tweet ID that is saved on the last_tweet file
def lastPostId():
    with open('last_tweet.txt', 'r') as last_tweet:
        lastId = last_tweet.readline().strip('\n')
        return lastId


# Checks if the target posted a new tweet since last check, if yes returns true
def postedNewTweet(api, since_id):

    # See if there's a new tweet posted after the since_id
    newTweetCheck = tweepy.Cursor(api.user_timeline, id=USER, since_id = since_id).items(1)
    isNewTweet = 0

    for tweet in newTweetCheck:
        print(tweet.text)
        isNewTweet = tweet.id

    # If there was a new tweet, overwrite the old one id with this new
    if isNewTweet > 1:
        with open("last_tweet.txt", 'w') as last_tweet:
            last_tweet.write(str(isNewTweet))
        return True
    
    return False



main()
