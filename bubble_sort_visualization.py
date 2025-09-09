import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


# Bubble Sort with Visualization for Streamlit
def bubble_sort_visual(lst, x):
    n = len(lst)
    iteration_counter = 0
    comparisons = 0

    # Create a placeholder for the chart in Streamlit
    chart_placeholder = st.empty()

    # Outer loop for bubble sort
    for i in range(n):
        for j in range(0, n - i - 1):
            # Update Streamlit iteration counter (one step per inner loop iteration)
            iteration_counter += 1
            comparisons += 1

            # Display the current iteration and number of comparisons
            st.write(f"Iteration: {iteration_counter}, Comparisons: {comparisons}")

            # Plot the current list as a bar chart
            fig, ax = plt.subplots()
            ax.bar(x, lst)
            chart_placeholder.pyplot(fig)

            # Add a small delay to simulate animation (you can adjust this delay)
            plt.pause(0.3)

            # Clear the plot (remove if not needed, depends on how you want the animation to appear)
            plt.clf()

            # Perform the swap in Bubble Sort
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    # Return sorted list and total iterations/comparisons
    return lst, iteration_counter, comparisons
