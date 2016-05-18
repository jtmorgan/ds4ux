# Copyright (C) 2016 Ben Lewis, Morten Wang, Nathan TeGrotenhuis, and Jonathan Morgan

# How many edits per day did Panama Papers receive, on average, in its first two weeks?
import requests

ENDPOINT = 'https://en.wikipedia.org/w/api.php'

parameters = { 'action' : 'query',
               'prop' : 'revisions',
               'titles' : 'Panama_Papers',
               'format' : 'json',
               'rvdir' : 'newer',
               'rvstart': '2016-04-03T00:00:00Z',
               'rvend' : '2016-04-17T00:00:00Z',
               'rvlimit' : 500,
               'continue' : '' }

days = {}

done = False
while not done:
    wp_call = requests.get(ENDPOINT, params=parameters)
    response = wp_call.json()

    pages = response['query']['pages']
    
    for page_id in pages:
        page = pages[page_id]
        revisions = page['revisions']
        for rev in revisions:
            revday = rev['timestamp'][5:10]
            revhour = rev['timestamp'][11:13]            
            if revday in days.keys():
                if revhour in days[revday].keys():
                    days[revday][revhour] += 1
                else:
                    days[revday][revhour] = 1
            else:
                days[revday] = {}
                days[revday][revhour] = 1

    if 'continue' in response:
        parameters['continue'] = response['continue']['continue']
        parameters['rvcontinue'] = response['continue']['rvcontinue']
    else:
        done = True


# print(days)
edits_per_day = []
for dkey, dval in days.items():
    daily_edits = 0
    for hkey, hval in dval.items():
        daily_edits += hval
    edits_per_day.append(daily_edits)

# print(edits_per_day)
avg_daily_edits = round(sum(edits_per_day)/14,1)

print("There were %r edits per day during the first two weeks." % (avg_daily_edits))