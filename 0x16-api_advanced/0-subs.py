#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function return 0.
    """
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(api_url, headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    data = response.json()
    if "data" in data and "subscribers" in data["data"]:
        return data["data"]["subscribers"]
    else:
        return 0
