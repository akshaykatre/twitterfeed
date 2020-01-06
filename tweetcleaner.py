from nltk.corpus import stopwords
from nltk import word_tokenize
import preprocessor
import re 
from emoticons import emoticons, emoji_pattern
import string


def clean_tweets(tweet):
    tweet = preprocessor.clean(tweet)
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(tweet)#after tweepy preprocessing the colon symbol left remain after      #removing mentions
    tweet = re.sub(r':', '', tweet)
    tweet = re.sub(r'‚Ä¶', '', tweet)
#replace consecutive non-ASCII characters with a space
    tweet = re.sub(r'[^\x00-\x7F]+',' ', tweet)#remove emojis from tweet
    tweet = emoji_pattern.sub(r'', tweet)#filter using NLTK library append it to a string
    filtered_tweet = [w for w in word_tokens if not w in stop_words]
    filtered_tweet = []#looping through conditions
    for w in word_tokens:
#check tokens against stop words , emoticons and punctuations
        if w not in stop_words and w not in emoticons and w not in string.punctuation:
            filtered_tweet.append(w)
    return ' '.join(filtered_tweet)
    #print(word_tokens)
    #print(filtered_sentence)return tweet

def tweettext(posts):
    try:
        ## Get the tweet from extended tweet
        tweet = posts['extended_tweet']['full_text']
        tweet = clean_tweets(tweet)
        return tweet
    except KeyError:
        pass
    
    try:
        ## Try from retweet
        tweet = posts['retweeted_status']['extended_tweet']['full_text']
        tweet = clean_tweets(tweet)
        return tweet
    except KeyError:
        pass 
    
    try:
        tweet = posts['text']
        tweet = clean_tweets(tweet)
        return tweet 
    except KeyError: 
        print("Can't find the tweet!")
        return None