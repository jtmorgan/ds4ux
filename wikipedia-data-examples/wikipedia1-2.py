import encoding_fix
import requests
"""
In this script, we are requesting the same data as in wikipedia1-1.py, but doing two new things:

1. We are 'parameterizing' our query (specifying each of the query components separately, and then concatenating them into the API endpoint right before we send our request.

2. We are using a 'while TRUE' loop to 'continue' our query—making multiple requests to retrieve MUCH more data than we did before. 
"""
# raw string:
# ?action=query&prop=revisions&titles=Python_(programming_language)&rvlimit=100&rvprop=timestamp|user&format=json')

# parameter version which makes a little more sense
parameters = {'action' : 'query',
              'prop' : 'revisions',
              'titles' : 'Python (programming language)',
              'rvlimit' : 100,
              'rvprop' : "timestamp|user",
              'format' : 'json',
              'continue' : ''}

while True:
    wp_call = requests.get('https://en.wikipedia.org/w/api.php', params=parameters)
    response = wp_call.json()
    print(parameters)
    print(response)

    for page_id in response["query"]["pages"].keys():
        page_title = response["query"]["pages"][page_id]["title"]
        revisions = response["query"]["pages"][page_id]["revisions"]

        for rev in revisions:
            print(page_title + "\t" + rev["user"] + "\t" + rev["timestamp"])

    if 'continue' in response:
        parameters.update(response['continue'])
    else:
        break
            
