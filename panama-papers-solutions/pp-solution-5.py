# documentation https://wikimedia.org/api/rest_v1/?doc

# What day in the first two weeks had the most views?
import requests
import json
from urllib.parse import quote

ENDPOINT = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/'

#first, we gather the total views from all devices....
wp_code = 'en.wikipedia'
access = 'all-access'
agents = 'all-agents'
page_title = 'Panama Papers'
period = 'daily'
start_date = '20160403'
end_date = '20160417'

wp_call = requests.get(ENDPOINT + wp_code + '/' + access + '/' + agents + '/' + quote(page_title, safe='') + '/' + period + '/' + start_date + '/' + end_date)
response = wp_call.json()

# print(json.dumps(response, indent=4))

max_views = 0
max_view_days = []
for day in response['items']:
    if day['views'] > max_views:
        max_views = day['views']        
        max_view_days[:] = []
        max_view_days.append(day['timestamp'])        
    elif day['views'] == max_views:
        max_view_days.append(day['timestamp'])

print("%s had the most page views, with %d views." % (", ".join(max_view_days), max_views))