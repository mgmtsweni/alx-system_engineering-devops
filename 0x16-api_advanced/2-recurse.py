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

    params = {
        'limit': 100,
        'after': after
    }

    re = get(url, headers=headers, params=params, allow_redirects=False)
    
    if re.status_code != 200:
        return None

    try:
        js = re.json()

    except ValueError:
        return None

    try:

        data = js.get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            post = child.get("data")
            hot_list.append(post.get("title"))

    except:
        return None

    return recurse(subreddit, hot_list, after)