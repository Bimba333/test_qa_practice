def calculate_delivery_cost(distance_km, weight_kg):
    if distance_km <= 0 or weight_kg <= 0:
        return None
    return distance_km * 10 + weight_kg * 5
    