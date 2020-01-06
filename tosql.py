from pymongo import MongoClient
from tweetcleaner import tweettext

client = MongoClient()
db = client.tweetsdata
collection = db.training_tweets_collection

'''
Attributes that we would like to have collected
    1. ID
    2. UserName
    3. Location of user
    4. Tweet text
    5. Location of tweet - if available 
    6. Tweet mentions - which users are mentioned in the tweet
'''

def userinfo(posts):
    try:
        uname = posts['user']['name']
        uscreenname = posts['user']['screen_name']
        uloc = posts['user']['location']
        return uname, uscreenname, uloc
    except:
        print("The user key was not found")
        return None, None, None



for posts in collection.find({}):
    id = posts['id']
    uname, uscreenname, ulocation = userinfo(posts)
    tweet = tweettext(posts)
    print(uname,  tweet)