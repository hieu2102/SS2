# coding: utf8
import Connect as conn

user = conn.api.me()


def subscriptionList():
    ids = []
    for page in conn.tweepy.Cursor(conn.api.friends_ids, screen_name="hieund2102").pages():
        ids.extend(page)
    screen_names = [user.screen_name for user in conn.api.lookup_users(user_ids=ids)]
    return screen_names

### does not get full tweet length
def getStatuses(screenName):
    print(screenName)
    tweets = conn.api.user_timeline(screen_name="@"+screenName):
    for tweet in tweets 
        if (tweet.lang =="en"):
            print ((tweet.text).encode("utf-8"))
    return tweets


def getRetweets(tweetId):
    retweets= conn.api.retweets(tweetId, 5)
    for retweet in retweets:
        print(retweet.text)
    return retweets