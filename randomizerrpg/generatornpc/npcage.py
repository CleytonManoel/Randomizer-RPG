import random 
import json


def random_age(agetype):

    with open("./lib/age.json", "r", encoding="utf-8") as ages_json:
        age_json = ages_json.read()

    age = json.loads(age_json)

    return random.randint(age[agetype]["min"],age[agetype]["max"])
