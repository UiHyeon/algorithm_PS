import sys
input = sys.stdin.readline().rstrip()

def move(dir_com, temp):
    if dir_com == 1:
        return [0, temp[3], temp[2], temp[6], temp[1], temp[5], temp[4]]
    if dir_com == 2:
        return [0, temp[4], temp[2], temp[1], temp[6], temp[5], temp[3]]
    if dir_com == 3:
        return [0, temp[2], temp[6], temp[3], temp[4], temp[1], temp[5]]
    if dir_com == 4:
        return [0, temp[5], temp[1], temp[3], temp[4], temp[6], temp[2]]

N, M, x, y, K = map(int, input.split())
num_map = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
dice = [0 for _ in range(7)]
command = map(int, sys.stdin.readline().rstrip().split())
direction = [[0,0], [0, 1], [0, -1], [-1, 0], [1, 0]]

for com in command:
    new_x = x + direction[com][0]
    new_y = y + direction[com][1]

    if -1 < new_x < len(num_map) and -1 < new_y < len(num_map[0]):
        dice = move(com, dice)
        x, y = new_x, new_y
        if num_map[x][y] == 0:
            num_map[x][y] = dice[1]
            print(dice[6])
        else:
            dice[1] = num_map[x][y]
            num_map[x][y] = 0
            print(dice[6])
    else:
        continue