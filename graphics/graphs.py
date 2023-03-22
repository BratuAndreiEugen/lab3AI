# plot a network
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt



def plotNetwork(network, communities = [1, 1, 1, 1, 1, 1], name = "ANY"):
    np.random.seed(123) #to freeze the graph's view (networks uses a random view)
    A=nx.to_numpy_array(network)
    G=network
    pos = nx.spring_layout(G)  # compute graph layout
    plt.figure(figsize=(4, 4))  # image is 8 x 8 inches
    nx.draw_networkx_nodes(G, pos, node_size=50, cmap=plt.cm.RdYlBu, node_color = communities)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    plt.title(name)
    plt.show()
