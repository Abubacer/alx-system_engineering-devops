#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing the titles of all hot
articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], count=None, after=None):
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
    data = response.json()
    posts = data.get('data', {}).get('children', [])
    if posts:
        for post in posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        if not after:
            return hot_list

        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
