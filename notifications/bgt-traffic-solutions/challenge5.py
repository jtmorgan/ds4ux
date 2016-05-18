"""
What day of the week does the Burke Gilman experience the most overall traffic, on average? The most pedestrian traffic?
"""
import bgt_traffic
import datetime
#For datetime object, see https://docs.python.org/3.5/library/datetime.html#

result_ped = [0,0,0,0,0,0,0] # result_ped[0] for Monday pedestrain traffic,[6] for Sunday
result_total = [0,0,0,0,0,0,0] # Likewise

#Step 1. Get the toll from data
for dkey, dval in bgt_traffic.traffic.items():
	#Get day of week
	month = int(dkey.split("/")[0])
	day = int(dkey.split("/")[1])
	year = int(dkey.split("/")[2])
	day_of_week = datetime.date(year, month, day).weekday()
	#Get tolls
	day_toll_total = 0
	day_toll_ped = 0
	for hval in dval.values():
		day_toll_ped += int(hval["ped sb"]) + int(hval["ped nb"])
		day_toll_total += int(hval["ped sb"]) + int(hval["ped nb"]) + int(hval['bike sb']) + int(hval['bike nb'])
	result_ped[day_of_week] += day_toll_ped
	result_total[day_of_week] += day_toll_total

#Step 2. Evaluate when is the busiest day
ped_biggest_toll = 0 #the biggest pedestrian tolls
ped_biggest_day = 0 #and which weekday
total_biggest_toll = 0 #the biggest total tolls
total_biggest_day = 0 #and which weekday
for i in range(7):
	#Find the busiest day for pedestrians
	if result_ped[i] > ped_biggest_toll:
		ped_biggest_toll = result_ped[i]
		ped_biggest_day = i
	#Find the buisest day for total
	if result_total[i] > total_biggest_toll:
		total_biggest_toll = result_total[i]
		total_biggest_day = i

#Step 3. Convert number to weekday
if ped_biggest_day == 0: ped_biggest_day = "Mon."
elif ped_biggest_day == 1: ped_biggest_day = "Tue."
elif ped_biggest_day == 2: ped_biggest_day = "Wed."
elif ped_biggest_day == 3: ped_biggest_day = "Thur."
elif ped_biggest_day == 4: ped_biggest_day = "Fri."
elif ped_biggest_day == 5: ped_biggest_day = "Sat."
else: ped_biggest_day = "Sun."
if total_biggest_day == 0: total_biggest_day = "Mon."
elif total_biggest_day == 1: total_biggest_day = "Tue."
elif total_biggest_day == 2: total_biggest_day = "Wed."
elif total_biggest_day == 3: total_biggest_day = "Thur."
elif total_biggest_day == 4: total_biggest_day = "Fri."
elif total_biggest_day == 5: total_biggest_day = "Sat."
else: total_biggest_day = "Sun."

#Step 4. Print out the result
print (ped_biggest_day + " is the busiest weekday in Burke Gilman : " + str(ped_biggest_toll) + " pedestrians used the trail.")
print (total_biggest_day + " is the busiest weekday in Burke Gilman : " + str(total_biggest_toll) + " bikers and pedestrians used the trail.")