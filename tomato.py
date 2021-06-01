import sys
from collections import deque

r = sys.stdin.readline

def tomato_bfs(M, N, box):

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    day = -1

    while first_ripe:
        day += 1

        for i in range(len(first_ripe)):
            x, y = first_ripe.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (0 <= nx < N) and (0 <= ny < M) and(box[nx][ny] == 0):
                    box[nx][ny] = 1
                    first_ripe.append([nx, ny])
    
    for i in range(len(box)):
        for j in range(len(box[0])):
            if box[i][j] == 0:
                return -1
    
    return day

M, N = map(int, r().split())
box, first_ripe = [], deque()
for i in range(N):
    row = list(map(int, r().split()))
    for j in range(M):
        if row[j] == 1:
            first_ripe.append([i, j])
    box.append(row)

print(tomato_bfs(M, N, box))