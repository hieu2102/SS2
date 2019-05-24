# coding: utf8
from Connect import api
from collections import defaultdict 
import tweepy
import sys
user = api.me()


def subscriptionList():
    ids = []
    for page in conn.tweepy.Cursor(api.friends_ids, screen_name="hieund2102").pages():
        ids.extend(page)
    screen_names = [user.screen_name for user in api.lookup_users(user_ids=ids)]
    return screen_names

def getStatuses(screenName):
    print(screenName)
    new_tweets = api.user_timeline(screen_name = "@"+screenName, tweet_mode="extended", search_params="exclude:replies")
    tweets = [[tweet.full_text] for tweet in new_tweets]
    list_tweet = {}
    for id,text in zip(new_tweets,tweets):
        #print(id.id, text)
        tId = id.id
        list_tweet.update({tId:text})
    return list_tweet

def getReplies(screenName, tweetId):
    query='to:'+screenName
    print(tweetId)
    replies = api.search(q=query, since_id = tweetId, count = 1000, result_type='recent')
    filtered_replies=[]
    for reply in replies:
        if hasattr(replies, 'in_reply_to_status_id_str'):
            if(replies.in_reply_to_status_id_str==tweetId):
                filtered_replies.append(replies.text)
    for reply in filtered_replies:
        print(reply)

def getNews():
    users = subscriptionList()
    while(True):
        for user in users:
            tweets= getStatuses(user)
            for tweet in tweets:
                print
                nlp.categorizes((tweets[tweet])[0], user)
        sleep(120)

getNews()
