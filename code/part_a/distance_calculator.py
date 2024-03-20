from geopy.distance import geodesic


def calculate_distance(lat1, lon1, lat2, lon2):
    # Define the coordinates as tuples
    coord1 = (lat1, lon1)
    coord2 = (lat2, lon2)

    # Calculate the distance using geodesic
    distance = geodesic(coord1, coord2).kilometers

    # Round off distance to 2 decimal places
    distance = round(distance, 2)

    return distance
