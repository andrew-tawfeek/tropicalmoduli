# num vertices = 2g - 2 + n
# num edges = 3g - 3 + n


# Computing maximals...
# https://oeis.org/A005967/a005967.pdf


# missing those not having loops on leaves

def trivalent_trees(n): #connected trees on n-many vertices with deg at most 3
    L = list(graphs.CompleteGraph(n).spanning_trees())
    final = []
    for G in L:
        deg_list = [G.degree(v) for v in G.vertices()]
        parity_list = [x%2 for x in deg_list]
        if max(deg_list) <= 3 and len([i for i in parity_list if i==0])%2 == 0:
            final = final + [G]
    return final

def loopy_dupe(G): #just does both the things above, everything output will have deg 3
    H = Graph(G, multiedges = True, loops = True) #incase
    even_verts = [v for v in G.vertices() if G.degree(v) == 2]
    leaves = [v for v in G.vertices() if G.degree(v) == 1]
    for v in even_verts:
        even_verts.remove(v)
        for w in even_verts:
            H.add_edge(v,w)
            even_verts.remove(w)
    for v in leaves:
        H.add_edge(v,v)
    return H

def looped_multi_trivalent_graphs(n): #IS MISSING GRAPHS WITH NO LOOPS
    L = trivalent_trees(n)
    return [loopy_dupe(G) for G in L]

# compare trivalent_trees(6)[-4].show() with looped_multi_trivalent_graphs(6)[-4].show()

# note for above: of course empty when n is even (prove with pigeon-hole principle...)


####
# COMPUTATIONALLY INTENSIVE PART BELOW 
####

def unlooped_multi_trivalent_graphs(g): #takes in genus (num vert = 2g - 2)
    return [G for G in graphs(2*g-2, size = 3*g-3) if G.is_regular(3)] #Finds all cubic/trivalent graphs on a number of vertices! Bad.
