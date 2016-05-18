import csv

INPUT_FILES = ["bgt_bike_and_peds.csv","mts_bike_and_peds.csv"]

both_trails_traffic = []

for f in INPUT_FILES:
    with open(f, 'r') as ifile:
        reader = csv.reader(ifile)

        headers = []
        traffic = {}
        for i1, row in enumerate(reader):
    #         print(row)
            if i1 == 0:
                headers = row
            else:
                tdatetime = row[0]
                tdate = tdatetime[:10]
                ttime = tdatetime[11:]
                if tdate not in traffic.keys():
                    traffic[tdate] = {}
                traffic[tdate][ttime] = {}
                for i2, val in enumerate(row):
                    if i2 == 0:
                        continue
                    elif len(val) == 0:
                        row[i2] = 0
                    else:
                        pass
                traffic[tdate][ttime][headers[1]] = int(row[1])
                traffic[tdate][ttime][headers[2]] = int(row[2])
                traffic[tdate][ttime][headers[3]] = int(row[3])
                traffic[tdate][ttime][headers[4]] = int(row[4])
                traffic[tdate][ttime][headers[5]] = int(row[5])
        both_trails_traffic.append(traffic) 

# print(trails_traffic)
# bgt_traffic = trails_traffic[0]
# mts_traffic = trails_traffic[1]

# print(bgt_traffic['09/30/2015']['07:00:00 PM']) 
# print(mts_traffic['09/30/2015']['07:00:00 PM']) 

