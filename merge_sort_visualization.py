import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Merge Sort with Visualization for Streamlit
def merge_sort_visual(arr, x, chart_placeholder):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively call merge_sort_visual for left and right halves
        merge_sort_visual(left_half, x[:mid], chart_placeholder)
        merge_sort_visual(right_half, x[mid:], chart_placeholder)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        # Display the current iteration and number of comparisons
        fig, ax = plt.subplots()
        ax.bar(x, arr, color='lightcoral')
        chart_placeholder.pyplot(fig)

        # Add a small delay to simulate animation
        plt.pause(0.5)

        # Clear the plot if necessary
        plt.clf()

    return arr
