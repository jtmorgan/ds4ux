"""
Which boy and girl names are the most popular 
across all four years in our dataset?
"""

import ssadata_allyears

most_popular_name = ""
most_popular_name_count = 0

for name, years in ssadata_allyears.girls.items():
    popularity = sum(years.values())
    if popularity > most_popular_name_count:
        most_popular_name_count = popularity
        most_popular_name = name

print("%s is the most popular name" % (most_popular_name))
print("%d babies have were given that name between 2010 and 2013" % (most_popular_name_count))

#OUTPUT
#sophia is the most popular name
#85720 babies have were given that name between 2010 and 2013