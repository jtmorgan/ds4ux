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
inside the list 'raw_responses'.
"""
raw_responses = []
with open("notifications_ranking_survey_data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
#         print(row)
        raw_responses.append(row)
# print(responses)

"""
Now we will transform our data into a list of dictionaries.
"""

headers = raw_responses[0]
# print(titles)

"""
Now that we've stored the column headers in the headers variable above, we can remove the first row from our list (responses), since we don't need it anymore.
"""
del raw_responses[0]

# print(responses)

"""
We'll add 0's anywhere we find an empty value, and make scores ints so we can add them together later.
"""

for r in raw_responses:
    for i in range(0,17): #new concept!
        if len(r[i]) == 0:
            r[i] = 0
        else:
            r[i] = int(r[i])

# print(raw_responses)

"""
For the final step in structuring our data, we will iterate through the list responses and turn each item into a dictionary, using the CSV row columns (which we've saved in the variable headers) as the keys for each value.

We are keeping responses a list, even though the individual items are dictionaries. We're doing this primarily because lists preserve ORDER, while dictionaries don't. Our response_ids are sequential, so it makes sense to store them in the order they were submitted (even if we don't plan on doing anything with them in order right now).
"""

responses = []
for r in raw_responses:
    r_diction = dict(zip(headers, r))
    responses.append(r_diction)
# print(responses)
