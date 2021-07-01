# 체스판은 8*8크기이고, 검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다. 가장 왼쪽 위칸 (0,0)은 하얀색이다. 
# 체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성하시오.

# 첫째 줄부터 8개의 줄에 체스판의 상태가 주어진다. ‘.’은 빈 칸이고, ‘F’는 위에 말이 있는 칸이다.

import sys

graph = []
count = 0
for _ in range(8):
    graph.append(list(sys.stdin.readline().rstrip()))

for i in range(len(graph)):
    for j in range(len(graph[0])):
        if (i+j) % 2 == 0 and graph[i][j] == 'F':
            count += 1

print(count)