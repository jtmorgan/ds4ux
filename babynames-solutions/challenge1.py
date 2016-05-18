import ssadata
"""
Are there more boys' names or girls' names? 
What about for particular first letters? 
What about for every first letter?
"""
number_of_boy_names = len(ssadata.boys)
print("There are %d boy names" % (number_of_boy_names))

number_of_girl_names = len(ssadata.girls)
print("There are %d girl names" % (number_of_girl_names))

start_letter = "a"
num_names = 0
for name in ssadata.boys.keys():
    if name[0] == start_letter:
        num_names = num_names +1

print("There are %d boy names that start with '%s'" % (num_names, start_letter))

letters = "abcdefghijklmnopqrstuvwxyz"
for l in letters:
    num_names = 0
    for name in ssadata.boys.keys():
        if name[0] == l:
            num_names = num_names +1
    print("There are %d boy names that start with '%s'" % (num_names, l))