import streamlit as st
import numpy as np
from bubble_sort_visualization import bubble_sort_visual
from selection_sort_visualization import selection_sort_visual
from insertion_sort_visualization import insertion_sort_visual
from merge_sort_visualization import merge_sort_visual
from binary_search_visualization import binary_search_visual
from huffman_coding import huffman_coding_solver
from knapsack_01 import knapsack_01_solver
from knapsack_fractional import fractional_knapsack_solver
from tsp_genetic import tsp_genetic_solver
from tsp_brute_force import tsp_brute_force_solver
from tsp_branch_bound import tsp_branch_bound_solver
from tsp_nearest_neighbor import tsp_nearest_neighbor_solver
from coin_change_dp import coin_change_dp_solver  # Correct import for DP Coin Change
from coin_change_greedy import coin_change_greedy_solver
from knapsack_dp import knapsack_dp_solver  # Import Dynamic Programming for Knapsack Problem

# Main function to display the dashboard
def main():
    st.title("Algorithms Dashboard")

    # Create a sidebar for navigation
    option = st.sidebar.selectbox(
        'Choose an Algorithm',
        (
            'Bubble Sort',
            'Selection Sort',
            'Insertion Sort',
            'Merge Sort',
            'Binary Search',
            "0/1 Knapsack",
            "Huffman Coding",
            "Fractional Knapsack",
            "TSP - Genetic Algorithm",
            "TSP - Brute Force",
            "TSP - Branch and Bound",
            "TSP - Nearest Neighbor",
            "Coin Change - Dynamic Programming",
            "Coin Change - Greedy Algorithm",
            "Knapsack Problem - Dynamic Programming"  # Added Knapsack DP
        )
    )

    # Run the corresponding algorithm based on the selected option
    if option == 'Bubble Sort':
        arr = np.random.randint(1, 100, 7)
        x = np.arange(0, 7, 1)
        bubble_sort_visual(arr, x)

    elif option == 'Selection Sort':
        arr = np.random.randint(1, 100, 7)
        x = np.arange(0, 7, 1)
        selection_sort_visual(arr, x)

    elif option == 'Insertion Sort':
        arr = np.random.randint(1, 100, 7)
        x = np.arange(0, 7, 1)
        insertion_sort_visual(arr, x)

    elif option == 'Merge Sort':
        arr = np.random.randint(1, 100, 7)
        x = np.arange(0, 7, 1)
        merge_sort_visual(arr, x, st.empty())

    elif option == 'Binary Search':
        arr = np.random.randint(1, 100, 7)
        sorted_arr = np.sort(arr)
        x = np.arange(0, 7, 1)
        target = sorted_arr[3]  # Target for binary search (middle element)
        binary_search_visual(sorted_arr, x, target, st.empty())


    elif option == "0/1 Knapsack":
        st.title("0/1 Knapsack Problem")
        knapsack_01_solver()

    elif option == "Fractional Knapsack":
        st.title("Fractional Knapsack Problem")
        fractional_knapsack_solver()

    elif option == "TSP - Genetic Algorithm":
        st.title("Traveling Salesman Problem (Genetic Algorithm)")
        tsp_genetic_solver()

    elif option == "TSP - Brute Force":
        st.title("Traveling Salesman Problem (Brute Force)")
        tsp_brute_force_solver()

    elif option == "TSP - Branch and Bound":
        st.title("Traveling Salesman Problem (Branch and Bound)")
        tsp_branch_bound_solver()

    elif option == "TSP - Nearest Neighbor":
        st.title("Traveling Salesman Problem (Nearest Neighbor)")
        tsp_nearest_neighbor_solver()

    elif option == "Coin Change - Dynamic Programming":
        st.title("Coin Change Problem (Dynamic Programming)")
        coin_change_dp_solver()

    elif option == "Coin Change - Greedy Algorithm":
        st.title("Coin Change Problem (Greedy Algorithm)")
        coin_change_greedy_solver()

    elif option == "Knapsack Problem - Dynamic Programming":
        st.title("Knapsack Problem (Dynamic Programming)")
        knapsack_dp_solver()

    elif option == "Huffman Coding":
        st.title("Huffman Coding")
        huffman_coding_solver()


if __name__ == "__main__":
    main()
