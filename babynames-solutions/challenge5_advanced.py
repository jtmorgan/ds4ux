import ssadata
"""
How many names are subsets of other names?
"""

names_in_other_names = []
for boy_name in ssadata.boys.keys():
    for other_boy_name in ssadata.boys.keys():
        if boy_name in other_boy_name:
            if boy_name != other_boy_name:
                names_in_other_names.append(boy_name)
                break
            else:
                pass
        else:
            pass

for girl_name in ssadata.girls.keys():
    for other_girl_name in ssadata.girls.keys():
        if girl_name in other_girl_name:
            #this time through, we check for duplicates
            if girl_name != other_girl_name and girl_name not in names_in_other_names:
                names_in_other_names.append(girl_name)
                break
            else:
                pass
        else:
            pass

print(names_in_other_names)
num_subset_names = len(names_in_other_names)
print("%d baby names are subsets of other baby names." % (num_subset_names))

#OUTPUT
#9046 baby names are subsets of other baby names.