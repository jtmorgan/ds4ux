"""
Write a program that generates a CSV file called march_2016_daily_ped_counts.csv of the daily north- and south-bound pedestrian counts for March 2016, in chronological order. 
Your file should contain column headers and it should be possible to open it in a spreadsheet program like Microsoft Excel or Google Sheets.
"""
import bgt_traffic

result = {}
fname = "march_2016_daily_ped_counts.csv"

# Step 1. get the information from bgt_traffic
# Step 1-1. fetch record day by day
for dkey, dval in bgt_traffic.traffic.items():
	eachday = []
	#If the dkey says the record is on March 2016
	if (dkey.split("/")[0] == "03" and dkey.split("/")[2] == "2016"):
		ped_south = 0
		ped_north = 0
		#Step 1-2. Fetch ped sb, nb and sum. 
		for hval in dval.values():
			ped_south += int(hval["ped sb"])
			ped_north += int(hval["ped nb"])
		eachday.append(ped_north)
		eachday.append(ped_south)
		#Step 1-3. Save results to result dictionary
		result[dkey] = eachday

#Step 2. File out
fout = open(fname, 'w')
#Step 2-1. Create header
fout.write("Date\tPed North\tPed South\n")
#Step 2-2. Write data in sorted order
for key, value in sorted(result.items()):
	string = key + "," + str(value[0]) + "," + str(value[1]);
	print (string)
	fout.write(string + "\n")
fout.close()