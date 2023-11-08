#!/usr/bin/python3
"""
Queries the Reddit API, parses the titles of all hot articles, and prints
a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, count={}, after=None):
    """
    Recursively queries the Reddit API, parses the titles of hot articles,
    and prints a sorted count of given keywords.
    """
    if not subreddit:
        return None
    api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(api_url, headers={"User-Agent": "My-User-Agent"},
                            params={"count": count, "after": after},
                            allow_redirects=False)

    if response.status_code >= 400:
        return None

    data = response.json()
    children = data["data"]["children"]
    for child in children:
        title = child["data"]["title"].lower()
        for w in word_list:
            w = w.lower()
            if w in count:
                count[w] += title.count(w)
            else:
                count[w] = title.count(w)
    after = data["data"]["after"]
    if after:
        return count_words(subreddit, word_list, count, after)

    sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    for keyword, keyword_count in sorted_count:
        print("{}: {}".format(keyword, keyword_count))
