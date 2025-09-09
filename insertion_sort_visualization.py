import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


# Insertion Sort with Visualization for Streamlit
def insertion_sort_visual(arr, x):
    n = len(arr)
    iteration_counter = 0
    comparisons = 0

    # Create a placeholder for the chart in Streamlit
    chart_placeholder = st.empty()

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            comparisons += 1  # Count comparisons
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        iteration_counter += 1  # Increment the iteration counter

        # Display the current iteration and number of comparisons
        st.write(f"Iteration: {iteration_counter}, Comparisons: {comparisons}")

        # Plot the current array as a bar chart
        fig, ax = plt.subplots()
        ax.bar(x, arr)
        chart_placeholder.pyplot(fig)

        # Add a small delay to simulate animation
        plt.pause(0.3)

        # Clear the plot (if needed)
        plt.clf()

    # Return sorted array, total iterations, and comparisons
    return arr, iteration_counter, comparisons
