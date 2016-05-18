import csv
import encoding_fix
import json
from operator import itemgetter
import requests

# load in the JSON file we created with download_building_permit_data.py
with open("data/residential_permits_2010-2016.json") as json_infile:
    bp_api_data = json.load(json_infile)   

json_infile.close()

# create an empty dictionary that will hold our per-month counts
permits_by_month = {}

# go through the JSON data. Tally up permits per month.
for x in bp_api_data:

    # get just the year and month from each datetime. It's always the first 7 characters
    month_string = x['issue_date'][0:7] #2012-03
    if month_string in permits_by_month:
        permits_by_month[month_string] = permits_by_month[month_string] + 1
    else:
        permits_by_month[month_string] = 1
 #   looks like: {'2010-11':1, '2010-12':1, 2011-01, '}    

# print the total number of permits issued for all months
print(sum(permits_by_month.values()))

# transfer our data from a dictionary to a list of dictionaries, so we can sort it easier
# I'm using a technique called 'list comprehension' here, to simplify my code.
# Read more about it here: http://www.pythonforbeginners.com/basics/list-comprehensions-in-python
monthly_counts_list = [[k,v] for k,v in permits_by_month.items()]

 #   looks like: [[2010-11,1], [2011-07,3], ...]

# sort that list chronologically by month
sorted_monthly_counts_list = sorted(monthly_counts_list, key=itemgetter(0))

# print out our monthly counts to the terminal window
for x in sorted_monthly_counts_list:
    print(x[0] + " " + str(x[1])) 

# store our monthly counts in a CSV file
with open('data/residential_by_month_2010-2016_by_num_permits.csv', 'w') as csv_outfile:
    writer = csv.writer(csv_outfile)
    writer.writerow(('month', 'permits issued'))
    for x in sorted_monthly_counts_list: 
        writer.writerow((x[0],x[1]))

csv_outfile.close()


