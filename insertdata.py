from datetime import datetime, timedelta, date
import time
import pdb 
import sqlite3
import GetOldTweets3 as got 

conn = sqlite3.connect('twitter.db')

tweetCriteria = got.manager.TweetCriteria().setQuerySearch("Rabobank").setMaxTweets(200)
maps = {}

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


def tweet_inserts(conn, values):
    cur = conn.cursor()
    query = '''INSERT or IGNORE INTO tweets(tweet, day,
            month, year, hour, min, seconds, username,
            geo, retweets, hashtags, mentions) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
 #   print(query)
    cur.execute(query, values)

start_date = date(2018,1,1)
end_date = date(2019,9,1)

with conn:
    ##for dates in :

#        print("On date: ", dates)
    for single_date in daterange(start_date, end_date):
        
        stdate = single_date.strftime('%Y-%m-%d')
        print("Start date: ", stdate)
        endate = (single_date+timedelta(1)).strftime('%Y-%m-%d')
        tweets = got.manager.TweetManager.getTweets(tweetCriteria.setSince(stdate).setUntil(endate))
        print("nTweets: ", str(len(tweets)))
        for tweet in tweets: 
            #print(tweet.text)
            tw_text = tweet.text
            tw_day = tweet.date.day
            tw_month = tweet.date.month
            tw_year = tweet.date.year
            tw_hour = tweet.date.time().hour 
            tw_min = tweet.date.time().minute 
            tw_seconds = tweet.date.time().second
            tw_username = tweet.username
            tw_geo = tweet.geo 
            tw_retweets = tweet.retweets
            tw_hashtags = tweet.hashtags 
            tw_mentions = tweet.mentions 

            values = (tw_text, tw_day, tw_month, tw_year,
                        tw_hour, tw_min, tw_seconds, tw_username,
                        tw_geo, tw_retweets, tw_hashtags, tw_mentions)

            tweet_inserts(conn, values)