import networkx

g = networkx.DiGraph()


g.add_edge('s','c',capacity=3)
g.add_edge('s','a',capacity=4)
g.add_edge('c','a',capacity=2)
g.add_edge('c','d',capacity=5)
g.add_edge('a','b',capacity=3)
g.add_edge('b','d',capacity=2)
g.add_edge('b','t',capacity=5)
g.add_edge('d','t',capacity=6)

print(networkx.maximum_flow(g,'s','t')[0])

print(list(g.neighbors('s')))

print(list(set([1,1,1,2,3])))
