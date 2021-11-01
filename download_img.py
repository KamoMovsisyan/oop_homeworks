import json
import requests

with open('img_links.json', 'r') as file_:
    data = json.load(file_)

for i in data:
    for val in i.values():
        if val == i['img_url']:
            response = requests.get(val)
        elif val == i['img_name']:
            with open(f'{val}', 'wb') as image:
                image.write(response.content)
                print(f'{val} downloaded')
