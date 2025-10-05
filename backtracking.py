def knapsack(values, weights, capacity):
    n = len(values)
    best = 0

    def solve(i, w, val):
        nonlocal best
        if i == n:
            best = max(best, val)
            return
        if w + weights[i] <= capacity:
            solve(i+1, w+weights[i], val+values[i])
        solve(i+1, w, val)

    solve(0, 0, 0)
    return best
