import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Dynamic Programming for Coin Change Problem
def coin_change_dp_solver():
    st.write("Dynamic Programming for Coin Change Problem")

    # Input the coin denominations and target amount
    coin_denominations = st.text_input("Enter coin denominations (comma separated)", "1, 2, 5")
    target_amount = st.number_input("Enter target amount", min_value=1, value=11)

    # Parse the input
    coin_denominations = list(map(int, coin_denominations.split(',')))

    if st.button("Solve"):
        # Dynamic programming solution
        dp, coins_used = coin_change_dp(coin_denominations, target_amount)
        st.write(f"Minimum number of coins needed: {dp[target_amount]}")
        st.write(f"Coins used: {coins_used}")

        # Display table showing intermediate results
        st.write("DP Table:")
        st.table(dp[:target_amount + 1])

        # Plot progression of the DP table
        plot_dp_table(dp[:target_amount + 1])

# Helper function for Dynamic Programming Coin Change
def coin_change_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    # Backtrack to find coins used
    coins_used = []
    remaining_amount = amount
    while remaining_amount > 0:
        coins_used.append(coin_used[remaining_amount])
        remaining_amount -= coin_used[remaining_amount]

    return dp, coins_used

# Plot the DP table progression
def plot_dp_table(dp_table):
    plt.plot(dp_table, marker='o')
    plt.xlabel('Amount')
    plt.ylabel('Minimum Coins')
    plt.title('DP Table Progression')
    st.pyplot(plt)
