from tools.flight_tool import search_flights
from tools.hotel_tool import recommend_hotels
from tools.places_tool import discover_places

print(search_flights("Hyderabad", "Goa"))

print(recommend_hotels("Goa"))

print(discover_places("Goa"))