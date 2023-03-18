import random 
import json


def random_population(populationtype):

    with open("./lib/city.json", "r", encoding="utf-8") as populations_json:
        population_json = populations_json.read()

    population = json.loads(population_json)

    population_select = populationtype

    return random.randint(population[populationtype]["min"],population[populationtype]["max"])
