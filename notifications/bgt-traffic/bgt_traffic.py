import csv

INPUT_FILE = "bgt_bike_and_peds.csv"

traffic = {}

with open(INPUT_FILE, 'r') as ifile:
    reader = csv.reader(ifile)

    counter = 0
    for row in reader:
#         print(row)
        if counter == 0:
            counter += 1
        else:
            tdatetime = row[0]
            tdate = tdatetime[:10]
            ttime = tdatetime[11:]
            if tdate not in traffic.keys():
                traffic[tdate] = {}
            traffic[tdate][ttime] = {}
            for i, val in enumerate(row):
                if i == 0:
                    continue
                elif len(val) == 0:
                    row[i] = 0
                else:
                    pass
            traffic[tdate][ttime]['total'] = int(row[1])
            traffic[tdate][ttime]['ped sb'] = int(row[2])
            traffic[tdate][ttime]['ped nb'] = int(row[3])
            traffic[tdate][ttime]['bike nb'] = int(row[4])
            traffic[tdate][ttime]['bike sb'] = int(row[5])
            counter += 1

# print(traffic['09/30/2015']['07:00:00 PM']) 

