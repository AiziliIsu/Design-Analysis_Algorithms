import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from coin_change_dp import coin_change_dp  # Import the DP function

# Greedy Algorithm for Coin Change Problem
def coin_change_greedy_solver():
    st.write("Greedy Algorithm for Coin Change Problem")

    # Input the coin denominations and target amount
    coin_denominations = st.text_input("Enter coin denominations (comma separated)", "1, 2, 5")
    target_amount = st.number_input("Enter target amount", min_value=1, value=11)

    # Parse the input
    coin_denominations = list(map(int, coin_denominations.split(',')))
    coin_denominations.sort(reverse=True)

    if st.button("Solve"):
        # Greedy solution
        coins_used, num_coins = coin_change_greedy(coin_denominations, target_amount)
        st.write(f"Coins used: {coins_used}")
        st.write(f"Number of coins used: {num_coins}")

        # Display the greedy steps
        st.write("Greedy Steps:")
        st.table(coins_used)

        # Compare with DP solution for optimality check
        dp, _ = coin_change_dp(coin_denominations, target_amount)
        if num_coins > dp[target_amount]:
            st.warning(f"The Greedy Algorithm is suboptimal. The Dynamic Programming solution requires only {dp[target_amount]} coins.")

# Helper function for Greedy Coin Change
def coin_change_greedy(coins, amount):
    result = []
    num_coins = 0

    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
            num_coins += 1

    return result, num_coins
