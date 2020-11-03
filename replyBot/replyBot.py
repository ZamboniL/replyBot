import tweepy
import random
from time import sleep

# Created By: ZamboniL
# This program serves as a BOT that checks someones twitter
# If the user posted a new tweet this BOT then replys to his tweet

# Defines the target of this BOT
BOT_CONFIG = {}

def main():
    config_bot()

    print('Authorizing')
    api = auth()

    try:
        api.verify_credentials()
        print('Authentication OK')
    except:
        print('Error during authentication')

    while True:
        # The BOT checks for new tweets every 10 minutes
        sleep(BOT_CONFIG['TIME_TO_CHECK'])
        print("starting new check")
        postId = lastPostId()

        # If there's a new tweet, reply to it
        if postedNewTweet(api, postId):
            
            # If the condition Spongefy on the config.txt is true, then mock the tweet.
            newPostId = lastPostId()
            if BOT_CONFIG['SPONGIFY'].capitalize() == 'True':
                BOT_CONFIG['MESSAGE'] = spongeText(api, newPostId)
            api.update_status(status = BOT_CONFIG['MESSAGE'] + ' @' + BOT_CONFIG['TARGET_USER'], in_reply_to_status_id = newPostId)
            print("posted reply")
        

def config_bot():
    with open('config.txt', 'r') as config:
        for line in config:
            (key, value) = line.split(':')

            if 'TIME_TO_CHECK' in key:
                if value != '':
                    BOT_CONFIG[key] = int(value)
                else:
                    BOT_CONFIG[key] = 600
            elif key in ['TARGET_USER', 'ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET', 'CONSUMER_KEY', 
                        'CONSUMER_SECRET', 'TARGET_USER', 'MESSAGE', 'LAST_ID_FILE', 'SPONGIFY']:
                if value == '':
                    print('Missing ' + key + " Parameter")
                    exit(1)
                else:
                    BOT_CONFIG[key] = value.strip('\n')
            elif key in 'TARGET_TEXT':
                BOT_CONFIG[key] = value.strip('\n')
            else:
                print('Invalid ' + key + ' Parameter')



# Checks the authorization for the API
def auth():
    # Opens a file with the API credentials
    auth = tweepy.OAuthHandler(BOT_CONFIG['CONSUMER_KEY'], BOT_CONFIG['CONSUMER_SECRET'])
    auth.set_access_token(BOT_CONFIG['ACCESS_TOKEN'], BOT_CONFIG['ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)
    # Returns the authorized command
    return api


# Serves to check the last tweet ID that is saved on the last_tweet file
def lastPostId():
    with open(BOT_CONFIG['LAST_ID_FILE'], 'r') as last_tweet:
        lastId = last_tweet.readline().strip('\n')
        print(lastId)
        return lastId


# Creates a mocked version of the tweet the target sent, example:
# "I love Lucy" becomes;
# "i lOVe lUcY"
def spongeText(api, postId):
    newTweet = api.get_status(postId, tweet_mode='extended')
    print(newTweet.full_text)
    upCount = 0
    downCount = 0
    mockedText = ''
    for letter in newTweet.full_text:
        i = random.randrange(2)
        if upCount < 2 and i == 1 or downCount >= 2:
            mockedText += letter.upper()
            upCount += 1
            downCount = 0
        else:
            mockedText += letter.lower()
            downCount += 1
            upCount = 0

    return mockedText


# Checks if the target posted a new tweet since last check, if yes returns true
def postedNewTweet(api, since_id):

    # See if there's a new tweet posted after the since_id
    newTweetCheck = tweepy.Cursor(api.user_timeline, id=BOT_CONFIG['TARGET_USER'], since_id = since_id).items(1)
    isNewTweet = 0 


    for tweet in newTweetCheck:
        print(tweet.text)
        isTextOnTweet = tweet.text
        isNewTweet = tweet.id


    targetText = BOT_CONFIG['TARGET_TEXT'].lower()

    if isNewTweet > 1:
        if targetText != '':
            if isTextOnTweet in targetText:
                # If there was a new tweet, overwrite the old one id with this new
                with open(BOT_CONFIG['LAST_ID_FILE'], 'w') as last_tweet:
                    last_tweet.write(str(isNewTweet))
                    return True
        else:
            with open(BOT_CONFIG['LAST_ID_FILE'], 'w') as last_tweet:
                    last_tweet.write(str(isNewTweet))
                    return True
    return False



main()