# coding: utf8
import Connect as conn
from collections import defaultdict 

user = conn.api.me()


def subscriptionList():
    ids = []
    for page in conn.tweepy.Cursor(conn.api.friends_ids, screen_name="hieund2102").pages():
        ids.extend(page)
    screen_names = [user.screen_name for user in conn.api.lookup_users(user_ids=ids)]
    return screen_names

def getStatuses(screenName):
    print(screenName)
    new_tweets = conn.api.user_timeline(screen_name = "@"+screenName, tweet_mode="extended", search_params="exclude:replies")
    tweets = [[tweet.full_text] for tweet in new_tweets]
    list_tweet = {}
    for id,text in zip(new_tweets,tweets):
        print(id.id, text)
        tId = id.id
        list_tweet.update({tId:text})
    return list_tweet


def getRetweets(tweetId):
    retweets= conn.api.retweets(tweetId, count=5)
    for retweet in retweets:
        print(retweet.text)
    return retweets

tDict = getStatuses("elonmusk")
for entry in tDict:
    print(tDict[entry])
    getRetweets(entry)