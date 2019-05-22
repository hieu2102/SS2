
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

def get_replies(screen_name, tweet_id):
    query='to:'+screen_name
    print(tweet_id)
    replies = api.search(q=query, since_id = tweet_id, count = 1000, result_type='recent')
    filtered_replies=[]
    for reply in replies:
        if hasattr(replies, 'in_reply_to_status_id_str'):
            if replies.in_reply_to_status_id_str == tweet_id:
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


if __name__ == '__main__':

    getRetweet()