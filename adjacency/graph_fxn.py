from __future__ import division
import networkx as nx
from pylab import *
import random as rnd



#code from 
rcParams['figure.figsize'] = 12, 12  # that's default image size for this interactive session

def draw_graph(graph, labels=None, 
               node_size=1600, node_color='blue', node_alpha=0.3,
               node_text_size=12,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):
    """ 
    Based on: https://courses.grainger.illinois.edu/ece398bd/sp2016/lab6.html and
    https://www.udacity.com/wiki/creating-network-graphs-with-python
    We describe a graph as a list enumerating all edges.
    Ex: graph = [(1,2), (2,3)] represents a graph with 2 edges - (node1 - node2) and (node2 - node3)
    """
    # create networkx graph
    G=nx.Graph()
    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])
    graph_pos=nx.shell_layout(G)
    # draw graph
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, 
                           alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)
    # show graph
    plt.show()
    
if __name__ == '__main__' :
    graph = [(1,2),(2,3),(1,3)]
    print(graph)
    draw_graph(graph)


