"""
How many names are subsets of other names?

Here's a partial solution that goes through the boy names only, and gathers them in a list.
See the notes below for explanations of what's happening at particular steps in the execution of the script.
"""
import ssadata

names_in_other_names = [] #see NOTE 1
for boy_name in ssadata.boys.keys():
    for other_boy_name in ssadata.boys.keys(): #see NOTE 2
        if boy_name in other_boy_name:
            if boy_name != other_boy_name: #see NOTE 3
                names_in_other_names.append(boy_name)
                break #see NOTE 4
            else: #see NOTE 5
                pass
        else:
            pass

print(names_in_other_names)


"""
NOTE 1
In this example, I'm storing all the names that exist in other names in a list, so that I can check them at the end (by printing the list). However, the question only asks for the NUMBER of names that are in other names, not a list of those names. How might you solve this challenge without using a list at all? 


NOTE 2
I'm using a 'nested' for-loop here. For each key in the ssadata.boys dictionary, I want to compare it to every OTHER key in that dictionary. This is a large dictionary, so that operation takes a while to do, even though Python is fast. Think about it: there are over 13,000 names in each dictionary, and when we use nested for-loops, we are checking EACH one of those against EVERY other name in the dictionary. That means Python is potentially performing approximately 170 MILLION checks--just for the boys names alone!

See NOTE 4 below for a trick that can speed up the execution of this script using 'break' to reduce the number of check operations Python has to make.           


NOTE 3
We only want to add boy_name to the list if it is a SUBSET of other_boy_name. Because we are using using nested loops, we are reading through the same list twice for each name--that means we will at some point be comparing each name to itself. 

Example: we know that the name 'chris' is in the name 'chris'--because they're the same name! We want to ignore that every time we see it, so we use an 'if' statement to check whether the two names are equal to one another. If they are equal, we ignore them and move on to check whether 'chris' is in some other name in ssadata.boys.


NOTE 4
Once we find one match--an other_boy_name that boy_name is a subset of, but not equal to--we append it to the list. Now that we found at least one match for boy_name, we don't need to keep looking for more matches. So we use 'break' to go directly to the next iteration of the 'for' loop. 

For example, if we found 'chris' in 'christopher', we don't care if it also shows up in 'christian'. We can move on and check the next boy name. This saves us some time (Python has to check fewer things), and also avoids adding duplicates to the list names_in_other_names.


NOTE 5
We put else/pass after each of our 'if' statements for clarity: "IF our conditions are NOT met, do nothing and move along." This isn't necessary (the code will work if you remove these else/pass statements), but is a good practice because it helps you keep track of the logic of the script, and will also help other people who need to read & understand your script later on--including your future self!
"""

