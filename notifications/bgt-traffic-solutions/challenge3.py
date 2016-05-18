"""
How much southbound traffic does the Burke-Gilman get, on average, during Morning commute hours? 
How much does it get during evening commute hours?
"""

import bgt_traffic

morning_commute_hours = ['07:00:00 AM', '08:00:00 AM', '09:00:00 AM']
evening_commute_hours = ['04:00:00 PM', '05:00:00 PM', '06:00:00 PM']

am_sb_totals = []
pm_sb_totals = []


for dkey, dval in bgt_traffic.traffic.items():
    am_sb = 0
    pm_sb = 0
    for hkey, hval in dval.items():
        if hkey in morning_commute_hours:
            am_sb += (hval['ped sb'] + hval['bike sb'])

        elif hkey in evening_commute_hours:
            pm_sb += (hval['ped sb'] + hval['bike sb'])
        else:
            pass
    am_sb_totals.append(am_sb)
    pm_sb_totals.append(pm_sb)           

print("On average, %d people travel south on the Burke-Gilman during morning commute hours." % ((sum(am_sb_totals)/len(am_sb_totals))))

print("On average, %d people travel south on the Burke-Gilman during evening commute hours." % ((sum(pm_sb_totals)/len(pm_sb_totals))))

#this isn't what I expected!
#On average, 118 people travel south on the Burke-Gilman during morning commute hours.
#On average, 203 people travel south on the Burke-Gilman during evening commute hours.
