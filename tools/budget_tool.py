def estimate_budget(
    flight_price,
    hotel_price,
    days,
    food_cost=2500,
    local_transport=1500
):

    return (
        flight_price
        +
        (hotel_price * days)
        +
        food_cost
        +
        local_transport
    )