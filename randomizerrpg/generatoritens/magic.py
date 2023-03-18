import random 
import json


def random_magic(type):

    with open("./lib/magic.json", "r", encoding="utf-8") as magics_json:
        magic_json = magics_json.read()

    magic = json.loads(magic_json)

    magic_select = type

    return random.choice(magic[magic_select])

