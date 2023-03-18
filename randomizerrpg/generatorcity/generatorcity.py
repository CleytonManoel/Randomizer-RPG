from . import cityname, citypopulation, citytype


def generator_city(type):

    cityn = cityname.random_citynames()

    cityt = citytype.random_citytype(type)

    cityp = citypopulation.random_population(type)

    return cityn,cityt,cityp
