**High-Level Explanation:**

The algorithm implemented here solves the Traveling Salesman Problem (TSP) for multiple datasets. It reads input data from CSV files, calculates distances between locations (orders and depot) using geographical coordinates, constructs a distance matrix, and then applies the TSP algorithm to find the shortest route that visits all locations (orders and depot) exactly once and returns to the starting location (depot).

1. **Input Data Preparation**:
   - The input data consists of geographical coordinates (latitude and longitude) of orders and depot.
   - The distances between locations are calculated using the Haversine formula provided by the `geodesic` function from the Geopy library.

2. **Create Distance Matrix**:
   - The distances calculated between locations are used to construct a distance matrix.
   - The distance matrix represents the pairwise distances between all locations.

3. **TSP Algorithm**:
   - The TSP algorithm implemented here uses brute force by trying all possible permutations of the locations.
   - It iterates through all permutations and calculates the total distance for each permutation.
   - The permutation with the minimum total distance is selected as the optimal route.

4. **Output Formatting**:
   - After finding the shortest route for each dataset, the algorithm prints the filename, shortest distance, and shortest path for each dataset.
   - It also writes these results to an output CSV file.

**Algorithm Time Complexity**:
- The TSP algorithm has a time complexity of O(n!), where n is the number of locations (orders + depot).
- Constructing the distance matrix has a time complexity of O(n^2).
- The overall time complexity of the algorithm depends on the number of datasets and the size of each dataset.

**Algorithm Space Complexity**:
- The space complexity of the algorithm primarily depends on storing the distance matrix, which has a space complexity of O(n^2), where n is the number of locations.
- Additional space is used for storing intermediate data structures, such as dictionaries and lists, which contribute to the overall space complexity. However, this space requirement is usually negligible compared to the distance matrix.

**Different Datasets and Corresponding Algorithm Complexity**:
- The time and space complexity of the algorithm may vary for different datasets based on the number of locations (orders + depot) and the geographical distribution of locations.
- Larger datasets with more locations will result in higher time and space complexity due to the exponential nature of the TSP algorithm.
- Datasets with locations scattered over a larger geographical area may require more time for distance calculations, leading to higher overall complexity.
