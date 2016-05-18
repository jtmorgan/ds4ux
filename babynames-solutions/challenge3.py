import ssadata
"""
What is the longest name in the dataset?
"""
longest_names = []
length_of_longest_name = 0

for name in ssadata.girls.keys():
    name_length = len(name)
    if name_length >= length_of_longest_name:
        longest_names.append(name)
        length_of_longest_name = len(name)
        for ln in longest_names:
            if len(ln) < length_of_longest_name:
                longest_names.remove(ln)
                
for name in ssadata.boys.keys():
    name_length = len(name)
    if name_length >= length_of_longest_name:
        longest_names.append(name)
        length_of_longest_name = len(name)
        for ln in longest_names:
            if len(ln) < length_of_longest_name:
                longest_names.remove(ln)


    
print("The longest name is %d letters" % (length_of_longest_name))
print("The following %d names are %d letters long:" % (len(longest_names), length_of_longest_name))
for ln in longest_names:
    print("\t%s" % (ln))

"""
Further exploration (on your own)
*Can you think of another way to do this?     
*Does it matter if you search the girl names first, then the boy names?
*How would you change this to find out how many people had each of the longest names?
"""
