# n = int(input("no of elements"))
# list = [int(x) for x in input("enter elements").split()]
# count = 0
# for ele in list:
#     count = count + ele
# print(count)
from collections import defaultdict

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(graph, V, E):
    result = []

    i = 0
    e = 0

    graph = sorted(graph, key=lambda item: item[2])

    parent = []
    rank = []

    for node in range(V):
        parent.append(node)
        rank.append(0)
    
    while e < V - 1:
        u, v, w = graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y)
    
    total_weight = 0
    for u, v, weight in result:
        total_weight += weight
    return result, total_weight

# Example usage
V = 4
E = 5

graph = [[0, 1, 10],
         [0, 2, 6],
         [0, 3, 5],
         [1, 3, 15],
         [2, 3, 4]]

minimum_spanning_tree, total_weight = kruskal(graph, V, E)

print("Minimum spanning tree:", minimum_spanning_tree)
print("Total weight:", total_weight)
