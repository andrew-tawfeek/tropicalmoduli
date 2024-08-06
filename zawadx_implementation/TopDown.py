from TropicalGraph import TropicalGraph
from ModuliSpace import *
import networkx as nx
import pickle as pkl
import os

project_directory = os.path.dirname(os.getcwd())

### HELPER FUNCTIONS

def get_valid_trees(n : int) -> list:
    """Given an integer n, gets all distinct (non-isomorphic) trees on n vertices 
    where no vertex has degree greater than 3. Returns these as a list of MultiGraphs."""
    out = []
    for T in nx.generators.nonisomorphic_trees(n):
        # get rid of trees where the degree of any vertex is > 3 (these would not be maximal)
        if any([T.degree(v) > 3 for v in T.nodes]):
            continue
        out += [nx.MultiGraph(T)]
    return out
 
def all_ways_add_edge(G) -> list:
    """Given a MultiGraph G, returns a list of all possible Multigraphs obtained by
    adding a single edge to G in such a way that the resulting graph has no vertex
    with degree greater than 3"""
    output = []
    checked = []
    for v in G.nodes:
        if G.degree(v) < 2 : # self loop allowed
            for w in G.nodes:
                if w not in checked and G.degree(w) < 3:
                    tempG = G.copy()
                    tempG.add_edge(v, w)
                    # make sure we don't add duplicates
                    if not any([nx.vf2pp_is_isomorphic(tempG, otherG) for otherG in output]):
                        output += [tempG]
        elif G.degree(v) < 3: # self loop not allowed
            for w in G.nodes:
                if (w not in checked) and (w != v) and G.degree(w) < 3:
                    tempG = G.copy()
                    tempG.add_edge(v, w)
                    # make sure we don't add duplicates
                    if not any([nx.vf2pp_is_isomorphic(tempG, otherG) for otherG in output]):
                        output += [tempG]
        checked += [v]
    
    return output

def add_edge_to_each(graphs : list) -> list: 
    """given a list of MultiGraphs, applies the all_ways_add_edge to each, and combines all the resulting 
    lists, removing any duplicates"""
    out = []
    for G in graphs:
        G_out = []
        for newG in all_ways_add_edge(G): # make sure we don't add duplicates
            if not any([nx.vf2pp_is_isomorphic(newG, older_newG) for older_newG in out]):
                G_out += [newG]
        out += G_out
    
    return out

def add_edge_n_times(graphs : list, n : int) -> list:
    """Given a list of graphs and an integer n, iterates add_edge_to_each n times with input graphs"""
    for _ in range(n):
        graphs = add_edge_to_each(graphs)
    
    return graphs

def add_marked_points(G) -> TropicalGraph:
    """Given a  MultiGraph, returns a TropicalGraph with graph = G, weight 0 at every vertex,
    and 3 - deg(v) marked points atr the vertex v"""
    markings = {}
    for v in G.nodes:
        markings[v] = 3 - G.degree(v)
    return TropicalGraph(G, {}, markings)


def all_contractions(G : TropicalGraph) -> list[TropicalGraph]:
    """Given a tropical graph, returns a list of all non-isomorphic tropical graphs obtained 
    by contracting a single edge"""
    out = []
    checked_vertices = []
    for v_1 in G.graph.nodes:
        for v_2 in G.graph.nodes:
            if v_2 not in checked_vertices:
                try:
                    new_G = contract(G, v_1, v_2)
                    pass

    



### MAIN FUNCTIONS

def generate_maximal_comb_types(g : int, n : int, pickle = True) -> list[TropicalGraph]:
    """Given genus g and n marked points (g and n both integers), returns a list of maximal graphs
    in the poset of combinatorial types of tropical curves with genus g and n marked points.
    
    Takes an optional argument pickle, which if True, will pickle the results for quicker access
    next time. Results are saved in a directory called pickled_results. pickle is True by default.
    """

    try:
        with open(project_directory + "/pickled_results/max_layer_{}_{}.pkl".format(g, n), "rb") as f:
            max_layer = pkl.load(f)
        return max_layer
    except:
        num_vertices = 2 * g - 2 + n 
        num_edges = 3 * g - 3 + n

        valid_trees = get_valid_trees(num_vertices)

        num_remaining_edges = g
        valid_graphs = add_edge_n_times(valid_trees, g)
        valid_tropical_graphs = list(map(add_marked_points, valid_graphs))

        if pickle:
            filename = project_directory + "/pickled_results/max_layer_{}_{}.pkl".format(g, n)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "wb") as f:
                pkl.dump(valid_tropical_graphs, f)
        
        return valid_tropical_graphs
    

def generate_poset_top_down(g : int, n : int) -> tuple[nx.DiGraph, dict[tuple[int], TropicalGraph]]:
    """
    The big one. Should generate the poset of combinatorial types in M_{g, n}^{trop} using a top
    down approach.
    Inputs:
        g - genus
        n - number of marked points
    Outputs:
        poset - nx.DiGraph, with vertices labeled (level, number). Edges represent poset structure
        graph_dict - dict of (level, number) -> TropicalGraph. Maps vertex in poset to 
                    corresponding tropical graph.

    Requires there to exist stable graphs of type (g, n) - i.e. 2*g - 2 + n > 0
"""
    max_layer = generate_maximal_comb_types(g, n)
    num_edges = 3 * g - 3 + n 
    graph_dict = {(num_edges, i) : max_layer[i] for i in range(len(max_layer))}
    poset = nx.DiGraph({(num_edges, i) : [] for i in range(len(max_layer))})
    pass

    
    

    