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

#create an empty dictionary that will hold our edit counts by day and by hour
days = {}

#while loop to keep grabbing revisions until we've got them all
done = False
while not done:
    wp_call = requests.get(ENDPOINT, params=parameters)
    response = wp_call.json()

    pages = response['query']['pages']
    
    for page_id in pages:
        page = pages[page_id]
        revisions = page['revisions']
        #for each revision, we will use string slicing to grab the day and the hour
        #from the timestamp, and save them as separate variables
        for rev in revisions:
            revday = rev['timestamp'][5:10]
            revhour = rev['timestamp'][11:13]
            #start adding individual days and hours to our dictionary 'day'. 
            #have we seen any revisions from this day before? 
            if revday in days.keys():
                #have we seen any revisions from this hour of this day before?
                #if so, increment the value for this hour, since we just saw another!
                if revhour in days[revday].keys():
                    days[revday][revhour] += 1
                #if not, create a dictionary inside this day for this hour, and give it
                #a value of 1, since we've seen one revision from this hour
                else:
                    days[revday][revhour] = 1
            else:
            #if we haven't seen any revisions from that day yet,
            #add that day as a new key in 'days', and add a key/value to THAT day's 
            #dictionary for the hour of the revision we just found.
                days[revday] = {}
                days[revday][revhour] = 1

    if 'continue' in response:
        parameters['continue'] = response['continue']['continue']
        parameters['rvcontinue'] = response['continue']['rvcontinue']
    else:
        done = True

print(json.dumps(days, indent=4))