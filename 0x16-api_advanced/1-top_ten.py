#!/usr/bin/python3
"""prints the titles of the first 10 hot posts """
from requests import get


def top_ten(subreddit):
    """Retrieves the title of the top ten posts from a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot".format(subreddit)
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
    sort = 'top'
    limit = 10
    res = get(
        '{}/r/{}/.json?sort={}&limit={}'.format(
            url,
            sort,
            limit
        ),
        headers=headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        for post in res.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)