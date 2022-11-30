#!/usr/bin/python3
"""prints the titles of the first 10 hot posts """
from requests import get


def top_ten(subreddit):
    """
    A function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit
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
        print(None)
        return None

    try:
        js = re.json()

    except ValueError:
        print(None)
        return None

    try:
        data = js.get("data")
        children = data.get("children")
        for child in children[:10]:
            post = child.get("data")
            print(post.get("title"))

    except:
        print(None)
