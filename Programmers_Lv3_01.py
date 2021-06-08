def solution(n, computers):
    answer = 0
    graph = {}
    visit = []
    
    for i in range(n):
        graph[i] = []
        
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if computers[i][j] == 1:
                graph[i].append(j)
                
    print(graph)
                
    for i in range(n):
        stack = [i]

        if i not in visit:
            answer += 1
        
        while stack:
            node = stack.pop()

            if node not in visit:
                visit.append(node)
                stack.extend(graph[node])
        
    return answer