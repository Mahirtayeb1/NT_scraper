import pandas as pd
from ntscraper import Nitter

scraper = Nitter()

# tweets = scraper.get_tweets('bethTmufc', mode = 'user', number= 5)
# print(tweets)

# tweets = scraper.get_tweets('omg', mode = 'term', number= 5)
# for tweet in tweets['tweets']:
#     print(tweet)
#     print('----------tweet---------')

# taking everything into a list
# final_tweets = []
# tweets = scraper.get_tweets('omg', mode = 'term', number= 5)
# for tweet in tweets['tweets']:
#     data = [tweet['user']['username'], tweet['date'], tweet['text'], tweet['link'], tweet['stats']['comments']]  #, tweet['stats']['comments']
#     final_tweets.append(data)
#     print(final_tweets)

# # using dataframe to vizualize the data

# data = pd.DataFrame(final_tweets, columns= ['user', 'date', 'tweet', 'link', 'no of comments'])  #, 'no of comments'
# print(data)

# creating a function for scraping the tweets
#key= name then mode = "user", key= word/hashtag then mode = 'term'/'hashtag'

def fetch_tweets(key, mode, number_of_tweets):
    tweets = scraper.get_tweets(key, mode = mode, number= number_of_tweets)
    final_tweets = []
    for tweet in tweets['tweets']:
        data = [tweet['user']['username'], tweet['date'], tweet['text'], tweet['link'], tweet['stats']['comments']]  #, tweet['stats']['comments']
        final_tweets.append(data)
        print(final_tweets)
    data = pd.DataFrame(final_tweets, columns= ['user', 'date', 'tweet', 'link', 'no of comments'])  #, 'no of comments'
    return data
data = fetch_tweets('omg', 'term', 10)
print(data)
#taking the data to a csv file
data.to_csv('omg_tweets.csv')