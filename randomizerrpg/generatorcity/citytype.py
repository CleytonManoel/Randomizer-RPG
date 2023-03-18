import random 
import json


def random_citytype(type):

    with open("./lib/city.json", "r", encoding="utf-8") as citytypes_json:
        citytype_json = citytypes_json.read()

    citytype = json.loads(citytype_json)

    selecttype = type


    return random.choice(citytype["type"][selecttype])
