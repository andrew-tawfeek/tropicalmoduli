def base_graph(g,n):
    return Graph({(g,0): list(range(-1,-n-1,-1))})

def m2(): #outputs the set of graphs for M2,0 -- labels are (weight, index)
    L = [Graph({(2,0): []}),
    Graph({(1,0): [(1,0)]}),
    Graph({(1,0): [(1,1)]}),
    Graph({(0,0): [(0,0),(1,1)], (1,1): []}),
    Graph({(0,0): [(0,0),(0,0)]}),
    Graph({(0,0): [(0,0),(0,1)], (0,1): [(0,1)]}),
    Graph({(0,0): [(0,1),(0,1),(0,1)], (0,1): []})]
    return L


#Stability

def local_check(G,v): #no need to worry about marked points here
    weight = v[0]
    if weight >= 2:
        return True
    elif weight == 1 and G.degree(v) >= 1:
        return True
    elif weight == 0 and G.degree(v) >= 3:
        return True
    else:
        return False


def stability_check(G):
    for v in G.vertices():
        if local_check(G,v) == False:
            return False
    return True


#e.g. take G = Graph({(0,0): [(0,1),(0,1),(0,1)], (0,1): [], (0,3): []})
# stability_check(G) returns False
# removing the (0,3) returns True
# more test cases eventually, later, but seems simplistic and fine
