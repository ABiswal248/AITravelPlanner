import json

def recommend_hotels(city):

    with open("data/hotels.json", "r") as file:

        hotels = json.load(file)

    results = []

    for hotel in hotels:

        if hotel["city"].lower() == city.lower():

            results.append(hotel)

    return results