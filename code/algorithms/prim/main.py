import networkx as nx
# import matplotlib

#WARN: change matplotlib backend to show image on linux 

# matplotlib.use('Agg')
import matplotlib.pyplot as plt






"""
Implementazione dell'algoritmo Prim per risolvere gli esercizi di MST
"""

def mst_prim():
    pass


if __name__ == '__main__':

    G = nx.Graph()

    G.add_edge("A", "B", weight=2)
    G.add_edge("A", "C", weight=3)
    G.add_edge("B", "C", weight=1)
    G.add_edge("B", "D", weight=1)
    G.add_edge("C", "D", weight=2)
    G.add_edge("C", "E", weight=1)
    G.add_edge("D", "E", weight=3)
    G.add_edge("D", "F", weight=1)
    G.add_edge("E", "F", weight=2)


    nx.draw_spring(G, with_labels=True)
    plt.show()



