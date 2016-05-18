"""
What day between January 1, 2014 and March 31, 2016 saw the most total traffic on the Burke-Gilman trail?
"""

import bgt_traffic

busiest_day = []
busiest_day_traffic = 0

for dkey, dval in bgt_traffic.traffic.items():
    daily_traffic = 0
    for hval in dval.values():
        daily_traffic += hval['total']
    if daily_traffic > busiest_day_traffic:
        busiest_day_traffic = daily_traffic
        busiest_day[:] = []
        busiest_day.append("%s %d" % (dkey, daily_traffic))        
    elif daily_traffic == busiest_day_traffic:
        busiest_day.append("%s %d" % (dkey, daily_traffic))        
    else:
        pass      

print("busiest day(s): " + ", ".join(busiest_day))