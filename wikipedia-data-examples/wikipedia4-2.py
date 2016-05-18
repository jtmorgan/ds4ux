"""
What categories contain the article "Albert Einstein"?

In this version of the script, we are printing the results to a text file called 'einstein_categiries.list'.
"""

import encoding_fix
import requests

# ?action=query&titles=Albert%20Einstein&prop=categories
parameters = {'action' : 'query',
              'titles' : 'Albert Einstein',
              'prop' : 'categories',
              'format' : 'json',
              'continue' :  ''}

with open("einstein_categories.list", 'w') as output_file:

    while True:
        wp_call = requests.get('http://en.wikipedia.org/w/api.php', params=parameters)
        response = wp_call.json()

        for page_id in response["query"]["pages"].keys():
            for category in response["query"]["pages"][page_id]['categories']:
                print(category['title'], file=output_file)

        if 'continue' in response:
            parameters.update(response['continue'])
        else:
            break


