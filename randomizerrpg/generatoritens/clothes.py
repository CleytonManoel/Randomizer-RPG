import random 
import json


def random_clothes():

    with open("./lib/clothes.json", "r", encoding="utf-8") as clothes_json:
        clothe_json = clothes_json.read()

    clothe = json.loads(clothe_json)

    return random.choice(clothe["clothes"])
