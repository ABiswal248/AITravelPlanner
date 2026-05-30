import json

def search_flights(source, destination):

    with open("data/flights.json", "r") as file:

        flights = json.load(file)

    results = []

    for flight in flights:

        if (
            flight["from"].lower() == source.lower()
            and
            flight["to"].lower() == destination.lower()
        ):

            results.append(flight)

    return results