import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt

# Branch and Bound for TSP
def tsp_branch_bound_solver():
    st.write("Branch and Bound Algorithm for Traveling Salesman Problem")

    # Input number of cities
    num_cities = st.number_input("Number of Cities", min_value=2, value=5)
    st.write(f"Generating a random {num_cities}x{num_cities} distance matrix...")

    # Generate a random distance matrix
    distances = np.random.randint(10, 100, size=(num_cities, num_cities))
    np.fill_diagonal(distances, 0)  # No distance to itself
    st.write("Distance Matrix:", distances)

    if st.button("Solve"):
        start_time = time.time()
        best_route, best_distance, branches_explored, branches_pruned = branch_and_bound_tsp(distances)
        end_time = time.time()

        st.write(f"Shortest route found: {best_route}")
        st.write(f"Shortest distance: {best_distance}")
        st.write(f"Branches explored: {branches_explored}")
        st.write(f"Branches pruned: {branches_pruned}")
        st.write(f"Execution time: {end_time - start_time:.2f} seconds")

        # Plot the cities and best route
        plot_cities_and_route(best_route, distances)

# Helper function for Branch and Bound TSP
def branch_and_bound_tsp(distances):
    n = len(distances)
    min_cost = float('inf')
    best_route = None
    branches_explored = 0
    branches_pruned = 0

    # Function to calculate the cost of a route
    def route_cost(route):
        return sum(distances[route[i], route[i + 1]] for i in range(len(route) - 1)) + distances[route[-1], route[0]]

    # Recursive function to explore all routes with pruning
    def explore_route(route, remaining_cities, current_cost):
        nonlocal min_cost, best_route, branches_explored, branches_pruned
        branches_explored += 1

        if len(remaining_cities) == 0:
            total_cost = current_cost + distances[route[-1], route[0]]
            if total_cost < min_cost:
                min_cost = total_cost
                best_route = route[:]
        else:
            for city in remaining_cities:
                new_cost = current_cost + distances[route[-1], city]
                if new_cost < min_cost:  # Prune if cost exceeds min_cost
                    explore_route(route + [city], [c for c in remaining_cities if c != city], new_cost)
                else:
                    branches_pruned += 1

    # Start exploring from city 0
    explore_route([0], list(range(1, n)), 0)

    return best_route, min_cost, branches_explored, branches_pruned

# Plot cities and the best route
def plot_cities_and_route(route, distances):
    num_cities = len(route)
    coords = np.random.rand(num_cities, 2) * 100  # Random 2D coordinates for cities

    plt.figure(figsize=(6, 6))
    for i, city in enumerate(route):
        plt.plot(coords[city, 0], coords[city, 1], 'bo')
        plt.text(coords[city, 0], coords[city, 1], f'{city}', fontsize=12)

    for i in range(num_cities):
        plt.plot([coords[route[i], 0], coords[route[(i + 1) % num_cities], 0]],
                 [coords[route[i], 1], coords[route[(i + 1) % num_cities], 1]], 'r-')

    plt.title("Cities and Optimal Route")
    st.pyplot(plt)
