def dfs(graph, start_node):
    visit = list()
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            temp = graph[node].sort(reverse=True)
            stack.extend(graph[node])
    return visit

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'G', 'H', 'I'],
    'D': ['B', 'E', 'F'],
    'E': ['D'],
    'F': ['D'],
    'G': ['C'],
    'H': ['C'],
    'I': ['C', 'J'],
    'J': ['I']
}

print(dfs(graph, 'A'))