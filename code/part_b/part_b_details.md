The solution provided utilizes a nearest neighbor algorithm to assign delivery routes to two vehicles while ensuring that each route starts and ends at the depot and respects the maximum distance constraint for each vehicle.

Here's a detailed description of the algorithms and methods used:

1. **Haversine Distance Calculation (haversine function):**
   - This function calculates the distance between two points on the Earth's surface given their latitude and longitude coordinates using the haversine formula.
   - **Time Complexity:** O(1)
   - **Space Complexity:** O(1)

2. **Read Input CSV (read_input_csv function):**
   - This function reads the input CSV file containing order IDs along with their longitude and latitude coordinates.
   - It parses the CSV file and extracts the order IDs, longitude, and latitude coordinates for each location.
   - **Time Complexity:** O(n), where n is the number of locations in the CSV file
   - **Space Complexity:** O(n), where n is the number of locations in the CSV file

3. **Calculate Distance Matrix (calculate_distance_matrix function):**
   - This function computes the distance matrix between all pairs of locations using the haversine distance calculation.
   - It initializes an empty matrix and fills it with the distances between all pairs of locations.
   - **Time Complexity:** O(n^2), where n is the number of locations
   - **Space Complexity:** O(n^2), where n is the number of locations

4. **Nearest Neighbor Algorithm (nearest_neighbor function):**
   - This algorithm finds the nearest neighbor route starting from the depot for a single vehicle.
   - It iteratively selects the nearest unvisited neighbor from the current location, ensuring that the total distance does not exceed the maximum distance constraint.
   - The algorithm continues until all locations have been visited, and then returns the path and the total distance traveled.
   - **Time Complexity:** O(n^2), where n is the number of locations
   - **Space Complexity:** O(n), where n is the number of locations

5. **Print Optimal Route (print_optimal_route function):**
   - This function prints the order of locations visited in the optimal route for a given vehicle.
   - It maps the indices of locations in the path to their corresponding order IDs and prints the route.
   - **Time Complexity:** O(n), where n is the number of locations in the path
   - **Space Complexity:** O(n), where n is the number of locations in the path

6. **Main Function (main function):**
   - This is the entry point of the program where the overall logic is orchestrated.
   - It reads the input CSV file, calculates the distance matrix, and finds the optimal routes for two vehicles using the nearest neighbor algorithm.
   - The function ensures that each vehicle's route starts and ends at the depot and prints the routes along with the total distance traveled by each vehicle.
   - **Time Complexity:** O(n^2), where n is the number of locations
   - **Space Complexity:** O(n^2), where n is the number of locations

Overall, the solution uses efficient algorithms and methods to assign delivery routes to two vehicles while ensuring compliance with the specified constraints. The time and space complexities are reasonable for practical input sizes, making the solution suitable for real-world application in route optimization scenarios.