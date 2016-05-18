import ssadata
"""
Search for your own name. Are there both boys and girls that have your name? 
Is it more popular for one group than for the other?
"""
for name in ssadata.boys.keys():
    if name == "jonathan":
        print("There were " + str(ssadata.boys[name]) + " boys named " + name)

for name in ssadata.girls.keys():
    if name == "jonathan":
        print("There were " + str(ssadata.girls[name]) + " girls named " + name)