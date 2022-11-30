#!/usr/bin/python3
from requests import get
"""Query Reddit API recursively for all hot articles"""


def recurse(subreddit, hot_list=[], after="tmp"):
    """
    A funtion that returns all hot articles for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
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

    if after != "tmp":
        url = url + "?after={}".format(after)
    res = get(url, headers=headers, allow_redirects=False)

    results = res.json().get('data', {}).get('children', [])
    if not results:
        return hot_list
    for i in results:
        hot_list.append(i.get('data').get('title'))

    after = res.json().get('data').get('after')
    if not after:
        return hot_list
    return (recurse(subreddit, hot_list, after))
