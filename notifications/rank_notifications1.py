from notifications import responses
from notifications import headers

import operator

"""
REMEMBER
There are 8 types of notification that a user can receive
- someone @mentioned you in a discussion
- someone left you a message on your user page
- someone reverted one of your edits
- someone changed your userrights
- someone sent you an email
- someone thanked you for your edit
- someone reviewed an article you created
- someone linked to an article you created
"""

"""
HOW TO USE THIS SCRIPT
To walk through this script and see what's happening at every step, un-comment the commented code below. If you un-comment these statements one at a time (and run the script every time you've un-commented a line), it should give you a good idea of what the data look like at different points in the script.

Now, we want to get a sense of how important each type 
of notification is to our users overall. First we will
create a new dictionary to hold our cumulative ranking counts,
like we did before with seen_counts.

This time, we want to capture more than one value
for each type of notification: we want the totals for each
of the 8 possible rankings. So our new
dictionary needs to be more complex: we will create a
'nested' dictionary: a 'dict of dicts'.
"""
rank_counts = {}
for h in headers:
    if 'rank' in h:
        rank_counts[h] = {}

for i in range(1,9):
    for rank, count in rank_counts.items():
        count[i] = 0
# print(rank_counts)

"""
Our new dictionary looks like this
notification_rank = {
'rank-revert': {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}, 
'rank-message': {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}, 
'rank-rights': {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}, 
'rank-link': {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}, 
'rank-thank': {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}, 
'rank-mention': {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}, 
'rank-review': {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}, 
'rank-email':{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
}

Now we will populate rank_counts with the survey response data.
We'll iterate through the responses, and the ranks for each notification type
within each response, using a double 'for' loop.
Because the keys in our sub-dictionary are the same as the values 
for each rank, every time we find a match, we can increment the value
of the corresponding key.
"""
for res in responses:
    for res_key, res_val in res.items():
        if res_key in rank_counts and res_val != 0: #we don't have a key for 0, so ignore
            rank_counts[res_key][res_val] += 1
# print(rank_counts)

"""
Now we want to determine which notifications are ranked as most important
by the most people. We will iterate through the dictionary again
and count how many people ranked a particular type of notification
in their number 1 priority, then print our responses, sorted from greatest to least.
"""
top_1_counts = {}
for rank_key, rank_val in rank_counts.items():
    top_1_counts[rank_key] = rank_val[1]


# print(top_1_counts)
# print(sorted(top_1_counts.items(), key=operator.itemgetter(1), reverse=True))