# TwitterReplyBot
Twitter reply bot, that for every new tweet a user posts it replies with a automated message. 
# usage

Before running the bot you have to configure certain .txt files, so it can connect to the twitter API and send your message correctly.

```
ACCESS_TOKEN:
ACCESS_TOKEN_SECRET:
CONSUMER_KEY:
CONSUMER_SECRET:
TARGET_USER:
TARGET_TEXT:
MESSAGE:
TIME_TO_CHECK:
LAST_ID_FILE:
```

This should be your config.txt file parameters; ```ACCESS_TOKEN```, ```ACCESS_TOKEN_SECRET```, ```CONSUMER_KEY```, ```CONSUMER_SECRET```, are your twitter API keys, they should never be empty; ```TARGET_USER```, ```TARGET_TEXT```, are respectively the Target of the reply @ and what should be on the tweets that you want to reply, the second parameter can be left empty if you want to reply to every tweet that the target makes.

```MESSAGE``` is the message that you want to leave for the user on the reply, the code always ends the message with @TARGET_USER in order to reply, so no need to put that on your text.

```TIME_TO_CHECK``` how fast the code will loop and search for a new tweet, it's in seconds, if you leave it empty it will default to 600(10 minutes).

```LAST_ID_FILE``` Which file the code will create and search for the users last tweet ID.
# example

```
ACCESS_TOKEN:1267998895633250178-COW7vE8Rw6UYEquJIQoVlNWYqg1J4B
ACCESS_TOKEN_SECRET:UCevtqmaidTmOvbP0RbHjm1nL0OMHQ3dJ6c7QyhRtjlRU
CONSUMER_KEY:fcmYPNpcYkljhnAMjCfXxVPQ6R
CONSUMER_SECRET:4P2i6e3IokkfTU4Hzvji9TkRCZKtLçoutyQHJpNpGCQLGbo7M8FRg
TARGET_USER:twitter
TARGET_TEXT:Hi
MESSAGE:Hi!
TIME_TO_CHECK:10
LAST_ID_FILE:last_tweet.txt
```

With this config.txt file for example, the code will take the API Keys, check if they are valid then tweet at ```@twitter```, the message ```"Hi! @twitter"``` if his last post since the id on ```last_tweet.txt``` contains the word ```Hi```, and will check for a new tweet with the word ```Hi``` every 10 seconds.
