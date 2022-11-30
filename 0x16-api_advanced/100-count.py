#!/usr/bin/python3
""" Count it titles of all hot articles"""
from requests import get


def count_words(subreddit, word_list, after="", instances={}):
    """
    A Function of a list containing the titles of all hot articles
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

    if not instances:
        for word in word_list:
            instances[word] = 0

    if after is None:
        word_list = [[key, value] for key, value in instances.items()]
        word_list = sorted(word_list, key=lambda x: (-x[1], x[0]))
        for w in word_list:
            if w[1]:
                print("{}: {}".format(w[0].lower(), w[1]))
        return None

    params = {
        'limit': 100,
        'after': after
    }

    r = get(url, headers=headers, params=params, allow_redirects=False)

    if r.status_code != 200:
        return None

    try:
        data = r.json().get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            title = child.get("data").get("title")
            lower = [s.lower() for s in title.split(' ')]

            for w in word_list:
                instances[w] += lower.count(w.lower())

    except ValueError:
        return None

    return count_words(subreddit, word_list, after, instances)
