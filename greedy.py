def knapsack(values, weights, capacity):
    ratio = sorted([(v/w, v, w) for v,w in zip(values, weights)], reverse=True)
    total, rem = 0, capacity
    for r,v,w in ratio:
        if rem >= w:
            total += v
            rem -= w
        else:
            total += r * rem
            break
    return round(total,2)
