import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
import itertools


# Brute Force for TSP
def tsp_brute_force_solver():
    st.write("Brute Force Solution for Traveling Salesman Problem")

    # Input number of cities
    num_cities = st.number_input("Number of Cities", min_value=2, value=5)
    st.write(f"Generating a random {num_cities}x{num_cities} distance matrix...")

    # Generate a random distance matrix
    distances = np.random.randint(10, 100, size=(num_cities, num_cities))
    np.fill_diagonal(distances, 0)  # No distance to itself
    st.write("Distance Matrix:", distances)

    if st.button("Solve"):
        start_time = time.time()
        best_route, best_distance = brute_force_tsp(distances)
        end_time = time.time()

        st.write(f"Shortest route found: {best_route}")
        st.write(f"Shortest distance: {best_distance}")
        st.write(f"Execution time: {end_time - start_time:.2f} seconds")

        # Visualize cities and the best route
        plot_cities_and_route(best_route, distances)


# Helper function to implement Brute Force TSP
def brute_force_tsp(distances):
    num_cities = len(distances)
    all_routes = itertools.permutations(range(num_cities))

    best_route = None
    best_distance = float('inf')

    for route in all_routes:
        current_distance = sum(distances[route[i], route[i + 1]] for i in range(num_cities - 1)) + distances[
            route[-1], route[0]]
        if current_distance < best_distance:
            best_distance = current_distance
            best_route = route

    return best_route, best_distance


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

    plt.title("Cities and Best Route")
    st.pyplot(plt)
