# 8. How many edits to the article "Python (programming language)"
# where made in 2015?

# Useful page is here: https://www.mediawiki.org/wiki/API:Revisions

import requests

parameters = {'action' : 'query',
              'prop' : 'revisions',
              'titles' : 'Python (programming language)',
              'rvlimit' : 500,
              'rvprop' : "timestamp",
              'format' : 'json',
              'continue' : ''}

edits_in_2015 = 0

# run a "while True" loop
while True:
    wp_call = requests.get('https://en.wikipedia.org/w/api.php', params=parameters)
    response = wp_call.json()
    
    for page_id in response["query"]["pages"].keys():
        revisions = response["query"]["pages"][page_id]["revisions"]
        
        for rev in revisions:
            if rev['timestamp'][0:4] == "2015":
                edits_in_2015 = edits_in_2015 + 1

    if 'continue' in response:
        parameters.update(response['continue'])
    else:
        break

print(edits_in_2015)
