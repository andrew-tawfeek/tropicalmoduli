import networkx as nx
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
        self.graph = nx.MultiGraph(graph, multigraph_input=False)
        self.weights = {vtx: weights.get(vtx, 0) for vtx in self.graph.nodes}
        self.markings = {vtx: markings.get(vtx, 0) for vtx in self.graph.nodes}

    @property
    def nodes(self) -> list[str]:
        """
        Returns a list of vertices
        """
        return list(self.graph.nodes)
    
    # def get_graph(self) -> nx.MultiGraph:
    #     return self.graph.copy()
    
    # def get_weights(self):
    #     return self.weights.copy()
    
    # def get_markings(self):
    #     return self.markings.copy()

    def check_isom(self, other: Self) -> bool:
        """
        Check if self is isomorphic to other as vertex-weighted marked graphs.
        """
        for isom in nx.vf2pp_all_isomorphisms(self.graph, other.graph):
            if (self.weights == {v: other.weights[isom[v]] for v in isom}
            and self.markings == {v: other.markings[isom[v]] for v in isom}):
                return True
        return False

    def check_stability_at(self, vtx: str) -> bool:
        """
        Check if self is stable at vtx
        """
        return 2*self.weights[vtx] - 2 + self.graph.degree[vtx] + self.markings[vtx] > 0

    def is_stable(self) -> bool:
        """
        Checks stability for the whole graph.
        """
        return all(self.check_stability_at(v) for v in self.nodes)

    def draw(self):
        # TODO: use Graphviz to implement visualization
        raise NotImplementedError

    

