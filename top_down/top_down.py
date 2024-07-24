# from zawadx_implementation.TropicalGraph import TropicalGraph
import networkx as nx
import numpy as np
# from typing import Self

g = 4
n = 0

num_vertices = 2 * g - 2 + n 
num_edges = 3 * g - 3 + n

for T in nx.generators.nonisomorphic_trees(num_vertices):
    if any([T.degree(v) > 3 for v in T.nodes]):
        continue
    print(T.nodes)
    print(T.edges)
    