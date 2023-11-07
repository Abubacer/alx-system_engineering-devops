#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    If not a valid subreddit, print None.
    """
    api_url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(api_url, headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    data = response.json()
    posts = data.get('data', {}).get('children', [])
    if posts:
        for count, post in enumerate(posts):
            print("{}".format(post['data']['title']))
    else:
        print("None")
