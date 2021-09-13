import sys
import heapq

def dijkstra(root):
    global graph, V

    distance[root] = 0

    queue = [[0, root]]
    heapq.heapify(queue)

    while queue:
        cost, node = heapq.heappop(queue)

        if cost > distance[node]:
            continue

        for item in graph[node]:
            new_cost, new_node = item[1], item[0]

            new_cost += cost

            if new_cost < distance[new_node]:
                distance[new_node] = new_cost
                heapq.heappush(queue, [new_cost, new_node])

global graph, V

temp = sys.stdin.readline().rstrip().split()
V, E = int(temp[0]), int(temp[1])
root = int(sys.stdin.readline().rstrip())
distance = [sys.maxsize] * (V+1)
graph = [[] for _ in range(V+1)]

for _ in range(E):
    start, end, cost = map(int, sys.stdin.readline().rstrip().split())
    graph[start].append([end, cost])

dijkstra(root)

for i in range(1, len(graph)):
    if distance[i] == sys.maxsize:
        print("INF")
    else:
        print(str(distance[i]))
