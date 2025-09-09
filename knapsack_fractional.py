import streamlit as st
import time
import matplotlib.pyplot as plt

# Fractional Knapsack Problem solver
def fractional_knapsack_solver():
    st.write("Enter the items' weights, values, and the knapsack capacity.")

    # Input section
    capacity = st.number_input("Knapsack Capacity", min_value=1)
    weights = st.text_input("Enter weights (comma separated)")
    values = st.text_input("Enter values (comma separated)")

    # Parse the inputs
    if st.button("Solve"):
        weights = list(map(int, weights.split(',')))
        values = list(map(int, values.split(',')))

        start_time = time.time()
        result, selected_fractions = fractional_knapsack(capacity, weights, values)
        end_time = time.time()

        # Display the result
        st.write(f"Maximum value that can be obtained: {result}")
        st.write(f"Selected items and their fractions: {selected_fractions}")

        # Plotting execution time
        exec_time = end_time - start_time
        st.write(f"Execution Time: {exec_time:.6f} seconds")


# Fractional Knapsack Algorithm
def fractional_knapsack(capacity, weights, values):
    n = len(weights)
    ratios = [(values[i] / weights[i], i) for i in range(n)]
    ratios.sort(reverse=True, key=lambda x: x[0])

    total_value = 0
    selected_fractions = []

    for ratio, i in ratios:
        if capacity > 0 and weights[i] <= capacity:
            # Take the whole item
            total_value += values[i]
            capacity -= weights[i]
            selected_fractions.append((i, 1))
        else:
            # Take a fraction of the item
            fraction = capacity / weights[i]
            total_value += values[i] * fraction
            selected_fractions.append((i, fraction))
            break

    return total_value, selected_fractions

# Helper function to plot execution time

