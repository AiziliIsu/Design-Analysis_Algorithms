import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Binary Search with Visualization for Streamlit
def binary_search_visual(arr, x, target, chart_placeholder):
    low, high = 0, len(arr) - 1
    iteration_counter = 0
    comparisons = 0

    while low <= high:
        comparisons += 1
        iteration_counter += 1
        mid = (low + high) // 2

        # Display the current search range
        st.write(f"Iteration: {iteration_counter}, Comparisons: {comparisons}, Mid Element: {arr[mid]}")

        # Plot the current array and highlight the middle element
        fig, ax = plt.subplots()
        bar_colors = ['lightblue' if i != mid else 'orange' for i in range(len(arr))]
        ax.bar(range(len(arr)), arr, color=bar_colors)
        chart_placeholder.pyplot(fig)

        # Add a small delay to simulate animation
        plt.pause(0.5)

        # Clear the plot (optional)
        plt.clf()

        if arr[mid] == target:
            st.write(f"Target {target} found at index {mid}")
            return mid, iteration_counter, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    st.write(f"Target {target} not found in the array.")
    return -1, iteration_counter, comparisons
