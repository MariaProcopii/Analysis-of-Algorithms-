from tabulate import tabulate
import random
import heapq
import time
import networkx as nx
import matplotlib.pyplot as plt
from heapq import heappop, heappush

def results(x, y, name):
    plt.plot(x, y)
    plt.xlabel('nr of elements in array')
    plt.ylabel('execution time (ms)')
    plt.title(name)
    plt.show()
    print(tabulate([['time (s)']+ y], headers=(['nr'] + x), tablefmt='orgtbl'))
    

def prim_mst(graph):
    num_vertices = len(graph)
    key = [float('inf')] * num_vertices
    parent = [None] * num_vertices
    mst_set = [False] * num_vertices

    key[0] = 0
    parent[0] = -1

    heap = [(0, 0)]

    while heap:
        weight, u = heappop(heap)
        mst_set[u] = True

        for v in range(num_vertices):
            if (
                graph[u][v] > 0
                and mst_set[v] == False
                and graph[u][v] < key[v]
            ):
                key[v] = graph[u][v]
                parent[v] = u
                heappush(heap, (key[v], v))

    print("Prim's Algorithm:")
    for i in range(1, num_vertices):
        print(f"Edge: {parent[i]} - {i}    Weight: {graph[i][parent[i]]}")

def kruskal_mst(graph):
    num_vertices = len(graph)
    parent = [i for i in range(num_vertices)]

    def find_parent(i):
        if parent[i] != i:
            parent[i] = find_parent(parent[i])
        return parent[i]

    def union(u, v):
        u_parent = find_parent(u)
        v_parent = find_parent(v)
        parent[u_parent] = v_parent

    edges = []
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph[i][j] > 0:
                edges.append((graph[i][j], i, j))

    edges.sort()

    print("Kruskal's Algorithm:")
    for edge in edges:
        weight, u, v = edge
        if find_parent(u) != find_parent(v):
            union(u, v)
            print(f"Edge: {u} - {v}    Weight: {weight}")
            
            
def create_random_graph(edges_per_node, num_nodes = 4):

    graph = [[0] * num_nodes for _ in range(num_nodes)]
    all_edges = []

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            all_edges.append((i, j))

    random.shuffle(all_edges)
for i in range(num_nodes):
        selected_edges = all_edges[i * edges_per_node : (i + 1) * edges_per_node]
        for edge in selected_edges:
            u, v = edge
            weight = random.randint(1, 10)  # Random weight between 1 and 10
            graph[u][v] = weight
            graph[v][u] = weight

    return graph

def visualize_graph(graph):
    G = nx.Graph()
    for i in range(len(graph)):
        for j in range(i + 1, len(graph[i])):
            if graph[i][j] != 0:
                G.add_edge(i, j, weight=graph[i][j])

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()

graphs = [create_random_graph(n, 4) for n in range(10, 500, 50)]

x = []
y_prim = []
y_kruskal = []
for graph in graphs:
    start_time = time.time()
    prim_mst(graph)
    end_time = time.time()
    y_prim.append(end_time - start_time)

    start_time = time.time()
    kruskal_mst(graph)
    end_time = time.time()
    y_kruskal.append(end_time - start_time)

    x.append(len(graph[1]))

    # visualize_graph(graph)

print("Sizes of graphs: ", x)

results(x, y_prim, "Prim")
print("\n--------------------------------------\n")
results(x, y_kruskal, "Kruskal")
