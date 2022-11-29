#!/usr/bin/python3
"""Reddit API for the total number of subscribers"""
from requests import get


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and
    returns the number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }

    req = get(url, headers=headers, allow_redirects=False).json()
    subscribers = req.get('data', {}).get('subscribers')
    if not subscribers or type(subscribers) is not str:
        return 0
    return subscribers
