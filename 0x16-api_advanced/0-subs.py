#!/usr/bin/python3
"""queries the Reddit API for all subscribers"""
from requests import get


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and 
    returns the number of subscribers (not active users
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

    re = get(url, headers=headers, allow_redirects=False)

    if re.status_code != 200:
        return 0
    try:
        js = re.json()
    except ValueError:
        return 0

    results = js.get("results")
    if results:
        subscribers = results.get("subscribers")
        if not subscribers:
            return 0
    return subscribers
