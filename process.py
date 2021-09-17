class Process:
    def __init__(self):
        # This class is very utilitarian
        pass

    def _remove_url(self, tweet):
        """Removes URLs from tweets because they might contain duplicates of keywords.

        Args:
            tweet (str): The tweet from which the URL is to be removed

        Returns:
            The tweet without URLs
        """

        return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet).split())

    def _make_lowercase(self, tweet):
        """Makes all tweets lowercase to be able to sort"""

    def _remove_duplicates(self):
        """Removes duplicate tweets (due to containing two, or more, keywords"""

    def _word_popularity(self):
        """Create a one big list, make it unique and count the occurrence of each word"""


# TODO: Athuga hvort að tístin leiti eftir orðum eða substrings (get þá leita eftir færri, styttri strengjum)
