# Write a script that generates daily page view counts for Panama Papers on German (de.wikipedia.org), English (en.wikipedia.org), and Spanish (es.wikipedia.org) Wikipedias. Output your results to CSV and graph them per the instructions for Challenge #6 above.

# Write a script that generates daily page view counts for Panama Papers, broken down by desktop and mobile (app + web) access methods over its first 30 days of existence, output them to a CSV file that you can open in Excel or a similar spreadsheet program. 

import csv
import requests
from urllib.parse import quote

ENDPOINT = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/'

access = 'all-access'
agents = 'all-agents'
page_title = 'Panama Papers'
period = 'daily'
start_date = '20160403'
end_date = '20160502'


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
        dv = [day['timestamp'],day['views']]
        daily_views.append(dv)
    return daily_views


##MAIN###
en_views = requestData(ENDPOINT,'en.wikipedia', access, agents, page_title, period, start_date, end_date)

es_views = requestData(ENDPOINT,'es.wikipedia', access, agents, page_title, period, start_date, end_date)

de_views = requestData(ENDPOINT,'de.wikipedia', access, agents, page_title, period, start_date, end_date)


with open('pp30days_en_es_de_views.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(('date', 'English Wikipedia', 'Spanish Wikipedia', 'German Wikipedia'))
    for i,d in enumerate(en_views): 
        writer.writerow((d[0], d[1], es_views[i][1], de_views[i][1]))

