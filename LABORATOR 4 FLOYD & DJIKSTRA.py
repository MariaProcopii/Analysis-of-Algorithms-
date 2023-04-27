from tabulate import tabulate
import random
import heapq
import time
import networkx as nx
import matplotlib.pyplot as plt

def results(x, y, name):
    plt.plot(x, y)
    plt.xlabel('nr of elements in array')
    plt.ylabel('execution time (ms)')
    plt.title(name)
    plt.show()
    print(tabulate([['time (s)']+ y], headers=(['nr'] + x), tablefmt='orgtbl'))

def floyd_warshall(graph):
    dist = graph.copy()
    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


def dijkstra(graph, start):
    num_vertices = len(graph)
    dist = [float('inf')] * num_vertices
    dist[start] = 0
    visited = set()
    heap = [(0, start)]
    while heap:
        (cost, current_vertex) = heapq.heappop(heap)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        for neighbor in range(num_vertices):
            if graph[current_vertex][neighbor] != 0:
                distance = dist[current_vertex] + graph[current_vertex][neighbor]
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))
    return dist


def generate_weighted_graph(num_nodes, max_edges_per_node = 4, has_negative_weights = False):
    graph = [[0] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        num_edges = random.randint(1, max_edges_per_node)
        for j in range(num_edges):
            dest_node = random.randint(0, num_nodes-1)
            if dest_node == i:
                continue
            if graph[i][dest_node] == 0:
                if has_negative_weights:
                    weight = random.randint(-10, 10)
                else:
                    weight = random.randint(1, 10)
                graph[i][dest_node] = weight
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

graphs = [generate_weighted_graph(n, 7) for n in range(10, 500, 50)]
x = []
y_floyd = []
y_djikstra = []
for graph in graphs:
    start_time = time.time()
    floyd_warshall(graph)
    end_time = time.time()
    y_floyd.append(end_time - start_time)

    start_time = time.time()
    dijkstra(graph, 0)
    end_time = time.time()
    y_djikstra.append(end_time - start_time)

    x.append(len(graph[1]))

    # visualize_graph(graph)

print("Sizes of graphs: ", x)

results(x, y_floyd, "Floyd")
print("\n--------------------------------------\n")
results(x, y_djikstra, "Djikstra")
