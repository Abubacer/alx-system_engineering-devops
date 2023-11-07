#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing the titles of all hot
articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    Returns a list of the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, return None.
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
    hot_list += [child["data"]["title"] for child in children]
    if "count" in data["data"]:
        count = data["data"]["count"]
    else:
        count = None

    if not data["data"]["after"]:
        return hot_list

    return recurse(subreddit, hot_list, count, data["data"]["after"])
