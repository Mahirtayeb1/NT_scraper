#importing libraries
from googletrans import Translator
import pandas as pd
import time
import traceback
import tweepy
import twitter
import re

access_token ="1651300681578610688-WvpOzdS3rBNt9VcENuoFWRt0FtTBM3"
access_token_secret = "dVuIFZ3pSuTWGNCEOj930CcFhQYELY9a55nLIMqJyZQlN"
consumer_key = "g6L5jCwkzZrAW0JVqHj3vnqRM"
consumer_secret = "ihogHoF370Xrzgi36wzli70EFZgAlXBHkWQSQ6cCnypotIVnJN"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# word_list = ['$', '€', '4ao', 'a.m', 'a3', 'aamof', 'acct', 'adih', 'afaic', 'afaict', 'afaik', 'afair', 'afk', 'app', 'approx', 'apps', 'asap', 'asl', 'atk', 'ave.', 'aymm', 'ayor', 'b&b', 'b+b', 'b.c', 'b2b', 'b2c', 'b4', 'b4n', 'b@u', 'bae', 'bak', 'bbbg', 'bbc', 'bbias', 'bbl', 'bbs', 'be4', 'bfn', 'blvd', 'bout', 'brb', 'bros', 'brt', 'bsaaw', 'btw', 'bwl', 'c/o', 'cet', 'cf', 'cia', 'csl', 'cu', 'cul8r', 'cv', 'cwot', 'cya', 'cyt', 'dae', 'dbmib', 'diy', 'dm', 'dwh', 'e123', 'eet', 'eg', 'embm', 'encl', 'encl.', 'etc', 'faq', 'fawc', 'fb', 'fc', 'fig', 'fimh', 'ft.', 'ft', 'ftl', 'ftw', 'fwiw', 'fyi', 'g9', 'gahoy', 'gal', 'gcse', 'gfn', 'gg', 'gl', 'glhf', 'gmt', 'gmta', 'gn', 'g.o.a.t', 'goat', 'goi', 'gps', 'gr8', 'gratz', 'gyal', 'h&c', 'hp', 'hr', 'hrh', 'ht', 'ibrb', 'ic', 'icq', 'icymi', 'idc', 'idgadf', 'idgaf', 'idk', 'ie', 'i.e', 'ifyp', 'IG', 'iirc', 'ilu', 'ily', 'imho', 'imo', 'imu', 'iow', 'irl', 'j4f', 'jic', 'jk', 'jsyk', 'l8r', 'lb', 'lbs', 'ldr', 'lmao', 'lmfao', 'lol', 'ltd', 'ltns', 'm8', 'mf', 'mfs', 'mfw', 'mofo', 'mph', 'mr', 'mrw', 'ms', 'mte', 'nagi', 'nbc', 'nbd', 'nfs', 'ngl', 'nhs', 'nrn', 'nsfl', 'nsfw', 'nth', 
#  'nvr', 'nyc', 'oc', 'og', 'ohp', 'oic', 'omdb', 'omg', 'omw', 'p.a', 'p.m', 'pm', 'poc', 'pov', 'pp', 'ppl', 'prw', 'ps', 'pt', 'ptb', 'pto', 'qpsa', 'ratchet', 'rbtl', 'rlrt', 'rofl', 'roflol', 'rotflmao', 'rt', 'ruok', 'sfw', 'sk8', 'smh', 'sq', 'srsly', 'ssdd', 'tbh', 'tbs', 'tbsp', 'tfw', 'thks', 'tho', 'thx', 'tia', 'til', 'tl;dr', 'tldr', 'tmb', 'tntl', 'ttyl', 'u', 'u2', 'u4e', 'utc', 'w/', 'w/o', 'w8', 'wassup', 'wb', 'wtf', 'wtg', 'wtpa', 'wuf', 'wuzup', 'wywh', 'yd', 'ygtr', 'ynk', 'zzz']

# # Search for tweets containing the words in the word list
# for word in word_list:
#     tweets = api.search_tweets(q=word, lang='en', count=20)  # You can adjust the count parameter as needed
#     print(f"Tweets containing '{word}':")
#     for tweet in tweets:
#         print(f" - {tweet.text}")
#     print("\n" + "="*30 + "\n")

# search_query = "OR".join(word_list)  # Join words with OR for wider search
# language = "en"  # Adjust for desired language
# count = 100  # Number of tweets to collect

# tweets = tweepy.Cursor(api.search_tweets, q=search_query, lang=language).items(count)


# sentences_with_words = []
# for tweet in tweets:
#     sentence = tweet.text
#     if any(word in sentence for word in word_list):  # Check if any word is present
#         sentences_with_words.append(sentence)


# df = pd.DataFrame({"sentence": sentences_with_words})


user = '@elonmusk'
limit = 10
tweets = api.user_timeline(screen_name = user, count = limit, tweet_mode = 'extended')

for tweet in tweets:
    print(tweet.text)

# client = tweepy.Client(consumer_key= consumer_key,consumer_secret= consumer_secret,access_token= access_token,access_token_secret= access_token_secret)
# query = 'news'
# tweets = client.search_recent_tweets(query=query, max_results=10)
# for tweet in tweets.data:
#     print(tweet.text)