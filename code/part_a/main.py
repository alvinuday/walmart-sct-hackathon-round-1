import numpy as np


def tsp_held_karp(distances):
    n = len(distances)
    memo = {}

    # Define the recursive function to compute the minimum cost and the path
    def held_karp_dp(curr, visited):
        if (curr, visited) in memo:
            return memo[(curr, visited)]

        if visited == (1 << n) - 1:
            return distances[curr][0], [0]

        min_cost = float("inf")
        min_path = None
        for next_city in range(n):
            if visited & (1 << next_city) == 0:
                cost, path = held_karp_dp(next_city, visited | (1 << next_city))
                cost += distances[curr][next_city]
                if cost < min_cost:
                    min_cost = cost
                    min_path = [curr] + path

        memo[(curr, visited)] = min_cost, min_path
        return min_cost, min_path

    # Compute the minimum cost and path starting from city 0
    shortest_distance, shortest_path = held_karp_dp(0, 1)
    shortest_path.append(0)  # Return to the starting city
    return shortest_distance, shortest_path


# Example usage:
distances = np.array(
    [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
)  # Example distance matrix

shortest_distance, shortest_path = tsp_held_karp(distances)
print("Shortest distance using Held-Karp algorithm:", shortest_distance)
print("Order of visiting cities:", shortest_path)
