# Copyright (C) 2016 Ben Lewis, Morten Wang, and Jonathan Morgan
# Licensed under the MIT license, see ../LICENSE

# How many views did Panama Papers have in the first week?
# What proportion of those views came from devices using the mobile web browser?
# documentation https://wikimedia.org/api/rest_v1/?doc

import requests
from urllib.parse import quote

ENDPOINT = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/'

#first, we gather the total views from all devices....
wp_code = 'en.wikipedia'
access = 'all-access'
agents = 'all-agents'
page_title = 'Panama Papers'
period = 'daily'
start_date = '20160403'
end_date = '20160409'

wp_call = requests.get(ENDPOINT + wp_code + '/' + access + '/' + agents + '/' + quote(page_title, safe='') + '/' + period + '/' + start_date + '/' + end_date)
response = wp_call.json()

# print(response)
week1_views = 0
for i,day in enumerate(response['items']):
#     print(response['items'][i])
    daily_views = response['items'][i]['views']
    week1_views += daily_views
    timestamp = response['items'][i]['timestamp']
    print("%s had %d page views on %s" % (page_title, daily_views, timestamp))

print("%s had %d page views in its first week" % (page_title, week1_views))


#next, we gather the views from 'mobile web'....

access = 'mobile-web'
wp_call = requests.get(ENDPOINT + wp_code + '/' + access + '/' + agents + '/' + quote(page_title, safe='') + '/' + period + '/' + start_date + '/' + end_date)
response = wp_call.json()

# print(response)
week1_mobile_views = 0

for i,day in enumerate(response['items']):
#     print(response['items'][i])
    daily_views = response['items'][i]['views']
    week1_mobile_views += daily_views
    timestamp = response['items'][i]['timestamp']
    print("%s had %d page views on %s" % (page_title, daily_views, timestamp))

print("%s had %d mobile web page views in its first week" % (page_title, week1_mobile_views))