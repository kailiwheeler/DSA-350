from graph_fxn import *
import networkx as nx
from pylab import *
import random

class Person:
    def __init__(self,first_name = "",last_name =""):
        self.first_name = first_name
        self.last_name = last_name
        self.num_friends = 0
        self.id = random.randint(1000,9999)
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.id})"
    def update(self):
        self.num_friends += 1

def build_adjacency(data):
    adj_dict = dict()
    for node in data:
        a = node[0]
        b = node[1]

        if a in adj_dict:
            adj_dict[a].append(b)
            a.update()
        else:
            adj_dict[a] = [b]
            a.update()

        if b in adj_dict:
            adj_dict[b].append(a)
            b.update()
        else:
            adj_dict[b] = [a]
            b.update()

    return adj_dict

def adjacency_to_graph(adjacency):
    graph = []
    for key,val in adjacency.items():
        n1 = key.first_name + " " + key.last_name
        for n in val:
            n2 = n.first_name + " " + n.last_name
            ls = (n1,n2)
            graph.append(ls)
    return graph

if __name__ == '__main__' :  
    p1 = Person("Anita", "Racinez")
    p2 = Person("Clem", "Jameson")
    p3 = Person("Lars", "Eriksson")
    p4 = Person("Jed", "Jones")
    graph = []
    data = [(p1, p2), (p2, p3), (p1, p4), (p2, p4)]
    adj = build_adjacency(data)
    graph = adjacency_to_graph(adj)
    draw_graph(graph)