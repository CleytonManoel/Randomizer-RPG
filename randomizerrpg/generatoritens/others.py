import random 
import json


def random_others(type):

    with open("./lib/others.json", "r", encoding="utf-8") as otherss_json:
        others_json = otherss_json.read()

    others = json.loads(others_json)

    others_select = type

    return random.choice(others[others_select])