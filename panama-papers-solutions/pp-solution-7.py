# Write a script that generates daily page view counts for Panama Papers, broken down by desktop and mobile (app + web) access methods over its first 30 days of existence, output them to a CSV file that you can open in Excel or a similar spreadsheet program. 

import csv
import requests
from urllib.parse import quote

ENDPOINT = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/'

def requestData(ENDPOINT, wp_code, access, agents, page_title, period, start_date, end_date):
    daily_views = []
    wp_call = requests.get(
        ENDPOINT 
        + wp_code 
        + '/' + access 
        + '/' + agents 
        + '/' + quote(page_title, safe='') 
        + '/' + period 
        + '/' + start_date 
        + '/' + end_date
        )    
    response = wp_call.json()
    for day in response['items']:
        dv = [day['timestamp'],day['access'],day['views']]
        daily_views.append(dv)
    return daily_views


##MAIN###
desktop_views = requestData(ENDPOINT,'en.wikipedia','desktop','all-agents','Panama_Papers','daily','20160403','20160502')
print(desktop_views)

mobile_web_views = requestData(ENDPOINT,'en.wikipedia','mobile-web','all-agents','Panama_Papers','daily','20160403','20160502')

mobile_app_views = requestData(ENDPOINT,'en.wikipedia','mobile-app','all-agents','Panama_Papers','daily','20160403','20160502')

with open('pp30days_desktop_mobile_views.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(('date', 'desktop views', 'mobile views'))
    for i,d in enumerate(desktop_views): 
        all_mobile = mobile_web_views[i][2] + mobile_app_views[i][2]
        writer.writerow((d[0], d[2], all_mobile,))

