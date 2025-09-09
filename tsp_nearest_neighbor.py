import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt

# Nearest Neighbor for TSP
def tsp_nearest_neighbor_solver():
    st.write("Nearest Neighbor Heuristic for Traveling Salesman Problem")

    # Input number of cities
    num_cities = st.number_input("Number of Cities", min_value=2, value=5)
    st.write(f"Generating a random {num_cities}x{num_cities} distance matrix...")

    # Generate a random distance matrix
    distances = np.random.randint(10, 100, size=(num_cities, num_cities))
    np.fill_diagonal(distances, 0)  # No distance to itself
    st.write("Distance Matrix:", distances)

    if st.button("Solve"):
        start_time = time.time()
        best_route, best_distance = nearest_neighbor_tsp(distances)
        end_time = time.time()

        st.write(f"Shortest route found: {best_route}")
        st.write(f"Shortest distance: {best_distance}")
        st.write(f"Execution time: {end_time - start_time:.2f} seconds")

        # Plot the cities and the resulting route
        plot_cities_and_route(best_route, distances)

# Helper function for Nearest Neighbor TSP
def nearest_neighbor_tsp(distances):
    n = len(distances)
    start_city = np.random.randint(0, n)  # Random starting city
    unvisited = list(range(n))
    unvisited.remove(start_city)

    route = [start_city]
    current_city = start_city

    total_distance = 0

    while unvisited:
        nearest_city = min(unvisited, key=lambda city: distances[current_city, city])
        total_distance += distances[current_city, nearest_city]
        current_city = nearest_city
        route.append(current_city)
        unvisited.remove(current_city)

    # Return to the starting city
    total_distance += distances[route[-1], route[0]]
    route.append(route[0])

    return route, total_distance

# Plot cities and the resulting route
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

    plt.title("Cities and Resulting Route")
    st.pyplot(plt)
