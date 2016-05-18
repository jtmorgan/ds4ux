"""
Which gets more inbound bike traffic per day, on average—the Burke-Gilman trail or the Mountain to Sound trail?
"""

import bgt_mts_traffic

daily_inbound_totals = [[],[]] #preserve the original order in our new list-of-lists for daily totals: BGT is index 0, MTS is index 1
for i, t in enumerate(bgt_mts_traffic.both_trails_traffic):
    for dkey, dval in t.items():
        inbound_ped = 0
        inbound_bike = 0
        for hval in dval.values():
            if i == 0: #we're looking at the BGT dataset
                inbound_ped += hval['Ped South']
                inbound_bike += hval['Bike South']
            elif i == 1: #we're looking at the MTS dataset
                inbound_ped += hval['Ped West']
                inbound_bike += hval['Bike West'] 
            else: #including this is optional, but recommended
                pass       
        daily_inbound_totals[i].append(inbound_bike + inbound_ped)

bgt_inbound_avg = sum(daily_inbound_totals[0])/len(daily_inbound_totals[0])
mts_inbound_avg = sum(daily_inbound_totals[1])/len(daily_inbound_totals[1])

print("On average, %d people travel inbound on the Burke-Gilman trail each day." % (bgt_inbound_avg))
print("On average, %d people travel inbound on the Mountain-to-Sound trail each day." % (mts_inbound_avg))

