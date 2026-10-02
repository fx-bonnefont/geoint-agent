def is_valid_bbox(
    min_long: float, min_lat: float, max_long: float, max_lat: float
) -> bool:
    return (-180 <= min_long < max_long <= 180) and (-90 <= min_lat < max_lat <= 90)
