def calculate_parking_fee(vehicle_type, parking_duration, day_type, is_public_holiday):
    if vehicle_type == "motorcycle":
        return 2
    elif vehicle_type == "car":
        return 5
    raise NotImplementedError