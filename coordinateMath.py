def dms_to_decimal(coords, ref):
    degrees, minutes, seconds = coords
    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal