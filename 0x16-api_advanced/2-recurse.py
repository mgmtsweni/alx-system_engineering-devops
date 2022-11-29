#!/usr/bin/python3
"""recursive function that returns list of hot articles"""
from requests import get


def recurse(subreddit, hot_list=[], after= None):
    """
    recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit, after)
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

    if subreddit is None:
        return None

    req = get(url, headers=headers, allow_redirects=False).json()
    if req.status_code == 200:
        top = req.json()
        key = top['data']['after']
        parent = top['data']['children']

        for obj in parent:
            hot_list.append(obj['data']['title'])

        if key is not None:
            recurse(subreddit, hot_list, key)
        return hot_list
    else:
        return None
