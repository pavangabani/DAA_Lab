def add_d_edge(g,v1,v2,w=1):
    g[v1][v2]=w

def add_ud_edge(g,v1,v2,w=1):
    g[v1][v2]=w
    g[v2][v1]=w
    
w, h = 5, 5
g = [[0 for x in range(w)] for y in range(h)] 
add_d_edge(g,1,2,4)
add_d_edge(g,1,3,10)
add_d_edge(g,2,3,12)
print(g)