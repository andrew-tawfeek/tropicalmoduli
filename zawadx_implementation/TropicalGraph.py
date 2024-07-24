import networkx as nx
import numpy as np
from typing import Self

class TropicalGraph:
    """
    Implements a vertex-weighted marked graph (see page 10 of Melody Chan notes)

    Representation:
        graph - a Networkx Multigraph containing the underlying graph
        weights - dict of vtx string -> weight of vtx
        markings - dict of vtx string -> number of marked pts at vtx.
                   Our implementation only knows the number of marked points at a given vertex, 
                   rather than their labels.
    """
    def __init__(self, graph: dict[str, list[str]], weights: dict[str, int], markings: dict[str, int]) -> None:
        """
        graph is a dict of vtx -> list of edges, specified by other vtx on edge
        Graph is not constructed properly if all edges not specified at both endpoints.

        keys for weights and markings should be in vertices specified by graph.
        Vertices not in weights assumed to have weight 0.
        Vertices not in markings assumed to have no markings.
        """
        # graph_copy = {v: list(graph[v][:]) for v in graph}
        self.graph = nx.MultiGraph(graph, multigraph_input=False)
        self.weights = {vtx: weights.get(vtx, 0) for vtx in self.graph.nodes}
        self.markings = {vtx: markings.get(vtx, 0) for vtx in self.graph.nodes}

    @property
    def nodes(self) -> list[str]:
        """
        Returns a list of vertices
        """
        return list(self.graph.nodes)
    
    def get_data(self) -> tuple[nx.MultiGraph, dict[str, int], dict[str, int]]:
        return self.graph.copy(), self.weights.copy(), self.markings.copy()

    def is_isom_to(self, other: Self) -> bool:
        """
        Check if self is isomorphic to other as vertex-weighted marked graphs.
        """
        for isom in nx.vf2pp_all_isomorphisms(self.graph, other.graph):
            if (self.weights == {v: other.weights[isom[v]] for v in isom}
            and self.markings == {v: other.markings[isom[v]] for v in isom}):
                return True
        return False

    def is_stable_at(self, vtx: str) -> bool:
        """
        Check if self is stable at vtx
        """
        return 2*self.weights[vtx] - 2 + self.graph.degree[vtx] + self.markings[vtx] > 0

    def is_stable(self) -> bool:
        """
        Checks stability for the whole graph.
        """
        return all(self.is_stable_at(v) for v in self.nodes)

    def draw(self, ax=None):
        # Parameters, can change to change look
        node_size = 500
        arc3_base = 0.15  # minimum amount of arcing for edges
        marking_distance = 0.3 # determines how close marked points are to actual nodes
        
        draw_graph = self.graph.copy()
        draw_labels = self.weights.copy()
        pos = nx.shell_layout(draw_graph)

        # Deduce amount of arcing needed for edges
        max_multidegree = max([draw_graph.number_of_edges(u, v) for u in draw_graph.nodes for v in draw_graph.nodes])
        connectionstyle = [f"arc3,rad={i*arc3_base}" for i in range(max_multidegree)]

        def random_direction():
            theta = 2 * np.pi * np.random.random()
            return np.array([np.cos(theta), np.sin(theta)])

        # Add marked points
        marked_so_far = 0
        for node in self.nodes:
            for _ in range(self.markings[node]):
                marked_so_far += 1
                marked_pt = f"m{marked_so_far}"
                draw_graph.add_edge(node, marked_pt)
                draw_labels[marked_pt] = marked_pt
                pos[marked_pt] = pos[node] + marking_distance * random_direction()
                
        colorlist = ['powderblue'] * self.graph.order() + ['salmon'] * marked_so_far

        nx.draw_networkx_nodes(draw_graph, pos, node_size=node_size, node_color=colorlist, ax=ax)
        nx.draw_networkx_labels(draw_graph, pos, labels=draw_labels, ax=ax)
        nx.draw_networkx_edges(draw_graph, pos, connectionstyle=connectionstyle, ax=ax)


    

