import json

def discover_places(city):

    with open("data/places.json", "r") as file:

        places = json.load(file)

    results = []

    for place in places:

        if place["city"].lower() == city.lower():

            results.append(place)

    return results