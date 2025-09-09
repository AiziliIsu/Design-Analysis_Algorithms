import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


# Selection Sort with Visualization for Streamlit
def selection_sort_visual(arr, x):
    n = len(arr)
    iteration_counter = 0
    comparisons = 0

    # Create a placeholder for the chart in Streamlit
    chart_placeholder = st.empty()

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1  # Increment comparisons for each comparison made
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        # Increment iteration counter (one step per outer loop iteration)
        iteration_counter += 1

        # Display the current iteration and number of comparisons
        st.write(f"Iteration: {iteration_counter}, Comparisons: {comparisons}")

        # Plot the current array as a bar chart
        fig, ax = plt.subplots()
        ax.bar(x, arr, color='lightgreen')
        chart_placeholder.pyplot(fig)

        # Add a small delay to simulate animation
        plt.pause(0.3)

        # Clear the plot (if needed, depending on animation style)
        plt.clf()

    # Return sorted array, total iterations, and comparisons
    return arr, iteration_counter, comparisons
