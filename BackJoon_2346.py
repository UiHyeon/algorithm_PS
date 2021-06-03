# N개의 풍선이 있다. 각 풍선 안에는 -N부터 N까지의 수가 적혀있는 종이가 들어 있다.
# 이 풍선들을 다음과 같은 규칙으로 터뜨린다.
# 우선, 제일 처음에는 1번 풍선을 터뜨린다. 다음에는 풍선 안에 있는 종이를 꺼내어 그 종이에 적혀있는 
# 값만큼 이동하여 다음 풍선을 터뜨린다. 양수가 적혀 있을 경우에는 오른쪽으로, 음수가 적혀 있을 때는 왼쪽으로 이동한다. 
# 풍선은 원형으로 놓여 있다고 생각한다. 즉, 1번 풍선의 왼쪽에 N번 풍선이 있고, N번 풍선의 오른쪽에 1번 풍선이 있는 것이다. 
# 이동할 때에는 이미 터진 풍선은 빼고 생각한다.

# 예를 들어 다섯 개의 풍선 안에 차례로 3, 2, 1, -3, -1이 적혀 있었다고 하자. 이 경우 3이 적혀 있는 1번 풍선, 
# -3이 적혀 있는 4번 풍선, -1이 적혀 있는 5번 풍선, 1이 적혀 있는 3번 풍선, 2가 적혀 있는 2번 풍선의 순서대로 터지게 된다.

import sys

N = int(sys.stdin.readline().rstrip())
temp = sys.stdin.readline().split()
balloon = []

for i in range(len(temp)):
    balloon.append([int(temp[i]),i+1])
idx = 0
answer = []

check = balloon.pop(idx)
answer.append(str(check[1]))

while balloon:
    if check[0] < 0 :
        idx = (idx + check[0]) % len(balloon)
    else:
        idx = (idx - 1 + check[0]) % len(balloon)

    check = balloon.pop(idx)
    answer.append(str(check[1]))

print(' '.join(answer))