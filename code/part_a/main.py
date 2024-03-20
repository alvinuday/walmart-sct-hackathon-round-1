import csv
import itertools
from geopy.distance import geodesic

def create_distance_matrix(distances):
    nodes = list(distances.keys())
    depot_index = nodes.index('depot')

    if depot_index != -1:
        nodes.pop(depot_index)
        nodes.insert(0, 'depot')

    matrix = [[0 for _ in range(len(nodes))] for _ in range(len(nodes))]

    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i != j:
                matrix[i][j] = distances[nodes[i]][nodes[j]]

    return matrix

def calculate_distance(points, order):
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += points[order[i]][order[i+1]]
    total_distance += points[order[-1]][order[0]]  # Return to the starting city
    return total_distance

def tsp(points):
    num_cities = len(points)
    all_cities = set(range(num_cities))
    best_distance = float('inf')
    best_path = None

    for perm in itertools.permutations(all_cities):
        distance = calculate_distance(points, perm)
        if distance < best_distance:
            best_distance = distance
            best_path = perm

    # Ensure the path returns to the starting city
    best_path = list(best_path) + [best_path[0]]

    return best_distance, best_path

def calculate_distances(nodes):
    distances = []
    depot = (float(nodes[0]['depot_lat']), float(nodes[0]['depot_lng']))

    for node in nodes:
        order_coords = (float(node['lat']), float(node['lng']))
        distance_to_depot = geodesic(depot, order_coords).meters
        distances.append({
            'from': "depot",
            'to': node['order_id'],
            'distance': distance_to_depot
        })

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            node_i_coords = (float(nodes[i]['lat']), float(nodes[i]['lng']))
            node_j_coords = (float(nodes[j]['lat']), float(nodes[j]['lng']))
            distance_between_orders = geodesic(node_i_coords, node_j_coords).meters
            distances.append({
                'from': nodes[i]['order_id'],
                'to': nodes[j]['order_id'],
                'distance': distance_between_orders
            })

    return distances

def convert_to_graph(distances):
    graph = {}
    for distance in distances:
        if distance['from'] not in graph:
            graph[distance['from']] = {}
        graph[distance['from']][distance['to']] = distance['distance']
        if distance['to'] not in graph:
            graph[distance['to']] = {}
        graph[distance['to']][distance['from']] = distance['distance']
    return graph

input_filenames = ['part_a_input_dataset_1.csv', 'part_a_input_dataset_2.csv', 'part_a_input_dataset_3.csv', 'part_a_input_dataset_4.csv', 'part_a_input_dataset_5.csv']

results = []

import os

def process_csv(folder, filename):
    file_path = os.path.join(folder, filename)
    data = []

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    distances = calculate_distances(data)
    graph = convert_to_graph(distances)
    matrix = create_distance_matrix(graph)
    distance, path = tsp(matrix)
    return distance, path, filename

input_folder = 'input_datasets/part_a'
input_filenames = ['part_a_input_dataset_1.csv', 'part_a_input_dataset_2.csv', 'part_a_input_dataset_3.csv', 'part_a_input_dataset_4.csv', 'part_a_input_dataset_5.csv']

results = []
for filename in input_filenames:
    distance, path, file_name = process_csv(input_folder, filename)
    results.append({'Filename': file_name, 'Shortest Distance': distance, 'Shortest Path': path})
    print("Input File:", file_name)
    print("Shortest Distance:", distance)
    print("Shortest Path:", path)
    print()

# Write results to another CSV file
output_filename = 'shortest_distances.csv'
with open(output_filename, 'w', newline='') as csvfile:
    fieldnames = ['Filename', 'Shortest Distance']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for result in results:
        writer.writerow({'Filename': result['Filename'], 'Shortest Distance': result['Shortest Distance']})

print("Shortest distances written to", output_filename)
