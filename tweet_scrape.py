import snscrape.modules.twitter as sntwitter
import pandas as pd
from tqdm.notebook import tqdm

scraper = sntwitter.TwitterSearchScraper("#python")

for tweet in scraper.get_items():
    break

print(tweet)
