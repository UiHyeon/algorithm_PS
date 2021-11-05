#2차원 배열 일정한 규칙이 적용되는 
#대각선 이동동작 구현

import sys

N = int(sys.stdin.readline().rstrip())

graph = [[0] * N for _ in range(N)]

place = [0,0]
check = False
direction = 'up'

for _ in range(N*N):
    graph[place[0]][place[1]] = 1

    for item in graph:
        print(item)

    print('=====================')
    #왼쪽 벽에 붙어있는 곳에 있을 경우
    if place[1] == 0  and (place[0]+1) < N:
        #한번만 대각선이 아닌 그냥 직선방향으로 움직이도록 check라는 flag를 세워 판별.
        if not check:
            place[0] += 1
            #직선이동을 하도록 place의 좌표점을 변경
            #벽에 붙엇을 경우 한번씩만 직선이동을 하기때문에 check를 변경
            #왼쪽 벽에 붙으면 대각선 이동은 오른쪽 위로 이동 
            #따라서 direction을 통해 방향을 지정.
            check = True
            direction = 'up'
            continue

    #상단 벽에 붙어있는 곳이 있을 경우
    elif place[0] == 0 and (place[1]+1) < N:
        #위의 왼쪽 벽에 붙어있는 경우의 반대로 처리를 한다.
        if not check:
            place[1] += 1
            check = True
            direction = 'down'
            continue

    #왼쪽 벽이나 상단의 벽이 아닌 대각선 이동을 하는 구간에서의 판별

    #오른쪽 위로 대각선 이동을 할때
    if direction == 'up':
        #상단벽에 도착했을때 오른쪽 직진 이동이 불가능 하다면
        if place[1] + 1 >= N:
            #하단으로 직진방향을 바꾼다.
            place[0] += 1
            #직진 이동을 한번 했으므로 check를 True로 만들어 직진이동이 다시 일어나지 않게 한다.
            check = True
            #상단 움직이 끝난후에는 대각선 이동을 하게 되면 왼쪽아래 방향으로 향한다.
            direction = 'down'
            continue
        #상단벽에 도착한게 아니라면 게속해서 오른쪽 상단으로 대각선 이동
        place[0] -= 1
        place[1] += 1
        #벽에 만난 것이 아니기 때문에 직진 이동을 할필요가 없다.
        check = False


    #위의 오른쪽 위 대각선 하는 로직의 반대의 의미
    if direction == 'down':
        if place[0] + 1 >= N:
            place[1] += 1
            check = True
            direction = 'up'
            continue
        place[0] += 1
        place[1] -= 1
        check = False
