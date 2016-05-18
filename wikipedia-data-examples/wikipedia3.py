"""
What articles are in the category "Programming Languages created in 1991"?
Category page here: https://en.wikipedia.org/wiki/Category:Programming_languages_created_in_1991
Documentation here: https://www.mediawiki.org/wiki/API:Categorymembers
"""

import encoding_fix
import requests

parameters = {'action' : 'query',
              'list' : 'categorymembers',
              'format' : 'json',
              'cmtitle' : 'Category:Programming languages created in 1991'}

wp_call = requests.get('http://en.wikipedia.org/w/api.php', params=parameters)

response = wp_call.json()

for page in response['query']['categorymembers']:
    print(page['title'])
