#!/usr/bin/python3
"""Reddit API for the total number of subscribers"""
from requests import get


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and
    returns the number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}

    req = get(url, headers=headers, allow_redirects=False).json()
    subscribers = req.get('data', {}).get('subscribers')
    if not subscribers or type(subscribers) is not str:
        return 0
    return subscribers
