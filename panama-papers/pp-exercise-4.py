# Copyright (C) 2016 Ben Lewis, Morten Wang, and Jonathan Morgan
# Licensed under the MIT license, see ../LICENSE

# Exercise 4:
# How many other articles has User:Czar edited on Wikipedia since they created Panama Papers?
import requests

ENDPOINT = 'https://en.wikipedia.org/w/api.php'

parameters = { 'action' : 'query',
               'list' : 'usercontribs',
               'titles' : 'Panama_Papers',
               'ucuser' : 'Czar',
               'format' : 'json',
               'ucdir' : 'newer',
               'ucnamespace' : 0,
               'ucprop':'title',
               'uclimit': 500,
               'ucstart': '2016-04-03T17:59:05Z',
               'ucend' : '2016-05-01T00:00:00Z',
               'continue' : '' }


pages_edited = []

done = False
while not done:
    wp_call = requests.get(ENDPOINT, params=parameters)
    response = wp_call.json()

    contribs = response['query']['usercontribs']
    for contrib in contribs:
        if contrib['title'] not in pages_edited:
            pages_edited.append(contrib['title'])
            print(contrib['title'])
        else:
            pass

    if 'continue' in response:
        parameters['continue'] = response['continue']['continue']
        parameters['uccontinue'] = response['continue']['uccontinue']
    else:
        done = True

print(parameters['ucuser'] + " has edited " + str(len(pages_edited)) + " articles since they created Panama Papers")
