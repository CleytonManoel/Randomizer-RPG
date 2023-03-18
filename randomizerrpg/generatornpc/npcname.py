import random 
import json


def random_names(nametype,gender):

    with open("./lib/names.json", "r", encoding="utf-8") as names_json:
        name_json = names_json.read()

    name = json.loads(name_json)

    name_select = nametype

    return random.choice(name[name_select+gender])
    
 
