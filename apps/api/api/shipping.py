def shipping_cost(distance_km):
    if distance_km <= 0:
        return 0
    return 5 + 0.5 * distance_km
