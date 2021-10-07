import heapq
import sys

def dijkstra(graph, start, length):
    visit = [sys.maxsize] * (length + 1)
    visit[start] = 0
    
    queue = [[0,start]]
    heapq.heapify(queue)
    
    while queue:
        cost, node = heapq.heappop(queue)
        
        if cost > visit[node]:
            continue
            
        for item in graph[node]:
            new_cost, new_node = item[1], item[0]
            new_cost += cost
        
            if new_cost < visit[new_node]:
                visit[new_node] = new_cost
                heapq.heappush(queue, [new_cost, new_node])
            
    return visit

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    
    for i, j, cost in road:
        graph[i].append([j, cost])
        graph[j].append([i, cost])
        
    result = dijkstra(graph, 1, N)
    for check in result:
        if check <= K:
            answer += 1

    return answer