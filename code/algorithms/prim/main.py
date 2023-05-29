import networkx as nx
import matplotlib.pyplot as plt
import random

"""
Implementazione dell'algoritmo Prim per risolvere gli esercizi di MST
"""

def mst_prim(graph: nx.Graph):

    mst = nx.Graph()

    REMAINING_NODES = len(graph.nodes())

    visited = set()

    random_node_index = random.randint(0, len(graph.nodes()) - 1)

    start = list(graph.nodes())[random_node_index]

    visited.add(start)

    while REMAINING_NODES > 0:

        min_weight = float("inf")
        min_edge = -1

        for node in visited:
            for edge in graph.edges(node):
                # perche (nodo_partenza, nodo_arrivo, peso)
                if edge[1] not in visited:
                    if graph.edges[edge]["weight"] < min_weight:
                        min_weight = graph.edges[edge]["weight"]
                        min_edge = edge


        if min_edge == -1:
            break

        else:

            visited.add(min_edge[1])
            mst.add_edge(min_edge[0], min_edge[1], weight=min_weight)
            REMAINING_NODES -= 1



    print("MST: ", mst.edges(data=True))
    return mst



if __name__ == '__main__':
    with open("README.md", "w") as f:

        f.write("# Esercizio MST\n\n\n")
        f.write("Implementazione dell'algoritmo Prim per risolvere gli esercizi di MST\n\n\n")


        G = nx.Graph()

        G.add_edge(0, 2, weight=2)
        G.add_edge(1, 3, weight=3)
        G.add_edge(2, 3, weight=1)
        G.add_edge(2, 4, weight=1)
        G.add_edge(3, 4, weight=2)
        G.add_edge(3, 5, weight=1)
        G.add_edge(4, 5, weight=3)

        f.write("Grafo di partenza: \n\n\n")
        for edge in G.edges(data=True):
            f.write(str(edge) + "\n\n\n")




        pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility
        # nodes
        nx.draw_networkx_nodes(G, pos, node_size=500)

        # edges
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=6)

        # labels
        nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

        # edge labels
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)


        plt.axis('off')
        plt.title("Graph")
        plt.savefig("graph.png")
        plt.show()


        plt.clf()
        f.write("![Graph](./graph.png)\n\n\n")


        # PRIM ALGORITHM
        mst_graph = mst_prim(graph=G)

        f.write("MST: \n\n\n")
        for edge in mst_graph.edges(data=True):
            f.write(str(edge) + "\n\n\n")


        pos = nx.spring_layout(mst_graph, seed=7)  # positions for all nodes - seed for reproducibility
        # nodes
        nx.draw_networkx_nodes(mst_graph, pos, node_size=500)

        # edges
        nx.draw_networkx_edges(mst_graph, pos, edgelist=G.edges(), width=6)

        # labels
        nx.draw_networkx_labels(mst_graph, pos, font_size=20, font_family="sans-serif")

        # edge labels
        labels = nx.get_edge_attributes(mst_graph, "weight")
        nx.draw_networkx_edge_labels(mst_graph, pos, edge_labels=labels)


        plt.axis('off')
        plt.title("MST Graph")
        plt.savefig("mst_graph.png")
        plt.show()

        f.write("![MST Graph](./mst_graph.png)\n\n\n")


        f.close()


