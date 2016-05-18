"""
What was the busiest hour of any day for northbound bike traffic? How about southbound pedestrian traffic?
"""

import bgt_traffic

busiest_bike_nb = []
busiest_bike_count = 0
busiest_ped_sb = []
busiest_ped_count = 0

for dkey, dval in bgt_traffic.traffic.items():
    for hkey, hval in dval.items():
        if hval['bike nb'] > busiest_bike_count:
            busiest_bike_count = hval['bike nb']
            busiest_bike_nb[:] = []
            busiest_bike_nb.append("%s %s %d" % (dkey, hkey, hval['bike nb']))
        elif hval['bike nb'] == busiest_bike_count:
            busiest_bike_nb.append("%s %s %d" % (dkey, hkey, hval['bike nb']))
        else:
            pass              
        if hval['ped sb'] > busiest_ped_count:
            busiest_ped_count = hval['ped sb']
            busiest_ped_sb[:] = []
            busiest_ped_sb.append("%s %s %d" % (dkey, hkey, hval['ped sb']))
        elif hval['ped sb'] == busiest_ped_count:
            busiest_ped_sb.append("%s %s %d" % (dkey, hkey, hval['ped sb']))
        else:
            pass 
                
print("bike: " + ", ".join(busiest_bike_nb))
print("pedestrian: " + ", ".join(busiest_ped_sb))


