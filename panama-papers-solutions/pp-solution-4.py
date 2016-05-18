# Who were the top 3 editors during that hour?
import requests
import json

ENDPOINT = 'https://en.wikipedia.org/w/api.php'

parameters = { 'action' : 'query',
               'prop' : 'revisions',
               'titles' : 'Panama_Papers',
               'format' : 'json',
               'rvdir' : 'newer',
               'rvstart': '2016-04-03T21:00:00Z',
               'rvend' : '2016-04-03T21:59:59Z',
               'rvlimit' : 500,
               'continue' : '' }

users = {}

done = False
while not done:
    wp_call = requests.get(ENDPOINT, params=parameters)
    response = wp_call.json()

    pages = response['query']['pages']
#     print(pages)
    for page_id in pages:
        page = pages[page_id]
        revisions = page['revisions']
        for rev in revisions:
            revuser = rev['user']
            if revuser in users.keys():
                users[revuser] += 1
            else:
                users[revuser] = 1

    if 'continue' in response:
        parameters['continue'] = response['continue']['continue']
        parameters['rvcontinue'] = response['continue']['rvcontinue']
    else:
        done = True

# print(json.dumps(users, indent=4))

top_3_users = []
user_list = []
for ukey,uval in users.items():
    user_list.append([ukey,uval])
# print(user_list)

top_3_editors = []

found_three = False

while not found_three:
    top_edit_val_seen = 0
    top_editors_seen = []
    for u in user_list:
        if u[1] > top_edit_val_seen:
            top_edit_val_seen = u[1]
            top_editors_seen[:] = []
            top_editors_seen.append(u[0])
        elif u[1] == top_edit_val_seen:
            top_editors_seen.append(u[0])
        else:
            pass
    for t in top_editors_seen:
        x = [t,top_edit_val_seen]   
        top_3_editors.append(x)
        user_list.remove(x)
    if len(top_3_editors) >= 3:
        break
    else:
        continue
        
print(top_3_editors)
