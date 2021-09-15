from collections import deque

def bfs(graph, root):
    visit = [[False] * 5 for _ in range(5)]
    distance = [[0] * 5 for _ in range(5)]
    
    visit[root[0]][root[1]] = True
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    queue = deque([root])
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            new_r = dr[i] + r
            new_c = dc[i] + c
            
            if -1 < new_r < 5 and -1 < new_c < 5 and graph[new_r][new_c] != "X":
                if not visit[new_r][new_c]:
                    distance[new_r][new_c] = distance[r][c] + 1
                    visit[new_r][new_c] = True
                    queue.append([new_r,new_c])
                    
    return distance

def solution(places):
    answer = []
    
    #각 고사장별로 검사를 실시.
    for place in places:
        #각 고사장의 응시자들의 좌표를 저장할 변수.
        check = []
        #각 고사장의 검사결과를 나타낼 boolean 변수.
        flag = True

        #고사장의 응시자들의 좌표를 찾아 check list에 담는다.
        for r in range(5):
            for c in range(5):
                if place[r][c] == "P":
                    check.append([r,c])
        
        #응시자들의 위치를 기점으로 고사장 내의 다른 응시자들의 거리를 계산
        for r, c in check:
            result = bfs(place, [r,c])
            #기준 응시자와 다른 응시자의 거리가 조건에 해당하지 않을 경우.
            for other_r, other_c in check:
                if [other_r,other_c] != [r, c] and 1 <= result[other_r][other_c] <= 2:
                    #맨해튼 거리 검사는 실패
                    flag = False
                    answer.append(0)
                    break
                    
            if not flag:
                break
        #위의 실패조건에 부합하지 않으면 올바른 자리 선정.
        if flag:
            answer.append(1)
        
    return answer