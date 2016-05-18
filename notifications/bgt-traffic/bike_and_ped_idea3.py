"""
Which hour during November 11, 2015 saw the most overall traffic?
"""

import bgt_traffic

nov_11 = bgt_traffic.traffic.get('11/11/2015')

busiest_hour = ""
most_traffic = 0

for h_key, h_val in nov_11.items():
    traffic = h_val['total']
    if traffic >  most_traffic:
        busiest_hour = h_key
        most_traffic = traffic     

print("%s experienced the most overall traffic, with a total of %d people" % (busiest_hour, most_traffic))