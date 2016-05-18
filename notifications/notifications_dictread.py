import csv

"""
There are 8 types of notification that a user can receive
- someone @mentioned you in a discussion
- someone left you a message on your user page
- someone reverted one of your edits
- someone changed your userrights
- someone sent you an email
- someone thanked you for your edit
- someone reviewed an article you created
- someone linked to an article you created

STEP 1: read in the data file, and save each row as a dictionary
inside the list 'responses'.

To do this, we're using a special function of the csv module called 'Dictreader'.
DictReader has a handy feature that csv.reader doesn't have: 
it allows you to automatically use the row headers of your csv file
as the keys for the resulting dictionaries.
"""
responses = []
notifications_data = csv.DictReader(open("notifications_ranking_survey_data1.csv"), delimiter=',', quotechar='"')

for row in notifications_data:
#     print(type(row)) 
    responses.append(row)
# print(responses)

"""
STEP 2: now we have a list of dictionaries, but there are two problems:
1) all values are stored as strings (e.g. '1','2'), not integers
2) some values are empty strings ('')

So, let's convert these values to integers so that we can use them like numbers.
We'll replace any empty values we find with the number 0,
so that it's easier to parse them later.
"""
for res in responses:
    for res_key, res_val in res.items():
        if len(res_val) > 0:
            res[res_key] = int(res_val)
        else:
            res[res_key] = 0

# print(responses)