from itertools import *
from random import choice
import networkx as nx
from networkx.algorithms import tree
def tour_length(P):
    total = 0
    for i in range(len(P)-1):
        x1 = P[i][0]
        y1 = P[i][1]
        x2 = P[i+1][0]
        y2 = P[i+1][1]
        total += ((x2-x1)**2+(y2-y1)**2)**0.5
    x1 = P[len(P)-1][0]
    y1 = P[len(P)-1][1]
    x2 = P[0][0]
    y2 = P[0][1]
    total += ((x2-x1)**2+(y2-y1)**2)**0.5
    return total

def TSP(P):
    bpathl = 999999999
    perm = permutations(P)
    for i in perm:
        pathl = tour_length(i)
        bpathl = min(bpathl,pathl)
        if bpathl == pathl:
            bpath = i
    return bpath

def cities(k,n):
    'create k cities in nxn grid'
    city_set = set()
    while len(city_set) < k:
        city_set.add((choice(range(n)), choice(range(n))))

    return list(city_set)


def approx_TSP(P):
    G = nx.Graph();
    for i in range(len(P)-1):
        x1 = P[i][0]
        y1 = P[i][1]
        x2 = P[i+1][0]
        y2 = P[i+1][1]
        G.add_edge((x1,y1),(x2,y2),weight = ((x2-x1)**2+(y2-y1)**2)**0.5)
        #G.add_edge("{},{}".format(x1,y1),"{},{}".format(x2,y2),weight = ((x2-x1)**2+(y2-y1)**2)**0.5)
    x1 = P[len(P)-1][0]
    y1 = P[len(P)-1][1]
    x2 = P[0][0]
    y2 = P[0][1]
    G.add_edge((x1,y1),(x2,y2),weight = ((x2-x1)**2+(y2-y1)**2)**0.5)
    #G.add_edge("{},{}".format(x1,y1),"{},{}".format(x2,y2),weight = ((x2-x1)**2+(y2-y1)**2)**0.5)
    mst = tree.minimum_spanning_edges(G,algorithm="kruskal",data = False)
    edgelist = list(mst)

    G2 = nx.Graph()
    for x in range(len(edgelist)-1):
        x1 = edgelist[x][0][0]
        y1 = edgelist[x][0][1]
        x2 = edgelist[x][1][0]
        y2 = edgelist[x][1][1]
        G2.add_edge((x1,y1),(x2,y2),weight = ((x2-x1)**2+(y2-y1)**2)**0.5)
    best = list(nx.dfs_preorder_nodes(G2))
    ttal = tour_length(best)
    return best,ttal
