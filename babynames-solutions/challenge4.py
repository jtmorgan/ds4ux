import ssadata
"""
How many boys' names are also girls' names? 
How many girls' names are also boys' names?
"""

shared_names = 0
for name in ssadata.boys.keys():
    if name in ssadata.girls.keys():
        print(name)
        shared_names += 1

print("%s names are in both datasets" % (shared_names))
