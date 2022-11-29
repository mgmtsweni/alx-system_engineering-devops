#!/usr/bin/python3
""" How many subs? """
from requests import get


def number_of_subscribers(subreddit):
    """ Returns subscriber count of subreddit or 0 """
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

    res = get(url, headers=headers, allow_redirects=False)
    subscribers = res.get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    return subscribers
