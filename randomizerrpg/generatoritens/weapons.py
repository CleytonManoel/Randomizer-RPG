import random 
import json


def random_weapon():

    with open("./lib/weapons.json", "r", encoding="utf-8") as weapons_json:
        weapon_json = weapons_json.read()

    weapon = json.loads(weapon_json)

    return random.choice(weapon["weapons"])

def random_specialweapon():

    with open("./lib/weapons.json", "r", encoding="utf-8") as specialweapons_json:
        specialweapon_json = specialweapons_json.read()

    specialweapon = json.loads(specialweapon_json)["specialweapons"] 

    return random.choice(specialweapon)
