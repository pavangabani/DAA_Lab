def add_vertex(g,v):
    g[v]=[]

def add_directed_edge(g,v1,v2,w=0):
    g[v1].append((v2,w))

def add_undirected_edge(g,v1,v2,w=0):
    g[v1].append((v2,w))
    g[v2].append((v1,w))

def print_graph(g):
    for v in g:
        print("vertex :",v," -> ",g[v])

graph = {}
add_vertex(graph,1)
add_vertex(graph,2)
add_vertex(graph,3)

add_directed_edge(graph,1,2,5)
add_directed_edge(graph,1,3,10)
add_directed_edge(graph,2,3,12)

print("directed graph :")
print_graph(graph)

graph1 = {}
add_vertex(graph1,1)
add_vertex(graph1,2)
add_vertex(graph1,3)

add_undirected_edge(graph1,1,2,5)
add_undirected_edge(graph1,1,3,10)
add_undirected_edge(graph1,2,3,12)

print("undirected graph :")
print_graph(graph1)
