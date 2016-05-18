from notifications import responses
from notifications import headers


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

HOW TO USE THIS SCRIPT
To walk through this script and see what's happening at every step, un-comment the commented code below. If you un-comment these statements one at a time (and run the script every time you've un-commented a line), it should give you a good idea of what the data look like at different points in the script.
"""

"""
We want to calculate how many people have seen each type of notification.
We'll find all the 'seen'-related keys, and make a new dictionary to hold our counts.

Since all responses have the same set of keys in them,
we only have to look at one response to get them all.
"""
seen_counts = {}
for h in headers:
    if 'seen' in h:
        seen_counts[h] = 0
# print(seen_counts)

"""
The new dictionary we made looks like this:
seen_counts = {
'seen-revert': 0, 
'seen-message': 0, 
'seen-rights': 0,
'seen-link': 0, 
'seen-thank': 0, 
'seen-mention': 0, 
'seen-review': 0, 
'seen-email': 0
}

Now, we want to iterate through the responses
and add the values to the totals in seen_counts.
If a user indicated that they'd seen this type 
of notification before, there will be a 1 in the dict value
if they havne't seen it, the value will be 0.
"""
for res in responses:
    for res_key, res_val in res.items():
        if res_key in seen_counts:
            seen_counts[res_key] += res_val #new trick!
# print(seen_counts)

"""
What if we wanted to sort the dictionary in order,
from most seen to least? Dictionaries don't have any
inherent order to them, but we can create a sorted
VERSION of the dictionary using the 'operator' module.
"""
import operator

sorted_seen_counts = sorted(seen_counts.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_seen_counts)

# sorted_seen_counts[0][1] = 1000
"""
Notice that our new, sorted version of seen_counts
isn't a dictionary anymore, it's a list of tuples.

Since our data is in a list now, we can easily iterate through it
using a 'for' loop, and print out the items IN ORDER
from most seen to least seen.

NOTE:Since individual items in sorted_seen_counts are tuples, you can't re-assign these values. Try un-commenting line 66 above, and see what happens! 
"""
for c in sorted_seen_counts:  
    n_type = c[0][5:]
    n_seen = c[1]
#     print("Number of respondents who have received '%s' notifications: %d" % (n_type, n_seen))      

"""
These raw counts are interesting, but it would be 
more useful to know what % of respondents had reported
seeing each type of notification.
"""
# for seen_count in sorted_seen_counts:
#     n_type = seen_count[0][5:]
#     percent_of_total = (seen_count[1]/len(responses)) * 100
#     percent_of_total_rounded = round(percent_of_total, 0)
#     print("Percent of respondents who have received '%s' notifications: %d%%" % (n_type, percent_of_total_rounded)) #double '%' escapes     
