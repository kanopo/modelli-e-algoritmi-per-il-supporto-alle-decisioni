import networkx as nx
import matplotlib.pyplot as plt

def kruskal(graph: nx.Graph):
    # Algoritmo di Kruskal
    """
    1. Sort all the edges in non-decreasing order of their weight. 
    2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If the cycle is not formed, include this edge. Else, discard it. 
    3. Repeat step#2 until there are (V-1) edges in the spanning tree.
    """
    # 1. Ordino gli archi in ordine crescente di peso

    sorted_edges = sorted(graph.edges(data=True), key=lambda x: x[2]["weight"])

    mst = nx.Graph()

    edges_to_remove = []

    for edge in sorted_edges:
        # Prendo uno spigolo e se agiungendolo non forma un ciclo posso aggiungerlo

        app = nx.Graph()
        for e in mst.edges(data=True):
            app.add_edge(e[0], e[1], weight=e[2]["weight"])

        app.add_edge(edge[0], edge[1], weight=edge[2]["weight"])

        # essendo foresta, non presenta cicli
        if nx.is_forest(app):
            mst.add_edge(edge[0], edge[1], weight=edge[2]["weight"])
            print("Aggiunto arco: ", edge)

        else:
            print("Scartato arco: ", edge)
            edges_to_remove.append(edge)


    return mst







if __name__ == "__main__":
    # Genero un grafo random

    fig = plt.figure(1, figsize=(10, 10))

    with open("README.md", "w") as f:

        f.write("# Esercizio MST\n\n\n")
        f.write("Implementazione dell'algoritmo Kruskal per risolvere gli esercizi di MST\n\n\n")


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
        mst_graph = kruskal(graph=G)

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




