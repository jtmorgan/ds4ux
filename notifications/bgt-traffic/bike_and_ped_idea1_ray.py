"""
How many people walked northbound on the BGT between 6 and 7 AM on August 28, 2014?
"""

import bgt_traffic
import json

dict_temp = bgt_traffic.traffic

#print(json.dumps(dict_temp, indent = 4))
print(json.dumps(dict_temp["06/09/2015"]["10:00:00 PM"]["total"], indent = 4))

for key, value in dict_temp.items():
	temp_list = key.split('/');
	print ("first:" + temp_list[0] + ",second:" + temp_list[1] + ",third:" + temp_list[2])
	
	if temp_list[2] == "2015":
		if temp_list[0] == "09" or temp_list[0] == "10":
			#do someting
	if temp_list[0] == "09": and temp_list[2] == "2015":
		for key2, value2 in dict_temp[key]
		# adding one for loop that iterate with time e.g., 10:00 - 11: 00 12: 0..
		 	#I will get the toll of e.g. nb ped nb cycle

	#if key == "06/09/2015":
	#	for key2, value2 in dict_temp[key].items():
	#		if key2 == "10:00:00 PM":
	#			print(dict_temp[key][key2]["total"])



#print(json.dumps(dict_temp["09/13/2015"]["06:00:00 PM"], indent = 4))

#print(bgt_traffic.traffic['08/20/2014']['06:00:00 AM']['ped nb'])
