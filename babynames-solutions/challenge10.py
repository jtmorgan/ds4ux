"""
Which boy and girl names have increased most in popularity 
between 2010 and 2013? Which ones have declined most in popularity?
"""

import ssadata_allyears

trending_name = ""
greatest_increase = [0, 0, 0]


for name, years in ssadata_allyears.girls.items():
    if 2010 in years.keys() and 2013 in years.keys():
        if years[2013] > years[2010]:
            increase_count = years[2013] - years[2010]
            percent_increase = round((increase_count/years[2010]) * 100,0) 
            if percent_increase > greatest_increase[0]:
                trending_name = name
                greatest_increase = [percent_increase, years[2010], years[2013]]

print("%s is trending!" % (trending_name))
print("%d babies were given that name in 2010" % (greatest_increase[1]))
print("%d babies were given that name in 2013" % (greatest_increase[2]))
print("That's an increase of %d%%!" % (greatest_increase[0]))

#OUTPUT
#marceline is trending!
#6 babies were given that name in 2010
#101 babies were given that name in 2013
#That's an increase of 1583%!
