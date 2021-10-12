import sys
N = int(sys.stdin.readline())
rgb = []

for i in range(N):
    rgb.append(list(map(int, sys.stdin.readline().split())))

for row in range(1, len(rgb)):
    rgb[row][0] += min(rgb[row-1][1], rgb[row-1][2])
    rgb[row][1] += min(rgb[row-1][0], rgb[row-1][2])
    rgb[row][2] += min(rgb[row-1][0], rgb[row-1][1])

print(min(rgb[-1]))

#프로그래머스의 땅따먹기 문제와 비슷한 문제이다.
#첫번째 집에서부터 주어진 조건에 만족하는 최소비용이
#드는 누적 비용들을 1번집부터 순서대로 타고 내려오는 방식을 사용.