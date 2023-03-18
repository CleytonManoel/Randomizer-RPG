import random 
import json


def random_citynames():

    with open("./lib/citynames.json", "r", encoding="utf-8") as citynamess_json:
        citynames_json = citynamess_json.read()

    citynames = json.loads(citynames_json)

    return random.choice(citynames["names"])

