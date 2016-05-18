"""
How many people walked or rode northbound during April 1, 2015?
"""

import bgt_traffic

april_1 = bgt_traffic.traffic.get('04/01/2015')

nb_total = 0
for h_key, h_val in april_1.items():
    nb_total += h_val['ped nb']
    nb_total += h_val['bike nb']    
        
print(nb_total)