import csv
import encoding_fix
import json
import requests

# create a base url for the api request
bp_api_url = "https://data.seattle.gov/resource/mags-97de.json?"

#set parameters that we are passing to the API, to filter the data we want
bp_api_params = {
"$select" : "application_permit_number, applicant_name, address, description, category, value, issue_date, latitude, longitude",
"$where" : "action_type='NEW' AND issue_date IS NOT NULL AND (category='MULTIFAMILY' OR category='SINGLE FAMILY / DUPLEX') AND (status='Permit Issued' OR status='Permit Finaled' OR status='Permit Closed')",
"$order" : "issue_date DESC",
"$limit" : "10000",
}

"""              
The following line is what the requests call is doing, basically. Paste it into your browser and try it!
https://data.seattle.gov/resource/mags-97de.json?$select=application_permit_number, applicant_name, address, description, category, value, applicant_name, issue_date, latitude, longitude&$order=issue_date asc&$where=action_type='NEW' AND issue_date IS NOT NULL AND latitude is not null and (category='MULTIFAMILY' OR category='SINGLE FAMILY / DUPLEX') AND (status='Permit Issued' OR status='Permit Finaled' OR status='Permit Closed')&$limit=10000)
"""
    
#request the data from data.seattle.gov API and store it as JSON
bp_api_req = requests.get(bp_api_url, params=bp_api_params)
bp_api_data = bp_api_req.json()

#save the JSON object as a file, so we can use it later
with open('data/residential_permits_2010-2016.json', 'w') as json_outfile:
    json.dump(bp_api_data, json_outfile)

json_outfile.close()

#read through the JSON file line by line and write it to CSV    
with open('data/residential_permits_2010-2016.csv', 'w') as csv_outfile:
    writer = csv.writer(csv_outfile)

    #first write the titles that will appear at the head of each column in the CSV
    writer.writerow(('permit id', 'applicant','address', 'description', 'category', 'value', 'issue date', 'latitude', 'longitude'))
    for x in bp_api_data:
        try:
            #rmv the time from the date/time stamp
            x['issue_date'] = x['issue_date'][:10]
        
            #write the data for each permit application onto a single row in the CSV 
            writer.writerow((x['application_permit_number'], x['applicant_name'], x['address'], x['description'], x['category'], x['value'], x['issue_date'], x['latitude'], x['longitude']))
        except:
            continue
csv_outfile.close()







