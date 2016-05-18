import csv
from notifications import responses
import operator

"""
In this example, we'll do everything exactly the same
as in rank_notifications1.py, EXCEPT:
- we will look at which notifications were included most often
  among the top 3 ranks, instead of just the first-ranked notification
- we will print our results to the terminal in a more reader-friendly format
- we will export our results to a CSV file

HOW TO USE THIS SCRIPT
To walk through this script and see what's happening at every step, un-comment the commented code below. If you un-comment these statements one at a time (and run the script every time you've un-commented a line), it should give you a good idea of what the data look like at different points in the script.
"""

"""same as rank_notifications1.py"""
rank_counts = {}
for res_key in responses[0].keys():
    if 'rank' in res_key:
        rank_counts[res_key] = {}        

for i in range(1,9):
    for rank, count in rank_counts.items():
        count[i] = 0
# print(rank_counts)

"""same as notifications1.py"""
for res in responses:
    for res_key, res_val in res.items():
        if res_key in rank_counts and res_val != 0: #we don't have a key for 0, so ignore
            rank_counts[res_key][res_val] += 1
# print(rank_counts)

"""
***NEW FOR THIS SCRIPT!***
Now we want to determine which notifications are ranked as one of the
TOP 3 most important types by the most people. Like before, we will iterate 
through the dictionary and count how many people ranked 
a particular type of notification in the top 3. 

We'll store the results in a list, so that we can print and save them in order.
"""

top_3_counts = {}
for rank_key, rank_val in rank_counts.items():
    top_3_count = 0
    total_count = 0
    percent_top_3 = 0
    for i in range(1,4):
        top_3_count += rank_val[i]
    total_count = sum(rank_val.values())
    percent_top_3 = round((top_3_count/total_count) * 100,0)    
    top_3_counts[rank_key] = [top_3_count, total_count, percent_top_3]
# print(top_3_counts)    

sorted_top_3_counts = sorted(top_3_counts.items(), key=lambda i: i[1][2], reverse=True)
# print(sorted_top_3_counts)

"""
Let's print these to the terminal in a format that's easy to read and analyze.
"""
for n in sorted_top_3_counts:
    print("'%s' notifications" % (n[0][5:]))
    print("\t%d respondents included this notification in their rankings" % (n[1][1]))
    print("\t%d respondents ranked this notification in their top 3" % (n[1][0]))    
    print("\t%d%% ranked this notification in their top 3" % (n[1][2]))
    print("\n")
    
"""
It's cool to print a formatted report to the terminal, but what if we wanted
to save it to a file for later analysis? We'll use the CSV 'writer' function
to copy our results into a new CSV file, one line at a time, starting with
the column header names we want to use. 
"""
with open('most_important_notifications.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(('notification type', 'num ranked', 'num top 3', 'percent top 3'))
    for n in sorted_top_3_counts: 
        writer.writerow((n[0], n[1][1], n[1][0], str(n[1][2]) + "%"))