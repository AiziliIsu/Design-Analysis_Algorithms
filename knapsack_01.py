import streamlit as st
import time


# 0/1 Knapsack Problem solver
def knapsack_01_solver():
    st.write("Enter the items' weights, values, and the knapsack capacity.")

    # Input section
    capacity = st.number_input("Knapsack Capacity", min_value=1)
    weights = st.text_input("Enter weights (comma separated)")
    values = st.text_input("Enter values (comma separated)")

    # Parse the inputs and check if lengths match
    if st.button("Solve"):
        try:
            weights = list(map(int, weights.split(',')))
            values = list(map(int, values.split(',')))

            if len(weights) != len(values):
                st.error("The number of weights and values must be the same.")
                return

            if any(w <= 0 for w in weights) or any(v <= 0 for v in values):
                st.error("Weights and values must be positive integers.")
                return

            # Solve the knapsack problem
            start_time = time.time()
            result, selected_items = knapsack_01(capacity, weights, values)
            end_time = time.time()

            # Display the result
            st.write(f"Maximum value that can be obtained: {result}")
            st.write(f"Selected items (by index): {selected_items}")
            selected_weights = [weights[i] for i in selected_items]
            total_weight = sum(selected_weights)
            st.write(f"Total weight of selected items: {total_weight} (Knapsack Capacity: {capacity})")

            if total_weight > capacity:
                st.error("The total weight of the selected items exceeds the knapsack capacity!")

            # Display execution time
            exec_time = end_time - start_time
            st.write(f"Execution Time: {exec_time:.6f} seconds")

        except ValueError:
            st.error("Please enter valid comma-separated integers for weights and values.")


# 0/1 Knapsack Algorithm
def knapsack_01(capacity, weights, values):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Find the selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], selected_items


# Streamlit app entry point
if __name__ == "__main__":
    st.title("0/1 Knapsack Problem Solver")
    knapsack_01_solver()
