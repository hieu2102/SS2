import tweepy
import pandas as pd
import twitter
from twitter import *

consumer_key = 'GVNzzENjHD8zGf87FhAxAAhNQ'
consumer_secret = 'mrGmyOMPNOWhw6uehNS51hzlKSA35dwhQ9BnR8pETcPD9bUUIM'
access_token = '1102239905755742213-t9DcW0XvPsTxAWzeVk41lAYLxXwUIi'
access_token_secret = 'WYpnLmwYcxWYX4IFTPq8fcwRpPa4Vglz91LUseGd9ujuC'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

from collections import defaultdict
import tweepy
import sys
user = api.me()
def subscriptionList():
    ids = []
    for page in tweepy.Cursor(api.friends_ids, screen_name="hieund2102").pages():
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

def getRetweet():
    queries = ["rt to win", "retweet to win"]
    tweets_per_query = 50

    # set a variable to count the amount of tweets re-tweeted
    # to use at the end and create a loop looping though the queries declared previously.
    new_tweets = 0

    # print what query we are querying and then create another for loop
    # that loops though tweets that are returned from the api
    for querry in queries:
        print("Starting new querry: " + querry)
        for tweet in tweepy.Cursor(api.search, q=querry, tweet_mode="extended").items(tweets_per_query):

            user = tweet.user.screen_name
            id = tweet.id
            url = 'https://twitter.com/' + user + '/status/' + str(id)
            print(url)

            # extended tweet_mode in the search querry to get all text rather than the normal 140
            try:
                # re-tweet tweet
                text = tweet.retweeted_status.full_text.lower()
            except:
                # original tweet
                text = tweet.full_text.lower()

            if "retweet" in text or "rt" in text:
                if not tweet.retweeted:
                    try:
                        tweet.retweet()
                        print("\tRetweeted")
                        new_tweets += 1         # avoid that we have tweet the tweets
                    except tweepy.TweepError as e:
                        print('\tAlready Retweeted')

            if "like" in text or "fav" in text:
                try:
                    tweet.favorite()
                    print('\t' + "Liked")
                except:
                    print('\tAlready Liked')
            if "follow" in text:
                try:
                    to_follow = [tweet.retweeted_status.user.screen_name] + [i['screen_name'] for i in
                                                                             tweet.entities['user_mentions']]
                    # Don't follow origin user (person who retweeted)
                except:
                    to_follow = [user] + [i['screen_name'] for i in tweet.entities['user_mentions']]

                for screen_name in list(set(to_follow)):
                    api.create_friendship(screen_name)
                    print('\t' + "Followed: " + screen_name)

    print("New Tweets: " + str(new_tweets))
# def get_retweet():
#
#     query = 0
#
#     for tweet_info in tweepy.Cursor(api.search, q=query, lang= "en", tweet_mode="extended").items(100):
#         if retweeted_status in dir(tweet_info):
#             tweet = tweet_info.retweeted_status.full_text
#         else:
#             tweet = tweet_info.full_text

def create_dataframe():
    message, favorite_count, retweet_count, created_at, user_name, favourites_count, description, friends_count, followers_count = [], [], [], [], [], [], [], [], []
    for status in tweepy.Cursor(api.home_timeline).items(100):
        message.append(status.text)
        favorite_count.append(status.favorite_count)
        retweet_count.append(status.retweet_count)
        created_at.append(status.created_at)
        user_name.append(status.user.name)
        favourites_count.append(status.user.favourites_count)
        description.append(status.user.description)
        friends_count.append(status.user.friends_count)
        followers_count.append(status.user.followers_count)

    df = pd.DataFrame({'Message': message,
                       'Tweet Favorite Count': favorite_count,
                       'Retweet Count': retweet_count,
                       'Created At': created_at,
                       'Username': user_name,
                       'Likes': favourites_count,
                       'User Description': description,
                       'Following': friends_count,
                       'Followers': followers_count})
    df.to_csv("Twitter Timeline.csv")
    print(df)

def get_reply():
    replies = []
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

    id_array = []

    for status in api.user_timeline():
        list = status.id
        id_array.append(list)
    for full_tweets in tweepy.Cursor(api.user_timeline, screen_name="hieund2102", timeout=999999).items(10):
        for id in id_array:
            for tweet in tweepy.Cursor(api.search, q='to:hieund2102', since_id=id, result_type='recent',
                                   timeout=999999).items(1000):
                if hasattr(tweet, 'in_reply_to_status_id_str'):
                    if (tweet.in_reply_to_status_id_str == full_tweets.id_str):
                        replies.append(tweet.text)
            print("Tweet :", full_tweets.text.translate(non_bmp_map))
            for elements in replies:
                print("Replies :", elements)
            replies.clear()

# def getReplies(screenName, tweetId):
#     query='to:'+screenName
#     print(tweetId)
#     replies = api.search(q=query, since_id = tweetId, count = 1000, result_type='recent')
#     filtered_replies=[]
#     for reply in replies:
#         if hasattr(replies, 'in_reply_to_status_id_str'):
#             if(replies.in_reply_to_status_id_str==tweetId):
#                 filtered_replies.append(replies.text)
#     for reply in filtered_replies:
#         print(reply)

twitter = Twitter(auth = OAuth(access_token,access_token_secret,consumer_key,consumer_secret))

def get_retweet():

    user = "hieund2102"
    results = twitter.statuses.user_timeline(screen_name=user)

    for status in results:
        print("@%s %s" % (user, status["text"]))
        retweets = twitter.statuses.retweets._id(_id=status["id"])
        for retweet in retweets:
            print(" - retweeted by %s" % (retweet["user"]["screen_name"]))




if __name__ == '__main__':

    getRetweet()
    get_retweet() 