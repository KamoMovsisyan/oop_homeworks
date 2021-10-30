import json
import yaml

# json to text
with open('new_file.json', 'r') as json_file:
    data = str(json.load(json_file))

with open('new_file.txt', 'w') as text_file:
    text_file.write(data)


# json to yaml
with open('new_file.json', 'r') as file_:
    json_file = json.load(file_)

with open('yaml_file.yaml', 'a') as yaml_file:
    yaml_file = yaml.dump(json_file, yaml_file, indent=4)


# yaml to json
with open('yaml_file.yaml', 'r') as file_:
    data = yaml.full_load(file_)

with open('new_file.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

# yaml to text
with open('yaml_file.yaml', 'r') as file_:
    data = str(yaml.full_load(file_))

with open('new_file.txt', 'w') as text_f:
    text_f.write(data)
