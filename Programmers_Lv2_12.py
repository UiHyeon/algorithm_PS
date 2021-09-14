# import heapq
# import sys

# def dijkstra(graph, length):
#     distance = [sys.maxsize] * (length+1)
#     distance[1] = 0
    
#     queue = [[0,1]]
#     heapq.heapify(queue)
    
#     while queue:
#         cost, node = heapq.heappop(queue)
        
#         if cost > distance[node]:
#             continue
            
#         for item in graph[node]:
#             new_cost,new_node = item[1], item[0]
            
#             new_cost += cost
#             if new_cost < distance[new_node]:
#                 distance[new_node] = new_cost
#                 heapq.heappush(queue, [new_cost, new_node])
        
#     return distance

# def solution(n, edge):
#     answer = 0
#     graph = [[] for _ in range(n+1)]
#     cost = 1
    
#     for start, end in edge:
#         graph[start].append([end,cost])
#         graph[end].append([start,cost])
        
#     result = dijkstra(graph, n)[1:]
    
#     result.sort(reverse  = True)
#     answer = result.count(result[0])
    
#     return answer

from collections import deque

def bfs(graph, root, n):
    visit = [False] * (n+1)
    visit[1] = True
    distance = [0] * (n+1)
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        for next_node in graph[node]:
            if not visit[next_node]:
                visit[next_node] = True
                distance[next_node] = distance[node] + 1
                queue.append(next_node)
            
    return distance

def solution(n, edge):
    answer = 0
    root = 1
    graph = {}
    
    for i in range(1, n+1):
        graph[i] = []
    
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
        
    result = bfs(graph, root, n)
    max_num = max(result)

    for check in result:
        if check == max_num:
            answer += 1
    
    return answer