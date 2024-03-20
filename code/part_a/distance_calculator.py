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


lat1, lon1 = 43.8121, 126.5669
lat2, lon2 = 43.81811, 126.55716

# Calculate distance
distance = calculate_distance(lat1, lon1, lat2, lon2)
print("Traveling distance:", distance, "kms")
