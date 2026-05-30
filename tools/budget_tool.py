def estimate_budget(
    flight_price,
    hotel_price,
    days
):

    food_cost = 2500

    total = (
        flight_price
        +
        (hotel_price * days)
        +
        food_cost
    )

    return total