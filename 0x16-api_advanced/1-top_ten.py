#!/usr/bin/python3
"""Module that queries the Reddit API and returns the titles of the
first top 10 hot posts of a subreddit
"""
import requests

BASE_URL = 'https://www.reddit.com'


def top_ten(subreddit):
    '''Retrieves the title of the top ten posts from a given subreddit.
    '''
    api_headers = {
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
    response = requests.get('{}/r/{}/.json?sort={}&limit={}'.format(
        BASE_URL, subreddit, sort, limit),
        headers=api_headers,
        allow_redirects=False
        )
    if response.status_code == 200:
        for post in response.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
