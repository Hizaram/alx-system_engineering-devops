#!/usr/bin/python3
"""A module that contains functions that deal with Reddit API"""
import requests

BASE_URL = 'https://www.reddit.com'


def number_of_subscribers(subreddit):
    """Retrieves the number of subscribers in a subreddit"""
    api_headers = {
            'Accept': 'application/json',
            'User-Agent': ' '.join([
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'AppleWebKit/537.36 (KHTML, like Gecko)',
                'Chrome/97.0.4692.71',
                'Safari/537.36',
                'Edge/97.0.1072.62'
                ])
            }
    response = requests.get(
            '{}/r/{}/about/.json'.format(BASE_URL, subreddit),
            headers=api_headers,
            allow_redirects=False
            )
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
