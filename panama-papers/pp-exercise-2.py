# Copyright (C) 2016 Ben Lewis, Morten Wang, and Jonathan Morgan
# Licensed under the MIT license, see ../LICENSE

# 2. How many edits has Panama Papers receive from mobile devices in since it was created?

import requests

ENDPOINT = 'https://en.wikipedia.org/w/api.php'

parameters = { 'action' : 'query',
               'prop' : 'revisions',
               'titles' : 'Panama_Papers',
               'format' : 'json',
               'rvprop' : 'tags|timestamp|user',
               'rvdir' : 'newer',
               'rvlimit': 500,
               'rvstart': '2016-04-03T17:59:05Z',
               'rvend' : '2016-05-02T14:53:00Z',

               'continue' : '' }

num_mobile_revisions = 0

done = False
while not done:
    wp_call = requests.get(ENDPOINT, params=parameters)
    response = wp_call.json()

    pages = response['query']['pages']

    for page_id in pages:
        page = pages[page_id]
        revisions = page['revisions']
        for revision in revisions:
            if 'mobile edit' in revision['tags']:
                print(revision['timestamp'] + " " + revision['user'] + ": " + ", ".join(revision['tags']))
                num_mobile_revisions += 1


    if 'continue' in response:
        parameters['continue'] = response['continue']['continue']
        parameters['rvcontinue'] = response['continue']['rvcontinue']
    else:
        done = True

print(parameters['titles'] + ' has had ' + str(num_mobile_revisions) + ' edits from mobile devices since it was created')
