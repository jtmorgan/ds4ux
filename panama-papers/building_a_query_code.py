"""
This script reproduces the steps in this lecture: https://github.com/makoshark/wikipedia-cdsw/blob/master/building-a-query.md

It starts with this API query: https://en.wikipedia.org/w/api.php?action=query&prop=links&titles=User:Zen-ben&continue=&format=json

#Consult this documentation
* https://www.mediawiki.org/wiki/API:Links
* https://www.mediawiki.org/wiki/API:Query
"""

import requests
ENDPOINT = 'https://en.wikipedia.org/w/api.php'

"""
Building a basic API call
"""
wp_call = requests.get(ENDPOINT + '?'
    + 'action=query&'
    + 'prop=links&'
    + 'titles=User:Zen-ben&'
    + 'continue=&'
    + 'format=json')

response = wp_call.json()

"""
Parsing the results of an API request
"""

print(response.keys())

print(type(response['query']))

print(response['query'].keys())

pages = response['query']['pages']
print(type(pages))

user_page = pages['44376332']
print(type(user_page['links']))
print(type(user_page['links'][0]))

for page in response['query']['pages']:
    print(response['query']['pages'][page]['title'])

for page in response["query"]["pages"]:
    for link in response["query"]["pages"][page]['links']:
        print(link['title'])


"""
Building a parameterized API call
"""
parameters = {'action' : 'query',
              'prop' : 'links',
              'titles' : 'User:Zen-ben|User:Benjamin Mako Hill',
              'format' : 'json',
              'continue' : ''}

wp_call = requests.get(ENDPOINT, params=parameters)


"""
Using a while loop to continue making API requests until all the data is delivered
"""
page_links = {}
while True:
    wp_call = requests.get(ENDPOINT, params=parameters)
    response = wp_call.json()

    for page in response['query']['pages']:
        page_title = response['query']['pages'][page]['title']
        if page_title not in page_links:
            page_links[page_title] = []
        if 'links' in response['query']['pages'][page]:
            page_links[page_title].extend(response['query']['pages'][page]['links'])

    if 'continue' in response:
        parameters['continue'] = response['continue']['continue']
        parameters['plcontinue'] = response['continue']['plcontinue']
    else:
        break

for pl_key, pl_vals in page_links.items():
    print(pl_key)
    for v in pl_vals:
        print(v['title'])
    print("\n")
