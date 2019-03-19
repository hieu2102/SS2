import tweepy

consumer_key = 'GVNzzENjHD8zGf87FhAxAAhNQ'
consumer_secret = 'mrGmyOMPNOWhw6uehNS51hzlKSA35dwhQ9BnR8pETcPD9bUUIM'
access_token = '1102239905755742213-t9DcW0XvPsTxAWzeVk41lAYLxXwUIi'
access_token_secret = 'WYpnLmwYcxWYX4IFTPq8fcwRpPa4Vglz91LUseGd9ujuC'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

