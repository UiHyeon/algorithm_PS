import sys
import heapq

def dijkstra(s, e):
    global graph, length
    
    visit = [sys.maxsize] *(length + 1)
    
    visit[s] = 0
    
    queue = [[0,s]]
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
                
    return visit[e]

def solution(n, s, a, b, fares):
    global graph, length
    
    answer = sys.maxsize
    graph = [[] for _ in range(n+1)]
    length = n
    
    for i, j, cost in fares:
        graph[i].append([j, cost])
        graph[j].append([i, cost])

    for i in range(1, n+1):
        answer = min(answer, dijkstra(s,i) + dijkstra(a,i) + dijkstra(b,i))
    
    return answer