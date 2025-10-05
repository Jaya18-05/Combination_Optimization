import matplotlib.pyplot as plt
import numpy as np

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,capacity+1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1]+dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]

def visualize_dp_table():
    values, weights, capacity = [60,100,120],[10,20,30],50
    n = len(values)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,capacity+1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1]+dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    dp_array = np.array(dp)
    plt.figure(figsize=(10,5))
    plt.imshow(dp_array, cmap="Blues", interpolation="nearest")
    plt.colorbar(label="Value")
    plt.title("DP Table Visualization")
    plt.xlabel("Capacity")
    plt.ylabel("Items")
    plt.savefig("static/dp_table.png")
    plt.close()
