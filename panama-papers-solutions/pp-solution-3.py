# What hour in the first two weeks had the highest number of edits?
import requests
import json

ENDPOINT = 'https://en.wikipedia.org/w/api.php'

parameters = { 'action' : 'query',
               'prop' : 'revisions',
               'titles' : 'Panama_Papers',
               'format' : 'json',
               'rvdir' : 'newer',
               'rvstart': '2016-04-03T17:59:05Z',
               'rvend' : '2016-04-17T17:59:05Z',
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


# print(json.dumps(days,indent=4))
max_edits = 0
hour_max = []
for dkey, dval in days.items():
    for hkey, hval in dval.items():
        if hval > max_edits:
            max_edits = hval
            hour_max[:] = []
            hour_max.append(dkey + "-" + hkey)
        elif hval == max_edits:
            hour_max.append(dkey + "-" + hkey)
        else:
            pass 

print("The highest number of edits in a single hour was %d" % (max_edits))
print("The hour(s) with the highest number of edits were %s" % (", ".join(hour_max)))