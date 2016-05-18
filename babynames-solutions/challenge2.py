import ssadata
"""
How many babies are in the dataset?
"""
total_boys = 0
total_girls = 0

total_boys = sum(ssadata.boys.values())
#     total_boys += number

for number in ssadata.girls.values():
    total_girls = total_girls + number

boys_and_girls = total_boys + total_girls  
    
print("There are %d people in the babyname dataset" % (boys_and_girls))
