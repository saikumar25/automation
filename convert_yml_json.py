import yaml
import json
with open("skills.yml", "r") as yaml_in, open("example.json", "w") as json_out:
    yaml_object = yaml.safe_load(yaml_in) # yaml_object will be a list or a dict
    json.dump(yaml_object, json_out)
