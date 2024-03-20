import csv
import numpy as np


def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of Earth in kilometers
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)
    a = (
        np.sin(delta_phi / 2) ** 2
        + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2) ** 2
    )
    res = R * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
    return np.round(res, 2)


def read_input_csv(file_path):
    locations = []
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            order_id = int(row["order_id"])
            lng = float(row["lng"])
            lat = float(row["lat"])
            locations.append({"order_id": order_id, "lng": lng, "lat": lat})
    return locations


def calculate_distance_matrix(locations):
    n = len(locations)
    distances = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            distances[i][j] = haversine(
                locations[i]["lat"],
                locations[i]["lng"],
                locations[j]["lat"],
                locations[j]["lng"],
            )
    return distances


def nearest_neighbor(distances, start_idx, max_distance, visited):
    n = len(distances)
    path = [start_idx]
    visited[start_idx] = True
    total_distance = 0

    while True:
        current_idx = path[-1]
        min_distance = float("inf")
        next_idx = -1

        for i in range(n):
            if (
                not visited[i]
                and distances[current_idx][i] < min_distance
                and total_distance + distances[current_idx][i] <= max_distance
            ):
                min_distance = distances[current_idx][i]
                next_idx = i

        if next_idx == -1:
            break

        total_distance += min_distance
        path.append(next_idx)
        visited[next_idx] = True

    path.append(start_idx)
    return path, total_distance, visited


def print_optimal_route(locations, path):
    optimal_route = [locations[i]["order_id"] for i in path]
    print("Optimal route order:", optimal_route)


def main(input_file, depot_lat, depot_lng, max_distance):
    locations = read_input_csv(input_file)
    distances = calculate_distance_matrix(locations)
    start_idx = 0  # Assuming the depot is at index 0

    total_distance = 0
    visited = [False] * len(locations)

    print("Shortest path for vehicle 1:")
    path1, total_distance1, visited = nearest_neighbor(
        distances, start_idx, max_distance, visited
    )
    print_optimal_route(locations, path1)
    print("Total distance for vehicle 1:", total_distance1, "kms")
    total_distance += total_distance1

    print("\nShortest path for vehicle 2:")
    path2, total_distance2, _ = nearest_neighbor(
        distances, start_idx, max_distance, visited
    )
    print_optimal_route(locations, path2)
    print("Total distance for vehicle 2:", total_distance2, "kms")
    total_distance += total_distance2

    print("\nTotal distance traveled by both vehicles:", total_distance, "kms")


# Example usage:
input_file = "../../input_datasets/part_b_input_dataset_2.csv"
depot_lat = 43.81
depot_lng = 126.57
max_distance = 20  # Maximum distance each vehicle can travel
main(input_file, depot_lat, depot_lng, max_distance)
