from TropicalGraph import *
from itertools import chain, combinations

# Helper functions

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def list_difference(list1, list2):
    """
    Returns the elements of list1 after removing things from list2, counting multiplicity
    """
    new_list1 = list1[:]
    for elem in list2:
        try:
            new_list1.remove(elem)
        except ValueError:
            pass
    return new_list1


def trop_graph_in_list(check_graph: TropicalGraph, graph_list: list[TropicalGraph]) -> bool:
    return any([check_graph.is_isom_to(g) for g in graph_list])


# building up to the big one

def contract(trop_graph: TropicalGraph, vtx1: str, vtx2: str) -> TropicalGraph:
    """
    Assumes vtx1 and vtx2 have an edge between them in trop_graph.
    Returns the tropical graph obtained by contracting along an edge joining vtx1 to vtx2
    If vtx1 = vtx2 has a loop, contraction removes the loop and adds 1 to the weight of the vertex.
    """
    graph, weights, markings = trop_graph.get_data()
    if vtx1 not in trop_graph.nodes or vtx2 not in trop_graph.nodes:
        raise ValueError("Vertex not in graph!")
    if not graph.has_edge(vtx1, vtx2):
        raise ValueError("Edge not in graph!")
    
    if vtx1 == vtx2:  # loop case
        weights[vtx1] += 1
        graph.remove_edge(vtx1, vtx1)
        return TropicalGraph(graph, weights, markings)
    else:  # edge case
        vtx_new = f"{vtx1}+{vtx2}"

        weights[vtx_new] = weights[vtx1] + weights[vtx2]
        markings[vtx_new] = markings[vtx1] + markings[vtx2]
        for (u, v) in graph.edges([vtx1, vtx2]):
            if u in [vtx1, vtx2]:
                if v in [vtx1, vtx2]:
                    graph.add_edge(vtx_new, vtx_new)  # add loops
                else:
                    graph.add_edge(vtx_new, v)
            else:
                graph.add_edge(u, vtx_new)  # if u not in [vtx1, vtx2], v must be
        graph.remove_edge(vtx_new, vtx_new) # remove one extra loop corresponding to the edge that got contracted

        # Remove vtx1 and vtx2
        del weights[vtx1]
        del weights[vtx2]
        del markings[vtx1]
        del markings[vtx2]
        graph.remove_nodes_from([vtx1, vtx2])

        return TropicalGraph(graph, weights, markings)


def lollipop(trop_graph: TropicalGraph, vtx: str) -> TropicalGraph:
    """
    Returns a new tropical graph, where genus at vtx has been reduced by one by adding a loop.
    Raises ValueError if vtx not in graph or if its weight is 0.
    """
    graph, weights, markings = trop_graph.get_data()
    if vtx not in trop_graph.nodes:
        raise ValueError("Vertex not in graph!")
    if weights[vtx] == 0:
        raise ValueError("Vertex has weight 0")
    
    weights[vtx] -= 1
    graph.add_edge(vtx, vtx)
    return TropicalGraph(graph, weights, markings)


def all_splits(trop_graph: TropicalGraph, vtx: str) -> list[TropicalGraph]:
    """
    Returns all possible tropical graphs obtained by splitting trop_graph at vtx, up to isomorphism
    The vertices obtained by splitting will be named [vtx]0 and [vtx]1, 
    where [vtx] is the name of vtx.
    """
    if vtx not in trop_graph.nodes:
        raise ValueError("Vertex not in graph!")

    v0, v1 = f"{vtx}0", f"{vtx}1"
    graph, weights, markings = trop_graph.get_data()
    w, m = weights[vtx], markings[vtx]
    v_edges = [e for e in graph.edges(vtx) if e != (vtx, vtx)]
    v_edge_nbrs = [u if v == vtx else v for (u, v) in v_edges]
    v_loops_num = graph.number_of_edges(vtx, vtx)

    splits = []

    for w0 in range(w + 1):
        for m0 in range(m + 1):
            for v0_edge_nbrs in powerset(v_edge_nbrs):
                for v0_loops in range(v_loops_num + 1):
                    for v1_loops in range(v_loops_num - v0_loops + 1):
                        # obtain data for a split, then construct it
                        s_graph, s_weights, s_markings = trop_graph.get_data()

                        s_weights[v0] = w0
                        s_weights[v1] = w - w0
                        del s_weights[vtx]

                        s_markings[v0] = m0
                        s_markings[v1] = m - m0
                        del s_markings[vtx]

                        s_graph.add_nodes_from([v0, v1])
                        s_graph.add_edges_from([(v0, u) for u in v0_edge_nbrs])
                        s_graph.add_edges_from([(v1, u) for u in list_difference(v_edge_nbrs, v0_edge_nbrs)])
                        # add in edges between v0 and v1
                        s_graph.add_edges_from([(v0, v0)]*v0_loops)
                        s_graph.add_edges_from([(v1, v1)]*v1_loops)
                        s_graph.add_edges_from([(v0, v1)]*(v_loops_num - v0_loops - v1_loops))  
                        s_graph.add_edge(v0, v1) # the edge for the split
                        s_graph.remove_node(vtx)

                        split = TropicalGraph(s_graph, s_weights, s_markings)
                        if not trop_graph_in_list(split, splits):
                            splits.append(split)
    
    return splits

    
# The big one

def combinatorial_type_poset(g: int, n: int):
    """
    The big one. Should generate the poset of combinatorial types in M_{g, n}^{trop}.
    """
    # TODO: midnight ramble code, needs cleaning up
    
    base_graph = TropicalGraph({'v': []}, {'v': g}, {'v': n})  # singleton with weight g, n markings
    levels = [['level0_graph1']]
    graph_dict = {'level0_graph1': base_graph}
    poset = nx.DiGraph({'level0_graph1': []})

    while True:
        print(levels)
        current_level = []
        for old_name in levels[-1]:
            print(f"Finding graphs above {old_name}")
            old_graph = graph_dict[old_name]
            for vtx in old_graph.nodes:
                new_graphs = all_splits(old_graph, vtx)
                if old_graph.weights[vtx] > 0:  # accessing private variable, big sin!!
                    new_graphs.append(lollipop(old_graph, vtx))
                for new_graph in new_graphs:
                    if new_graph.is_stable():
                        if not trop_graph_in_list(new_graph, graph_dict.values()):  # searching through all values, could only do current level
                            new_name = f"level{len(levels)}_graph{len(current_level)+1}"
                            current_level.append(new_name)
                            graph_dict[new_name] = new_graph
                            poset.add_edge(new_name, old_name)
                        else:
                            for name, graph in graph_dict.items():  # searching again
                                if graph.is_isom_to(new_graph):
                                    poset.add_edge(name, old_name)
                                    break
        levels.append(current_level)
        if len(current_level) == 0:  # no new stable graphs added in current level
            return poset, graph_dict

