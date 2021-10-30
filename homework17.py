import json
import requests

with open('img_links.json', 'r') as images:
    data = json.load(images)

print(data)

with open(f"{data[0]['img_name']}", 'wb') as img1:
    image1 = requests.get(data[0]['img_url'])
    img1.write(image1.content)
    print(f"{data[0]['img_name']} downloaded")

with open(f"{data[1]['img_name']}", 'wb') as img2:
    image2 = requests.get(data[1]['img_url'])
    img2.write(image2.content)
    print(f"{data[1]['img_name']} downloaded")

with open(f"{data[2]['img_name']}", 'wb') as img3:
    image3 = requests.get(data[2]['img_url'])
    img3.write(image1.content)
    print(f"{data[2]['img_name']} downloaded")

with open(f"{data[3]['img_name']}", 'wb') as img4:
    image4 = requests.get(data[3]['img_url'])
    img4.write(image4.content)
    print(f"{data[3]['img_name']} downloaded")

with open(f"{data[4]['img_name']}", 'wb') as img5:
    image5 = requests.get(data[4]['img_url'])
    img5.write(image5.content)
    print(f"{data[4]['img_name']} downloaded")
