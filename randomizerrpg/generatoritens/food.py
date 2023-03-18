import random 
import json


def random_food(type):

    with open("./lib/food.json", "r", encoding="utf-8") as foods_json:
        food_json = foods_json.read()

    food = json.loads(food_json)

    food_select = type

    return random.choice(food[food_select])



