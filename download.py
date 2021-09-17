"""Twitter API docs: https://bit.ly/3CsGy5P"""


import os
import re
import json
import tweepy as tw
import pandas as pd

DATE_START = "01-07-2021"


class Twitter:
    def __init__(self):
        with open('keys.json') as f:
            keys = json.load(f)

        self.auth = tw.OAuthHandler(
            keys["consumer_key"], keys["consumer_secret"])
        self.auth.set_access_token(
            keys["access_token"], keys["access_token_secret"])
        self.api = tw.API(self.auth, wait_on_rate_limit=True)

    def get_keywords(self):
        with open('keywords.json') as f:
            keywords = json.load(f)

        return keywords

    # Define the search term and the date_since date as variables
    def download(self, keyword: str, date_start: str, filter_retweets: bool = True):
        """Downloads all tweets that contain a keyword from date_start.
        The API looks for substrings (not whole words) which simplifies
        searching for Icelandic's complicated conjucation

        Args:
            keyword (str): the keyword to be searched for
            date_start (str): Starting date for searches, dd-mm-yyyy
            filter_retweets (bool, optional): Whether to omit retweets or not. Defaults to True.

        Returns:
            tweets (list): A list containing all  
        """

        query = keyword
        if filter_retweets:
            query += ' -filter:retweets'

        # Collect tweets
        tweets = tw.Cursor(self.api.search,
                           q=query,
                           since=date_start)

        return tweets
