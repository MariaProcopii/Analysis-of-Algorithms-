from tabulate import tabulate
import random
import time
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def results(x, y, name):
    plt.plot(x, y)
    plt.xlabel('nr of elements in array')
    plt.ylabel('execution time (ms)')
    plt.title(name)
    plt.show()
    print(tabulate([['time (s)']+ y], headers=(['nr'] + x), tablefmt='orgtbl'))

def generate_graph(n):
    graph = {}
    for i in range(n):
        neighbors = set(random.sample(range(n), random.randint(1, n)))
        graph[i] = neighbors
    return graph


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next_vertex in graph[start] - visited:
        dfs(graph, next_vertex, visited)
    return visited


def draw_g(graph):
    g = nx.Graph(graph)
    nx.draw(g, with_labels=True)
    plt.title(f"Graph of size {len(graph)}")
    plt.show()


graphs = [generate_graph(n) for n in range(10, 1000, 100)]

y_bfs = []
y_dfs = []
x = []
for graph in graphs:
    start_time = time.time()
    bfs(graph, 0)
    end_time = time.time()
    y_bfs.append(end_time - start_time)

    start_time = time.time()
    dfs(graph, 0)
    end_time = time.time()
    y_dfs.append(end_time - start_time)

    x.append(len(graph))

    draw_g(graph)

print("Sizes of graphs: ", x)

results(x, y_bfs, "Breadth First Search")
print("\n---------------------------------\\n")
results(x, y_dfs, "Depth First Search")



