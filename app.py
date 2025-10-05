from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import networkx as nx
from algorithms import greedy, dp, tsp, backtracking
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    problem = request.form.get('problem')
    results = {}
    chart_path, graph_path = None, None

    if problem == "knapsack":
        values, weights, capacity = [60,100,120],[10,20,30],50
        results["Greedy"] = greedy.knapsack(values, weights, capacity)
        results["DP"] = dp.knapsack(values, weights, capacity)
        results["Backtracking"] = backtracking.knapsack(values, weights, capacity)

        # Visualization: comparison bar chart
        plt.figure(figsize=(6,4))
        plt.bar(results.keys(), results.values(), color=['#007bff','#28a745','#ffc107'])
        plt.title("Knapsack Algorithm Comparison")
        plt.ylabel("Max Value")
        chart_path = "static/comparison_chart.png"
        plt.savefig(chart_path)
        plt.close()

    elif problem == "tsp":
        graph_path, total_cost = tsp.visualize_tsp()
        results["Greedy TSP Path Cost"] = total_cost

    elif problem == "dp_table":
        dp.visualize_dp_table()
        graph_path = "static/dp_table.png"
        results["DP Table Visualization"] = "Generated below"

    return render_template("results.html", results=results,
                           chart=chart_path, graph=graph_path)

if __name__ == "__main__":
    app.run(debug=True)
