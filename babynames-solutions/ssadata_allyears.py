names_lists = ["yob2013.txt", "yob2012.txt", "yob2011.txt", "yob2010.txt"]

girls = {}

for nlist in names_lists:
    with open(nlist, 'r') as f:
        reader = f.readlines()
        for line in reader:
            name, gender, count = line.strip().split(",")
            count = int(count)
            year = int(nlist[3:7])
            name = name.lower()
            if gender == "F":
                if name in girls.keys():
                    girls[name][year] = count
                else:
                    girls[name] = {}
                    girls[name][year] = count

        f.close()
# print(girls['mary'])

