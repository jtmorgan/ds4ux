import csv
import encoding_fix
import json

###if you don't have access to the API ####
with open("data/residential_permits_2010-2016.json") as json_infile:
    bp_api_data = json.load(json_infile)

json_infile.close()
   
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







