import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Dynamic Programming for Knapsack Problem
def knapsack_dp_solver():
    st.write("Dynamic Programming for Knapsack Problem")

    # Input: Get weights, values, and knapsack capacity from user
    weights = st.text_input("Enter the weights of the items (comma separated)", "2, 3, 4, 5")
    values = st.text_input("Enter the values of the items (comma separated)", "3, 4, 5, 6")
    capacity = st.number_input("Enter the capacity of the knapsack", min_value=1, value=5)

    # Parse the inputs
    weights = list(map(int, weights.split(',')))
    values = list(map(int, values.split(',')))

    if st.button("Solve"):
        # Solve the Knapsack Problem using Dynamic Programming
        max_value, selected_items, dp_table = knapsack_dp(capacity, weights, values)

        st.write(f"Maximum value that can be obtained: {max_value}")
        st.write(f"Selected items: {selected_items}")

        # Display the DP table
        st.write("Dynamic Programming Table:")
        st.table(dp_table)

        # Plot the progression of the DP table
        plot_dp_table(dp_table)

# Helper function to implement DP Knapsack algorithm
def knapsack_dp(capacity, weights, values):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Find the selected items by backtracking
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)  # Item i-1 is selected
            w -= weights[i - 1]

    return dp[n][capacity], selected_items, dp

# Plot DP table progression
def plot_dp_table(dp_table):
    # Sum of each row to see the progression
    row_sums = [sum(row) for row in dp_table]

    plt.plot(row_sums, marker='o')
    plt.xlabel('Row (Items considered)')
    plt.ylabel('Sum of Values in DP Table')
    plt.title('DP Table Progression')
    st.pyplot(plt)
