#from dijkstar import Graph, find_path
from networkx import *
##g = Graph()
###s = 1, a = 2, b = 3, c = 4
##g.add_edge(1,2,0)
##g.add_edge(1,3,-1)
##g.add_edge(2,3,-2)
##g.add_edge(3,4,1)
##print(find_path(g,1,4))

#s = 1, a = 2, b = 3, c = 4
g2 = nx.DiGraph()
g2.add_node(1)
g2.add_node(2)
g2.add_node(3)
g2.add_node(4)
g2.add_edge(1,2,weight = 0)
g2.add_edge(1,3,weight = -1)
g2.add_edge(2,3,weight = -2)
g2.add_edge(3,4,weight = 1)
print(nx.dijkstra_path(g2,1,3))
#print(nx.bellman_ford_path(g2,1,4))
#print(nx.bellman_ford_path(g2,1,3))
