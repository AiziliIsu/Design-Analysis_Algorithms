import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import itertools


# Genetic Algorithm for TSP
def tsp_genetic_solver():
    st.write("Genetic Algorithm for Traveling Salesman Problem")

    # Input number of cities
    num_cities = st.number_input("Number of Cities", min_value=2, value=5)
    st.write(f"Generating a random {num_cities}x{num_cities} distance matrix...")

    # Generate a random distance matrix
    distances = np.random.randint(10, 100, size=(num_cities, num_cities))
    np.fill_diagonal(distances, 0)  # No distance to itself
    st.write("Distance Matrix:", distances)

    # Parameters for the Genetic Algorithm
    population_size = st.slider("Population Size", 10, 500, 100)
    mutation_rate = st.slider("Mutation Rate", 0.01, 1.0, 0.05)
    generations = st.slider("Number of Generations", 10, 1000, 200)

    if st.button("Solve"):
        start_time = time.time()
        best_route, best_distance = genetic_algorithm_tsp(distances, population_size, mutation_rate, generations)
        end_time = time.time()

        st.write(f"Shortest route found: {best_route}")
        st.write(f"Shortest distance: {best_distance}")
        st.write(f"Execution time: {end_time - start_time:.2f} seconds")

        # Visualize cities and the best route
        plot_cities_and_route(best_route, distances)


# Helper function to implement the Genetic Algorithm
def genetic_algorithm_tsp(distances, population_size, mutation_rate, generations):
    # Function definitions and evolution logic
    def create_route():
        return random.sample(range(len(distances)), len(distances))

    def route_distance(route):
        return sum(distances[route[i], route[i + 1]] for i in range(len(route) - 1)) + distances[route[-1], route[0]]

    def mutate(route):
        for swapped in range(len(route)):
            if random.random() < mutation_rate:
                swap_with = int(random.random() * len(route))
                route[swapped], route[swap_with] = route[swap_with], route[swapped]
        return route

    def breed(parent1, parent2):
        child = []
        gene_a = int(random.random() * len(parent1))
        gene_b = int(random.random() * len(parent2))
        start_gene = min(gene_a, gene_b)
        end_gene = max(gene_a, gene_b)

        child = parent1[start_gene:end_gene]
        child += [item for item in parent2 if item not in child]
        return child

    population = [create_route() for _ in range(population_size)]
    best_route = min(population, key=route_distance)
    best_distance = route_distance(best_route)

    for generation in range(generations):
        ranked_population = sorted(population, key=route_distance)
        population = ranked_population[:population_size // 2]
        for _ in range(population_size // 2):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = breed(parent1, parent2)
            population.append(mutate(child))

        current_best_route = min(population, key=route_distance)
        current_best_distance = route_distance(current_best_route)
        if current_best_distance < best_distance:
            best_route = current_best_route
            best_distance = current_best_distance

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
