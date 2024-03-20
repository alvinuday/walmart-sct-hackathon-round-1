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
    total_distance += points[order[-1]][order[0]]
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

def process_csv(filename):
    data = []

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    distances = calculate_distances(data)
    graph = convert_to_graph(distances)
    matrix = create_distance_matrix(graph)
    distance, path = tsp(matrix)
    return distance, path

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
for filename in input_filenames:
    distance, path = process_csv(filename)
    results.append({'Filename': filename, 'Shortest Distance': distance, 'Shortest Path': ' -> '.join(map(str, path))})

for result in results:
    print("Filename:", result['Filename'])
    print("Shortest Distance:", result['Shortest Distance'])
    print("Shortest Path:", result['Shortest Path'])
    print()

output_filename = 'output.csv'
with open(output_filename, 'w', newline='') as csvfile:
    fieldnames = ['Filename', 'Shortest Distance', 'Shortest Path']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for result in results:
        writer.writerow(result)

print("Output written to", output_filename)
