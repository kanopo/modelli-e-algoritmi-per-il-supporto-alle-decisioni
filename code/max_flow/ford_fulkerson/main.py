import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


"""
1. Start with initial flow as 0.
2. While there exists an augmenting path from the source to the sink:  
    - Find an augmenting path using any path-finding algorithm, such as breadth-first search or depth-first search.
    - Determine the amount of flow that can be sent along the augmenting path, which is the minimum residual capacity along the edges of the path.
    - Increase the flow along the augmenting path by the determined amount.
3. Return the maximum flow.
"""


"""
Breath First Search to find path from source to sink
"""
def BFS():
    pass


if __name__ == "__main__":
    graph = nx.read_adjlist("./adjacency.txt", create_using=nx.DiGraph())

    print(graph.edges(data=True))

    nx.draw(
            graph,
            with_labels=True,
            font_weight='bold',
            node_color="skyblue",
            edge_color="grey",
            font_size=8,
            node_size=500,
            nodelist=dict(graph.degree),
            pos=nx.spring_layout(graph, scale=20, k=3/np.sqrt(graph.order()))
            )
    plt.savefig("graph.png")


