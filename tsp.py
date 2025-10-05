import networkx as nx
import matplotlib.pyplot as plt

def visualize_tsp():
    cities = ["A", "B", "C", "D"]
    dist = {
        ("A","B"):10, ("A","C"):15, ("A","D"):20,
        ("B","C"):35, ("B","D"):25,
        ("C","D"):30
    }
    def d(a,b): return dist.get((a,b)) or dist.get((b,a))
    path, unvisited = ["A"], {"B","C","D"}
    total = 0
    while unvisited:
        last = path[-1]
        next_city = min(unvisited, key=lambda c: d(last,c))
        total += d(last,next_city)
        path.append(next_city)
        unvisited.remove(next_city)
    total += d(path[-1],"A")
    path.append("A")

    # Graph visualization
    G = nx.Graph()
    for (a,b), c in dist.items():
        G.add_edge(a,b, weight=c)

    pos = nx.circular_layout(G)
    plt.figure(figsize=(6,6))
    nx.draw(G, pos, with_labels=True, node_color="#90ee90", node_size=2000, font_size=14)
    edge_labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(f"TSP Greedy Path: {' → '.join(path)} (Cost: {total})")
    plt.savefig("static/tsp_graph.png")
    plt.close()
    return "static/tsp_graph.png", total
